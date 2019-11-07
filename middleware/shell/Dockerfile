#FROM jupyter/minimal-notebook
FROM middleware_jupyterbase
MAINTAINER  motoki daisuke <motto.smiley1123@gmail.com>
#####------------------------------
#####  shell & editor environment 
#####------------------------------
USER root
RUN apt-get update && apt-get install -yq --no-install-recommends \
      zsh \
      tmux \
      vim
# これらの設定ファイルはローカルに置いておけるようにする
