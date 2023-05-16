Lambdaでcurlで手軽に疎通テストしたい。

# なにこれ？

CDKを使ってcurlを実行するLambdaをデプロイするだけ。

# 構成

![](docs/imgs/diagram.png)

構成の出力には https://github.com/pistazie/cdk-dia を使わせて頂いてます！感謝！

レイヤーの中身は[こちら](https://github.com/andey/curl-lambda-layer/tree/master)のものをそのまま利用させていただきました。

# 準備

```
npm install
pip install -r requirements.txt
```

# デプロイ

```
make deploy
```
