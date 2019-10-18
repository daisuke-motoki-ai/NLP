FROM jupyter/datascience-notebook
MAINTAINER  motoki daisuke <motto.smiley1123@gmail.com>

RUN pip install --upgrade pip && pip install -U cmake 
RUN pip install openjij

# 必要なモジュールは以下のような形で連ねて書くこともできる
RUN pip install geopandas \
    descartes \
    dwave_networkx \
    dwavebinarycsp \
    dwave-ocean-sdk \
    networkx \
    jupyter-contrib-nbextensions

USER $NB_USER
ENTRYPOINT ["tini", "--"]
WORKDIR /home/jovyan/.jupyter/
COPY jupyter_notebook_config.py /home/jovyan/.jupyter
RUN mkdir nbconfig
COPY notebook.json /home/jovyan/.jupyter/nbconfig
WORKDIR /home/jovyan/notebook/jupyter
CMD ["jupyter", "notebook"]
