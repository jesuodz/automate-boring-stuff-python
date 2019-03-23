#! python3
# password-locker.py a NSFW password locker program
import sys, pyperclip

PASSWORDS = {
            'email': 'abc123',
            'facebook': '123abc',
            'twitter': 'xlr8'
            }

if len(sys.argv) < 2:
    print('Usage: python password-locker.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
