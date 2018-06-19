# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse,antolib,subprocess,unicodedata,GACSender
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()
#==============================================================================#
line = LINE()
#line = LINE("เมล","พาส")
#line = LINE('')
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))

print ("Login Succes")

lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()

oepoll = OEPoll(line)
#call = Call(line)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
Rfu = [line]
Exc = [line]
lineMID = line.getProfile().mid
bot1 = line.getProfile().mid
RfuBot=[lineMID]
Family=["u3930826c2f2dbf7b11a27efbcc37add",lineMID]
admin=['u3930826c2f2dbf7b11a27efbcc37add',lineMID]
RfuFamily = RfuBot + Family

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
#==============================================================================#
settings = {
    "autoAdd": True,
    "autoJoin": False,
    'autoCancel':{"on":True,"members":10},	
    "autoLeave": False,
    "autoRead": False,
    "leaveRoom": False,
    "detectMention": True,
    "checkSticker": False,
    "kickMention": False,
    "potoMention": True,
    "lang":"JP",
    "Wc": False,
    "Lv": False,
    "blacklist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "message":"บัญชีนี้ได้การป้องกันโดย ༺ πနးຫຮี่のีধ์ ༻ ระบบได้ทำการบล็อคคุณอัตโนมัติ",
    "comment":"ขอบคุณที่แอดมา",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": True,
}

Setmain = {
    "foto": {},
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    }

user1 = lineMID
user2 = ""
	
setTime = {}
setTime = rfuSet['setTime']

contact = line.getProfile() 
backup = line.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time() 
dangerMessage = ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","makasih :d","!kickall","nuke","บิน",".???","งงไปดิ","บินไปดิ","เซลกากจัง","@พี่อาร์ท","@ATR","ขอคลิปหน่อยครับ"]

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
#==============================================================================#
def Rapid1Say(mtosay):
    line.sendText(Rapid1To,mtosay)

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       line.sendMessage(msg)
    except Exception as error:
       print(error)

def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
        
