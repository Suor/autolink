from autolink import linkify


def test_simple():
    assert linkify('a http://example.com link') \
        == 'a <a href="http://example.com">http://example.com</a> link'
    assert linkify('a https://ya.ru link') \
        == 'a <a href="https://ya.ru">https://ya.ru</a> link'
    assert linkify('a example.com link') \
        == 'a <a href="http://example.com">example.com</a> link'

def test_query():
    assert linkify('xx.com/?a=hi&b=bye') \
        == '<a href="http://xx.com/?a=hi&amp;b=bye">xx.com/?a=hi&b=bye</a>'

def test_fragment():
    assert linkify('http://xx.com/path#frag') \
        == '<a href="http://xx.com/path#frag">http://xx.com/path#frag</a>'

def test_port():
    assert linkify('foo.com:8000') \
        == '<a href="http://foo.com:8000">foo.com:8000</a>'
    assert linkify('foo.com:xkcd') \
        == '<a href="http://foo.com">foo.com</a>:xkcd'

def test_complete():
    assert linkify('https://user:pass@ftp.mozilla.org/x/y.exe?a=b&c=d&e#f')           \
        == '<a href="https://user:pass@ftp.mozilla.org/x/y.exe?a=b&amp;c=d&amp;e#f">' \
           'https://user:pass@ftp.mozilla.org/x/y.exe?a=b&c=d&e#f</a>'


def test_non_domain():
    assert linkify('ha.ha') == 'ha.ha'

def test_bad_protocols():
    assert linkify('foohttp://bar') == 'foohttp://bar'
    assert linkify('fohttp://exampl.com') \
        == 'fohttp://<a href="http://exampl.com">exampl.com</a>'

def test_uppercase():
    assert linkify('HTTP://EXAMPLE.COM') \
        == '<a href="HTTP://EXAMPLE.COM">HTTP://EXAMPLE.COM</a>'


def test_punct():
    assert linkify('http://example.com.') \
        == '<a href="http://example.com">http://example.com</a>.'
    assert linkify('http://example.com,') \
        == '<a href="http://example.com">http://example.com</a>,'


def test_wrapping_parentheses():
    assert linkify('(example.com/)') \
        == '(<a href="http://example.com/">example.com/</a>)'
    assert linkify('example.com/hi_(there)') \
        == '<a href="http://example.com/hi_(there)">example.com/hi_(there)</a>'
    assert linkify('(example.com/hi_(there))') \
        == '(<a href="http://example.com/hi_(there)">example.com/hi_(there)</a>)'


def test_attrs():
    assert linkify('ya.ru', attrs={'rel': 'nofollow'}) \
        == '<a href="http://ya.ru" rel="nofollow">ya.ru</a>'


def test_email():
    assert linkify('mailto:me@ya.ru') \
        == '<a href="mailto:me@ya.ru">mailto:me@ya.ru</a>'
    assert linkify('me@ya.ru') \
        == '<a href="mailto:me@ya.ru">me@ya.ru</a>'


def test_nonascii():
    assert linkify(u'http://\u5350.net/') \
        == u'<a href="http://\u5350.net/">http://\u5350.net/</a>'


def test_nested_email():
    assert linkify('http://example.com?email=foo@example.com') \
        == '<a href="http://example.com?email=foo@example.com">' \
           'http://example.com?email=foo@example.com</a>'
