# -*- coding: utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from shuziHB.spiders.tool.fileHandle import readFile,writeFile,fileTruncate
from datetime import datetime

import smtplib

fileName = 'emailTimeData'
maxEmails = 2

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

def sendEmail(title,content):
    # 获取当前时间
    now = datetime.now().strftime('%Y%m%d')
    lines = readFile(fileName)
    if len(lines) < 1:
        writeFile(fileName,now)
    else:
        line = lines[0]
        cday = line
        if cday != now:
            fileTruncate(fileName)
            writeFile(fileName,now)
        else:
            if len(lines) > maxEmails:
                return
            else:
                writeFile(fileName,now)


    from_addr = 'pythonchaintest@126.com' #input("Form:")
    password = 'j123123'#input("password:")
    to_addr = '15974156301@139.com'#input("To :")
    smtp_server = 'smtp.126.com'#input("SMTP server :")

    msg = MIMEText(content,'plain','utf-8 ')
    msg['From'] = _format_addr("python <%s>" % to_addr)
    msg['To']   = _format_addr("管理员 <%s>" % to_addr)
    msg['Subject'] = Header(title,'utf-8').encode()

    server = smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(from_addr,password)
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()