def sendMessageWithMention(to, lineMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(lineMID)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
 
def myhelp():
    myHelp = "____ ༺ πနးຫຮี่のีধ์ ༻ _____ " + "\n" \
                  "°•About" + "\n" + \
                  "°•คำสั่งโซเชียล" + "\n" + \
                  "°•คำสั่งคิก" + "\n" + \
                  "°•คำสั่งกลุ่ม" + "\n" + \
                  "°•Help protect" + "\n" + \
                  "°•คำสั่งตั้งค่า" + "\n" + \
                  "°•คำสั่งสิริพูด" + "\n" + \
                  "°•คำสั่งแปล" + "\n" + \
                  "°•คท" + "\n" + \
                  "°•มิด" + "\n" + \
                  "°•ชื่อ" + "\n" + \
                  "°•Mybio" + "\n" + \
                  "°•Mypict" + "\n" + \
                  "°•Mycover" + "\n" + \
                  "°•Myvideo" + "\n" + \
                  "°•Mid" + "\n" + \
                  "°•Name" + "\n" + \
                  "°•Bio" + "\n" + \
                  "°•Pict" + "\n" + \
                  "°•Cover" + "\n" + \
                  "°•Video" + "\n" + \
                  "°•Copy" + "\n" + \
                  "°•Restore" + "\n" + \
                  "°•Mimic on/off" + "\n" + \
                  "°•MimicList" + "\n" + \
                  "°•MimicAdd" + "\n" + \
                  "°•MimicDel" + "\n" + \
                  "°•Broadcastvoice" + "\n" + \
                  "°•Cbroadcastvoice" + "\n" + \
                  "°•รีบอท" + "\n" + \
                  "°•เชคออน์" + "\n" + \
                  "______༺ πနးຫຮี่のีধ์ ༻_____"
    return myHelp

def listgrup():
    listGrup = "*****༺ คำสั่งกลุ่ม ༻ ***** " + "\n" + \
                  "•°GroupCreator" + "\n" + \
                  "•°ไอดีกลุ่ม" + "\n" + \
                  "•°ชื่อกลุ่ม" + "\n" + \
                  "•°รูปกลุ่ม" + "\n" + \
                  "•°GroupList" + "\n" + \
                  "•°GroupMemberList" + "\n" + \
                  "•°GroupInfo" + "\n" + \
                  "•°Url" + "\n" + \
                  "•°ลิ้ง on/off" + "\n" + \
                  "•°Gurl" + "\n" + \
                  "•°รายชื่อเพื่อน" + "\n" + \
                  "•°รายชื่อบล็อค" + "\n" + \
                  "•°Friendlist mid" + "\n" + \
                  "•°Invite:gcreator" + "\n" + \
                  "•°Spam on/off" + "\n" + \
                  "•°Reject inv" + "\n" + \
                  "•°Allban" + "\n" + \
                  "•°Grouplist" + "\n" + \
                  "•°Blist" + "\n" + \
                  "•°แทค" + "\n" + \
                  "•°Lurking on" + "\n" + \
                  "•°Lurking off" + "\n" + \
                  "•°Lurking reset" + "\n" + \
                  "•°Lurking" + "\n" + \
                  "•°Invite" + "\n" + \
                  "•°uninstall" + "\n" + \
                  "•°เตะ" + "\n" + \
                  "•°แบน:on" + "\n" + \
                  "•°ปลดแบน:on" + "\n" + \
                  "**********"
    return listGrup

def socmedia():
    socMedia = "---- คำสั่งมีเดีย ----" + "\n" + \
                  "°•°Instagram" + "\n" + \
                  "°•°Fotoig" + "\n" + \
                  "°•°Youtube" + "\n" + \
                  "°•°Music" + "\n" + \
                  "°•°Lyric" + "\n" + \
                  "°•°ScreenshootWebsite" + "\n" + \
                  "°•°Film:" + "\n" + \
                  "°•°Kalender" + "\n" + \
                  "°•°CheckDate" + "\n" + \
                  "°•°Textig" + "\n" + \
                  "°•°Wikipedia" + "\n" + \
                  "°•°Urban" + "\n" + \
                  "°•°Anime" + "\n" + \
                  "°•°Image" + "\n" + \
                  "°•°Pornhub" + "\n" + \
                  "--------"
    return socMedia
    
def helpset():
    helpSet = "++++คำสั่งเชค++++" + "\n" + \
    "•°•ᴍʏ sᴇʟғ" + "\n" + \
    "•°•sᴏᴄᴍᴇᴅɪᴀ" + "\n" + \
    "•°•ʟɪsᴛ ɢʀᴜᴘ" + "\n" + \
    "•°•ʟɪsᴛ ᴘʀᴏᴛᴇᴄᴛ" + "\n" + \
    "•°•ʟɪsᴛ ᴋɪᴄᴋᴇʀ" + "\n" + \
    "•°•sᴛᴀᴛᴜs" + "\n" + \
    "•°•ᴛᴇxᴛᴛᴏsᴘᴇᴇᴄʜ" + "\n" + \
    "•°•ʟɪsᴛ ᴛʀᴀɴsʟᴀᴛᴇ" + "\n" + \
    "++++++++"
    return helpSet 

def helpkicker():
    helpKicker = "/////คำสั่งคิก/////" + "\n" + \
    "║K1 kick" + "\n" + \
    "║K2 kick" + "\n" + \
    "║K3 kick" + "\n" + \
    "║K1 invite" + "\n" + \
    "║K2 inv" + "\n" + \
    "║K3 vit" + "\n" + \
    "║K1 tag" + "\n" + \
    "║K1gruplist" + "\n" + \
    "║K2listgrup" + "\n" + \
    "║K3listrom" + "\n" + \
    "║Cleanse" + "\n" + \
    "║Scan blacklist" + "\n" + \
    "║cb" + "\n" + \
    "║Nameall:" + "\n" + \
    "║Bioall" + "\n" + \
    "//////////"
    return helpKicker
    
def helpsetting():
    helpSetting = "╭════SettingList " + "\n" + \
    "║เปิดกัน/ปิดกัน " + "\n" + \
    "║Cancel pro on/off" + "\n" + \
    "║เปิดกันยก/ปิดกันยก" + "\n" + \
    "║เปิดกันลิ้ง/ปิดกันลิ้ง" + "\n" + \
    "║เปิดกันเข้า/ปิดกันเข้า" + "\n" + \
    "║เปิดกันสมาชิก/ปิดกันสมาชิก" + "\n" + \
    "║เปิดหมด/ปิดหมด" + "\n" + \
    "║Autojoin on/off" + "\n" + \
    "║Autoadd on/off" + "\n" + \
    "║Autoleave on/off" + "\n" + \
    "║Autoread on/off" + "\n" + \
    "║แทคออน/แทคออฟ" + "\n" + \
    "║Selfbot on/off" + "\n" + \
    "║แทค2ออน/แทค2ออฟ" + "\n" + \
    "║Checksticker on/off" + "\n" + \
    "║Sider on/off" + "\n" + \
    "║เปิดต้อนรับ/ปิดต้อนรับ" + "\n" + \
    "║ปิดคนออก/เปิดคนออก" + "\n" + \
    "╰════"
    return helpSetting

def helptexttospeech():
    helpTextToSpeech =   "╔══════════════┓" + "\n" + \
                         "╠⌬ ✰self protect✰    ⌬" + "\n" + \
                         "╚══════════════┛" + "\n" + \
                         "────┅═ই۝ई═┅────" + "\n" + \
                         "        •°คำสั่งสิริ°•" + "\n" + \
                         "────┅═ই۝ई═┅────" + "\n" + \
                         "╔══════════════┓" + "\n" + \
                         "╠❂ af : Afrikaans" + "\n" + \
                         "╠❂ sq : Albanian" + "\n" + \
                         "╠❂ ar : Arabic" + "\n" + \
                         "╠❂ hy : Armenian" + "\n" + \
                         "╠❂ bn : Bengali" + "\n" + \
                         "╠❂ ca : Catalan" + "\n" + \
                         "╠❂ zh : Chinese" + "\n" + \
                         "╠❂ zh-cn : Chinese (Mandarin/China)" + "\n" + \
                         "╠❂ zh-tw : Chinese (Mandarin/Taiwan)" + "\n" + \
                         "╠❂ zh-yue : Chinese (Cantonese)" + "\n" + \
                         "╠❂ hr : Croatian" + "\n" + \
                         "╠❂ cs : Czech" + "\n" + \
                         "╠❂ da : Danish" + "\n" + \
                         "╠❂ nl : Dutch" + "\n" + \
                         "╠❂ en : English" + "\n" + \
                         "╠❂ en-au : English (Australia)" + "\n" + \
                         "╠❂ en-uk : English (United Kingdom)" + "\n" + \
                         "╠❂ en-us : English (United States)" + "\n" + \
                         "╠❂ eo : Esperanto" + "\n" + \
                         "╠❂ fi : Finnish" + "\n" + \
                         "╠❂ fr : French" + "\n" + \
                         "╠❂ de : German" + "\n" + \
                         "╠❂ el : Greek" + "\n" + \
                         "╠❂ hi : Hindi" + "\n" + \
                         "╠❂ hu : Hungarian" + "\n" + \
                         "╠❂ is : Icelandic" + "\n" + \
                         "╠❂ id : Indonesian" + "\n" + \
                         "╠❂ it : Italian" + "\n" + \
                         "╠❂ ja : Japanese" + "\n" + \
                         "╠❂ km : Khmer (Cambodian)" + "\n" + \
                         "╠❂ ko : Korean" + "\n" + \
                         "╠❂ la : Latin" + "\n" + \
                         "╠❂ lv : Latvian" + "\n" + \
                         "╠❂ mk : Macedonian" + "\n" + \
                         "╠❂ no : Norwegian" + "\n" + \
                         "╠❂ pl : Polish" + "\n" + \
                         "╠❂ pt : Portuguese" + "\n" + \
                         "╠❂ ro : Romanian" + "\n" + \
                         "╠❂ ru : Russian" + "\n" + \
                         "╠❂ sr : Serbian" + "\n" + \
                         "╠❂ si : Sinhala" + "\n" + \
                         "╠❂ sk : Slovak" + "\n" + \
                         "╠❂ es : Spanish" + "\n" + \
                         "╠❂ es-es : Spanish (Spain)" + "\n" + \
                         "╠❂ es-us : Spanish (United States)" + "\n" + \
                         "╠❂ sw : Swahili" + "\n" + \
                         "╠❂ sv : Swedish" + "\n" + \
                         "╠❂ ta : Tamil" + "\n" + \
                         "╠❂ th : Thai" + "\n" + \
                         "╠❂ tr : Turkish" + "\n" + \
                         "╠❂ uk : Ukrainian" + "\n" + \
                         "╠❂ vi : Vietnamese" + "\n" + \
                         "╠❂ cy : Welsh" + "\n" + \
                         "╚══════════════┛" + "\n" + "\n\n" + \
                          "「ตัวอย่าง say-th หนูสวย」"
    return helpTextToSpeech
    
def helplanguange():
    helpLanguange =    "╔══════════════┓" + "\n" + \
                       "╠⌬ ✰self protect✰    ⌬" + "\n" + \
                       "╚══════════════┛" + "\n" + \
                       "────┅═ই۝ई═┅────" + "\n" + \
                       "       คำสั่งแปลภาษา" + "\n" + \
                       "────┅═ই۝ई═┅────" + "\n" + \
                       "╔══════════════┓" + "\n" + \
                       "╠❂ af : afrikaans" + "\n" + \
                       "╠❂ sq : albanian" + "\n" + \
                       "╠❂ am : amharic" + "\n" + \
                       "╠❂ ar : arabic" + "\n" + \
                       "╠❂ hy : armenian" + "\n" + \
                       "╠❂ az : azerbaijani" + "\n" + \
                       "╠❂ eu : basque" + "\n" + \
                       "╠❂ be : belarusian" + "\n" + \
                       "╠❂ bn : bengali" + "\n" + \
                       "╠❂ bs : bosnian" + "\n" + \
                       "╠❂ bg : bulgarian" + "\n" + \
                       "╠❂ ca : catalan" + "\n" + \
                       "╠❂ ceb : cebuano" + "\n" + \
                       "╠❂ ny : chichewa" + "\n" + \
                       "╠❂ zh-cn : chinese (simplified)" + "\n" + \
                       "╠❂ zh-tw : chinese (traditional)" + "\n" + \
                       "╠❂ co : corsican" + "\n" + \
                       "╠❂ hr : croatian" + "\n" + \
                       "╠❂ cs : czech" + "\n" + \
                       "╠❂ da : danish" + "\n" + \
                       "╠❂ nl : dutch" + "\n" + \
                       "╠❂ en : english" + "\n" + \
                       "╠❂ eo : esperanto" + "\n" + \
                       "╠❂ et : estonian" + "\n" + \
                       "╠❂ tl : filipino" + "\n" + \
                       "╠❂ fi : finnish" + "\n" + \
                       "╠❂ fr : french" + "\n" + \
                       "╠❂ fy : frisian" + "\n" + \
                       "╠❂ gl : galician" + "\n" + \
                       "╠❂ ka : georgian" + "\n" + \
                       "╠❂ de : german" + "\n" + \
                       "╠❂ el : greek" + "\n" + \
                       "╠❂ gu : gujarati" + "\n" + \
                       "╠❂ ht : haitian creole" + "\n" + \
                       "╠❂ ha : hausa" + "\n" + \
                       "╠❂ haw : hawaiian" + "\n" + \
                       "╠❂ iw : hebrew" + "\n" + \
                       "╠❂ hi : hindi" + "\n" + \
                       "╠❂ hmn : hmong" + "\n" + \
                       "╠❂ hu : hungarian" + "\n" + \
                       "╠❂ is : icelandic" + "\n" + \
                       "╠❂ ig : igbo" + "\n" + \
                       "╠❂ id : indonesian" + "\n" + \
                       "╠❂ ga : irish" + "\n" + \
                       "╠❂ it : italian" + "\n" + \
                       "╠❂ ja : japanese" + "\n" + \
                       "╠❂ jw : javanese" + "\n" + \
                       "╠❂ kn : kannada" + "\n" + \
                       "╠❂ kk : kazakh" + "\n" + \
                       "╠❂ km : khmer" + "\n" + \
                       "╠❂ ko : korean" + "\n" + \
                       "╠❂ ku : kurdish (kurmanji)" + "\n" + \
                       "╠❂ ky : kyrgyz" + "\n" + \
                       "╠❂ lo : lao" + "\n" + \
                       "╠❂ la : latin" + "\n" + \
                       "╠❂ lv : latvian" + "\n" + \
                       "╠❂ lt : lithuanian" + "\n" + \
                       "╠❂ lb : luxembourgish" + "\n" + \
                       "╠❂ mk : macedonian" + "\n" + \
                       "╠❂ mg : malagasy" + "\n" + \
                       "╠❂ ms : malay" + "\n" + \
                       "╠❂ ml : malayalam" + "\n" + \
                       "╠❂ mt : maltese" + "\n" + \
                       "╠❂ mi : maori" + "\n" + \
                       "╠❂ mr : marathi" + "\n" + \
                       "╠❂ mn : mongolian" + "\n" + \
                       "╠❂ my : myanmar (burmese)" + "\n" + \
                       "╠❂ ne : nepali" + "\n" + \
                       "╠❂ no : norwegian" + "\n" + \
                       "╠❂ ps : pashto" + "\n" + \
                       "╠❂ fa : persian" + "\n" + \
                       "╠❂ pl : polish" + "\n" + \
                       "╠❂ pt : portuguese" + "\n" + \
                       "╠❂ pa : punjabi" + "\n" + \
                       "╠❂ ro : romanian" + "\n" + \
                       "╠❂ ru : russian" + "\n" + \
                       "╠❂ sm : samoan" + "\n" + \
                       "╠❂ gd : scots gaelic" + "\n" + \
                       "╠❂ sr : serbian" + "\n" + \
                       "╠❂ st : sesotho" + "\n" + \
                       "╠❂ sn : shona" + "\n" + \
                       "╠❂ sd : sindhi" + "\n" + \
                       "╠❂ si : sinhala" + "\n" + \
                       "╠❂ sk : slovak" + "\n" + \
                       "╠❂ sl : slovenian" + "\n" + \
                       "╠❂ so : somali" + "\n" + \
                       "╠❂ es : spanish" + "\n" + \
                       "╠❂ su : sundanese" + "\n" + \
                       "╠❂ sw : swahili" + "\n" + \
                       "╠❂ sv : swedish" + "\n" + \
                       "╠❂ tg : tajik" + "\n" + \
                       "╠❂ ta : tamil" + "\n" + \
                       "╠❂ te : telugu" + "\n" + \
                       "╠❂ th : thai" + "\n" + \
                       "╠❂ tr : turkish" + "\n" + \
                       "╠❂ uk : ukrainian" + "\n" + \
                       "╠❂ ur : urdu" + "\n" + \
                       "╠❂ uz : uzbek" + "\n" + \
                       "╠❂ vi : vietnamese" + "\n" + \
                       "╠❂ cy : welsh" + "\n" + \
                       "╠❂ xh : xhosa" + "\n" + \
                       "╠❂ yi : yiddish" + "\n" + \
                       "╠❂ yo : yoruba" + "\n" + \
                       "╠❂ zu : zulu" + "\n" + \
                       "╠❂ fil : Filipino" + "\n" + \
                       "╠❂ he : Hebrew" + "\n" + \
                       "╚══════════════┛" + "\n" + "\n\n" + \
                       "「ตัวอย่าง tr-yi 」"
    return helpLanguange
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                line.blockContact(op.param1)           
        if op.type == 13:
            if lineMID in op.param3:
                G = line.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                        else:
                            line.acceptGroupInvitation(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)				
#        if op.type == 13:
#            group = line.getGroup(op.param1)
#            if settings["autoJoin"] == True:
#                line.acceptGroupInvitation(op.param1)
#        if op.type == 24:
#            if settings["autoLeave"] == True:
#                line.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if ".say " in msg.text.lower():
                    spl = re.split(".say ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        mts = spl[1]
                        mtsl = mts.split()
                        mtsTimeArg = len(mtsl) - 1
                        mtsTime = mtsl[mtsTimeArg]
                        del mtsl[mtsTimeArg]
                        mtosay = " ".join(mtsl)
                        global Rapid1To
                        Rapid1To = msg.to
                        RapidTime = mtsTime
                        rmtosay = []
                        for count in range(0,int(RapidTime)):
                            rmtosay.insert(count,mtosay)
                        p = Pool(20)
                        p.map(Rapid1Say,rmtosay)
                        p.close()
                if text.lower() == 'คำสั่ง':
                    myHelp = myhelp()
                    line.sendMessage(to, str(myHelp))
                elif text.lower() == 'คำสั่งเซ็ท':
                    helpSet = helpset()
                    line.sendMessage(to, str(helpSet))
                    sendMessageWithMention(to, lineMID)
                elif text.lower() == 'คำสั่งคิก':
                    helpKicker = helpkicker()
                    line.sendMessage(to, str(helpKicker))
                elif text.lower() == 'คำสั่งกลุ่ม':
                    listGrup = listgrup()
                    line.sendMessage(to, str(listGrup))
                elif text.lower() == 'คำสั่งตั้งค่า':
                    helpSetting = helpsetting()
                    line.sendMessage(to, str(helpSetting))
                elif text.lower() == 'คำสั่งโซเชียล':
                    socMedia = socmedia()
                    line.sendMessage(to, str(socMedia))
                elif text.lower() == 'คำสั่งสิริพูด':
                    helpTextToSpeech = helptexttospeech()
                    line.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == 'คำสั่งแปล':
                    helpLanguange = helplanguange()
                    line.sendMessage(to, str(helpLanguange))
#==============================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    line.sendMessage(to, "กำลังทดสอบ")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif text.lower() == 'sp':
                    start = time.time()
                    line.sendMessage(to, "กำลังทดสอบ")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")						
                elif text.lower() == 'รีบอท':
                    line.sendMessage(to, "กำลังเริ่มต้นใหม่ ... โปรดรอสักครู่ ..")
                    line.sendMessage(to, "Success Restarting.")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "ระยะเวลาการทำงานของบอท {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u7a4febc4c650fc7679eadf4245c2a5ad"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╔══[ ✯༺ πနးຫຮี่のีধ์ ༻ ]"
                        ret_ += "\n╠۝ ชื่อ ═ {}".format(contact.displayName)
                        ret_ += "\n╠۝ กลุ่ม ═ {}".format(str(len(grouplist)))
                        ret_ += "\n╠۝ เพื่อน ═ {}".format(str(len(contactlist)))
                        ret_ += "\n╠۝ บล็อค ═ {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[สถานะ]"
                        ret_ += "\n╠۝ ผู้สร้าง ═ {}".format(creator.displayName)
                        ret_ += "\n╚══[ ✯༺ πနးຫຮี่のีধ์ ༻✯ ]"
                        line.sendContact(to, owner)
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'set':
                    try:
                        ret_ = "╔════[ Status ]═════┓"
                        if settings["autoAdd"] == True: ret_ += "\n╠ รับแอดออโต้ ✔"
                        else: ret_ += "\n╠ รับแอดออโต้    ✘ "
                        if settings["autoJoin"] == True: ret_ += "\n╠ เข้าห้องออโต้ ✔"
                        else: ret_ += "\n╠ เข้าห้องออโต้    ✘ "
                        if settings["autoCancel"]["on"] == True:ret_+="\n╠ ยกเลิกเชิญกลุ่มเมื่อมีสมาชิกต่ำกว่า: " + str(settings["autoCancel"]["members"]) + " → ✔"
                        else: ret_ += "\n╠ ยกเลิกเชิญกลุ่ม    ✘ "						
                        if settings["autoLeave"] == True: ret_ += "\n╠ ออกแชทรวม ✔"
                        else: ret_ += "\n╠ ออกแชทรวม ✘ "
                        if settings["autoRead"] == True: ret_ += "\n╠ อ่านออโต้ ✔"
                        else: ret_ += "\n╠ อ่านออโต้   ✘ "				
                        if settings["checkSticker"] == True: ret_ += "\n╠ Sticker ✔"
                        else: ret_ += "\n╠ Sticker        ✘ "
                        if settings["detectMention"] == True: ret_ += "\n╠ ตอบกลับคนแทค ✔"
                        else: ret_ += "\n╠ ตอบกลับคนแทค ✘ "
                        if settings["potoMention"] == True: ret_ += "\n╠ แสดงภาพคนแทค ✔"
                        else: ret_ += "\n╠ แสดงภาพคนแทค ✘ "						
                        if RfuProtect["inviteprotect"] == True: ret_ += "\n╠ กันเชิญ ✔"
                        else: ret_ += "\n╠ กันเชิญ ✘ "
                        if RfuProtect["cancelprotect"] == True: ret_ += "\n╠ กันยกเชิญ ✔"
                        else: ret_ += "\n╠ กันยกเชิญ ✘ "
                        if RfuProtect["protect"] == True: ret_ += "\n╠ ป้องกัน ✔"
                        else: ret_ += "\n╠ ป้องกัน ✘ "
                        if RfuProtect["linkprotect"] == True: ret_ += "\n╠ ป้องกันเปิดลิ้ง ✔"
                        else: ret_ += "\n╠ ป้องกันเปิดลิ้ง ✘ "
                        if RfuProtect["Protectguest"] == True: ret_ += "\n╠ ป้องกันสมาชิก ✔"
                        else: ret_ += "\n╠ ป้องกันสมาชิก ✘ "
                        if RfuProtect["Protectjoin"] == True: ret_ += "\n╠ ป้องกันเข้ากลุ่ม ✔"
                        else: ret_ += "\n╠ ป้องกันเข้ากลุ่ม ✘ "						
                        ret_ += "\n╚════[ Status ]═════┛"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    line.sendMessage(to, "Autoadd enabled.")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    line.sendMessage(to, "Autoadd disabled.")
                elif text.lower() == 'autojoin on':
                    settings["autoJoin"] = True
                    line.sendMessage(to, "Autojoin enabled.")
                elif text.lower() == 'autojoin off':
                    settings["autoJoin"] = False
                    line.sendMessage(to, "Auto Join disabled.")
                elif "Gcancel:" in msg.text:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                                else:
                                    line.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,strnum + " สมาชิกในกลุ่มจะปฏิเสธคำเชิญโดยอัตโนมัติ")
                                else:
                                    line.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                    except:
                        if settings["lang"] == "JP":
                                line.sendText(msg.to,"Value is wrong")
                        else:
                                line.sendText(msg.to,"Bizarre ratings")					
                elif text.lower() == 'autoleave on':
                    settings["autoLeave"] = True
                    line.sendMessage(to, "Autoleave enabled.")
                elif text.lower() == 'autoleave off':
                    settings["autoLeave"] = False
                    line.sendMessage(to, "Autoleave disabled.")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    line.sendMessage(to, "Autoread message enabled.")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    line.sendMessage(to, "Autoread message disabled.")
                elif text.lower() == 'sticker on':
                    settings["checkSticker"] = True
                    line.sendMessage(to, "Check sticker enabled.")
                elif text.lower() == 'sticker off':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "Check sticker disabled.")                
