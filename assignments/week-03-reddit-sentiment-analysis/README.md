<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png"
     width="200px"
     height="auto"/>
</p>



# <h1 align="center" id="heading">Sentiment Analysis of Reddit Data using Reddit API</h1>

In this live coding session, we leverage the Python Reddit API Wrapper (`PRAW`) to retrieve data from subreddits on [Reddit](https://www.reddit.com), and perform sentiment analysis using [`pipelines`](https://huggingface.co/docs/transformers/main_classes/pipelines) from [HuggingFace ( 🤗 the GitHub of Machine Learning )](https://techcrunch.com/2022/05/09/hugging-face-reaches-2-billion-valuation-to-build-the-github-of-machine-learning/), powered by [transformer](https://arxiv.org/pdf/1706.03762.pdf).


## ☑️ Objectives
At the end of this session, you will be able to:
- [ ] Know how to work with APIs
- [ ] Feel more comfortable navigating through documentation, even inspecting the source code
- [ ] Understand what a `pipeline` object is in HuggingFace
- [ ] perform sentiment analysis using `pipeline`
- [ ] Run a python script in command line and get the results
- [ ] Examine the quality of data
- [ ] Understand data lineage


## :hammer_and_wrench: Pre-Assignment

### Get the latest MLE-10 repo version

Let's get started by pulling the latest updates from MLE-10!

1. In terminal, navigate to the location of your MLE-10 repository by `cd` to the desired repo. 

2. From there, run the command

     ```console
      git pull
     ```

3. Once that is complete, we'll `cd` into the latest directory

     ```console
     cd week-03-reddit-sentiment-analysis
     ```


### Setting up your environment 🐍🖥️

Activate your Conda environment that you created for Fourthbrain.

1. If Conda is not activate, first activate conda in the terminal

     ```console
     conda activate
     ```

     You should be in the base Conda environment now. 
     This is indicated by `(base)` in the beginning of each line in terminal. 

3. If you are not sure how you named your Fourthbrain environment, list all the current existing environments

     ```console
     conda env list
     ```

     A little star `*` will indicate the current Conda environment.

4. Activate Fourthbrain environment you created in the previous weeks. 
Note to put the name of your environment instead `fourthbrain_env` in the given command.

     ```console
     conda activate frouthbrain_env
     ```

5. Open the jupyter-notebook

     ```console
     jupyter-notebook
     ```

6. Navigate through the repo in the notebook to find `imports.ipynb` for this week and open it.
Run all of the cells in the notebook.


## Background
Please review the weekly narrative [here](https://great-yamamomo-5c3.notion.site/Week-3-Ensuring-High-Quality-Data-e6542a6b93924579b974ba00fd1d1d9a)
