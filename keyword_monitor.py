import feedparser
import subprocess
import time
import webbrowser
import smtplib 
from termcolor import colored
from email.mime.text import MIMEText
from config import RSS_URL, KEYWORDS, IGNORE_LIST, MONITOR_INTERVALS, MAIL_ACCOUNT_ADDRESS, MAIL_ACCOUNT_PASSWORD, SOURCE_MAIL

visited_id = {}

def check_feed(feed_url, keywords):
    try:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            for keyword in keywords:
                if (keyword in entry.title or keyword in entry.description) and (entry.title not in visited_id.keys()):
                    if any(ignore in entry.title or ignore in entry.description for ignore in IGNORE_LIST):
                        continue
                    visited_id[entry.title] = entry.id
                    play_sound()
                    print(colored(f'{entry.title}:\n{entry.link}\n', 'green',  attrs=['bold']))
                    sendMail(entry.title, entry.link)
                    webbrowser.open(entry.link)
                    break
    except Exception as err:
        print("Something went wrong....",err)

def sendMail(title : str, link : str):
    try:
        message = MIMEText(link, 'plain', 'utf-8')
        message['Subject'] = title
        message['From'] = SOURCE_MAIL
        message['To'] = MAIL_ACCOUNT_ADDRESS
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(MAIL_ACCOUNT_ADDRESS,MAIL_ACCOUNT_PASSWORD)
        smtp.sendmail(SOURCE_MAIL, MAIL_ACCOUNT_ADDRESS, message.as_string())
        smtp.quit()
    except Exception as err:
        print("Something went wrong....",err)

def play_sound():
    subprocess.run(["aplay", "sound.wav"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    print(colored(f'Tracking keywords: {", ".join(KEYWORDS)}...', 'yellow',  attrs=['bold']))

    while True:
        check_feed(RSS_URL, KEYWORDS)
        time.sleep(MONITOR_INTERVALS)
