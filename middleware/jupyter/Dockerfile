FROM jupyter/datascience-notebook
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
USER $NB_USER
ENTRYPOINT ["tini", "--"]

#  ref https://github.com/pollenjp/shell_script_for_setup/blob/30daf8f14e7e71b60af0a9fa04c3771121d6f93c/python-setup/pyenv-default-python3.5.2/pyenv-default-python3.5.2-install_jupyter-extensions.sh
#####------------------------------
#####  Jupyter Extensions
#####------------------------------
RUN jupyter contrib nbextension install --user
RUN git clone --quiet https://github.com/lambdalisue/jupyter-vim-binding $(jupyter --data-dir)/nbextensions/vim_binding && \
    jupyter nbextension enable vim_binding/vim_binding
RUN jupyter nbextension enable python-markdown/main  # MarkdownセルでPythonの変数を表示可能
RUN jupyter nbextension enable toc2/main             # TableOfContents


RUN pip install jupyterthemes
RUN pip install --upgrade jupyterthemes
RUN jt -t onedork -fs 95 -altp -tfs 11 -nfs 115 -cellw 88% -T


#####------------------------------
#####  Work directry
#####------------------------------

WORKDIR /home/jovyan/notebook/jupyter
CMD ["jupyter", "notebook"]
