#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from selenium import webdriver
from utils import login, get_mailboxes, fetch_emails
from argparse import ArgumentParser


def get_argparser():
    parser = ArgumentParser()
    parser.add_argument('-u', '--email', dest='email', help=u"Email do qual será feito o backup", required=True)
    parser.add_argument('-p', '--passwd', dest='password', help=u'Senha da conta de email', required=True)
    parser.add_argument('--ignore', dest='ignore', nargs='+', help=u'Pastas a serem ignoradas. A lixeira, pasta de spam e rascunhos são ignorados por padrão', required=False)
    return parser


def main():
    parser = get_argparser()
    args = parser.parse_args()
    username = args.email
    password = args.password
    blacklist = ['junk', 'trash', 'drafts']
    if args.ignore:
        blacklist.extend([b.lower() for b in args.ignore])

    if not os.path.isdir('backup'):
        os.makedirs('backup')

    browser = webdriver.Firefox()
    try:
        login(browser, username, password)
        mailboxes = get_mailboxes(browser, blacklist)
        print('The following folders will be backed up:')
        for box in mailboxes:
            print(box)

        for box in mailboxes:
            print('Backing %s up' % box)
            fetch_emails(browser, box)
            print('%s backup complete!' % box)

    finally:
        browser.close()
        print('Backup complete!')

if __name__ == '__main__':
    main()
