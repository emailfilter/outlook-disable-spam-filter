import imaplib


def transfer_spam_emails(outlook_email, outlook_app_password, move_to_mailbox="Inbox"):
    """
    Transfer spam emails from Junk folder to another mailbox

    Args:
        outlook_email (str): outlook.com email address like username@outlook.com
        outlook_app_password (str): App password for outlook.com
        move_to_mailbox (str): Mailbox to move the messages to (default: Inbox)
    """
    server_outlook = "outlook.office365.com"
    with imaplib.IMAP4_SSL(host=server_outlook, port=993) as imap_outlook:
        _ = imap_outlook.login(
            outlook_email,
            outlook_app_password
        )
        _ = imap_outlook.select(
            "Junk",
            readonly=False
        )
        print('Fetching messages from Spam Folder ...')
        resp, items = imap_outlook.search(None, 'ALL')
        msg_nums = items[0].split()
        print('%s messages to archive' % len(msg_nums))
        for msg_num in msg_nums:
            resp, data = imap_outlook.fetch(
                msg_num,
                "(FLAGS INTERNALDATE BODY.PEEK[])"
            )
            message = data[0][1]
            date = imaplib.Time2Internaldate(
                imaplib.Internaldate2tuple(
                    data[0][0]
                )
            )
            copy_result = imap_outlook.append(
                move_to_mailbox,
                b"",
                date,
                message
            )
            if copy_result[0] == 'OK':
                _ = imap_outlook.store(
                    msg_num,
                    '+FLAGS',
                    '\\Deleted'
                )
        ex = imap_outlook.expunge()
        print('expunge status: %s' % ex[0])
        if not ex[1][0]:
            print('expunge count: 0')
        else:
            print('expunge count: %s' % len(ex[1]))
