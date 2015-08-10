#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import random
import names
import requests
import urlparse
from hashlib import md5
from bs4 import BeautifulSoup

# ARGUMENTS
parser = argparse.ArgumentParser(description='KingSumo Entries Generator.',
                                 prog="queensumo")

parser.add_argument(
    'uri', help='Set the KingSumo URL. e.g.' +
                'http://*****.com/giveaways/****/?lucky=[YOUR_NUMBER]')

parser.add_argument('answer', help='Question answer')

parser.add_argument('-e', '--entries', type=int, required=True,
                    help='Set the amount of entries you need')

parser.add_argument('-v', '--verbose', action='count')
parser.add_argument('-s', '--simulate', action='store_true')

args = parser.parse_args()

# LOGIC

parsedUri = urlparse.urlparse(args.uri)

domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsedUri)
httpReferer = '{uri.path}{uri.query}'.format(uri=parsedUri)
luckyNumber = urlparse.parse_qs(parsedUri.query)['lucky'][0]

emailDomains = ["hotmail.com", "gmail.com", "yahoo.com"]
emailFormats = ['{firstName}{space}{lastName}@{domain}',
                '{firstName}{space}{lastName}{space}{year}@{domain}',
                '{firstName}{space}{year}@{domain}',
                '{firstName}{year}@{domain}',
                '{firstName}@{domain}',
                '{firstName}{lastName}@{domain}',
                '{firstName}{lastName}{year}@{domain}']

if args.simulate:
    print('\033[1;35mThis is a simulation\033[1;m')

print('URL:\t%s' % domain)
print('Answer:\t%s' % args.answer)
print('Lucky:\t%s' % luckyNumber)
print('\n\033[1;35mGenerating %d entries ...\033[1;m\n' % args.entries)

for x in range(0, args.entries):

    # Nonce
    if not args.simulate:
        gRequest = requests.get(args.uri)
        gSoup = BeautifulSoup(gRequest.text, 'html.parser')
        giveawaysNonce = gSoup.find(id="giveaways_nonce")['value']

    # Email
    firstName = names.get_first_name().lower()
    lastName = names.get_last_name().lower()

    randomDomain = emailDomains[random.randint(0, len(emailDomains) - 1)]
    randomSpace = random.choice('._')
    randomYear = random.randint(60, 99)
    randomEmailFormat = emailFormats[random.randint(0, len(emailFormats) - 1)]

    emailAccount = randomEmailFormat.format(firstName=firstName,
                                            lastName=lastName,
                                            year=randomYear,
                                            space=randomSpace,
                                            domain=randomDomain)

    # Signature
    if not args.simulate:
        m = md5()
        m.update(args.answer + '|' + emailAccount)
        giveawaysSig = m.hexdigest()

        querystring = {"lucky": luckyNumber}

        payload = {'giveaways_nonce': giveawaysNonce,
                   '_wp_http_referer': httpReferer,
                   'lucky': luckyNumber,
                   'giveaways_email': emailAccount,
                   'giveaways_answer': args.answer,
                   'giveaways_sig': giveawaysSig
                   }

        response = requests.post(args.uri, data=payload, params=querystring)

    if args.verbose > 0:
        if not args.simulate:
            mailOutput = '%s [ \033[1;36m%s\033[1;m / \033[1;32m%s\033[1;m ]'
            print mailOutput % (emailAccount, giveawaysNonce, giveawaysSig)
        else:
            print "%s" % (emailAccount)
