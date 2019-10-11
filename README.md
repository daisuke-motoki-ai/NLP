# jupyter notebook (debian:jessie base) のDockerプロジェクト

## リンク

- [software](./software/software.md)
- [middleware](./middleware/middleware.md)


## CI（継続的インテグレーション）ツール
	
### GUIの自動化
[MacBookのGUI操作をAutomatorで記録して自動化する](http://d.hatena.ne.jp/zariganitosh/20090129/1233271424)

## Docker 
### Docker-composeを用いた仮想環境の立ち上げと終了
jupyter-science folder から以下のコマンドで立ち上げ

```sh
% docker-compose -f ./middleware/docker-compose.yml up -d --build                
```

以下のコマンドをブラウザ上のURLに書き込む

```sh
http://localhost:8285/
```


以下のコマンドで終了

```sh
% docker-compose -f ./middleware/docker-compose.yml down                            
```

### Dockerの中に入る方法

以下で実行中のDocker コンテナを確認
```bash
% docker ps                                                                                                                                                                           ⮀ INSERT ⮀
CONTAINER ID        IMAGE                COMMAND                  CREATED             STATUS              PORTS                    NAMES
db5bfd557a95        middleware_science   "tini -- jupyter n..."   43 hours ago        Up 43 hours         0.0.0.0:8285->8888/tcp   middleware_science_1
```
次にコンテナの中に入る

```
docker exec -i -t db5bf bash
```


## git
ref. 10倍速の開発・運用ツール（雑誌）pp18

フォルダは一つのgitで管理する．ミドルウェア・ソフトウェアの役割分担は，gitのブランチに任せる．
これでgitのブランチ毎にcommitして，それをJenkinsが別々に処理してくれれば，ビルド＆テストも役
割毎にログが残りいい感じになる．


**gitのブランチ間の関係**

ブランチごとにドキュメントを作成して，ドキュメントもまとめてコミットする．
![Kobito.XIze08.png](https://qiita-image-store.s3.amazonaws.com/0/65815/ed131a5a-1b9e-5587-38ab-01babd2fb656.png "Kobito.XIze08.png")



## メモ

1. Docker関連  
docker-compose.yml にpythonフォルダのCOPY命令をするようにかく．  
[docker-compose.ymlが環境別にある場合は〜](...)


1.  git関連  
masterブランチに間違えてコミットしまくったので，change3ブランチにコミットを繋げ変える．  

1. markdown viewer   
Chrome から見れるようにできるらしい．  
[ブラウザでMarkdownを表示する方法]()	


