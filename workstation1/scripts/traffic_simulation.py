import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scapy.all import *
import os

def send_email():
    from_addr = 'youremail@example.com'
    to_addr = 'recipient@example.com'
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Test Email'
    body = 'This is a test email with an attachment.'
    msg.attach(MIMEText(body, 'plain'))

    filename = 'test.txt'
    attachment = open('path_to_file/test.txt', 'rb')
    msg.attach(MIMEText(attachment.read(), 'base64', 'utf-8'))
    attachment.close()

    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(from_addr, 'yourpassword')
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

def simulate_file_access():
    for i in range(10):
        with open(f'/path_to_shared_drive/test_file_{i}.txt', 'w') as f:
            f.write('This is a test file.\n')
    for i in range(10):
        os.remove(f'/path_to_shared_drive/test_file_{i}.txt')

def simulate_port_scan(target_ip):
    for port in range(1, 1024):
        pkt = IP(dst=target_ip) / TCP(dport=port, flags='S')
        send(pkt)

# Simulate activities periodically
while True:
    send_email()
    simulate_file_access()
    simulate_port_scan('192.168.1.10')
    time.sleep(60)  # Sleep for 60 seconds before repeating
