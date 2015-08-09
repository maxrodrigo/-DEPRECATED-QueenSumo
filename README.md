# QueenSumo
QueenSumo is a tool for generating KingSumo’s Giveaways entries.
Basically it creates random emails ( name.lastname@domain.com ) using Trey Hunner’s library [names](https://github.com/treyhunner/names) and POST it to the given URL.
It automatically searches for the [nonce](https://codex.wordpress.org/WordPress_Nonces) and generates a signature string for the registration.

## Getting Started
Clone the repository

```
git clone [https://github.com/wxrod/QueenSumo.git]()
```

The basic third-party dependencies are: __names__, for generating random email accounts, __requests__, for making the form POST and __BeautifulSoup__, for parsing the page and get the nonce. These libraries can be easily installed by executing. ( You may need sudo permissions)

```
pip install requirements.txt
```

You’re ready!

## Usage

```
queensumo [-h]() -e ENTRIES [-v]() [-s]() uri answer
```

## Parameters
* uri KingSumo's giveaway URL
* answer Answer to the giveaway question. Copy this from the URL
* --entries -e Set the amount of entries you want. (required)
* --verbose -v Print the generated email accounts with nonce and the signature
* --simulate -s Simulate the process without posting to the URL

## Example

This generate 1 entry for sublime text giveaway

```
./queensumo.py -e 1 -v http://sublimetexttips.com/giveaways/win-sublime-text/?lucky=###### 'Sublime Text!!!'
```

## Version
1.0

## Notes
For feedback and bug reports use [Issues](https://github.com/wxrod/QueenSumo/issues).

Like QueenSumo ? Follow the repository on GitHub.

