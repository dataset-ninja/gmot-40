import os
import shutil
from collections import defaultdict

import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import (
    file_exists,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from tqdm import tqdm

import src.settings as s


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # Possible structure for bbox case. Feel free to modify as you needs.

    images_path = "/home/alex/DATASETS/TODO/GMOT-40/GenericMOT_JPEG_Sequence"
    bboxes_path = "/home/alex/DATASETS/TODO/GMOT-40/track_label"
    batch_size = 30
    ds_name = "ds"

    def create_ann(image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        seq = sly.Tag(seq_meta, value=folder)

        obj_class = meta.get_obj_class(folder.split("-")[0])

        ann_data = curr_im_name_to_data[get_file_name_with_ext(image_path)]
        for curr_ann_data in ann_data:
            coords = list(map(int, curr_ann_data))
            tag = sly.Tag(identity_meta, value=coords[0])
            left = int(coords[1])
            top = int(coords[2])
            right = left + int(coords[3])
            bottom = top + int(coords[4])
            rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
            label = sly.Label(rect, obj_class, tags=[tag])
            labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=[seq])

    airplane = sly.ObjClass("airplane", sly.Rectangle)
    ball = sly.ObjClass("ball", sly.Rectangle)
    balloon = sly.ObjClass("balloon", sly.Rectangle)
    bird = sly.ObjClass("bird", sly.Rectangle)
    boat = sly.ObjClass("boat", sly.Rectangle)
    car = sly.ObjClass("car", sly.Rectangle)
    fish = sly.ObjClass("fish", sly.Rectangle)
    insect = sly.ObjClass("insect", sly.Rectangle)
    person = sly.ObjClass("person", sly.Rectangle)
    stock = sly.ObjClass("stock", sly.Rectangle)

    identity_meta = sly.TagMeta("identity id", sly.TagValueType.ANY_NUMBER)
    seq_meta = sly.TagMeta("sequence", sly.TagValueType.ANY_STRING)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[airplane, ball, balloon, bird, boat, car, fish, insect, person, stock],
        tag_metas=[identity_meta, seq_meta],
    )
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    folder_to_frames = {}
    for bbox_file in os.listdir(bboxes_path):
        bbox_path = os.path.join(bboxes_path, bbox_file)
        im_name_to_data = defaultdict(list)
        with open(bbox_path) as f:
            content = f.read().split("\n")
            for row in content:
                if len(row) > 0:
                    row_data = row.split(",")
                    im_name_to_data[row_data[0].zfill(6) + ".jpg"].append(row_data[1:6])
        folder_to_frames[get_file_name(bbox_file)] = im_name_to_data

    for folder in os.listdir(images_path):
        curr_im_name_to_data = folder_to_frames[folder]
        curr_images_path = os.path.join(images_path, folder, "img1")

        images_names = os.listdir(curr_images_path)

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

        for images_names_batch in sly.batched(images_names, batch_size=batch_size):
            im_names_batch = []
            img_pathes_batch = []
            for image_name in images_names_batch:
                img_pathes_batch.append(os.path.join(curr_images_path, image_name))
                im_names_batch.append(folder + "_" + image_name)

            img_infos = api.image.upload_paths(dataset.id, im_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(images_names_batch))

    return project
