# Heavy-Vehicle-Segmentation-using-YOLOv8
## Preview
![sample for git](https://github.com/Muhammad-Zeerak-Khan/Heavy-Vehicle-Segmentation-using-YOLOv8/assets/79400407/1486f9eb-2cf0-4420-9406-d2044106dab1)


## Data

The dataset used in this tutorial can be downloaded [here](https://universe.roboflow.com/spcv-lab-iitt/heavy-vehicle-detection-qiop2)

## Model

A Yolov8 pre-trained model (YOLOv8n) was used to detect vehicles.

The model was trained on Tesla T4 provided by Google Collab and the vehicle segmentation model can be found [here](https://drive.google.com/file/d/11brwx1dOZ5dGAlrCMQ_IQrYt51Y4lIJ2/view?usp=sharing)

## Project Setup

* Make an environment with python=3.8 using the following command 
``` bash
conda create --prefix ./env python==3.8 -y
```

* Install the project dependencies using the following command 
```bash
pip install -r requirements.txt
```
* Run train.py to start training the pre-trained segmentation model.
``` python
python train.py
```

* Finally run predict.py to get the segmentation masks.
```python
python predict.py
```
