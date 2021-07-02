import os
import json

os.system("color fc")
os.system("pip install keyring")
os.system("pip install notion")

import keyring

codeFilePath = os.path.realpath(__file__)
parentFilePath = os.path.abspath(os.path.join(codeFilePath,os.pardir))
jsonFilePath = os.path.join(parentFilePath,"values.json")

with open(jsonFilePath) as data:
    d = json.load(data)

for key,value in d.items():
    if value == "":
        d[key] = input("Input "+ key  + ": ")

if keyring.get_password("emailPassword","username") == None:
    password = input("Sender email address password: ")
    keyring.set_password("emailPassword","username", password)

import random
from notion.client import NotionClient

client = NotionClient(token_v2=d["notionToken"])

page = client.get_block(d["notionPage"])

numberOfNotes = d["numberOfNotes"]
startRecording = False

acceptablePages = []

for child in page.children:
    if not startRecording:
        if type(child).__name__ == "DividerBlock":
            startRecording = True
    else:
        if type(child).__name__ == "PageBlock":
            acceptablePages.append(child)

amountOfNotes = 0

notes = []


while amountOfNotes < int(numberOfNotes):
    randomPage = random.choice(acceptablePages)
    randomNote = random.choice(randomPage.children)

    if type(randomNote).__name__ == "BulletedListBlock":
        amountOfNotes = amountOfNotes + 1

        notes.append(
        [randomPage.title, randomNote.title]
        )

import smtplib
from email.message          import EmailMessage

senderEmail   = d["EmailSender"]
receiverEmail = d["EmailReceiver"]

msg = EmailMessage()
msg['Subject'] = "Notes"
msg['From'] = senderEmail
msg['To'] = receiverEmail

msg.set_content("test")

message = """<html><body style = "font-size: 24px">"""

for i in notes:
    message = message + "<h1>" + i[0] + ": " + "</h1>"
    message = message + i[1] + "<br>"

message = message + "</body></html>"

msg.add_alternative(message.format(), subtype="html")

password = keyring.get_password("emailPassword","username")

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(senderEmail, password)

server.send_message(msg)

with open("values.json","w") as data:
    json.dump(d,data)
