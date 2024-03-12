Dataset **GMOT-40** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/v/p/xf/M5gEXJ9iad6uXkjwB2pOW11rmsiC8my3Y2M6XlWEjOtdmgXBryPnhatLtatnX2ChaSUmh2pmZlsO5rtUTNKFXrFanbEUc8kGV2Mn6fY5z4hsE1rGyRaj4BS5QXmN.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='GMOT-40', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [Image Sequences](https://drive.google.com/file/d/1DanCUXPrn4b5AUVCcawELXghYIWxewoP/view?usp=sharing)
- [Trajectory labels](https://drive.google.com/file/d/1zOR04COTGVgqoKocxFx6vx1hZSBO8wEC/view?usp=sharing)