#==============================================================================#
                elif text.lower() == 'คท':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                elif text.lower() == 'creator':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, "u3930826c2f2dbf7b11a27efbcc37add5")
                elif text.lower() == 'มิด':
                    line.sendMessage(msg.to,"[มิด]\n" +  lineMID)
                elif text.lower() == 'ชื่อ':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[ชื่อ/เฮด]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypict':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideo':
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("me "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("name "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("bio "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("pict "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("video "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cover "):
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("copy "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            line.cloneContactProfile(contact)
                            line.sendMessage(msg.to, "😊😊")
                        except:
                            line.sendMessage(msg.to, "😊😊")
                            
                elif text.lower() == 'backup':
                    try:
                        lineProfile.displayName = str(myProfile["displayName"])
                        lineProfile.statusMessage = str(myProfile["statusMessage"])
                        lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                        line.updateProfileAttribute(8, lineProfile.pictureStatus)
                        line.updateProfile(lineProfile)
                        line.sendMessage(msg.to, "Berhasil restore profile")
                    except:
                        line.sendMessage(msg.to, "Gagal restore profile")
						
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Mimic has been added as")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"Mimic deleting succes...")
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Mimic enabled.")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Mimic disabled.")
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                    line.sendMessage(to, "Itu Pembuat Groupnya")
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "ID GROUP \n" + gid.id)
                elif text.lower() == 'รูปกลุ่ม':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "Name Group -> \n" + gid.name)
                elif text.lower() == 'url':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "Link Qr Group\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == 'ลิ้ง on':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "Link Qr to open")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "Link Qr to open")
                elif text.lower() == 'ลิ้ง off':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "Link Qr to closed.")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "Link Qr to closed.")
                elif text.lower() == 'groupinfo':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))				
                elif "โทร" == msg.text.lower():
                    line.inviteIntoGroupCall(msg.to,[uid.mid for uid in line.getGroup(msg.to).members if uid.mid != line.getProfile().mid])
                    line.sendMessage(msg.to,"เชิญเข้าร่วมการโทรสำเร็จ(｀・ω・´)")	
                elif ".sh " in msg.text.lower():
                    spl = re.split(".sh ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,subprocess.getoutput(spl[1]))
                        except:
                            pass	
                elif msg.text.lower() == ".getjoined":
                    line.sendText(msg.to,"กรุณารอสักครู่ ใจเย็นๆ")
                    all = line.getGroupIdsJoined()
                    text = ""
                    cnt = 0
                    for i in all:
                        text += line.getGroup(i).name + "\n" + i + "\n\n"
                        cnt += 1
                        if cnt == 10:
                            line.sendText(msg.to,text[:-2])
                            text = ""
                            cnt = 0
                    line.sendText(msg.to,text[:-2])
                    cnt = 0				
                elif ".info " in msg.text.lower():
                    spl = re.split(".info ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            uid = prov[i]["M"]
                            userData = line.getContact(uid)
                            try:
                                line.sendImageWithUrl(msg.to,"http://dl.profile.line.naver.jp/"+userData.pictureStatus)
                            except:
                                pass
                            line.sendText(msg.to,"ชื่อที่แสดง: "+userData.displayName)
                            line.sendText(msg.to,"ข้อความสเตตัส:\n"+userData.statusMessage)
                            line.sendText(msg.to,"ไอดีบัญชี: "+userData.mid)
                            msg.contentType = 13
                            msg.text = None
                            msg.contentMetadata = {'mid': userData.mid}
                            line.sendMessage(msg)
                elif "|!" in msg.text:
                    spl = msg.text.split("|!")
                    if spl[len(spl)-1] == "":
                        line.sendText(msg.to,"กดที่นี่เพื่อเขย่าข้อความด้านบน:\nline://nv/chatMsg?chatId="+msg.to+"&messageId="+msg.id)	
                elif "ยกค้างเชิญ" in msg.text.lower():
                    spl = re.split(".denyall",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = line.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        line.sendText(msg.to,txt)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                line.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    line.sendText(gr,spl[1])
                                line.leaveGroup(gr)
                            except:
                                pass
                        line.sendText(msg.to,"สำเร็จแล้ว")	
                elif ".whois " in msg.text.lower():
                    spl = re.split(".whois ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        msg.contentType = 13
                        msg.text = None
                        msg.contentMetadata = {"mid":spl[1]}
                        line.sendMessage(msg)
                elif ".remove " in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            random.choice(Exc).kickoutFromGroup(msg.to,[prov[i]["M"]])
                elif ".bye " in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            line.kickoutFromGroup(msg.to,[prov[i]["M"]])
                            allmid.append(prov[i]["M"])
                        line.findAndAddContactsByMids(allmid)
                        line.inviteIntoGroup(msg.to,allmid)
                        line.cancelGroupInvitation(msg.to,allmid)

                elif msg.text.lower() == ".myid":
                    line.sendText(msg.to,user1)
                elif ".tx " in msg.text.lower():
                    spl = re.split(".tx ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        line.kedapkedip(msg.to,spl[1])
                elif ".name " in msg.text.lower():
                    spl = re.split(".name ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = spl[1]
                        line.updateProfile(prof)
                        line.sendText(msg.to,"สำเร็จแล้ว")
                elif ".nmx " in msg.text.lower():
                    spl = re.split(".nmx ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = line.nmxstring(spl[1])
                        line.updateProfile(prof)
                        line.sendText(msg.to,"สำเร็จแล้ว")
                elif ".join " in msg.text.lower():
                    spl = re.split(".join ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            gid = spl[1].split(" ")[0]
                            ticket = spl[1].split(" ")[1].replace("line://ti/g/","") if "line://ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1].replace("http://line.me/R/ti/g/","") if "http://line.me/R/ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1]
                            line.acceptGroupInvitationByTicket(gid,ticket)
                        except Exception as e:
                            line.sendText(msg.to,str(e))	
                elif msg.text.lower().startswith(".ctt "):
                    try:
                        text = msg.text.split(" ",1)[1]
                        headers = {
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
                        }
                        data = {
                        "q":text
                        }
                        conv = BeautifulSoup(requests.post("http://lullar-de-2.appspot.com/",headers=headers,data=data).content,"html.parser").find("span",attrs={"style":"font-size:40px"}).text
                        if msg.toType != 0:
                                line.sendText(msg.to,"Conversion:\n"+conv)
                        else:
                                line.sendText(msg.from_,"Conversion:\n"+conv)
                    except Exception as e:
                        print(e)						
                elif msg.text.lower().startswith("ส่งข้อความ "):
                    pnum = re.split("ส่งข้อความ ",msg.text,flags=re.IGNORECASE)[1]
                    pnum = "66"+pnum[1:]
                    GACReq = GACSender.send(pnum)
                    if GACReq.responseNum == 0:
                        if msg.toType != 0:
                                line.sendText(msg.to,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                        else:
                                line.sendText(msg.from_,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                    elif GACReq.responseNum == 1:
                        if msg.toType != 0:
                                line.sendText(msg.to,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                        else:
                                line.sendText(msg.from_,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                    else:
                        if msg.toType != 0:
                                line.sendText(msg.to,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                        else:
                                line.sendText(msg.from_,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                elif msg.text.lower() == ".groupurl":
                    if msg.toType == 2:
                        line.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(msg.to)))
                    else:
                        line.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น")
                elif ".groupurl " in msg.text.lower():
                    spl = re.split(".groupurl ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(spl[1])))
                        except Exception as e:
                            line.sendText(msg.to,"พบข้อผิดพลาด (เหตุผล \""+e.reason+"\")")				
#==============================================================================#
                elif text.lower() == 'แทค':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        line.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        line.sendMessage(to, "ทั้งหมด {} คน".format(str(len(nama))))  
                elif text.lower() == 'lurking on':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                line.sendMessage(msg.to,"Lurking enabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            line.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'lurking off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        line.sendMessage(msg.to,"Lurking disabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        line.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'lurking reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        line.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        line.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'lurking':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if list(read["ROM"][receiver].items()) == []:
                            line.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in list(read["ROM"][receiver].items()):
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ *** LurkDetector *** ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            line.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        line.sendMessage(receiver,"Lurking has not been set.")
#==============================================================================#
                elif msg.text.lower().startswith("say-af "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'af'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
        
                elif msg.text.lower().startswith("say-sq "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sq'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ar "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ar'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-bn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'bn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ca "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ca'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-cn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-cn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-tw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-tw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-yue "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-yue'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cs "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cs'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-da "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'da'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-nl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'nl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-au "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-au'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-eo "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'eo'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-de "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'de'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-el "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'el'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hu "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hu'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-is "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'is'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-id "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-it "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'it'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ja "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-km "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'km'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ko "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ko'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-la "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'la'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-lv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'lv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-mk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'mk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-no "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'no'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pt "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pt'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-do "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ro'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ru "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ru'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-si "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'si'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ta "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ta'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-th "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-tr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'tr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-vi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'vi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
#==============================================================================# 
                elif msg.text.lower().startswith("tr-af "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='af')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sq "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sq')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-am "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='am')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ar "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ar')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-az "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='az')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-eu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='eu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-be "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='be')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ca "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ca')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ceb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ceb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ny "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ny')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-cn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-cn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-tw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-co "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='co')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-da "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='da')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-nl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='nl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-en "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-et "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='et')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ka "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ka')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-de "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-el "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='el')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ht "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ht')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ha "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ha')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-haw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='haw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-iw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='iw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hmn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hmn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-is "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='is')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ig "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ig')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-id "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ga "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ga')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-it "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='it')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ja "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-jw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='jw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-km "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='km')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ko "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ko')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ku "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ku')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ky "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ky')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-la "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='la')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ms "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ms')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ml "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ml')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-my "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='my')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ne "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ne')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-no "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='no')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ps "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ps')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ro "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ro')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ru "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ru')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sm "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sm')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-st "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='st')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-si "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='si')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-so "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='so')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-es "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='es')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-su "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='su')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ta "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ta')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-te "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='te')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ur "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ur')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uz "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uz')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-vi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='vi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-xh "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='xh')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fil "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fil')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-he "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='he')
                    A = hasil.text
                    line.sendMessage(msg.to, A)

                elif msg.text in ["Jumanji"]:
                    hasil = "https://youtu.be/2QKg5SZ_35I"
                    A = hasil
                    line.sendVideoWithURL(msg.to, A)

