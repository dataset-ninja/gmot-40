from typing import Dict, List, Literal, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "GMOT-40"
PROJECT_NAME_FULL: str = "GMOT-40: Generic Multiple Object Tracking Dataset"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_SA_4_0(source_url="https://github.com/Spritea/GMOT40#License")
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Surveillance()]
CATEGORY: Category = Category.Surveillance()

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection(), CVTask.Identification()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2021-04-07"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://spritea.github.io/GMOT40/"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 15120565
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/gmot-40"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "Image Sequences": "https://drive.google.com/file/d/1DanCUXPrn4b5AUVCcawELXghYIWxewoP/view?usp=sharing",
    "Trajectory labels": "https://drive.google.com/file/d/1zOR04COTGVgqoKocxFx6vx1hZSBO8wEC/view?usp=sharing",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]] or Literal["predefined"]] = {
    "airplane": [230, 25, 75],
    "ball": [60, 180, 75],
    "balloon": [255, 225, 25],
    "bird": [0, 130, 200],
    "boat": [245, 130, 48],
    "car": [145, 30, 180],
    "fish": [70, 240, 240],
    "insect": [240, 50, 230],
    "person": [210, 245, 60],
    "stock": [250, 190, 212],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = "https://arxiv.org/pdf/2011.11858"
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {
    "GitHub": "https://github.com/Spritea/GMOT40"
}

CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = [
    "Hexin Bai",
    "Wensheng Cheng",
    "Peng Chu",
    "Juehuan Liu",
    "Kai Zhang",
    "Haibin Ling",
]
AUTHORS_CONTACTS: Optional[List[str]] = [
    "hexin.bai@temple.edu",
    "wenscheng@cs.stonybrook.edu",
    "pengchu@microsoft.com",
    "juehuan.liu@temple.edu",
    "zhang.kai@temple.edu",
    "hling@cs.stonybrook.edu",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "Temple University Philadelphia, USA",
    "Stony Brook University, USA",
    "Microsoft Redmond, USA",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.temple.edu/",
    "https://www.stonybrook.edu/",
    "https://www.microsoft.com/fi-fi/",
]

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "__POSTTEXT__": "Additionally, every image marked with its ***sequence*** tag. Every label contains information about its ***identity id***. Explore it in Supervisely labelling tool"
}
TAGS: Optional[
    List[Literal["multi-view", "synthetic", "simulation", "multi-camera", "multi-modal"]]
] = ["multi-object-tracking"]


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
