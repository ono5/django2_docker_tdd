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

# Django Form

* They can process user input and validate it for errors.
* They can be used in templates to render HTML input elements, and error messages too.
* And, as we'll see later, some of them can even save data to the database for you.

# Cross-Site Request Forgery in AJAX requests
With the CSRF protection active, Django checks for a CSRF token in all POST requests.
It is a bit inconvenient for AJAX requests to pass the CSRF toekn as a POST data in with every post reqeust.

Therefore, Django allows you to set a custom X-CSRFToken header in your AJAX requests with the value
of the CSRF token.

This allow you to set up jQuery or any other jQuery or any other JavaScript library to automatically 
set the X-CSRFToken header in every request.

Take the following steps

1. Retrieve the CSRF token from the csrftoken cookie, which is set if CSRF protection is active
2. Send the token in the AJAX request using the X-CSRFToken header

[Ref](https://docs.djangoproject.com/ja/2.1/ref/csrf/#ajax)

```bash
# 1
<script src="https://cdn.jsdelivr.net/npm/js-cookie@2/src/js.cookie.min.js"></script>
<script>
    # 2
    var csrftoken = Cookies.get('csrftoken');
    # 3
    function csrfSafeMethod(method) {
        // these Http methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    # 4
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
</script>
```

1. JS Cookie is a lightweight JavaScript for handling cookies.
[Ref](https://github.com/js-cookie/js-cookie)

2. We read the value of the csrftoken cookie iwth Cookies.get().

3. We define the csrfSafeMethod() function to check whether an HTTP method is safe.
   Safe methods don't require CSRF protection - these are GET, HEAD, OPTIONS, and TRACE.
   
4. We set up jQuery Ajax requests using $.ajaxSetup(). Before each AJAX request is performed,
   We check whether the request method is safe and the current request is not cross-domain.
   If the request is unsafe, we set the X-CSRFToken header with the value obtained from the cookie.
   This setup will apply to all AJAX requests peforemed with jQuery.

The CSRF token will be included in all AJAX requests that use unsafe HTTP methods, such as POST or PUT.


