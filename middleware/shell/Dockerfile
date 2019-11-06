FROM ubuntu:18.04

#####------------------------------
#####  python virtual environment
#####------------------------------
RUN apt update && apt install -y \
      software-properties-common \
      python3.7 \
      python3-pip
RUN add-apt-repository ppa:deadsnakes/ppa

#####------------------------------
#####  shell & editor environment 
##### > もう一つのコンテナはjupyter environmentで構成
##### > python env までを先にbuild して その他は依存関係にする
#####------------------------------

# Common packages
RUN apt update && apt install -y \
      zsh \
      tmux \
      vim

# これらの設定ファイルはローカルに置いておけるようにする


#####------------------------------
#####  processing on terminal
#####------------------------------
