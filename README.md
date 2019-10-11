# jupyter-Jij のDockerフォルダ




## Docker 
### Docker-composeを用いた仮想環境の立ち上げと終了
jupyter-science folder から以下のコマンドで立ち上げ

```sh
cd middleware

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

