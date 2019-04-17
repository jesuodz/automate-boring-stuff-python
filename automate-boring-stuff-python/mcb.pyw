#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage:    py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#           py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#           py.exe mcb.pyw list - Loads all keywords to clipboard.
#           py.exe mcb.pyw delete <keyword> - Delete a keyword.
#           py.exe mcb.pyw delete <keyword> - Delete all keywords.

import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('mcb')

opc = sys.argv[1].lower()

# Save clipboard content.
if len(sys.argv) == 3:
    if opc == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    # Delete a keyword
    elif opc == 'delete':
        del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if opc == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    # Delete all keywords
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    elif opc == 'delete':
        mcb_shelf.clear()

mcb_shelf.close()
