FROM jupyter/minimal-notebook
MAINTAINER  motoki daisuke <motto.smiley1123@gmail.com>

#####------------------------------
#####  python module install
#####------------------------------
RUN yes | pip install --upgrade pip
RUN yes | pip install --quiet -U cmake
RUN yes | pip install --quiet --no-cache-dir \
    openjij \
    geopandas \
    descartes \
    networkx \
    jupyter-contrib-nbextensions \
    dwave_networkx \
    dwavebinarycsp \
    dwave-ocean-sdk


RUN yes | pip install --quiet --no-cache-dir \
    mecab-python3