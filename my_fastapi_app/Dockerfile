FROM python:3.9

# ADD ./my_fastapi_app /my_fastapi_app
# ADD ./entrypoint.sh /my_fastapi_app
WORKDIR /my_fastapi_app

COPY my_fastapi_app . 

RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y