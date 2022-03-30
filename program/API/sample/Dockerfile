FROM public.ecr.aws/lambda/python:3.8

COPY src ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt
CMD ["app.handler"]