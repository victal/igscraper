# iGscraper
A simple scraper to backup emails from webmail.ig.com.br 

## The story so far

For those of you who don't know it, iG (internet Grátis, which can be translated as Gratis Internet) 
is a brazilian online service provider that exists since the 1990s, first as a dial-up provider and currently as a content provider (think AOL).

They also provide a webmail service, with an ad-supported tier and paid tiers.
That is, until they decided to unilaterally kill the ad-paid service **without means for the current users to backup their data without paying**.

Seriously, you have to pay about BRL 39 for premium service and IMAP/POP access.

*Or* you can use the script in this repository and backup your emails to a series of .eml files, which can later be imported to a e-mail client such as 
[Thunderbird](https://www.mozilla.org/en-US/thunderbird/) with an addon like [ImportExportTools](https://addons.mozilla.org/en-US/thunderbird/addon/importexporttools/), for example.

## Requirements

This script uses [selenium-python](https://pypi.python.org/pypi/selenium/) and [Firefox](https://www.mozilla.org/en-US/firefox/).

selenium-python can be installed via Pypi with 

```
pip install -U selenium
```

or via your distribution's package manager (Haven't tested the script on Windows, so...)

PRs to make the script do everything via requests or urllib2 are more than welcome, but making it work with PhantomJS instead of Firefox would be nice as well.

## Usage

So, how do you use this thing?

```
usage: ig_scraper.py [-h] [-u EMAIL] [-p PASSWORD]
                     [--ignore IGNORE [IGNORE ...]]

optional arguments:
  -h, --help            show this help message and exit
  -u EMAIL, --email EMAIL
                        Email account to backup
  -p PASSWORD, --passwd PASSWORD
                        Your email password. 
  --ignore IGNORE [IGNORE ...]
                        Folders to be ignored (case-insensitive). Spam, Trash and Drafts are ignored by default
```

## License

MIT
