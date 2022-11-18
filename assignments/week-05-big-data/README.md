<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png"
     width="200px"
     height="auto"/>
</p>

# <h1 align="center" id="heading">Subscription Prediction with Delta Lake, PySpark, and MLlib</h1>
During this session, from data collected from direct marketing campaigns of a Portuguese banking institution, you will build a logistic regression model to predict whether a client will subscribe to a term deposit using [Delta Lake](https://delta.io), [PySpark](https://databricks.com/glossary/pyspark), and [MLlib](https://spark.apache.org/docs/latest/ml-guide.html).

## ☑️ Objectives
At the end of this session, you will be able to 

- Load, save, partition data with Delta Lake tables
- Explore data with Spark DataFrames 
- Build a pipeline in MLlib for machine learning workflow
- Fit a logistic regression model, make predictions, and evaluate the model

## :hammer_and_wrench: Pre-Work
### Option I: Databricks Community Edition
Sign up Databricks Community Edition following [official documentation](https://docs.databricks.com/getting-started/community-edition.html). Make sure you follow through ALL six steps. 

For a video demo how to set up Databricks Community Edition, [watch this short video](https://www.youtube.com/watch?v=x3n0bixfP_4&feature=youtu.be&ab_channel=FourthBrainAI). 

Note: It is NOT the same as Free Trial. Free trial lasts 14 days and Databricks uses compute and storage resources in your account ( AWS / Azure / GCP ).

### Option II: Google CoLab
If the first option takes too long, one alternative is to use Google CoLab. Following this [Medium article](https://colab.research.google.com/drive/1jU3IkSTKbB6iHcHr9JYbfp-W0zTRgFWt?usp=sharing) to the section **Get coding**. 

Test it by running this [notebook](https://colab.research.google.com/drive/1jU3IkSTKbB6iHcHr9JYbfp-W0zTRgFWt?usp=sharing) in Google Colab.

For the live session, upload the notebooks under nb folder to your Google Drive, make sure you install `Colaboratory` Add-ons, open the notebook with `Google Colaboratory`, and you are ready to go. Check if all dependencies are met by running the imports.ipynb notebook.

### Option III: Locally
If you are up for a challenge, to run the notebook locally, follow instructions: 
 
- MacOS [(Reference)](https://sparkbyexamples.com/pyspark/how-to-install-pyspark-on-mac/). Spark was written in Scala, but for our purpose (i.e., run `PySpark`), you can skip Scala installation. 

    The following has been tested on macOS Monterey 12.0.1 with M1 chip:
    ```
    # Install OpenJDK 11 (java)
    brew install openjdk@11

    # Install Apache Spark
    brew install apache-spark

    # Activate environment
    conda activate py39_12
    pip install -U pyspark delta-spark
    ```

    If `which pip` is not pointing to your env, then find the path to the correct env, and run the following to finish the installation.
    ```
    /usr/local/Caskroom/miniforge/base/envs/py39_12/bin/python -m pip install pyspark 
    ```

    To verify that you have installed `pyspark` and `delta-spark`, run notebook [imports](nb/imports.ipynb) and make sure no error messages are displayed when importing the packages. 

- Windows [Reference](https://sparkbyexamples.com/pyspark/how-to-install-and-run-pyspark-on-windows/). 

## Background
Please review the weekly narrative [here](https://www.notion.so/Week-5-Big-Data-and-AI-76bc0670bbe5431d90efab0d137716f3)
