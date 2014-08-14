from setuptools import setup

setup(
    name='autolink',
    version='0.1',
    author='Alexander Schepanovski',
    author_email='suor.web@gmail.com',

    description='Linkify plain text',
    long_description=open('README.rst').read(),
    url='http://github.com/Suor/autolink',
    license='BSD',

    py_modules=['autolink'],
    install_requires=[
        'six'
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',

        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Filters',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
