vue-flask
=========

vueとflaskを使ったサーバのテンプレート。
勉強用です。

- Flask(Web & API Server)
- Vue.js(Front)
  - axios(非同期API通信)
- npm
- Vue Router不使用

## Requirements

- Docker
- Docker-Compose

## Installation

初回起動時はfrontコンテナに入って以下のコマンドを叩く必要があります

```
# npm install --save axios
```

## build

frontコンテナでbuild

```
npm run build
```

## Todo?

- .dockerignore作る
- コンテナ間通信を利用してVue.jsのAPI Proxyを利用したい
  - 現状ではdev環境は利用できない…
- 初回起動時の`npm install`はなくしたい

## 参考

- [Vue.js(vue-cli)とFlaskを使って簡易アプリを作成する【前半 - フロントエンド編】](https://qiita.com/mitch0807/items/2a93d93adbf6b5fc445c)
- [Vue.js(vue-cli)とFlaskを使って簡易アプリを作成する【後半 - サーバーサイド編】](https://qiita.com/mitch0807/items/c2e84beee6c9a61e86cd)
- [gtalarico/flask-vuejs-template](https://github.com/gtalarico/flask-vuejs-template)