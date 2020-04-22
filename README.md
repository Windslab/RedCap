<h1 align="center">Welcome to RedCap ⛑</h1>

<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/Version-1.1-green.svg" />
  <img alt="Version" src="https://img.shields.io/badge/Google-Chrome-blue" />
  <img src="https://img.shields.io/badge/Python-%3E%203.8-blue.svg" />
  <img src="https://img.shields.io/badge/Selenium-%3E%203.141-blue.svg" />
</p>

> That's script will automatically up to date or send your Curriculum Vitae to hh.ru. You are beautiful and worthy to have a nice job!

## Install

1. Download and install a [Google Chrome](https://www.google.com/intl/en/chrome/) unless you don't have it.
2. Download this repository as [ZIP](https://github.com/Windslab/RedCapBot/archive/master.zip) file and unpack.
3. Download and install [Python](https://www.python.org/downloads/)
4. Install Selenium from `cmd`:

```sh
py -m pip install selenium
```

## Preferences
**1. for UPDATE your Curriculum Vitae**
* Script will be automatically update your CV each a few moments. You should not close your [Google Chrome](https://www.google.com/intl/en/chrome/) window.

**2. for SEND your Curriculum Vitae**
* Configure your `url` with filters and wage expectation, it should looks like thise:
```sh
url = https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&text=Engineer&page=
```
* Put name of your already created CV to `name`.
* Type the Cover Letter text to `letter`.
* Choiche a start `page` from `0` to `39`.
* The `sent` variable is current reply count of CV. For 24 hour you have ability to send untill 200 CVs.

```sh
url = https://hh.ru/search/vacancy?***&page=
name = Your CV name
letter = Hello, please take a look to my CV.
page = 0
sent = 0
```

## Usage

1. Run script by link file:

```sh
run.bat
```

2. Decide between two alternatives `Update` or `Send` your Curriculum Vitae.

## License

Copyright 2020 [Yevgeny Shevchenko](https://github.com/windslab/RedCap)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.