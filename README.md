# Deep-Learning-for-Perception-CS452-Final-Project
# Deep-Learning-project-for-fall-17-semester-Product-Category-Classifier-for-Daraz
# Contributor#1
Shaiq Munir Malik
# Contributor#2
Kinaan Aamir
# Description-of-uploaded-files
# Daraz.py
"daraz.py" file contains all the code that was used for scrapping images and their labels from the website using scrapy
# Settings.py
"settings.py" contains settings for the scrapy code written in "daraz.py"
# preprocess-images.ipynb
"preprocess-images.ipynb" is an ipython notebook that contains code for preprocessing the scrapped images from Daraz. Our preprocessing of images included cropping of images to a size of 220x220 so that all the images have the same size, we cropped all images to 220x220 because it was the smallest size in our dataset. Further preprocessing included creating batches from the dataset that were then used during the transfer learning phase
# tranfer-learn2.ipynb
"tranfer_learn2.ipynb" is an ipython notebook that contains the code of transfer learning and fine tuning the ResNet50 model
# weights-improvement-02-1.2280.hdf5
"_weights-improvement-02-1.2280.hdf5" is a weights file that contains the tuned weights for our ResNet50 model
# tranfer-learn.ipynb
"tranfer_learn.ipynb" is an ipython notebook that contains the code of transfer learning and fine tuning the InceptionV3 model
# weights-improvement-05-0.9795.hdf5
"weights-improvement-05-0.9795.hdf5" is a weights file that contains the tuned weights for our InceptionV3 model
