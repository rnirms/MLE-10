# New articles classification

Today, you are a machine learning engineer at [Upday](https://www.upday.com/home), a news app. The engine behind the app processes almost 100k news articles every day in many languages and context. In order to connect people with the right content, we need to know what the articles are about. 

The job here is to build a classifier that identify the category of an article accurately that will be fed into the recommendation algorithms of the app for better personalized content for the readers. 

You will first train a Transformer from scratch; then fine-tune a pre-trained Transformer model for text classification using 🤗; and compare performances using the same test data set.

## Learning objectives

By the end of this session, you will be able to:
- Understand how Transformer models work
- Build a Transformer model for text classification from scratch
- Fine-tune a pre-trained Transformer model for text classification using 🤗 

## Pre-work

We will use Google Colab to run this notebook.

If you are not familiar with Transformer, reviewing [Text Classification - Attention](https://www.kaggle.com/code/ritvik1909/text-classification-attention) will be helpful. 

It is possible that you may hit usage limit using Google CoLab; see [explanations](https://stackoverflow.com/questions/61126851/how-can-i-use-gpu-on-google-colab-after-exceeding-usage-limit). Particularly it could happen when fine-tuning DistilBert. Completely optional to upgrade to CoLab Pro; just wait for a cool-down period (1--2 days), try again.

## Background
Please review the weekly narrative [here](https://great-yamamomo-5c3.notion.site/Week-10-Natural-Language-Processing-059b5bfc084a4e8da0f9b86882e7eb86)