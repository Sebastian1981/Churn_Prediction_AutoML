FROM python:3.8.3
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./churn_api.py
    
#FROM python:3.8-slim
#WORKDIR /app
#ADD . /app
#RUN apt-get update && apt-get install -y libgomp1
#RUN pip install -r requirements.txt
#EXPOSE 8000
#CMD ["python", "churn_api.py"]