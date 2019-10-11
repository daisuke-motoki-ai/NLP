# Jupyter上でopenJijを利用するための仮想環境
## Docker-composeを用いた仮想環境の立ち上げと終了
jupyter-Jij/middleware ディレクトリから以下のコマンドで立ち上げ

```sh
docker-compose -f docker-compose.yml down && docker-compose -f docker-compose.yml up -d --build && docker-compose exec science bash
```

そのままターミナル上で以下コマンドを打ち込みTokenを取得（そのうちToken必要ないようにします。）
```sh
jupyter notebook list
```

以下のコマンドをブラウザ上のURLに書き込む

```sh
http://localhost:8285/
```


以下のコマンドで終了

```sh
% docker-compose -f ./middleware/docker-compose.yml down                            
```

