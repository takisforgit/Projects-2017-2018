import win32clipboard

win32clipboard.OpenClipboard()
try :
    clip2 = win32clipboard.GetClipboardData()
    print(clip2)
except TypeError:
    print("Nothing in clipboard !!!")
##win32clipboard.SetClipboardText(clip2)
win32clipboard.EmptyClipboard()
win32clipboard.CloseClipboard()
