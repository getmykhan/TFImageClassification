This project is a result of a 24 hours Hackathon.


## Introduction
In this project we use Python and TensorFlow to train an Image Classifier and then we classify images using this trained Classifier.
To train the Image Classifier we have used the **Transfer Learning** process.

#### Transfer Learning
> Transfer learning and domain adaptation refer to the situation where what has been learned in one setting … is exploited to improve generalization in another setting

In practice, very few people train an entire Convolutional Network from scratch (with random initialization), because it is relatively rare to have a dataset of sufficient size. Instead, it is common to pretrain a ConvNet on a very large dataset (e.g. **ImageNet**, which contains 1.2 million images with 1000 categories), and then use the ConvNet either as an initialization or a fixed feature extractor for the task of interest. 

With Transfer Learning, we need not spend a lot of computing power and time on training our model from scratch instead we can use a small dataset to train the model.

![](https://api.ning.com/files/1a5R6o7JsEHZ9j2SOd20XYu2GYExArt4Kr*0U07Z1JYbfSnF2ugTP7wmqMJn-l2auLHblJkG2QbtZcVqzScB81vPibkAjqBg/transferlearning.png)

In this project, We are going to use a model trained on the ImageNet Large Visual Recognition Challenge dataset. These models can differentiate between 1,000 different classes, like Dalmatian or dishwasher. We will then retrain it on a similar problem, which in our case is recognizing a person.

## Implementation
ImageNet models are networks with millions of parameters that can differentiate a large number of classes. We only trained the final layer of that network, so training will end in a reasonable amount of time. We gathered a small size of training data of people images clicked using the laptop camera and trained the model on it. ImageNet did not include any of the pictures that we used to train the model.

## Deployment
We created a basic interface which has 2 options:
* Option 1 (System already knows you):
    This means that the system is already trained on your images and can recogize you.
    * In this case, it takes a picture of you and displays your name(Category in which you were classified)
* Option 2 (System does not recognize you):
    This means that no images were provided to the system to train it on your pictures
    * In this case, 150 images are clicked using the laptop camera and fed into the model as training data. And a category name (Your Name) is provided to the system.
    * Now the system can recognize you and display your name if you select Option 1
    
## Use Cases
The use cases for such an application are as follows:
* Security (Image Recognition for providing Authorized access)
* Automatically Organizing Images (Classifying a gallery of Images into different categories(people))
 
## Future Scope
The future scope for this project is implementing **Active Learning** into the existing model. Which for our project is: taking the picture which is used in option 1 and pushing it into the training data for the model.
