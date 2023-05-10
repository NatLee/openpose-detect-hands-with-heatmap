FROM tensorflow/tensorflow:1.15.0-gpu-py3
ENV TZ=Asia/Taipei \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /src
COPY ./src /src
COPY ./requirements.txt /src

RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub 
RUN apt-get update && \
    apt-get install -y tzdata

RUN python -m pip install --upgrade pip
# ========================
RUN pip install opencv-python-headless==4.5.5.64
# ========================
RUN pip install -r requirements.txt
RUN chmod a+x docker-entrypoint.sh