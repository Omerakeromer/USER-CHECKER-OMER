#------------[Labrarys]----------------
import requests,random,os;from user_agent import generate_user_agent 
import pyfiglet
#-------------[Colors]-----------------
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  #omer
a30 = '\x1b[38;5;255m'  #omer
#----------[BEGIN LOGO]-------------
logo2 = pyfiglet.figlet_format('USER CHECKER')
print(a5+logo2)
logo = pyfiglet.figlet_format('BY OMER AKER')
print(a2+logo)
print(a5+"—"*60)
#-----------[TOKEN, ID]---------------
from rich.prompt import Prompt
from rich.panel import Panel
from rich import print as PRENTO
TOK =input(f"{a5}[{a4}?{a5}]{a6} TELEGRAM BOT TOKEN:{a3}")
PRENTO(Panel("•"*56, style="green",title="GOOD"))
ID =input(f"{a5}[{a4}?{a5}]{a6} telegram id:{a3}")
os.system("clear")
#------------[TIK TOK]----------------
def TIK():
    R="qwertyuiopasdfghjklzxcvbnm_."
    RND="".join(random.choices(R,k=5))
    url=f"https://www.tiktok.com/@{RND}"
    headers = {"user-agent": generate_user_agent()}
    req = requests.get(f"{url}", headers=headers).text
    if "heart" in req:
        if req.count("heart") == 1:
            print(f"{a5}[{a4}•{a5}]{a3} GOOD:{RND}")
            TIK=f"""< TIK TOK USER > 🫧
[•] < {RND} > 
_______
BY : @omerislamaker"""
            requests.get('https://api.telegram.org/bot' + str(TOK) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(TIK))
        else:
            print(f"{a5}[{a3}•{a5}]{a1} BAD:{RND}")
    else:
        exit(f"{a5}[{a3}•{a5}]{a4} bad net")
#-----------[SNAP CHAT]--------------
def SNAP():
    R="qwertyuiopasdfghjklzxcvbnm_."
    RND="".join(random.choices(R,k=5))
    url=f"https://www.snapchat.com/add/{RND}"
    req=requests.get(url).text
    if len(req)< 9000:
        print(f"{a5}[{a4}•{a5}]{a3} GOOD:{RND}")
        SNAP=f"""< SNAP CHAT USER > 🫧
[•] < {RND} > 
_______
BY : omerislamaker"""
        requests.get('https://api.telegram.org/bot' + str(TOK) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(SNAP))
    else:
        print(f"{a5}[{a3}•{a5}]{a1} BAD:{RND}")
#-----------[YOU TUBE]---------------
def TUBE():
    R="qwertyuiopasdfghjklzxcvbnm_"
    RND="".join(random.choices(R,k=5))
    url=f"https://m.youtube.com/@{RND}"
    req=requests.get(url).text
    if len(req) < 1000:
        print(f"{a5}[{a4}•{a5}]{a3} GOOD:{RND}")
        TUB=f"""< YOU TUBE USER > 🫧
[•] < {RND} > 
_______
BY : @omerislamaker"""
        requests.get('https://api.telegram.org/bot' + str(TOK) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(TUB))
    else:
        print(f"{a5}[{a3}•{a5}]{a1} BAD:{RND}")
#-----------[INSTAGRAM]-------------
def INSTA():
    R="qwertyuiopasdfghjklzxcvbnm_."
    RND="".join(random.choices(R,k=5))
    url=f"https://www.instagram.com/{RND}"
    req=requests.get(url).text
    if len(req) < 260000:
        print(f"{a5}[{a4}•{a5}]{a3} GOOD:{RND}")
        INSTA=f"""< INSTAGRAM USER > 🫧
[•] < {RND} > 
_______
BY : omerislamaker"""
        requests.get('https://api.telegram.org/bot' + str(TOK) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(INSTA))
    else:
        print(f"{a5}[{a3}•{a5}]{a1} BAD:{RND}")
#-------------[LOGO]-----------------
LOG="""⠀⠀⠀⢠⣾⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢰⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⣀⣤⣤⣶⣾⣿⣿⣿⡷
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
⣿⣿⣿⡇⠀⡾⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀
⣿⣿⣿⣧⡀⠁⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⢹⠉⠙⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⠀⣀⣼⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠀⠤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⠿⠋⢃⠈⠢⡁⠒⠄⡀⠈⠁⠀⠀⠀⠀⠀⠀⠀
⣿⣿⠟⠁⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
print(LOG)
print(f"{a3}_"*60)
#-------------[Setting]----------------
print(f"""__________________________
{a5}[{a3}1{a5}]{a30} - {a4}|{a3}TIK TOK{a4}|
{a5}[{a3}2{a5}]{a30} - {a4}|{a3}SNAP CHAT{a4}|
{a5}[{a3}3{a5}]{a30} - {a4}|{a3}YOU TUBE{a4}|
{a5}[{a3}4{a5}]{a30} - {a4}|{a3}INSTAGRAM{a4}|
—————————————————————————""")
def clr():
    os.system("clear")
X =input(f"{a5}[{a4}?{a5}]{a6} CHOSE:{a3}")
if X =="1":
    clr()
    from cfonts import render, say 
    output = render('TIKTOK',colors=['green','white'], align='center')
    print(output)
    print(f"{a4}_"*60)
    while True:
        TIK()
elif X =="2":
    clr()
    from cfonts import render, say 
    output = render('SNAP',colors=['green','white'], align='center')
    print(output)
    print(f"{a4}_"*60)
    while True:
        SNAP()
elif X =="3":
    clr()
    from cfonts import render, say 
    output = render('TUBE',colors=['green','white'], align='center')
    print(f"{a4}_"*60)
    print(output)
    print(f"{a4}_"*60)
    while True:
        TUBE()
elif X =="4":
    clr()
    from cfonts import render, say 
    output = render('INSTA',colors=['green','white'], align='center')
    print(output)
    print(f"{a4}_"*60)
    while True:
        INSTA()
else:
    clr()
    exit(f"{a5}[{a1}✘{a5}]{a3} BAD CHOSE")
#--------------[]DESCORD-------------
