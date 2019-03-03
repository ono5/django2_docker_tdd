# Django Testing

Django で、TDD 手順を確立する。　


# -vv オプション
超詳細情報を出力してくれる。

# POST リクエスト
response の content の中に form から送った情報が入る。

# import 順

1. 標準ライブラリ
2. サードパーティに関連するもの
3. ローカルなアプリケーション/ライブラリに特有のもの

# Nginx Settings
[Ref](https://github.com/Gpzim98/django-apache-nginx-uwsgi-vps-ubuntu)

# Selenium Gruid

[Ref](https://itnext.io/scaling-selenium-test-execution-with-kubernetes-c79bc53979f5)

```bash
make release option="--scale chrome=2"
```

# zalenium  

http://localhost:4444/grid/admin/live

[ref1](https://github.com/zalando/zalenium/blob/master/docs/docker/docker-compose.yaml)  
[ref2](https://opensource.zalando.com/zalenium/)

# Bootstrap

```bash
wget -O bootstrap.zip https://github.com/twbs/bootstrap/releases/download/v3.3.4/bootstrap-3.3.4-dist.zip
unzip bootstrap.zip 
mkdir src/lists/static
mv bootstrap-3.3.4-dist src/lists/bootstrap
```

# Validation at the Database Layer

Web アプリでは、クライアントサイド(JavaScript, HTML5)とサーバーサイドでバリデーションを行うことが可能。
(サーバー側の方がより安全)

Django では、2 つのレベルでバリデーションを行うことが可能。

1 つ目は、model レベルのバリデーション。もう一つは、フォームレベルのバリデーション。

# Context manager Unittest

```bash
With self.assertRaises(ValidationError):
    item.save()
```
Django には、完全検証を手動で実行する full_clean メソッドが存在する。


```bash
def test_validatoin_errors_are_sent_back_to_home_page_template(self):
    response = self.client.post('/lists/new', data={'item_text': ''})
    assert response.status_code == 200
    self.assertTemplateUsed(response, 'home.html')
    expected_error = "You can't have an empty list item"
    self.assertContains(response, expected_error)
```

# HTML Excape
```bash
from django.utils.html import escape

escape("You can't have an empty list item")
```

# Context

To output context text, you can use the below function.

```bash
print(response.content.decode())
```


