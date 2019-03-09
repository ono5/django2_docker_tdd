# GitLab

```bash
# GitLab コンテナイメージの起動
docker run --detach \
  --hostname gitlab.example.com \
  --publish 443:443 --publish 80:80 --publish 22:22 \
  --name gitlab \
  --restart always \
  --volume /Users/hono/docker/gitlab/config:/etc/gitlab \
  --volume /Users/hono/docker/gitlab/logs:/var/log/gitlab \
  --volume /Users/hono/docker/gitlab/data:/var/opt/gitlab \
  gitlab/gitlab-ce:rc
```

# git clone

git clone は、ip指定で行う。

```
git clone git@localhost:root/qplathome.git
```

# 継続的インテグレーション
継続的インテグレーションツールとは、アプリケーションのビルドや単体テストのオペレーションを自動化し、
品質を維持するためのツール。

* 品質の維持
  - リポジトリへのコミットタイミングなどで、小さな変更ごとにビルドとテストを繰り返し行うことにより、
  　 ライブラリのリンク確認やソースコードのバグを確認できる

* 作業コストの削減
  - 自動化することにより、ビルドやテスト作業の手間を省き、簡単かつ均一な作業を提供できる。

* 継続的な分析と改善
  - ビルドやテストを行うたびにログをレポーティングすることによって、結果を動的に表示することで改善に繋げられる。
  
GitLab の 「CI/CD」 のジョブ機能を使用することで、ビルドツールやテストツールと連携したインテグレーションの自動化が可能。

# GitLab Runner
GitLab Runner とは、GitLab CI/CD 上から支持されたスクリプトを実行したり、一時的に Docker コンテナを生成してジョブを実行したりするプロセス。

GitLab CI/CD は、かく Runner にビルド実行を要求し、その結果を管理する役割を担う。

実際のビルド作業を行うのは、Runner が別プロセスでビルドやテストジョブを実行する仕組みになっている。

-> ビルド用のパソコンに Runner を起動させる?

# Executor の種類
Runner は、ジョブを実行するプラットフォームに応じて、「Executor」と呼ばれるジョブの実行方式があり、
Runner を GitLab CI/CD に登録する時点で Executor を選択する必要がある。

* Shell Executor  
Runner が導入されているサーバー上で、ビルドやテストを実行できるシンプルな Executor。  
Linux -> Bash, Windows -> Bash on Windows or WInsows PowerShell で実行。

* Docker Executor
Docker API を通して Docker Engine と接続することにより、コンテナからかくビルド作業を実行する。  
コンテナイメージを用意しておくことで、どのプラットフォームでも再現性のあるビルドやテストが実行可能。

* VirtualBox Executor
VirtualBox の VM を利用したビルド環境を提供します。
VM 上の SSH を経由してビルドやテストを実行するため、SSH と Bash さえ動作すれば、VirtualBox 上で稼働する
全ての VM に対応しています。  
また、Windows VM からも Cygwin にて実行可能です。

* SSH Executor
Ruuner から SSH 接続可能な特定のサーバーに対して、コマンドを SSH 経由で送りつけるシンプルな Executor。
リモート接続先のサーバー上で、Bash やスクリプトを実行できる。

* Kubernetes Executor 
Kubernetes API 経由でクラスタ上の Pod を作成してビルドを実施する。
Kubernetes の Pod は、.gitlab-ci.yml 内で定義された Service パラメータごとに新たにコンテナが生成され、ビルドやテストを実施する。

Docker が一番望ましい。
                                       Shell            Docker
- ジョブごとに新しい環境で実施できる         -                 o
- Runner が稼働するサーバーを移動できる      -                 o
- 複雑なビルド実行ができる                  n                 o
- トラブルシューティング                 比較的容易          普通

# Runner の種類
Shared Runners と Specific Runners の 2 種類の利用方法が存在する。

## Shared Runners
複数のプロジェクトのジョブ実行を、共有の Runner で処理する方式。

Shared RUnners の登録には、管理者ユーザー権限が必要であり、[Admin Area] にある登録用のトークンを使用する。

[Admin Area] -> [Overview] -> [Runners] から確認できる。

## Specific Runners 
特定のプロジェクトのジョブのみを実行する方式。

Specific Runners では、タグなどを利用して、特定のジョブのみを処理するように設定しておくと、
リソースを有効に利用できる。

Specific Runner の登録には、プロジェクトページの [Settings] -> [CI/CD] -> [Runners settings] セクションにある
登録用トークンを使用する。

また、プロジェクトで Shared Runners の利用を避けたい場合は、どうページ上の [Disable Shared Runners] を押下すると
Specific Runners のみを利用する構成になる。

## Runner の制限項目
Runner には、制限を儲けることも可能。

* Runner untagged jobs
ユーザーがランナーにタグを割り当てていない時、タグ付きジョブを選択できなくするオプション。

* Lock to current projects
他のプロジェクトから指定の Runner が利用できないようにロックするオプション。

### Runner のインストール手順

```bash
docker run -d --name gitlab-runner --restart always \
-v /Users/hono/docker/gitlab-runner/config:/etc/gitlab-runner \
-v /var/run/docker.sock:/var/run/docker.sock \
gitlab/gitlab-runner:latest

# gitlab と gitlab runner を同一 network に所属させる
docker network create -d bridge gitlab_network
docker network connect --alias=gitlab.example.com gitlab_network gitlab
docker network connect gitlab_network gitlab-runner

# 接続確認
docker container exec -it gitlab-runner curl http://gitlab.example.com

<html><body>You are being <a href="http://gitlab.example.com/users/sign_in">redirected</a>.</body></html>
```

### Runner の登録

```bash
docker container exec -it gitlab-runner gitlab-runner register

gitlab.example.com
okenwHjwyoLKxY7pPhfb
```

## GitLab CI/CD Jobs の基本設定
GitLab CI/CD では、複数のプロジェクト間で共通の Runner を利用する場合、ジョブの設定は、プロジェクトごとに行う。

プロジェクトのリポジトリのソースコードに変更が行われた時、ジョブに定義されたビルドやテストを動的に実行し、
アーティファクタの信頼性を常に担保する。

ジョブは、「.gitlab-ci.yml」ファイルに定義し、これをプロジェクトリポジトリのトップディレクトリに隠しファイル形式で、
コミットすることにより、動的にジョブが登録される仕組みになっている。

ブランチを利用した場合は、異なるジョブも定義できる。

[YAMLの記法](https://yaml.org/spec/1.2/spec.html)


|パラメータ|内容|
|:------|:------|
|scripts|Runner 上で実行されるスクリプトやコマンドを指定|
|image|コンテナを利用する Executor の Docker イメージを指定|
|services|コンテナを利用する Executor の Docker サービスを指定|
|stage|ジョブのステージ設定|
|variables|ジョブ内で利用される変数定義|
|only|指定したブランチ、およびタグの更新があった場合のみジョブが実行|
|except|指定した以外のブランチ、およびタグの更新があった場合のみジョブが実行|
|tags|実行する Runner のタグを指定|
|allow_failure|失敗することを許可するか否かを指定|
|when|特定の条件にマッチした場合のみジョブを実行|
|dependencies|アーティファクトを他のジョブ間で受け渡す際のアーティファクトの指定|
|artifcts|ジョブのアーティファクトの保存を定義|
|cache|プロジェクトワークスペース内にあるパスを使用して、ジョブ間のファイルキャッシュのリストを指定|
|before_script|script の前に行うタスクを定義|
|after_script|script の後に行うタスクを定義|
|retry|ジョブが失敗しても動的にリトライを行う回数を指定|











