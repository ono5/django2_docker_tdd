# 変更差分を確認する

何の変更をしたのか確認する。

## stage 追加前
git diff

## stage 追加後
git diff --staged

# Git からファイルを削除

パスワードファイルなど誤って Git に乗せてしまった場合の対処方法。

```bash
# ファイルこと削除
git rm <ファイル名>
git rm -r <ディレクトリ名>

# ファイルを残しておきたいとき
git rm --cached <ファイル名>

# 元に戻す
git reset HEAD index.html
git checkout index.html

```

# ファイルの変更を取り消す

```bash
git checkout -- <filename>
git checkout -- <dirname>

git checkout -- .
```

# ステージの変更を取り消す

指定した返納をステージから取り消す。
ワークツリーのファイルに影響を与えない。

```bash
git reset HEAD <filename>
git reset HEAD <dirname>

git reset HEAD .
```
HEAD は、最新のコミットという意味。

# 超然のコミットの修正

```bash
git commit --amend
```

ただし、リモートレイポジ取りに Push したコミットのやり直しはしてはならない。

```bash
git log -p -n 1
commit e98cdf54db64cd4e13123143dca65598dc1b5ddc (HEAD -> master)
Author: ono5 <kuroneko_head_lord@yahoo.co.jp>
Date:   Sun Feb 24 23:23:55 2019 +0900

    git commit --amend を追記

diff --git a/index.html b/index.html
index 598d314..c16fb95 100644
--- a/index.html
+++ b/index.html
@@ -1,3 +1,4 @@
 <h1>Git Tutorial</h1>
 <p>git status</p>
 <p>git diff</p>
+<p>git commit --amend</p>
```


# ブランチの情報を表示

```bash
$ git branch -a
* (HEAD detached at origin/master)
  master
  remotes/origin/master
  
# 情報を取り込む  
git merge origin/master
```

# ブランチを切り替える

```bash
git checkout <branch name>
```

# git fetch
fetch は、リモートリポジトリからローカルリポジトリへコピーするコマンド。
ワーキングディレクトリに反映されない。

# git pull
リモートから情報を取得し、マージまで行う。

```bash
git pull <remote name> <branch name>

or

git pull
```

# fetch と pull の使い分け

git pull を行うと、現在、自分のいるブランチに統合されてしまうので、注意が必要。

git pull を行うときは、master ブランチにいる場合のみ、など運用ルールが必要。

# ブランチの新規作成

```bash
git branch <branch name>
git branch feature
```

# ブランチの一覧表示

```bash
git branch

git branch -a


git log --oneline --decorate
7c065ba (HEAD -> feature, origin/master, master) Update home.html
```

# ブランチの切り替え

```bash
git checkout <branch name>
git checkout feature

# ブランチを新規作成して、切り替える
git checkout -b <branch name>

# push
git push origin feature
```

# 変更履歴をマージ

```bash
git merge <branch name>
git merge <remote name/branch name>
git merge origin/master
```

master ブランチに feature ブランチの内容を取り込みたい場合は、master ブランチで、
git merge feature とうつ。

# ブランチを使用した開発の流れ

* master ブランチ
  * リリース用のブランチとして作成
* 開発
  * トピックブランチを作成
  
# プルリクエスト
自分の変更したコードをリポジトリに取り込んでもらえるよう依頼する機能。

1. master ブランチを最新に更新
2. ブランチを作成
3. ファイルを変更
4. 変更をコミット
5. GitHubへプッシュ
6. プルリクエストを送る
7. コードレビュー
8. プルリクエストをマージ
9. ブランチを削除　

# ローカルレポジトリを綺麗にする

1. git branch -D master
2. git fetch
3. git branch master origin/master
4. git merge origin/master
5. git status
6. git add .
7. git commit
8. git push origin pull_request
9. git checkout master
10. git pull origin master
11. git branch -d pull_request

# Git Hub フロー

|--------local----------|  
1. master ブランチからブランチを作成
2. ファイルを変更し、コミット
3. 同名のブランチを GitHub へプッシュ
|--------remote----------|  
4. プルリクエストを送る
5. コードをレビューし、master ブランチにマージ
6. master ブランチをデプロイ(本番サーバーへ)


@ポイント  
* master ブランチは常にデプロイできる状態に保つ
* 新開発は、master ブランチから新しいブランチを作成してスタート
* 作成した新しいブランチ上で作業し、コミットする。
* 定期的に Push する
* master にマージするためにプルリクエストを使う
* 必ずレビューを受ける
* master ブランチにマージしたらすぐにデプロイする
  (テストとデプロイ作業は自動化)
  
# リベース
変更を統合する際に、履歴を綺麗に整えるために使うのがリベース。

```bash
git rebase <branch name>
```

