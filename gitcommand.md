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

