from setuptools import setup, find_packages

setup(
    name='markdown-include',
    packages=find_packages(),
    version='0.5.1',
    description='This is an extension to Python-Markdown to include JSON content.',
    author='Mohammad Mohammadi',
    author_email='mohammad@exabyte.io',
    url='https://github.com/Exabyte-io/markdown-include',
    keywords=['Markdown', 'typesetting', 'include', 'plugin', 'extension', 'json'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=[
        "markdown",
    ],
    dependency_links=[
        "https://github.com/Exabyte-io/json_include.git#egg=json_include"
    ],
)