#sender = msg._from
#            if msg.toType == 0:
#                if sender != line.profile.mid:
#==============================================================================#   
                elif "Broadcastvoice " in msg.text:
                    bctxt = msg.text.replace("Bcvoice ", "")
                    bc = (".Bdw.. Ini adalah Broadcast.. Salam Owner ARDIAN PURNAMA.. by. RFU boot sekawan")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "Cbroadcastvoice " in msg.text:
                    bctxt = msg.text.replace("Cbcvoice ", "")
                    bc = (".Bdw.. Ini adalah Broadcast.. Salam Owner ARDIAN PURNAMA.. by. RFU boot sekawan")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = line.getAllContactIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "Wikipedia " in msg.text:
                      try:
                          wiki = msg.text.lower().replace("Wikipedia ","")
                          wikipedia.set_lang("id")
                          pesan="Title ("
                          pesan+=wikipedia.page(wiki).title
                          pesan+=")\n\n"
                          pesan+=wikipedia.summary(wiki, sentences=1)
                          pesan+="\n"
                          pesan+=wikipedia.page(wiki).url
                          line.sendMessage(msg.to, pesan)
                      except:
                              try:
                                  pesan="Over Text Limit! Please Click link\n"
                                  pesan+=wikipedia.page(wiki).url
                                  line.sendText(msg.to, pesan)
                              except Exception as e:
                                  line.sendMessage(msg.to, str(e))

                elif "Film:" in msg.text:
                    proses = msg.text.split(":")
                    get = msg.text.replace(proses[0] + ":","")
                    getfilm = get.split()
                    title = getfilm[0]
                    tahun = getfilm[1]
                    r = requests.get('http://www.omdbapi.com/?t='+title+'&y='+tahun+'&plot=full&apikey=4bdd1d70')
                    start = time.time()
                    data=r.text
                    data=json.loads(data)
                    hasil = "Informasi \n" +str(data["Title"])+ " (" +str(data["Year"])+ ")"
                    hasil += "\n\n " +str(data["Plot"])
                    hasil += "\n\nDirector : " +str(data["Director"])
                    hasil += "\nActors   : " +str(data["Actors"])
                    hasil += "\nRelease : " +str(data["Released"])
                    hasil += "\nGenre    : " +str(data["Genre"])
                    hasil += "\nRuntime   : " +str(data["Runtime"])
                    path = data["Poster"]
                    line.sendImageWithURL(msg.to, str(path))
                    line.sendMessage(msg.to,hasil)

                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    line.sendMessage(msg.to, readTime)                 
                elif "screenshotwebsite" in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        line.sendImageWithURL(to, data["result"])
                elif "checkdate" in msg.text.lower():
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    ret_ = "╔══[ D A T E ]"
                    ret_ += "\n╠ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                    ret_ += "\n╠ Age : {}".format(str(data["data"]["usia"]))
                    ret_ += "\n╠ Birthday : {}".format(str(data["data"]["ultah"]))
                    ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                    ret_ += "\n╚══[ Success ]"
                    line.sendMessage(to, str(ret_))
                
                elif "instagram" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠ Nama : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠ Username : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠ Akun Pribadi : Tidak"
                            ret_ += "\n╠ จำนวน Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            line.sendImageWithURL(to, str(path))
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "Pengguna tidak ditemukan")
                elif "fotoig" in msg.text.lower():
                    separate = msg.text.split(" ")
                    user = msg.text.replace(separate[0] + " ","")
                    profile = "https://www.instagram.com/" + user
                    with requests.session() as x:
                        x.headers['user-agent'] = 'Mozilla/5.0'
                        end_cursor = ''
                        for count in range(1):
                            print(('send foto : ', count))
                            r = x.get(profile, params={'max_id': end_cursor})                        
                            data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                            j    = json.loads(data)                        
                            for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                print((node['display_src']))
                                line.sendImageWithURL(msg.to,node['display_src'])
                elif "image" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "anime" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "youtube" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผมการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))

                elif msg.text in ["Cctv on"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to,"Cctv on Ready")
                elif msg.text in ["Cctv off"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        line.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                    else:
                        line.sendMessage(msg.to, "Cctv Already Off")

                elif text.lower() == 'selfbot off':
                    line.sendMessage(receiver, 'หยุดการทำงานเซลบอทเรียบร้อย')
                    print ("Selfbot Off")
                    exit(1)

                elif text.lower() == 'รายชื่อเพื่อน':
                    contactlist = line.getAllContactIds()
                    kontak = line.getContacts(contactlist)
                    num=1
                    msgs="🎎List Friend🎎"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n🎎List Friend🎎\n\nTotal Teman : %i" % len(kontak)
                    line.sendMessage(msg.to, msgs)

                elif msg.text in ["รายชื่อบล็อค"]: 
                    blockedlist = line.getBlockedContactIds()
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="═════Daftar Akun Yang di Blocked═════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n════════List Blocked════════\n\nTotal Blocked : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text in ["มิดเพื่อนทั้งหมด"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="═════════List FriendMid═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════List FriendMid═════════\n\nTotal Friend : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)
			
                elif msg.text.lower() == 'gurl':
                	if msg.toType == 2:
                         g = line.getGroup(receiver)
                         line.updateGroup(g)
                         gurl = line.reissueGroupTicket(receiver)
                         line.sendMessage(receiver,"╔══════════════┓\n╠❂line://ti/g/" + gurl + "\n╠\n╠❂Link Groupnya Tanpa Buka Qr\n╚══════════════┛")

                elif msg.text == "Pornhub":
                	line.sendMessage(receiver,">nekopoi.host\n>sexvideobokep.com\n>memek.com\n>pornktube.com\n>faketaxi.com\n>videojorok.com\n>watchmygf.mobi\n>xnxx.com\n>pornhd.com\n>xvideos.com\n>vidz7.com\n>m.xhamster.com\n>xxmovies.pro\n>youporn.com\n>pornhub.com\n>youjizz.com\n>thumzilla.com\n>anyporn.com\n>brazzers.com\n>redtube.com\n>youporn.com")

                elif msg.text.lower() == 'invite:gcreator':
                	if msg.toType == 2:                
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Type👉 Invite Pembuat Group Succes")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Pembuat Group Sudah di dalam")

                elif msg.text in ["/uninstall"]:
                    if msg.toType == 2:
                        ginfo = line.getGroup(receiver)
                        try:
                            line.leaveGroup(receiver)							
                        except:
                            pass

                elif msg.text in ["Tagimage on","แทค2ออน"]:
                        settings['potoMention'] = True
                        line.sendMessage(msg.to,"Respon enabled.")
                
                elif msg.text in ["Tagimage off","แทค2ออฟ"]:
                        settings['potoMention'] = False
                        line.sendMessage(msg.to,"Respon disabled.")

                elif msg.text in ["Respontag on","แทคออน","My respon on","Respon:on"]:
                    settings["detectMention"] = True
                    line.sendMessage(msg.to,"AutoRespon enabled.")
                
                elif msg.text in ["Respontag off","แทคออฟ","My respon off","Respon:off"]:
                    settings["detectMention"] = False
                    line.sendMessage(msg.to,"Autorespon disabled.")

                elif msg.text.lower().startswith("textig "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    line.sendImageWithURL(msg.to, urlnya)

                elif "kedip " in msg.text:
                    txt = msg.text.replace("kedip ", "")
                    t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                    t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                    line.sendMessage(msg.to, t1 + txt + t2)						
                elif msg.text in ["Inviteuser"]:
                        settings["winvite"] = True
                        line.sendMessage(msg.to,"send a contact to invite user")                            
                elif msg.text.lower() == ".invitecancel":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            line.cancelGroupInvitation(msg.to,[i])
                elif msg.text.lower() == ".invitecancel2":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            random.choice(Exc).cancelGroupInvitation(msg.to,[i])
#=============COMMAND KICKER===========================#
                elif msg.text in ["ลบดำ"]:
                    settings["blacklist"] = {}
                    line.sendMessage(msg.to,"ทำการลบัญชีดำทั้งหมดเรียร้อย")
                    print ("Clear Ban")

                elif 'kick' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(Rfu).kickoutFromGroup(msg.to,[target])      
                               print ("Rfu kick User")
                           except:
                               random.choice(Rfu).sendMessage(msg.to,"Limit kaka 😫")

                elif 'kill' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])             
                               print ("Sb Kick User")
                           except:
                               line.sendMessage(msg.to,"Limit kaka 😫")                               

                elif 'invite' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.inviteIntoGroup(msg.to,[target])
                               line.sendMessage(receiver, "Type👉 Invite Succes")
                           except:
                               line.sendMessage(msg.to,"Type👉 Limit Invite")
                elif "Cleanse" in msg.text:
                	if msg.toType == 2:
                         _name = msg.text.replace("Cleanse","")
                         gs = line.getGroup(receiver)
                         line.sendMessage(receiver,"Just some casual cleansing ô")
                         targets = []
                         for g in gs.members:
                             if _name in g.displayName:
                                 targets.append(g.mid)
                         if targets == []:
                             line.sendMessage(receiver,"Not found.")
                         else:
                             for target in targets:
                             	if not target in Rfu:
                                     try:
                                         klist=[line]
                                         kicker=random.choice(klist)
                                         kicker.kickoutFromGroup(receiver,[target])
                                         print((receiver,[g.mid]))
                                     except:
                                         line.sendMessage(receiver,"Group cleanse")
                                         print ("Cleanse Group")

                elif msg.text in ["Scan blacklist"]:
                	if msg.toType == 2:
                         group = line.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             line.sendMessage(receiver,"Nots in Blacklist")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[line]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     line.sendMessage(receiver,"sorry bl ke cyduk")
                                     print ("Blacklist di Kick")
                elif "ชื่อเรา: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"Update to " + string)
                        print ("Update Name")

                elif "upbio: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"Succes Update 👉 " + string)
                        print ("Update Bio Succes")
                elif msg.text.lower().startswith("bitcoin"):
                   search = msg.text.split("bitcoin")
                   with requests.session() as web:
                       web.headers["User-Agent"] = random.choice(settings["userAgent"])
                       url = "https://xeonwz.herokuapp.com/bitcoin.api"
                       r = web.get(url)
                       data=r.text
                       data=json.loads(data)
                       print(data)
                       hasil = "「 Bitcoin Result 」"
                       hasil += "\nPrice : " +str(data["btc"])                                
                       hasil += "\nExpensive : " +str(data["high"])
                       hasil += "\nCheap : " +str(data["low"])               
                       line.sendMessage(to, str(hasil))
