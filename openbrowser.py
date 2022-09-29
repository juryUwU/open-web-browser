import webbrowser
def yt():
    webbrowser.open('https://www.youtube.com')
def fb():
    webbrowser.open('https://www.facebook.com')
def msg():
    webbrowser.open('https://www.messenger.com')
def gg():
    webbrowser.open('https://www.google.com')
print('\033[0;34mMỞ WEB THÔNG MINH:')
def WEB(webbrowser):
    return webbrowser
def yourweb(WEB):
    print('\033[0;32mWeb bạn muốn:')
    if WEB == "youtube":
        print("youtube")
       
        return yt()
    elif WEB == "facebook":
        print("facebook")
        
        return fb()
    elif WEB == "google":
        print("google")
        
        return gg()
    elif WEB == "messenger":
        print("messenger")
        
        return msg()
a = str(input('\033[0;33mNhập vào web bạn muốn:'))
web = WEB(a)
print(yourweb(web))
