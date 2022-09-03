#! python3
#mapIt - opens google maps page for the address
# Usage: C:\> mapit 870 Valencia St, San Francisco, CA 94110

import sys, pyperclip, webbrowser
if len(sys.argv)>1:
    address = sys.argv[1:]
elif len(sys.argv)==1:
    address = pyperclip.paste()

webbrowser.open(f'https://www.google.com/maps/place/{address}')
