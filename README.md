# Outlook Disable Spam Filter
Unfortunatley [Outlook.com](http://outlook.live.com) does not have an option to disable the online spam filter. So this repository includes a [scheduled Github Action](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#scheduled-events) to connect to the outlook servers and move the emails from the spam folder to the inbox. 

## Installation 
- [Fork this repository](https://github.com/jan-janssen/outlook-disable-spam-filter/fork)
- Create two [encrypted secrets](https://docs.github.com/en/actions/reference/encrypted-secrets). The first named `OUTLOOK_EMAIL` for your outlook.com email address `username@outlook.com`. The second named `OUTLOOK_APP_PASSWORD` which includes your [outloop app password](https://support.microsoft.com/en-us/account-billing/using-app-passwords-with-apps-that-don-t-support-two-step-verification-5896ed9b-4263-e681-128a-a6f2979a7944)

## Testing 
You can test the code on the command line using: 
```
python -m outlookdisablespamfilter --outlook_email <username@outlook.com> --outlook_app_password <your_app_password>
```
By replacing `<username@outlook.com>` and `<your_app_password>` with your corresponding login data. 

Or you can test it in a python environment:
```
from outlookdisablespamfilter import transfer_spam_emails
transfer_spam_emails(
    outlook_email="<username@outlook.com>",
    outlook_app_password="<your_app_password>"
)
```

## Implementation
This script is implemented in Python using the [imaplib](https://docs.python.org/3/library/imaplib.html). 
