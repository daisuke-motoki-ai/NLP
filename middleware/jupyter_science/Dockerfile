#FROM jupyter/datascience-notebook:c411f52fcc93
FROM jupyter/datascience-notebook
## FROM jupyter/base-notebook
MAINTAINER  motoki daisuke <motto.smiley1123@gmail.com>

## USER root
## RUN pip install --upgrade pip && pip install \
##     line_profiler \

#     Flask==0.12.2 requests==2.18.4 
# https://qiita.com/hidehiro98/items/841ece65d896aeaa8a2a

#RUN apt-get update && apt-get -y install \
#    python-lxml \

# RUN conda update conda && conda install -y \
#     scikit-learn \
##    cython

#RUN apt-get update && apt-get -y install \
#    cython
#RUN conda install -y cython 

RUN pip install --upgrade pip && pip install -U cmake 
RUN pip install \
    openjij \
    geopandas \
    descartes
# Docker内で直接pythonを動かすために以下が必要
#RUN conda install -y matplotlib
USER $NB_USER
ENTRYPOINT ["tini", "--"]
CMD ["jupyter", "notebook"]
#ADD [".vimrc", "/home/notebook/jupyter"]
#COPY ["Dockerfile", "/home/notebook/jupyter/"]
#COPY ["momomo", " $HOME/notebook/jupyter/"]
#COPY ./momomo $HOME/notebook/jupyter/
