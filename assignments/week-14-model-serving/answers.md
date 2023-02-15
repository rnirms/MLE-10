## Interview Readiness

* <i> What are 3 advantages of deploying using Model Serving methods Vs. deploying on GitHub Pages or HuggingFace for free? </i>
Compared to deploying for free on GitHub pages or HuggingFace, model serving methods allow for more scalability, performance and security. 
  * <b> Scalability </b>: Model serving methods allow ML models to be deployed on scalable infrastructure that can handle large volumes of traffic. Depending on traffic the systems scale up or down as needed, so that the deployed models are always available to serve incoming requests. The free API for inference endpoints on Huggingface or Github pages apply rate limits and cannot guarantee availability. 
  * <b> Performance </b>: Unlike the free services, model serving methods use specialised hardware such as GPUs and TPUs, in their infrastructure that improves the performance for ML model inference. 
  * <b> Security </b>: Model serving methods provide robust security features such as encryption, authentication, and access controls to ensure that the deployed model is protected from unauthorized access or tampering. These features are especially important when deploying sensitive or confidential models. GitHub Pages and HuggingFace do not offer the same level of security, and models deployed on these platforms may be more vulnerable to attacks. Only with the Enterprise plan, additional layers of security is provided in HuggingFace. 


* <i> What is ML model deployment? </i>
Model deployment is the process of making a machine learning model available for use in a production environment, either through a web API, serverless function, containerization, or directly on a mobile or edge IoT device.

* <i> What is Causal Inference and How Does It Work? </i>
Causal inference is a statistical method used to determine the cause-and-effect relationship between variables. It involves the use of observational data to infer causality by controlling for confounding variables. Randomized controlled trials achieve this by creating a treatment and control group, and study participants are randomly assigned to either of the groups. The only difference is the treatment itself and so the RCT allows us to see if the treatment causes the observations. The key to causal inference is to control for confounding variables. 

* <i> What is serverless deployment and how its compared with deployment on server? </i>
Serveless deployment is a method to deploy ML models (or any software) using third party services to provide infrastructure to run the inference/application. This way the developer needs to focus only on model development and the cloud service provider manages the underlying servers, operating systems etc. The application is broken down into small functions (e.g. AWS Lambda functions) that can respond to requests for inference or database changes etc. 

When deploying on a server - even using a cloud service provider such as Amazon EC2 instance - the developer needs to provision the environment and manage it.  

  There are many advantages to serverless deployments: 
    * They more cost effective than deployment on a server as they are charged for compute time usage and not for pre-provisioned servers. 
    * Maintenance is easy as all security updates etc is managed by the cloud service provider.

  Drawbacks of serverless deployment vs deployment on a server are: 
    * It is non-trivial to move from one cloud service provider to another. 
    * Functionality is limited - for instance, the applications need to be event-driven for serverless setup. 
