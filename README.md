# QueenSumo
QueenSumo is a tool for generating KingSumo’s Giveaways entries.
It creates a random email, searches for the [nonce](https://codex.wordpress.org/WordPress_Nonces), generates a signature string and POST those values to the given URL.
For the emails I used Trey Hunner’s library [names](https://github.com/treyhunner/names) for the names and make a list of email templates where {space} is "." or "_" and {year} is a number between 60 and 99.
* {firstName}{space}{lastName}@{domain}
* {firstName}{space}{lastName}{space}{year}@{domain}
* {firstName}{space}{year}@{domain}
* {firstName}{year}@{domain}
* {firstName}@{domain}
* {firstName}{lastName}@{domain}
* {firstName}{lastName}{year}@{domain}

## Getting Started
Clone the repository

```sh
git clone https://github.com/wxrod/QueenSumo.git
```

The basic third-party dependencies are: __names__, for generating random email accounts, __requests__, for making the form POST and __BeautifulSoup__, for parsing the page and get the nonce. These libraries can be easily installed by executing. ( You may need sudo permissions)

```sh
cd QueenSumo
pip install -r requirements.txt
```

You’re ready!

## Usage

```sh
queensumo [-h] -e ENTRIES [-v] [-s] uri answer
```

## Parameters
* uri KingSumo's giveaway URL
* answer Answer to the giveaway question. Copy this from the URL
* --entries -e Set the amount of entries you want. (required)
* --verbose -v Print the generated email accounts with nonce and signature
* --simulate -s Simulate the process without posting to the URL

## Example

This generate 1 entry for sublime text giveaway

```sh
./queensumo.py -e 1 -v http://sublimetexttips.com/giveaways/win-sublime-text/?lucky=###### 'Sublime Text!!!'
```

## Version
1.0

## Notes
For feedback and bug reports use [Issues](https://github.com/wxrod/QueenSumo/issues).

Like QueenSumo ? Follow the repository on GitHub.

