import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import numpy as np
import codecs
from email.mime.text import MIMEText

def sendMail(params):

  templateFile = 'mail_templates/template_couple.html'
  if (params['friends']) :
    templateFile = 'mail_templates/templateFriends.html'

  file = codecs.open(templateFile, 'r', 'utf-8')
  msg_content = file.read().format(**params)
  message = MIMEText(msg_content, 'html')
  
  message['From'] = 'Roborregos Team <sample_mail@mail>'

  serverName = params['email'][0: params['email'].rfind('.')]
  message['To'] = params['FirstName'] + ' <' + serverName + '>'
  message['Subject'] = 'RoboCupido: Tu San Valentín de EnamóraTec'

  msg_full = message.as_string()

  server = smtplib.SMTP('smtp.host.mx:port_number')
  server.starttls()
  server.login('sample_mail@mail.com', 'pasword_mail')
  server.sendmail('sample_mail@mail.com',
                  [params['email']],
                  msg_full)
  server.quit()

friends = np.array(pd.read_csv('mail_data/friends.csv', keep_default_na=False))
couples_casual = pd.read_csv('mail_data/relationshipandcasual.csv', keep_default_na=False)
data = np.array(couples_casual)

count = 0

for mail in data:
  params = {
    'friends' : False,
    'FirstName' : mail[0],
    'email' : mail[1],
    'Valentine1' : mail[2],
    'Porcentaje1' : mail[3],
    'insta1' : mail[4],
    'tel1' : mail[5],
    'Description1' : mail[6],
    'Valentine2' : mail[7],
    'Porcentaje2' : mail[8],
    'insta2' : mail[9],
    'tel2' : mail[10],
    'Description2' : mail[11],
    'Valentine3' : mail[12],
    'Porcentaje3' : mail[13],
    'insta3' : mail[14],
    'tel3' : mail[15],
    'Description3' : mail[16],
    'Valentine4' : '',
    'Porcentaje4' : '',
    'insta4' : '',
    'tel4' : '',
    'Description4' : '',
    'Valentine5' : '',
    'Porcentaje5' : '',
    'insta5' : '',
    'tel5' : '',
    'Description5' : '',
    'MyValentines' : mail[17],
  }
  sendMail(params)
  count+=1
  print(count)

print("Sending friend emails!!")

count = 0

for mail in friends:
  params = {
    'friends' : True,
    'FirstName' : mail[0],
    'email' : mail[1],
    'Valentine1' : mail[2],
    'insta1' : mail[3],
    'tel1' : mail[4],
    'Description1' : mail[5],
    'Valentine2' : mail[6],
    'insta2' : mail[7],
    'tel2' : mail[8],
    'Description2' : mail[9],
    'Valentine3' : mail[10],
    'insta3' : mail[11],
    'tel3' : mail[12],
    'Description3' : mail[13],
    'Valentine4' :  mail[14],
    'insta4' :  mail[15],
    'tel4' :  mail[16],
    'Description4' : mail[17],
    'Valentine5' : '',
    'insta5' : '',
    'tel5' : '',
    'Description5' : '',
  }
  sendMail(params)
  count+=1
  print(count)
  