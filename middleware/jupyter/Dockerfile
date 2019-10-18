FROM jupyter/datascience-notebook
MAINTAINER  motoki daisuke <motto.smiley1123@gmail.com>

# # ROOTにパスワードをセット
# RUN echo 'root:newpassword' |chpasswd
# 
# # ユーザを作成
# RUN useradd newuser
# RUN echo 'newuser:newuserpass' |chpasswd
# RUN echo "newuser    ALL=(ALL)       ALL" >> /etc/sudoers


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
USER $NB_USER
ENTRYPOINT ["tini", "--"]

# WORKDIR /home/jovyan/.jupyter/
# COPY jupyter_notebook_config.py /home/jovyan/.jupyter
# RUN mkdir nbconfig
# COPY notebook.json /home/jovyan/.jupyter/nbconfig
## Install Jupyter-vim-binding
RUN git clone --quiet https://github.com/lambdalisue/jupyter-vim-binding $(jupyter --data-dir)/nbextensions/vim_binding && \
    jupyter nbextension enable vim_binding/vim_binding

WORKDIR /home/jovyan/notebook/jupyter
CMD ["jupyter", "notebook"]
