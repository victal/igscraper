#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(browser, email, password, timeout=50):
    browser.get('https://login.ig.com.br/static/html/login-home-2016.html?domain=http://www.ig.com.br/')
    user_input = browser.find_element_by_id('headerFormEmail')
    user_input.send_keys(email)
    passwd_input = browser.find_element_by_id('headerFormSenha')
    passwd_input.send_keys(password)
    browser.find_element_by_id('btn-submit').click()
    WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body.igmail"))
    )
    print('Logged in!')

def get_mailboxes(browser, blacklist=[]):
    elements = browser.find_elements_by_css_selector('#mailboxlist > .mailbox > a')
    mailboxes = [ e.get_attribute('rel') for e in elements ]
    mailboxes = [ box for box in mailboxes if box and box.lower() not in blacklist ]
    return mailboxes

def fetch_emails(browser, box):
    basedir = os.path.join('backup', box)
    if not os.path.isdir(basedir):
        os.makedirs(basedir)

    #get last message id
    files = sorted(os.listdir(basedir))
    last_msg = files[-1] if files else None
    if last_msg:
        max_id = int(last_msg.split('.')[0][6:]) - 1
        print('Last message found: %s' % last_msg)
        print('starting from %s' % str(max_id))
    else:
        browser.get('https://webmail.ig.com.br/?_task=mail&_mbox=%s' % box)
        try:
            msg = browser.find_element_by_class_name('message')
        except Exception:
            return # no messages
        msgid = msg.get_attribute('id')
        assert msgid.startswith('rcmrow')
        max_id = int(msgid[6:])

    source_url = 'https://webmail.ig.com.br/?_task=mail&_action=viewsource&_uid=%s&_mbox=%s'

    for i in range(max_id, 0, -1):
        print("processing message %s" % str(i))
        browser.get(source_url % (str(i), box))
        content = browser.find_element_by_tag_name('pre').text.encode('utf-8')
        msgid = 'rcmrow' + str(i)
        with open(os.path.join(basedir, '%s.eml' % msgid), 'w') as f:
             f.write(content)


