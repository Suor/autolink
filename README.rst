Autolink
========

Convert URL-like and email-like strings into links.


Installation
------------

::

    pip install autolink


Usage
-----

.. code:: python


    from autolink import linkify

    linkify('some text google.com, ...')
    # -> 'some text <a href="http://google.com">google.com</a>, ...'

    linkify('https://github.com', {'rel': 'nofollow'})
    # -> '<a href="https://github.com" rel="nofollow">https://github.com</a>'

    linkify('me@ya.ru')
    # -> '<a href="mailto:me@ya.ru">me@ya.ru</a>'
