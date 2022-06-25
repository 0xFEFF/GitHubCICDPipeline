FROM python:3.9-slim

# setting up environment
WORKDIR /srv/flask_app

# copying the necessary files 
COPY rest_api.py ./
COPY start.sh ./
COPY ./uwsgi/uwsgi.ini ./

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential \
    && rm -rf /var/lib/apt/lists/*


# install needed python packages
COPY requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt 

COPY ./nginx/nginx.conf /etc/nginx
RUN chmod +x ./start.sh
CMD ["./start.sh"]