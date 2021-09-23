#!/usr/bin/python
import imaplib
import email
from email.header import decode_header

username = "ahmedbelhadjadji7@gmail.com"
password = "GHgh4545"


imap = imaplib.IMAP4_SSL("imap.gmail.com")

imap.login(username, password)


imap.select("INBOX")

#you can write the email without @gmail.com
#you can choose any search criteria
status, messages = imap.search(None, 'FROM "ahmedbelhadjadji10"')

messages = messages[0].split(b' ')
if messages != [b'']:
        for mail in messages:
            _, msg = imap.fetch(mail, "(RFC822)")
            # you can delete the for loop for performance if you have a long list of emails
            # because it is only for printing the SUBJECT of target email to delete
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    # decode the email subject
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        # if it's a bytes type, decode to str
                        subject = subject.decode()
                    print("Deleting", subject)
                    # mark the mail as deleted
                    imap.store(mail, "+FLAGS", "\\Deleted")

if messages == [b''] : print("No message found !")

imap.expunge()
# close the mailbox
imap.close()
# logout from the account
imap.logout()
