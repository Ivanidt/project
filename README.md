# Project Name

Welcome to my demo model! Its project about scan around in the environment animals and people. Its will helps to hunter with searching animals (like foxes and bears and etc.But my model only detects first two animals.) and avoid shooting to the people by accident.  

![add image descrition here](direct image link here)

## The Algorithm

In this demo model using only ai (called detectnet, if you want learns about this , goes to the link: https://github.com/dusty-nv/jetson-inference/blob/master/docs/detectnet-console-2.md). Ai trained by ssd mobile net with using data downloaded from Open Images dataset with 480 images/label (to retrain the model follow the link: https://github.com/dusty-nv/jetson-inference/blob/master/docs/pytorch-ssd.md).Model trained in google colab with 35 epochs and exported to jetson-nano under the project folder.

I train a model to only detect foxes and combined it with the default ssd-mobilenet model, so that it can detect also detect people and bears.

## Running this project
1.Download my projects with using this command:
```
git clone https://github.com/Ivanidt/project.git
```

2.Clone ssd-repository under the jetson-inference library using this command
```
git clone https://github.com/dusty-nv/pytorch-ssd.git
```
3.Once you train the model on colab, donwload the model with the lowest loss value and labels.txt and drag them under the models/animal folder

4.Export the model using 
```
python3 ssd/onnx_export.py --model-dir=models/animal
```

5.Run (its a example command in [] you can use your file)
```
python3 detectnet.py "data/images/[image].jpg" data/test/[result].jpg
```
6.After the running if a person is detected, it will show a message "Warning, people in there" in the terminal, if a fox or a bear is detected , it will show a message "Animal in there" in the terminal. If nothing is detected, it will show "Clear".

[View a video explanation here](video link)