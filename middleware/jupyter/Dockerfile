FROM jupyter/datascience-notebook
MAINTAINER  motoki daisuke <motto.smiley1123@gmail.com>

RUN pip install --upgrade pip && pip install -U cmake 
RUN pip install openjij

# 必要なモジュールは以下のような形で連ねて書くこともできる
RUN pip install geopandas \
    descartes \
    dwave_networkx \
    dwavebinarycsp \
    networkx

RUN pip install dwave-ocean-sdk 

USER $NB_USER
ENTRYPOINT ["tini", "--"]
CMD ["jupyter", "notebook"]
