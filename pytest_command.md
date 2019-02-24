# pytest command

## -h
ヘルプを出力できる。

## -v
詳細情報を出力する。

## 省略実行

```bash
py.test
========================================================================================================= test session starts =========================================================================================================
platform darwin -- Python 3.6.4, pytest-4.3.0, py-1.8.0, pluggy-0.8.1
rootdir: /Users/hono/Desktop/django2-tdd-book/sample, inifile:
plugins: django-3.4.7
collected 2 items                                                                                                                                                                                                                     

test_math_func.py ..  
```

## -k
キーワード。

pytest -k "add(テスト関数の一部)"

## -m
マーク

```bash
import pytest


@pytest.mark.number
def test_add():
    pass
```

## -tb
トレースバック設定

## --maxfail
何回失敗できるか。

## skip
@pytest.mark.skip(reason='do not run number add test')

If want to show the reason for skips in verbose mode on the termianl,
you can pass -rsx to report skipped tests.

```bash
pytest -v -rsx

SKIPPED [1] test_math_func.py:5: do not run number add test
```

```bash
py.test --help

-r chars              show extra test summary info as specified by chars
                    (f)ailed, (E)error, (s)skipped, (x)failed, (X)passed,
                    (p)passed, (P)passed with output, (a)all except pP.
                    Warnings are displayed at all times except when
                    --disable-warnings is set
```

## -s
print の中身が出力できる。


## 引数つき実行

```bash
@pytest.mark.parametrize('num1, num2, result',
                         [
                             (7, 3, 10),
                             ('Hello', ' World', 'Hello World'),
                             (10.5, 25.5, 36)
                         ])
def test_add(num1, num2, result):
    assert math_func.add(num1, num2) == result
```

