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


# ホームディレクトリ
WORKDIR $HOME
# tarファイルをダウンロード
RUN wget "https://github.com/peco/peco/releases/download/v0.5.1/peco_linux_386.tar.gz"
# 解凍
RUN tar xzvf peco_linux_386.tar.gz

WORKDIR $HOME/peco_linux_386
# 実行権限変更
RUN chmod +x peco
# PATHの通っている所にpecoを配置
RUN cp peco /usr/local/bin

ADD ./setting /home/jovyan
