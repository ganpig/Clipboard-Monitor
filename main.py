from time import sleep
from win32clipboard import GetClipboardData, OpenClipboard, CloseClipboard, CF_TEXT

last = ''
while True:
    OpenClipboard()
    tmp = GetClipboardData(CF_TEXT).decode()
    CloseClipboard()
    if tmp != last:
        print(tmp)
        last = tmp
    sleep(1)
