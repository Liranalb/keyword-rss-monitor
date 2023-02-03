# RSS Monitoring App

This app allows you to monitor a RSS feed for keywords of your choice and notify you if any new entries contain those keywords.

## Features

- Check a RSS feed for keywords you specify.
- Notify you when a new entry with the keywords is found.
- Play a sound to alert you.
- Open the link to the new entry in a browser.
- Send an email with the title and link to the new entry.

## Requirements

- Python 3.x
- feedparser
- termcolor
- smtplib
- email

## Usage

1. Clone the repository
2. Install the required libraries using pip
3. Fill in the configurations in `config.py`
   - RSS URL
   - Keywords to monitor
   - Ignore list (optional)
   - Monitoring intervals in seconds
   - Email account details
   - Source email address
4. Run `python3 keyword_monitor.py` to start monitoring.

## Contributing

If you are interested in contributing to this project, feel free to open an issue or submit a pull request. Any help would be appreciated!
