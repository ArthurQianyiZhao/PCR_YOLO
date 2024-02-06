# PCRyolo: Multi-Purpose Cleaning Robot Based on YOLO-V7

# Project Description

The Multi-<u>P</u>urpose <u>C</u>leaning <u>R</u>obot trained based on <u>yolo</u>-V7, embedded into an autonomous robot chassis, can automatically navigate, identify different types of rubbishes/resources, and collect them.

The deep learning model `mpcryolo.pt` was trained based on YOLO-V7, which can identify 5 classes, including "coin", "paper", "plastic", "can" and "water", with impressive accuracy.

![confusion_matrix](/Photos/confusion_matrix.png)

*Fig.1 The confusion matrix*

To access YOLO-v7 pretrained model and environment setup, go to:

https://github.com/WongKinYiu/yolov7



For the labelled training and validation dataset, you can have access at:

https://drive.google.com/drive/folders/1Cp0gC1_IgugWHFTNZ-MxYV5n6-BozK3c?usp=sharing, https://drive.google.com/drive/folders/1bB5pMYbI_IrGh3C9LoxWuooe1P4-QxEg?usp=sharing



To modify the repository to run PCRyolo, simply replace the `detect.py` with our given file, which integrates the webcam stream and communication module. Then add the `pcryolo.pt` to the root address.



Step 1: 

Upload `robot.c` to Arduino.

Step 2:

At the raspberry pi, run:

`python3 robot.py `

to start the streaming.

Step 3:

At the server (can be your laptop), run:

`python3 detect.py --source http://192.168.43.37:8000/stream.mjpg --weights pcryolo.pt`

at the root folder of YOLO-V7 
