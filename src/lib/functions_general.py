import time

red = "\033[01;31m{0}\033[00m"
grn = "\033[01;36m{0}\033[00m"
blu = "\033[01;34m{0}\033[00m"
cya = "\033[01;36m{0}\033[00m"


def pbot(message, channel=''):
    if channel:
        msg = '[%s %s] [%s] %s' % (
            time.strftime('%H:%M:%S', time.gmtime()), channel, 'BOT', message)
    print msg
