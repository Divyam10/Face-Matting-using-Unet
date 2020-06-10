#ace-Matting-using-Unet
Text-Detection-Model
Text Detection Model trained with Precision Score of 98% on Test Set of 200 images. 
===================

## Description
Potrait Matting Model with 90% accuracy build on fine tuning vgg_unet using https://github.com/switchablenorms/CelebAMask-HQ Dataset. 
This model is made using amazing package made by Divam Gupta : https://divamgupta.com. Link to his repo https://github.com/divamgupta/image-segmentation-keras


## Setup
1. create a viruatual environment  and activate it 
2. install required libs
```
   apt-get install -y libsm6 libxext6 libxrender-dev
   pip install opencv-python
```
2. install keras-segmenatation pacakge using
```
pip install keras-segmentation
```
3. Downlaod Celeb Dataset

4. Edit the path to the dataset in preprocessing.py and run it.
```
python preprocessing.py
```

5. Run the traning.py file using
```
python traning.py
```
6. Test the image using inference-image.py

## Samples 
### 3 images from the datset - 6 images from the internet
Disclaimer -  I do not own/clicked any of the images below. 

![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/0.jpg) ![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/0.png)
![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/1.jpg) ![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/1.png)
![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/2.jpg) ![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/2.png)
![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/3.jpg) ![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/3.png)
![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/4.jpg) ![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/4.png)
![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/5.jpg) ![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/5.png)
![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/6.jpg) ![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/6.png)
![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/7.jpg) ![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/7.png)
![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/8.jpg) ![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/8.png)
![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/9.jpg) ![alt text](https://github.com/Divyam10/Face-Matting-using-Unet/blob/master/results/9.png)







## Extentions to the project
1. Face attritube changing like color of the  hair,skin
2. potrait regeneration using Gans, regenerating new attributes like long hair, beard, etc

