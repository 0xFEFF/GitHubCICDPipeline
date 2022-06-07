FROM python:3 

# setting up environment
WORKDIR /usr/src/app 

# install needed python packages
COPY requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt 

COPY ./rest_api.py ./ 

CMD ["python", "rest_api.py"]