FROM supervisely/base-py-sdk:6.73.158

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y build-essential
RUN apt-get install -y git ffmpeg libsm6 libxext6 ninja-build

RUN python3 -m pip install setuptools==69.5.1
RUN pip3 install torch==2.0.1 torchvision==0.15.2
RUN pip3 install openmim==0.3.7
RUN mim install mmengine==0.7.4 mmcv==2.0.0
RUN pip install yapf==0.40.1

# mmdet
RUN mim install mmdet==3.0.0 "mmcls>=1.0.0rc0"

RUN python3 -m pip install supervisely==6.73.278
RUN python3 -m pip install pycocotools scikit-learn plotly==5.22.0

LABEL python_sdk_version=6.73.278
