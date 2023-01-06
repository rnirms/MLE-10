<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png"
     width="200px"
     height="auto"/>
</p>

# <h1 align="center" id="heading">Object Detection</h1>

Today you are a machine learning engineer on the Spatial Perception Team (SPT) at Apple. The goal is to leverage an existing object detector model to automatically detect dogs, an application of **transfer learning**. 

The idea is that you have access to a model that you or one of your colleagues has already trained on a large and diverse set of images, but the model is not very specific for your task (dog detection). We'll do transfer learning by fine-tuning this existing model on a small dataset of dog images. 

*This is only a small part of the end product -- Visual Look Up feature released in iOS 15 -- snap a picture, identify if an object belonging to five categories (art, landmarks, nature, books, and pets) exists, if yes, highlight with a object symbol, and further identify, e.g., the species of a plant. Examples are shown below ([picture credits](https://www.iphonetricks.org/how-to-visual-look-up-photos-on-iphone/))*

<div>
<img src="https://149493502.v2.pressablecdn.com/wp-content/uploads/2021/07/visual-look-up-categories.jpg" width="500"/>
</div>

# 📚 Learning Objectives

At the end of this session, you will be able to

- understand [few-shot learning (FSL)](https://neptune.ai/blog/understanding-few-shot-learning-in-computer-vision)
- understand the mechanics of using pretrained model and fine tune a pretrained model 
- calculate metrics and evaluate detection model

# 🛠️ Pre-work

For this assignment, we will use Colab to take advantage of its free GPU. Setup are included inside the notebook, yet tricky (tested okay as of late June 2022). Make sure to run [demo-interactive-fsl-rubberduck](nb/demo-interactive-fsl-rubberduck.ipynb) in Colab without errors. This demo notebook will also better prepare you for the upcoming coding session.

In addition, you need to upload the data, images and annotation files, under `dat/dog_dataset` to your google drive, ideally you will use the same path `/content/drive/My Drive/fourthbrain/dog_dataset`.

```
.
└── dog_dataset
    ├── test
    │   ├── annotations
    │   └── images
    └── train
        ├── annotations
        └── images
```

## Background
Please review the weekly narrative [here](https://great-yamamomo-5c3.notion.site/Week-9-Computer-Vision-ace914f6aa2447789c8d120748ec814a)
