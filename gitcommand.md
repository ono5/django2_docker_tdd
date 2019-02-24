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



