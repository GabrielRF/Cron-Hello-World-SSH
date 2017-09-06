import telebot
import commands
import os

token = ''
dest = ''

bot = telebot.TeleBot(token)

def send_message(text):
    bot.send_message(dest, text)

def get_ip():
    output = commands.getoutput("ip addr | grep wlan0 | grep inet")
    if '255' not in output:
        return 0
    return output

def get_hostname():
    output = commands.getoutput("hostname")
    return output

if __name__ == '__main__':
    ip = get_ip()
    while ip == 0:
        ip = get_ip()
    hostname = get_hostname()
    message = (str(hostname) + '\n' + str(ip))
    send_message(message)
