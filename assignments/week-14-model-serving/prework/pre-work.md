# Pre-work: install SAM CLI
For this assignment, we will be using the Serverless Application Model Command Line Interface (SAM CLI) to build and deploy the app. 

SAM CLI is an extension of the AWS CLI that adds functionality for building and testing Lambda applications, and makes it easy for you to create and manage serverless applications. You need to install and configure a few things in order to use the AWS SAM CLI.It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

In addition to an AWS account and Docker, you need to install the SAM CLI.

- for MacOS
    ```
    brew tap aws/tap
    brew install aws-sam-cli 
    ```
    for the second command, you may have to run `arch -x86_64 brew install aws-sam-cli` if you are on M1. 

- Or
    1. Download SAM CLI to a folder of your choice using CURL/WGET or directly using your browser [aws-sam-cli](https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip)

    2. unzip the file to sam-installation

        ```bash
        unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
        ```

    2. Install the AWS SAM CLI.  

        ```bash
        sudo ./sam-installation/install
        ```
    3. Verify the installation using

        ```bash
        sam --version
        ```
        On successful installation, you should see output like the following:

        ```
        SAM CLI, version 1.53.0
        ```

    For more information [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
