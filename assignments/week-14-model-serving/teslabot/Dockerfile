#FROM public.ecr.aws/lambda/python:3.8
FROM amazon/aws-lambda-python:3.8
RUN yum install gcc -y
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
COPY ./get_model.py ${LAMBDA_TASK_ROOT}
RUN python ${LAMBDA_TASK_ROOT}/get_model.py
COPY . ${LAMBDA_TASK_ROOT}
CMD [ "app.handler" ]