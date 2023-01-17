<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png" 
     width="200px"
     height="auto"/>
</p>

# <h1 align="center" id="heading">Hate Speech Detector</h1>

Today you are a machine learning engineer, a member of Birdwatch at Twitter. 

The objective of this task is to detect hate speech in tweets. 
For the sake of simplicity, here a tweet contains hate speech if it has a racist or sexist sentiment associated with it. 
In other words, we need to classify racist or sexist tweets from other tweets.

A labelled dataset of 31,962 tweets is provided in the form of a compressed csv file with each line storing a tweet id, its label, and the tweet. 
Label '1' denotes the tweet is racist/sexist while label '0' denotes the tweet is not racist/sexist.

We will first approach the problem in a traditional way: clean the raw text using simple regex (regular expression), extract features, build naive Bayes models to classify tweets; then we build a deep learning model and explain our deep learning model with LIME.

## ☑️ Learning Objectives

By the end of this lesson, you will be able to:

- Understand the basic concepts in natural language processing (NLP)
- Perform basic NLP tasks on tweets
- Build a naive Bayes classifier to detect hate speech 
- Build a bidirectional long short-term memory (BiLSTM) to detect hate speech
- Visualize the embedding of tweets with Tensorboard projector
- Explain models with LIME

## :hammer_and_wrench: Pre-work

1. Complete this assignment using Google Colab.
2. All dependencies (`numpy`, `pandas`, `scikit-learn`, `nltk`, `genism`, `wordcloud`, `tensorflow`, `lime`) are included in the notebook.
3. Use Chrome browser for least friction running Tensorboard.
4. To be better prepared to use Tensorboard to visualize the embedding, go over this [tutorial](https://www.tensorflow.org/tensorboard/tensorboard_projector_plugin) before session.  
5. Upload file `img/twitter-mask.pn` to your Google Drive for plotting masked wordcloud and update the path in notebook accordingly.
6. Upload  `dat/tweets.csv.gz` to your Google Drive and update the path in notebook accordingly.

## Background

Please review the weekly narrative [here](https://www.notion.so/Week-10-Natural-Language-Processing-711df00c09654a968e7accc70b1c54f3)
