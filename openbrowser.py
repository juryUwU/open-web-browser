import webbrowser
import pyttsx3

robot_mouth = pyttsx3.init()
robot_mouth = pyttsx3.init()
voices = robot_mouth.getProperty('voices')
robot_mouth.setProperty('voice', voices[17].id)
robot_mouth.say("hello")
robot_mouth.runAndWait()
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
        robot_mouth.say("hello")
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
