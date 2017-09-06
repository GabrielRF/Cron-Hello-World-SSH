import telebot
import subprocess
import os

token = ''
dest = ''

bot = telebot.TeleBot(token)

def send_message(text):
    bot.send_message(dest, text)

def get_ip():
    cmd = "ip addr | grep wlan0 | grep inet"
    output = subprocess.check_output(cmd, shell=True)
    if '255' not in str(output):
        return 0
    return output.decode('utf-8')

def get_hostname():
    output = subprocess.check_output("hostname")
    return output.decode('utf-8')

if __name__ == '__main__':
    ip = get_ip()
    while ip == 0:
        ip = get_ip()
    hostname = get_hostname()
    message = (str(hostname) + str(ip))
    send_message(message)