#=============COMMAND PROTECT=========================#
                elif msg.text.lower() == 'เปิดกัน':
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")

                elif msg.text.lower() == 'ปิดกัน':
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")

                elif msg.text.lower() == 'cancel pro on':
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")

                elif msg.text.lower() == 'cancel pro off':
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")

                elif msg.text.lower() == 'เปิดกันยก':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")

                elif msg.text.lower() == 'ปิดกันยก':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")

                elif msg.text.lower() == 'เปิดกันลิ้ง':
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")

                elif msg.text.lower() == 'ปิดกันลิ้ง':
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")

                elif msg.text.lower() == 'เปิดกันสมาชิก':
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")

                elif msg.text.lower() == 'ปิดกันสมาชิก':
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")

                elif msg.text.lower() == 'เปิดกันเข้า':
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")

                elif msg.text.lower() == 'ปิดกันเข้า':
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")

                elif msg.text.lower() == 'เปิดหมด':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰")
                        else:
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเชิญ")
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ")
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")

                elif msg.text.lower() == 'ปิดหมด':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰")
                        else:
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเชิญ")
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")

#==============FINNISHING PROTECT========================#
                elif msg.text.lower() == 'เปิดต้อนรับ':
                        if settings["Wc"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   .")
                        else:
                            settings["Wc"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   ")
                elif msg.text.lower() == 'ปิดต้อนรับ':
                        if settings["Wc"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   ")
                        else:
                            settings["Wc"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   ")

                elif msg.text.lower() == 'เปิดคนออก':
                        if settings["Lv"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")
                        else:
                            settings["Lv"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")
                elif msg.text.lower() == 'ปิดคนออก':
                        if settings["Lv"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")
                        else:
                            settings["Lv"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")

                elif text.lower() == 'ลบรัน':
                    gid = line.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    line.sendMessage(to, "ลบรันเสร็จแล้วขอรับ")
                    line.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))								
								
                elif "Allban" in msg.text:
                  if msg._from in Family:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.replace("Allban","")
                           gs = line.getGroup(msg.to)
                           line.sendMessage(msg.to,"Banned all")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                line.sendMessage(msg.to,"Maaf")
                           else:
                               for target in targets:
                                   if not target in Family:
                                       try:
                                           settings["blacklist"][target] = True
                                           f=codecs.open('st2__b.json','w','utf-8')
                                           json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           line.sentMessage(msg.to,"All members has been added ban.")
										   
                elif 'แบน' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               settings["blacklist"][target] = True
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes added for the blacklist ")
                               print ("Banned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found")

                elif 'เลิกแบน' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               del settings["blacklist"][target]
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes unban from the blacklist. ")
                               print ("Unbanned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found")

                elif msg.text in ["เชคดำ"]:
                  if msg._from in Family:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"ไม่พบ") 
                    else:
                        line.sendMessage(msg.to,"รายชื่อผู้ติดดำ")
                        mc = "Blacklist User\n"
                        for mi_d in settings["blacklist"]:
                            mc += "[√] " + line.getContact(mi_d).displayName + " \n"
                        line.sendMessage(msg.to, mc + "")

                elif msg.text.lower().startswith("urban "):
                    sep = msg.text.split(" ")
                    judul = msg.text.replace(sep[0] + " ","")
                    url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                    with requests.session() as s:
                        s.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = s.get(url)
                        data = r.text
                        data = json.loads(data)
                        y = "[ Result Urban ]"
                        y += "\nTags: "+ data["tags"][0]
                        y += ","+ data["tags"][1]
                        y += ","+ data["tags"][2]
                        y += ","+ data["tags"][3]
                        y += ","+ data["tags"][4]
                        y += ","+ data["tags"][5]
                        y += ","+ data["tags"][6]
                        y += ","+ data["tags"][7]
                        y += "\n[1]\nAuthor: "+str(data["list"][0]["author"])
                        y += "\nWord: "+str(data["list"][0]["word"])
                        y += "\nLink: "+str(data["list"][0]["permalink"])
                        y += "\nDefinition: "+str(data["list"][0]["definition"])
                        y += "\nExample: "+str(data["list"][0]["example"])
                        line.sendMessage(to, str(y))
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
              
#==============================================================================#
        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)              
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)             
#==============================================================================#
#==============================================================================#
        if op.type == 17:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
            if RfuProtect["protect"] == True:
                if settings["blacklist"][op.param2] == True:
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            G = line.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["protect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Rfu).inviteIntoGroup(op.param1,[op.param2])

        if op.type == 13:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["inviteprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Family:
                        if op.param2 in Family:
                            pass
                        elif RfuProtect["inviteprotect"] == True:
                            settings ["blacklist"][op.param2] = True
                            random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                            if op.param2 not in Family:
                                if op.param2 in Family:
                                    pass
                                elif RfuProtect["cancelprotect"] == True:
                                    settings ["blacklist"][op.param2] = True
                                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])

        if op.type == 11:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["linkprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if RfuProtect["autoAdd"] == True:
                if (settings["message"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["message"]))                    

        if op.type == 11:
            if RfuProtect["linkprotect"] == True:
                if op.param2 not in Family:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Rfu).updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param3])                    

        if op.type == 13:
           if RfuProtect["Protectguest"] == True:
               if op.param2 not in Family:
                  random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 17:
           if RfuProtect["Protectjoin"] == True:
               if op.param2 not in Family:
                   random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 1:
            if sender in Setmain["foto"]:
                path = line.downloadObjectMsg(msg_id)
                del Setmain["foto"][sender]
                line.updateProfilePicture(path)
                line.sendMessage(to,"Foto berhasil dirubah")

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    line.sendChatChecked(to, msg_id)				
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                         if settings['potoMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.pictureStatus
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = random.choice(balas)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention["MENTIONEES"]
                             for mention in mentionees:
                                   if mention["M"] in lineMID:
                                          line.sendImageWithURL(to,ret_)
                                          break  
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             balas = ["『 ตอบอัตโนมัติ 』\n " + cName + "\n『แทคงี้ชอบเค้าหรา』"]
                             ret_ = "" + random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          line.sendMessage(to,ret_)
                                          sendMessageWithMention(to, contact.mid)
                                          break											  
                if msg.text in ["Me","me",".me",".Me","คท","/me"]:
                    line.sendText(msg.to,"เชคทะมุยกลัวหลุดออ")
                if msg.text in ["sp","speed",".speed","/speed","Sp",".Speed"]:
                    line.sendText(msg.to,"เร็วแรงไหมพี่")
                if msg.text in ["runtime","Runtime","/uptime","ออน",".uptime"]:
                    line.sendText(msg.to,"นานยังๆ")							  
                if msg.text in [".มอง"]:
                    line.sendText(msg.to,"มองไยยยย")	  
                if msg.text in ["555","5555","55555"]:
                    line.sendText(msg.to,"ขำอะไรนักหนา-.-")	
                if msg.text in dangerMessage:
                    random.choice(Rfu).kickoutFromGroup(receiver,[sender])
                    random.choice(Rfu).sendText(msg.to,"ตรวจพบคำสั่งของบอทลบกลุ่ม จำเป็นต้องนำออกเพื่อความปลอดภัยของสมาชิก โจ๊ะๆ (｀・ω・´)")										
        if op.type == 17:
        	dan = line.getContact(op.param2)
        	tgb = line.getGroup(op.param1)
        	line.sendMessage(op.param1, "สวัสดี {}, Welcome to Group {}\nเข้ามาแล้วทำตัวดีๆละ\nอ่ย่าไปเป็นบ้าลบเพื่อนๆออกกลุ่มนะ (｀・ω・´)".format(str(dan.displayName),str(tgb.name)))
        	line.sendContact(op.param1, op.param2)
        	line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        if op.type == 15:
        	dan = line.getContact(op.param2)
        	tgb = line.getGroup(op.param1)
        	line.sendMessage(op.param1, "ง้ะ {}, ได้ออกจากกลุ่ม {} \nยืนไว้อาลัยแด่เขาเป็นเวลา3วินาที งุงิ (｀・ω・´)".format(str(dan.displayName),str(tgb.name)))
        	line.sendContact(op.param1, op.param2)
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n🔰" + Name
                            pref=['eh ada','hai kak','hay kamu','nah ada','halo lg ngapain','halo','sini kak','cctv yah kak']
                            line.sendMessage(op.param1, str(random.choice(pref))+' '+Name)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	line.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            print ("[ 55 ] ตรวจพบข้อความ")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
