# -*- coding: utf-8 -*-
from Rin2.linepy import *
from Rin2.akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.request, urllib.parse, urllib.error, urllib.parse,antolib,subprocess,unicodedata,GACSender,pafy, youtube_dl, timeit, atexit, traceback
_session = requests.session()
from gtts import gTTS
from googletrans import Translator
import youtube_dl
#========================
#loop = asyncio.get_event_loop()
#========================
client = LINE()
client.log("Auth Token : " + str(client.authToken))
client.log("Timeline Token : " + str(client.tl.channelAccessToken))
#========================
print ("SELFBOT-BY:MAX")
# =====================================
clientMid = client.profile.mid
clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientPoll = OEPoll(client)

DHENZA = [client]
BOT = [clientMid]
#=====================================
msg_dict = {}
botStart = time.time()
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")

images = json.load(imagesOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)
videos = json.load(videosOpen)

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

settings = {
    "autoAdd": False,
    "autoBlock": False,
    "autoJoin": False,
    'autoCancel':{"on":True,"members":4},
    "autoLeave": True,
    "groupParam": {},
    "autoRead": False,
    "system": True,
    "addAudio": {
        "name": "",
        "status": False
    },
    "addImage": {
        "name": "",
        "status": False
    },
    "addSticker": {
        "name": "",
        "status": False
    },
    "addVideo": {
        "name": "",
        "status": False
    },
    "nilaiSpam": "1",
    "GroupSpam": {},
    "changeProfileVideo": False,
    "autoRespon": False,
    "autoJoinTicket": False,
    "checkContact": False,
    "checkPost": False,
    "checkSticker": False,
    "save_sticker": False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "chatEvent": {},
    "pkgid": {},
    "stkid": {},
    "welcome": {},
    "team": {},
    "welcomeimg": {},
    "welcometext": {},
    "friendlist": {},
    "like": {},
    "autoPurge": {},
    "update_mention": False,
    "save_mention": " ",
    "textwelcome": ".....",
    "keyCommand": ".",
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "setKey": False,
    "unsendMessage": False,
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
    ]
}

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

settings["myProfile"]["displayName"] = clientProfile.displayName
settings["myProfile"]["statusMessage"] = clientProfile.statusMessage
settings["myProfile"]["pictureStatus"] = clientProfile.pictureStatus
settings["myProfile"]["coverId"] = client.getProfileDetail()["result"]["objectId"]

def Refresh():
    time.sleep(10)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def Ratakan(targ):
    client.kickoutFromGroup(settings["groupParam"],[targ])


def backupData():
    try:
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = images
        f = codecs.open('image.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = audios
        f = codecs.open('audio.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = videos
        f = codecs.open('video.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def ChangeVideoProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = client.genOBSParams({'oid': clientMid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'Hello_World.mp4'})
        data = {'params': obs_params}
        r_vp = client.server.postContent('{}/talk/vp/upload.nhn'.format(str(client.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        client.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    client.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    client.sendMessage(to, '', contentMetadata, 7)

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                client.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd

def helpmessage():
    if settings['setKey'] == True:
        key = settings['keyCommand']
        key = key.title()
    else:
        key = ''
    helpMessage =   "âââHá´Êá´ Êá´á´Ë¢áµâââ" + "\n\n" + \
                    key + "â Help" + "\n" + \
                    key + "â Help Trans" + "\n" + \
                    key + "â Help Media" + "\n" + \
                    key + "â Help Settings" + "\n" + \
                    key + "â Help Group" + "\n" + \
                    key + "â Help Bot" + "\n" + \
                    key + "â Reboot" + "\n" + \
                    key + "â Runtime" + "\n" + \
                    key + "â Speed" + "\n" + \
                    key + "â Settings" + "\n" + \
                    key + "â MyKey" + "\n" + \
                    key + "â SetKeyãOn/Offã" + "\n" + \
                    key + "â SbãOn/Offã" + "\n" + \
                    key + "â Me" + "\n" + \
                    key + "â Myinfo" + "\n" + \
                    key + "â Gift" + "\n" + \
                    key + "â Mymid" + "\n" + \
                    key + "â Myname" + "\n" + \
                    key + "â Mybio" + "\n" + \
                    key + "â Mypicture" + "\n" + \
                    key + "â Myvideoprofile" + "\n" + \
                    key + "â Mycover" + "\n" + \
                    key + "â ContactãMentionã" + "\n" + \
                    key + "â MidãMentionã" + "\n" + \
                    key + "â NameãMentionã" + "\n" + \
                    key + "â BioãMentionã" + "\n" + \
                    key + "â PictureãMentionã" + "\n" + \
                    key + "â VideoprofileãMentionã" + "\n" + \
                    key + "â CoverãMentionã" + "\n" + \
                    key + "â Myrestore" + "\n" + \
                    key + "â Backup" + "\n" + \
                    key + "â Rejectall" + "\n" + \
                    key + "â Myticket" + "\n" + \
                    key + "â Byee" + "\n" + \
                    key + "â Bye all" + "\n" + \
                    key + "â Rechat" + "\n" + \
                    key + "â Refresh" + "\n" + \
                    key + "â Tagall" + "\n" + \
                    key + "Sá´ÊÒÊá´á´ á´ .10 By: TBP Ë¢áµ" + "\n" + \
                    "http://line.me/ti/p/~teambotprotect"
    return helpMessage

def helpsettings():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpSettings =  "âââHá´Êá´ sá´á´á´ÉªÉ´É¢sâââ" + "\n" + \
                          key + "â AddãOn/Offã" + "\n" + \
                          key + "â JoinãOn/Offã" + "\n" + \
                          key + "â TicketãOn/Offã" + "\n" + \
                          key + "â LeaveãOn/Offã" + "\n" + \
                          key + "â ReadãOn/Offã" + "\n" + \
                          key + "â ResponãOn/Offã" + "\n" + \
                          key + "â ContactãOn/Offã" + "\n" + \
                          key + "â PostãOn/Offã" + "\n" + \
                          key + "â StickerãOn/Offã" + "\n" + \
                          key + "â UnsendãOn/Offã" + "\n" + \
                          key + "â SiderãOn/Offã" + "\n" + \
                          key + "â RejectãOn/Offã" + "\n" + \
                          key + "â ChatstickerãOn/Offã" + "\n" + \
                          key + "â WelcomeimgãOn/Offã" + "\n" + \
                          key + "â WelcometextãOn/Offã" + "\n" + \
                          key + "â NamelockãOn/Offã" + "\n" + \
                          key + "â IconlockãOn/Offã" + "\n" + \
                          key + "â ProqrãOn/Offã" + "\n" + \
                          key + "â UrlãOn/Offã" + "\n" + \
                          key + "â ClearãOn/Offã" + "\n" + \
                          key + "â KickãOn/Offã" + "\n" + \
                          key + "â MemberlockãOn/Offã" + "\n" + \
                          key + "â ProinviteãOn/Offã" + "\n" + \
                          key + "â Setwelcome:ãQueryã" + "\n" + \
                          key + "â Setmention:ãQueryã" + "\n" + \
                          key + "â Changename:ãQueryã" + "\n" + \
                          key + "â Changebio:ãQueryã" + "\n" + \
                          key + "Sá´ÊÒÊá´á´ á´ .10 By: TBP Ë¢áµ" + "\n" + \
                          "http://line.me/ti/p/~teambotprotect"
    return helpSettings

def helpmedia():
    if settings['setKey'] == True:
        key = settings['keyCommand']
        key = key.title()
    else:
        key = ''
    helpMedia =  "âââHá´Êá´ Má´á´Éªá´âââ" + "\n" + \
               key + "â Ytmp3ãQueryã" + "\n" + \
               key + "â HoroscopãQueryã" + "\n" + \
               key + "â ZodiakãQueryã" + "\n" + \
               key + "â Ytmp4ãQueryã" + "\n" + \
               key + "â Google searchãQueryã" + "\n" + \
               key + "â CheckdateãDateã" + "\n" + \
               key + "â Checkwebsiteãurlã" + "\n" + \
               key + "â Hitungãno+ÃÃ·noã" + "\n" + \
               key + "â Mysticker" + "\n" + \
               key + "â Line id" + "\n" + \
               key + "â InstainfoãNameã" + "\n" + \
               key + "â InstapostãNameã|ãNoã" + "\n" + \
               key + "â InstastoryãNameã|ãNoã" + "\n" + \
               key + "â YoutubeãSearchã" + "\n" + \
               key + "â BokepãSearchã" + "\n" + \
               key + "â TulisãSearchã" + "\n" + \
               key + "â MusicãSearchã" + "\n" + \
               key + "â LyricãSearchã" + "\n" + \
               key + "â ImageãSearchã" + "\n" + \
               "Sá´ÊÒÊá´á´ á´ .10 By: TBP Ë¢áµ" + "\n" + \
               "http://line.me/ti/p/~teambotprotect"
    return helpMedia

def helpgroup():
    if settings['setKey'] == True:
        key = settings['keyCommand']
        key = key.title()
    else:
        key = ''
    helpGroup =  "âââHá´Êá´ GÊá´á´á´âââ" + "\n" + \
              key + "â Creator" + "\n" + \
              key + "â Groupid" + "\n" + \
              key + "â Groupname" + "\n" + \
              key + "â Picture group" + "\n" + \
              key + "â Linkqr" + "\n" + \
              key + "â QrãOn/Offã" + "\n" + \
              key + "â Grouplist" + "\n" + \
              key + "â Member group" + "\n" + \
              key + "â Nk" + "\n" + \
              key + "â Kickall" + "\n" + \
              key + "â Info group" + "\n" + \
              key + "â Setgroupimage" + "\n" + \
              key + "â Gn:ãQueryã" + "\n" + \
              key + "Sá´ÊÒÊá´á´ á´ .10 By: TBP Ë¢áµ" + "\n" + \
              "http://line.me/ti/p/~teambotprotect"
    return helpGroup

def helpbot():
    if settings['setKey'] == True:
        key = settings['keyCommand']
        key = key.title()
    else:
        key = ''
    helpBot =  "âââHá´Êá´ Bá´á´âââ" + "\n" + \
          key + "â Listblock" + "\n" + \
          key + "â Block contact" + "\n" + \
          key + "â Unblockall" + "\n" + \
          key + "â Changepicture" + "\n" + \
          key + "â Respon" + "\n" + \
          key + "â In" + "\n" + \
          key + "â Bye" + "\n" + \
          key + "â Ghost in|lv" + "\n" + \
          key + "â Botlist" + "\n" + \
          key + "â Bot add ãMentionã" + "\n" + \
          key + "â Delbot ãMentionã" + "\n" + \
          key + "â Kick ãMentionã" + "\n" + \
          key + "â Kicker ãMentionã" + "\n" + \
          key + "â Bunuh ãMentionã" + "\n" + \
          key + "â Tabok ãMentionã" + "\n" + \
          key + "â SayãQueryã" + "\n" + \
          key + "â B1 setpict" + "\n" + \
          key + "â B2 setpict" + "\n" + \
          key + "â B1 setname:ãQueryã" + "\n" + \
          key + "â B2 setname:ãQueryã" + "\n" + \
          key + "â B1 setbio:ãQueryã" + "\n" + \
          key + "â B2 setbio:ãQueryã" + "\n" + \
          key + "â B1 restore" + "\n" + \
          key + "â B2 restore" + "\n" + \
          key + "â Addsticker" + "\n" + \
          key + "â Ban ãMentionã" + "\n" + \
          key + "â Unban ãMentionã" + "\n" + \
          key + "â Cban" + "\n" + \
          key + "â Banlist" + "\n" + \
          key + "â Broadcast ãQueryã" + "\n" + \
          key + "â Groupcast ãQueryã" + "\n" + \
          key + "â ReplyãOn/Offã" + "\n" + \
          key + "â ReplyList" + "\n" + \
          key + "â ReplyaddãMentionã" + "\n" + \
          key + "â Del replyãMentionã" + "\n" + \
          key + "â Tagall" + "\n" + \
          key + "â LurkingãOn/Off/Resetã" + "\n" + \
          key + "â Lurking" + "\n" + \
          key + "â Gift" + "\n" + \
          key + "â Max:ãnoã" + "\n" + \
          key + "â Spamtext:ãtextã" + "\n" + \
          key + "â Spamtag ãMentionã" + "\n" + \
          key + "â Call" + "\n" + \
          key + "Sá´ÊÒÊá´á´ á´ .10 By: TBP Ë¢áµ" + "\n" + \
          "http://line.me/ti/p/~teambotprotect"
    return helpBot

def helptranslate():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTranslate = "âââHá´Êá´ TÊá´É´sâââ" + "\n" + \
                    key + "â af : afrikaans" + "\n" + \
                    key + "â sq : albanian" + "\n" + \
                    key + "â am : amharic" + "\n" + \
                    key + "â ar : arabic" + "\n" + \
                    key + "â hy : armenian" + "\n" + \
                    key + "â az : azerbaijani" + "\n" + \
                    key + "â eu : basque" + "\n" + \
                    key + "â be : belarusian" + "\n" + \
                    key + "â bn : bengali" + "\n" + \
                    key + "â bs : bosnian" + "\n" + \
                    key + "â bg : bulgarian" + "\n" + \
                    key + "â ca : catalan" + "\n" + \
                    key + "â ceb : cebuano" + "\n" + \
                    key + "â ny : chichewa" + "\n" + \
                    key + "â zhcn : chinese (simplified)" + "\n" + \
                    key + "â zhtw : chinese (traditional)" + "\n" + \
                    key + "â co : corsican" + "\n" + \
                    key + "â hr : croatian" + "\n" + \
                    key + "â cs : czech" + "\n" + \
                    key + "â da : danish" + "\n" + \
                    key + "â nl : dutch" + "\n" + \
                    key + "â en : english" + "\n" + \
                    key + "â eo : esperanto" + "\n" + \
                    key + "â et : estonian" + "\n" + \
                    key + "â tl : filipino" + "\n" + \
                    key + "â fi : finnish" + "\n" + \
                    key + "â fr : french" + "\n" + \
                    key + "â fy : frisian" + "\n" + \
                    key + "â gl : galician" + "\n" + \
                    key + "â ka : georgian" + "\n" + \
                    key + "â de : german" + "\n" + \
                    key + "â el : greek" + "\n" + \
                    key + "â gu : gujarati" + "\n" + \
                    key + "â ht : haitian creole" + "\n" + \
                    key + "â ha : hausa" + "\n" + \
                    key + "â haw : hawaiian" + "\n" + \
                    key + "â iw : hebrew" + "\n" + \
                    key + "â hi : hindi" + "\n" + \
                    key + "â hmn : hmong" + "\n" + \
                    key + "â hu : hungarian" + "\n" + \
                    key + "â is : icelandic" + "\n" + \
                    key + "â ig : igbo" + "\n" + \
                    key + "â id : indonesian" + "\n" + \
                    key + "â ga : irish" + "\n" + \
                    key + "â it : italian" + "\n" + \
                    key + "â ja : japanese" + "\n" + \
                    key + "â jw : javanese" + "\n" + \
                    key + "â kn : kannada" + "\n" + \
                    key + "â kk : kazakh" + "\n" + \
                    key + "â km : khmer" + "\n" + \
                    key + "â ko : korean" + "\n" + \
                    key + "â ku : kurdish (kurmanji)" + "\n" + \
                    key + "â ky : kyrgyz" + "\n" + \
                    key + "â lo : lao" + "\n" + \
                    key + "â la : latin" + "\n" + \
                    key + "â lv : latvian" + "\n" + \
                    key + "â lt : lithuanian" + "\n" + \
                    key + "â lb : luxembourgish" + "\n" + \
                    key + "â mk : macedonian" + "\n" + \
                    key + "â mg : malagasy" + "\n" + \
                    key + "â ms : malay" + "\n" + \
                    key + "â ml : malayalam" + "\n" + \
                    key + "â mt : maltese" + "\n" + \
                    key + "â mi : maori" + "\n" + \
                    key + "â mr : marathi" + "\n" + \
                    key + "â mn : mongolian" + "\n" + \
                    key + "â my : myanmar (burmese)" + "\n" + \
                    key + "â ne : nepali" + "\n" + \
                    key + "â no : norwegian" + "\n" + \
                    key + "â ps : pashto" + "\n" + \
                    key + "â fa : persian" + "\n" + \
                    key + "â pl : polish" + "\n" + \
                    key + "â pt : portuguese" + "\n" + \
                    key + "â pa : punjabi" + "\n" + \
                    key + "â ro : romanian" + "\n" + \
                    key + "â ru : russian" + "\n" + \
                    key + "â sm : samoan" + "\n" + \
                    key + "â gd : scots gaelic" + "\n" + \
                    key + "â sr : serbian" + "\n" + \
                    key + "â st : sesotho" + "\n" + \
                    key + "â sn : shona" + "\n" + \
                    key + "â sd : sindhi" + "\n" + \
                    key + "â si : sinhala" + "\n" + \
                    key + "â sk : slovak" + "\n" + \
                    key + "â sl : slovenian" + "\n" + \
                    key + "â so : somali" + "\n" + \
                    key + "â es : spanish" + "\n" + \
                    key + "â su : sundanese" + "\n" + \
                    key + "â sw : swahili" + "\n" + \
                    key + "â sv : swedish" + "\n" + \
                    key + "â tg : tajik" + "\n" + \
                    key + "â ta : tamil" + "\n" + \
                    key + "â te : telugu" + "\n" + \
                    key + "â th : thai" + "\n" + \
                    key + "â tr : turkish" + "\n" + \
                    key + "â uk : ukrainian" + "\n" + \
                    key + "â ur : urdu" + "\n" + \
                    key + "â uz : uzbek" + "\n" + \
                    key + "â vi : vietnamese" + "\n" + \
                    key + "â cy : welsh" + "\n" + \
                    key + "â xh : xhosa" + "\n" + \
                    key + "â yi : yiddish" + "\n" + \
                    key + "â yo : yoruba" + "\n" + \
                    key + "â zu : zulu" + "\n" + \
                    key + "â fil : Filipino" + "\n" + \
                    key + "â he : Hebrew" + "\n" + \
                    "\n" + \
                    "â Contoh : " + key + "tr-id dhenza" + "\n" + \
                    "\n" + \
                    key + "Sá´ÊÒÊá´á´ á´ .10 By: TBP Ë¢áµ" + "\n" + \
                    "http://line.me/ti/p/~teambotprotect"
    return helpTranslate
def cek(mid):
    if mid in ( clientMid):
        return True
    else:
        return False
async def clientBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
               sendMention(op.param1, "แอดมาหาพ่อมึงหรอ @! ไอ่ควาย 55555555",[op.param1])
               client.blockContact(op.param1)
            if settings["autoBlock"] == True:
               client.blockContact(op.param1)
#-----------------------------------
        if op.type == 13:
            if clientMID in op.param3:
                G = client.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            client.rejectGroupInvitation(op.param1)
                        else:
                            client.acceptGroupInvitation(op.param1)
                    else:
                        client.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        client.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    client.cancelGroupInvitation(op.param1, matched_list)				
        if op.type == 13:
            group = client.getGroup(op.param1)
            group.members = [] if not group.members else group.members
            if settings["autoLeave"] == True:
                if len(group.members) <= 4:
                    client.acceptGroupInvitation(group.id)
                    client.sendMessage(group.id,"???????????????? ??")
                    client.leaveGroup(group.id)
                    ronum = (ronum + 1)
                    print(ronum)
        if op.type == 13:
            if clientMid in op.param3:
                if settings["autoReject"] == True:
                    client.rejectGroupInvitation(op.param1)

#-----------------------------------------------------------------

        if op.type == 17:
           print ("[ 17 ] NOTIFIED JOINED INTO GROUP")
           if op.param1 in settings["welcomeimg"]:
               if op.param2 in settings["welcome"]:
                    pass
               elif cek(op.param2):
                    pass
               else:
                   path = "http://dl.profile.line.naver.jp/" + client.getContact(op.param2).pictureStatus
                   client.sendImageWithURL(op.param1, str(path))

        if op.type == 17:
          if op.param1 in settings["welcome"]:
             if op.param2 in settings["welcome"]:
                  pass
             elif cek(op.param2):
                  pass
             else:
                  ginfo = client.getGroup(op.param1)
                  contact = client.getContact(op.param2)
                  if op.param1 not in settings["welcometext"]:
                      client.sendMessage(op.param1,"Assalamualaikum kak " + str(contact.displayName) + "\n"+ "selamat datang  disini\nsemoga betah\nbersama kami disini di" +"\n"+ str(ginfo.name))
                  else:
                      client.sendMessage(op.param1,"Assalamualaikum kak " + str(contact.displayName) + "\n\n"+ settings["textwelcome"])
#-----------------------------------------------------------------
        if op.type == 25:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if cmd == "sb on":
                                if settings["system"] == True:
                                   client.sendMessage(to,"Sb on")
                                else:
                                   settings["system"] = True
                                   client.sendMessage(to,"has been enabled")
                            elif cmd == "sb off":
                                if settings["system"] == False:
                                    client.sendMessage(to,"Sb off")
                                else:
                                    settings["system"] = False
                                    client.sendMessage(to,"has been disabled")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        if op.type == 25:
          print ("[ 25 ] SEND MESSAGE")
          if settings["system"] == True:
            try:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if cmd == "help":
                                helpMessage = helpmessage()
                                client.sendMessage(to, str(helpMessage))
                            elif cmd == "help settings":
                                helpSettings = helpsettings()
                                client.sendMessage(to, str(helpSettings))
                            elif cmd == "help media":
                                helpMedia = helpmedia()
                                client.sendMessage(to, str(helpMedia))
                            elif cmd == "help group":
                                helpGroup = helpgroup()
                                client.sendMessage(to, str(helpGroup))
                            elif cmd == "help bot":
                                helpBot = helpbot()
                                client.sendMessage(to, str(helpBot))
                            elif cmd == "help trans":
                                helpTranslate = helptranslate()
                                client.sendMessage(to, str(helpTranslate))
                            elif cmd.startswith("changekey:"):
                                sep = text.split(":")
                                key = text.replace(sep[0] + ":","")
                                if " " in key:
                                    client.sendMessage(to, "jangan menggunakan spasi")
                                else:
                                    settings["keyCommand"] = str(key).lower()
                                    client.sendMessage(to, "Success mengubah key command menjadi [ {} ]".format(str(key).lower()))
                            elif cmd.startswith("setwelcome:"):
                                sep = text.split(":")
                                key = text.replace(sep[0] + ":","")
                                settings["welcometext"][msg.to] = "pipo"
                                settings["textwelcome"] = str(key).lower()
                                client.sendMessage(to, "Success mengubah welcometext menjadi [ {} ]".format(str(key).lower()))
                            elif cmd.startswith("setmention:"):
                                sep = text.split(":")
                                key = text.replace(sep[0] + ":","")
                                settings["update_mention"] = True
                                settings["save_mention"] = str(key).lower()
                                client.sendMessage(to, "Success mengubah text mention menjadi [ {} ]".format(str(key).lower()))
                            elif cmd.lower().startswith("broadcast:"):
                                 sep = text.split(":")
                                 tum = text.replace(sep[0] + ":","")
                                 me = client.getContact(lineMID)
                                 teman = client.getAllContactIds()
                                 for cerry in teman:
                                     client.sendMessage(cerry, tum + "\nBroadcasted By:\n" + me.displayName)
                            elif cmd.startswith("groupcast:"):
                                 sep = text.split(":")
                                 tum = text.replace(sep[0] + ":","")
                                 me = client.getContact(lineMID)
                                 grup = client.getGroupIdsJoined()
                                 for cerry in grup:
                                     client.sendMessage(cerry, tum + "\nBroadcasted By:\n" + me.displayName)
                            elif cmd.startswith("say"):
                                     pisah = msg.text.split(" ")
                                     isi = msg.text.replace(pisah[0]+" ","")
                                     client2.sendMessage(msg.to,str(isi))
                                     client3.sendMessage(msg.to,str(isi))
#                                     client4.sendMessage(msg.to,str(isi))
#                                     client5.sendMessage(msg.to,str(isi))

                            elif cmd == "addsticker":
                                 settings["save_sticker"] = True
                                 client.sendMessage(to,"please send sticker")
                            elif cmd == "speed":
                                start = time.time()
                                client.sendMessage(to, "Waiting...")
                                elapsed_time = time.time() - start
                                client.sendMessage(to, "{} detik".format(str(elapsed_time)))
                            elif cmd == "dell":
                                client.removeAllMessages(op.param2)
#                                client2.removeAllMessages(op.param2)
#                                client3.removeAllMessages(op.param2)
#                                client4.removeAllMessages(op.param2)
#                                client5.removeAllMessages(op.param2)
                                client.sendMessage(to,"Success clearchat")
                            elif cmd == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                client.sendMessage(to, "The Bot Is Running {}".format(str(runtime)))
                            elif cmd == "myinfo":
                                saya = client.getContact(clientMid)
                                grupku = client.getGroupIdsJoined()
                                temanku = client.getAllContactIds()
                                blocked = client.getBlockedContactIds()
                                tiket = client.reissueUserTicket()
                                ret_ = "âââ[My Info]"
                                ret_ +="\n\nâ  Nick: {}".format(saya.displayName)
                                ret_ +="\nâ  Friend: {}".format(str(len(temanku)))
                                ret_ +="\nâ  Group: {}".format(str(len(grupku)))
                                ret_ +="\nâ  Blocked: {}".format(str(len(blocked)))
                                ret_ +="\nâââ Ticket: {}".format("\nline.me/ti/p/"+str(tiket))
                                client.sendMessage(msg.to,str(ret_))
                            elif cmd == "reboot":
                                client.sendMessage(to, "Please waiting for in 5 minutes")
                                restartBot()
# Pembatas Script #
                            elif cmd == "add on":
                                settings["autoAdd"] = True
                                client.sendMessage(to, "Success mengaktifkan auto add")
                            elif cmd == "add off":
                                settings["autoAdd"] = False
                                client.sendMessage(to, "Success menonaktifkan auto add")
                            elif cmd == "join on":
                                settings["autoJoin"] = True
                                settings["autoLeave"] = False
                                client.sendMessage(to, "Success mengaktifkan auto join")
                            elif cmd == "join off":
                                settings["autoJoin"] = False
                                client.sendMessage(to, "Success menonaktifkan auto join")
                            elif cmd == "leave on":
                                settings["autoLeave"] = True
                                settings["autoJoin"] = False
                                client.sendMessage(to, "Success mengaktifkan auto leave")
                            elif cmd == "leave off":
                                settings["autoLeave"] = False
                                client.sendMessage(to, "Success menonaktifkan auto leave")
                            elif cmd == "respon on":
                                settings["autoRespon"] = True
                                client.sendMessage(to, "Success mengaktifkan auto respon")
                            elif cmd == "respon off":
                                settings["autoRespon"] = False
                                settings["update_mention"] = False
                                client.sendMessage(to, "Success menonaktifkan auto respon")
                            elif cmd == "read on":
                                settings["autoRead"] = True
                                client.sendMessage(to, "Success mengaktifkan auto read")
                            elif cmd == "read off":
                                settings["autoRead"] = False
                                client.sendMessage(to, "Success menonaktifkan auto read")
                            elif cmd == "reject on":
                                settings["autoReject"] = True
                                settings["autoLeave"] = True
                                settings["autoJoin"] = False
                                client.sendMessage(to, "Success on reject all invite")
                            elif cmd == "reject off":
                                settings["autoReject"] = False
                                client.sendMessage(to, "Success off reject all invite")
                            elif cmd == "ticket on":
                                settings["autoJoinTicket"] = True
                                client.sendMessage(to, "Success mengaktifkan auto join dengan ticket")
                            elif cmd == "ticket off":
                                settings["autoJoin"] = False
                                client.sendMessage(to, "Success menonaktifkan auto join dengan ticket")
                            elif cmd == "contact on":
                                settings["checkContact"] = True
                                client.sendMessage(to, "Success mengaktifkan check contact")
                            elif cmd == "contact off":
                                settings["checkContact"] = False
                                client.sendMessage(to, "Success menonaktifkan check contact")
                            elif cmd == "post on":
                                settings["checkPost"] = True
                                client.sendMessage(to, "Success mengaktifkan check post")
                            elif cmd == "post off":
                                settings["checkPost"] = False
                                client.sendMessage(to, "Success menonaktifkan check post")
                            elif cmd == "sticker on":
                                settings["checkSticker"] = True
                                client.sendMessage(to, "Success mengaktifkan check sticker")
                            elif cmd == "sticker off":
                                settings["checkSticker"] = False
                                client.sendMessage(to, "Success menonaktifkan check sticker")
                            elif cmd == "unsend on":
                                settings["unsendMessage"] = True
                                client.sendMessage(to, "Success mengaktifkan unsend message")
                            elif cmd == "unsend off":
                                settings["unsendMessage"] = False
                                client.sendMessage(to, "Success menonaktifkan unsend message")
                            elif cmd == "chatsticker on":
                                settings["chatEvent"][msg.to] = "pipo"
                                client.sendMessage(to,"Success mengaktifkan chatsticker")
                            elif cmd == "chatsticker off":
                                del settings["chatEvent"][msg.to]
                                client.sendMessage(to,"Success menonaktifkan chatsticker")
                            elif cmd == "welcomeimg on":
                                settings["welcomeimg"][msg.to] = "pipo"
                                client.sendMessage(to,"Success mengaktifkan welcomeimage")
                            elif cmd == "welcomeimg off":
                                del settings["welcomeimg"][msg.to]
                                client.sendMessage(to,"Success menonaktifkan welcomeimage")
                            elif cmd == "welcometext on":
                                settings["welcome"][msg.to] = "pipo"
                                client.sendMessage(to,"Success mengaktifkan welcometext")
                            elif cmd == "welcometext off":
                                del settings["welcome"][msg.to]
                                client.sendMessage(to,"Success menonaktifkan welcometext")
                            elif cmd == 'sider on':
                                try:
                                    del cctv['point'][msg.to]
                                    del cctv['sidermem'][msg.to]
                                    del cctv['cyduk'][msg.to]
                                except:
                                    pass
                                    cctv['point'][msg.to] = msg.id
                                    cctv['sidermem'][msg.to] = ""
                                    cctv['cyduk'][msg.to] = "pipo"
                                    settings["Sider"] = True
                                    client.sendMessage(msg.to,"Success on sider")

                            elif cmd == 'sider off':
                                if msg.to in cctv['point']:
                                    del cctv['cyduk'][msg.to]
                                    settings["Sider"] = False
                                    client.sendMessage(msg.to,"Success off sider")
                                else:
                                    client.sendMessage(msg.to, "Success off sider")

                            elif cmd == "url on":
                                if msg.to in settings["lockUrl"]:
                                    client.sendMessage(to,"already done")
                                else:
                                    gid = msg.to
                                    settings["lockUrl"][gid] = "pipo"
                                    client.sendMessage(to,"done")
                            elif cmd == "url off":
                                if msg.to not in settings["lockUrl"]:
                                    client.sendMessage(to,"already off")
                                else:
                                    gid = msg.to
                                    del settings["lockUrl"][gid]
                                    client.sendMessage(to,"done")
                            elif cmd == "clear on":
                                if msg.to in settings["autoPurge"]:
                                    client.sendMessage(to,"Done on")
                                else:
                                    gid = msg.to
                                    settings["autoPurge"][gid] = "pipo"
                                    client.sendMessage(to,"Success Clear on")
                            elif cmd == "clear off":
                                if msg.to not in settings["autoPurge"]:
                                    client.sendMessage(to,"Done off")
                                else:
                                    gid = msg.to
                                    del settings["autoPurge"][gid]
                                    client.sendMessage(to,"Success clear off")

                            elif cmd == "settings":
                                try:
                                    ret_ = "âââStstus Bot SKYâââ\n"
                                    if settings["autoAdd"] == True: ret_ += "\nð´ Auto Add  [+]"
                                    else: ret_ += "\nâ« Auto Add  [-]"
                                    if settings["autoJoin"] == True: ret_ += "\nð´ Auto Join  [+]"
                                    else: ret_ += "\nâ« Auto Join  [-]"
                                    if settings["autoLeave"] == True: ret_ += "\nð´ Auto Leave  [+]"
                                    else: ret_ += "\nâ« Auto Leave  [-]"
                                    if settings["autoJoinTicket"] == True: ret_ += "\nð´ Join Ticket  [+]"
                                    else: ret_ += "\nâ« Join Ticket  [-]"
                                    if settings["autoRead"] == True: ret_ += "\nð´ Auto Read  [+]"
                                    else: ret_ += "\nâ« Auto Read  [-]"
                                    if settings["autoRespon"] == True: ret_ += "\nð´ Respon  [+]"
                                    else: ret_ += "\nâ« Respon  [-]"
                                    if settings["checkContact"] == True: ret_ += "\nð´ Contact  [+]"
                                    else: ret_ += "\nâ« Contact  [-]"
                                    if settings["checkPost"] == True: ret_ += "\nð´ Check Post  [+]"
                                    else: ret_ += "\nâ« Check Post  [-]"
                                    if settings["checkSticker"] == True: ret_ += "\nð´ Check Sticker  [+]"
                                    else: ret_ += "\nâ« Check Sticker  [-]"
                                    if settings["setKey"] == True: ret_ += "\nð´ Set Key  [+]"
                                    else: ret_ += "\nâ« Set Key  [-]"
                                    if settings["unsendMessage"] == True: ret_ += "\nð´ Unsend Message  [+]"
                                    else: ret_ += "\nâ« Unsend Message  [-]"
                                    if msg.to in cctv["cyduk"]: ret_ += "\nð´ Sider  [+]"
                                    else: ret_ += "\nâ« Sider  [-]"
                                    if msg.to in settings["welcome"]: ret_ += "\nð´ Welcometext  [+]"
                                    else: ret_ += "\nâ« Welcometext  [-]"
                                    if msg.to in settings["welcomeimg"]: ret_ += "\nð´ Welcomeimage  [+]"
                                    else: ret_ += "\nâ« Welcomeimage  [-]"
#                                    if msg.to in settings["lockqr"]: ret_ += "\nð´ Proqr  [+]"
#                                    else: ret_ += "\nâ« Proqr  [-]"
                                    if msg.to in settings["lockname"]: ret_ += "\nð´ Namelock  [+]"
                                    else: ret_ += "\nâ« Namelock  [-]"
                                    if msg.to in settings["lockicon"]: ret_ += "\nð´ Iconlock  [+]"
                                    else: ret_ += "\nâ« Iconlock  [-]"
                                    if msg.to in settings["lockinvite"]: ret_ += "\nð´ Proinvite  [+]"
                                    else: ret_ += "\nâ« Proinvite  [-]"
                                    if msg.to in settings["lockJoin"]: ret_ += "\nð´ Joinlock  [+]"
                                    else: ret_ += "\nâ« Joinlock  [-]"
                                    if msg.to in settings["lockMember"]: ret_ += "\nð´ Memberlock  [+]"
                                    else: ret_ += "\nâ« Memberlock  [-]"
                                    if msg.to in settings["autoPurge"]: ret_ += "\nð´ AutoClear  [+]"
                                    else: ret_ += "\nâ« AutoClear  [-]"
                                    client.sendMessage(to, str(ret_))
                                except Exception as e:
                                    client.sendMessage(msg.to, str(e))
# Pembatas Script 
                            elif cmd == 'myticket':
                                 tiket = client.reissueUserTicket()
                                 client.sendMessage(to, "My ticket\n\nline.me/ti/p/"+tiket)
                            elif cmd == 'bye me':
                                if msg.toType == 2:
                                    client.sendMessage(to, "pamit dulu ya..")
                                    client.leaveGroup(msg.to)
                            elif cmd == 'bye all':
                                if msg.toType == 2:
                                    td = client.getGroupIdsJoined()
                                    client.sendMessage(to,"see you next time")
                                    for i in td:
                                        client.leaveGroup(i)
                            elif cmd == 'block contact':
                                blockedlistt = client.getBlockedContactIds()
                                for zx in blockedlistt:
                                    client.sendContact(to,zx)
                            elif cmd == 'unblockall':
                                blockedlistt = client.getBlockedContactIds()
                                for zx in blockedlistt:
                                    client.unblockContact(zx)
                                client.sendMessage(to, "Success")
                            elif cmd == 'listblock':
                                blockedlist = client.getBlockedContactIds()
                                kontak = client.getContacts(blockedlist)
                                num=1
                                msgs="âââà¿List Blockedà¿âââ"
                                for ids in kontak:
                                    msgs+="\n[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nâââà¿ Total Blocked : %i" % len(kontak)
                                client.sendMessage(to, msgs)
                            elif cmd == "crash":
                                 client.sendContact(to, "00000000000000000000000000000000000000000000000000',")
                            elif cmd.startswith("changename:"):
                                sep = text.split(":")
                                string = text.replace(sep[0] + ":","")
                                if len(string) <= 20:
                                    profile = client.getProfile()
                                    profile.displayName = string
                                    client.updateProfile(profile)
                                    client.sendMessage(to,"Success mengganti display name menjadi{}".format(str(string)))
                            elif cmd.startswith("setname:"):
                                sep = text.split(":")
                                string = text.replace(sep[0] + ":","")
                                if len(string) <= 20:
                                    profile = client.getProfile()
                                    profile.displayName = string
                                    client.updateProfile(profile)
                                    client.sendMessage(to,"Success mengganti display name menjadi{}".format(str(string)))
                            elif cmd.startswith("changebio:"):
                                sep = text.split(":")
                                string = text.replace(sep[0] + ":","")
                                if len(string) <= 5000:
                                    profile = client.getProfile()
                                    profile.statusMessage = string
                                    client.updateProfile(profile)
                                    client.sendMessage(to,"Success mengganti status message menjadi{}".format(str(string)))
                            elif cmd.startswith("max: "):
                                            pisah = text.split(":")
                                            strnum = text.replace(pisah[0] + ":","")
                                            settings["nilaiSpam"] = str(strnum)
                                            client.sendMessage(to, "Jumlah spam telah di tetapkan menjadi:"+str(strnum))
                            elif cmd.startswith("spamtext: "):
                                            pisah = text.split(":")
                                            tulisan = text.replace(pisah[0] + ":","")
                                            num = int(settings["nilaiSpam"])
                                            for var in range(0,num):
                                                client.sendMessage(to, str(tulisan))
                            elif cmd == "call":
                                            grupnya = client.getGroup(msg.to)
                                            membernya = [mem.mid for mem in grupnya.members]
                                            num = int(settings["nilaiSpam"])
                                            for var in range(0,num):
                                                client.inviteIntoGroupCall(to, contactIds=membernya)
                                            client.sendMessage(to,"succes spam {} Groupcall".format(str(settings["nilaiSpam"])))
                            elif cmd.startswith("spamtag "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    num = int(settings["nilaiSpam"])
                                    for ls in lists:
                                        for var in range(0,num):
                                            client.sendMessageWithMention(to,ls," "," ")
#SC SpaM group#
                            elif cmd.startswith("gspam "):
                                data = msg.text.replace("gspam ","")
                                korban = data.split('|')
                                korban = korban[1].replace(' ','')
                                num = data.split('|')
                                num = num[2].replace(' ','')
                                midd = korban
                                jumlah = int(num)
                                if jumlah <= 500:
                                    for var in range(0,jumlah):
                                        client.sendMessage(msg.to,"Sukses Spamming Grup!\nTarget: "+client.getContact(midd).displayName+"\nJumlah Grup Yang Di Spam: "+jumlah)
                                        client.findAndAddContactsByMid(midd)
                                        client.createGroup(settings["GroupSpam"],midd)
                                        client.inviteIntoGroup(msg.to,midd)
                                else:
                                    client.sendMessage(msg.to, "Over Spam Boss Kasihan Korban ")
                            elif cmd.startswith("setgroup: "):
                                sep = msg.text.split(" ")
                                settings["GroupSpam"] = msg.text.replace(sep[0] + " ","")
                                client.sendMessage(msg.to,"Nama Group Berhasil Diubah Menjadi : "+settings["GroupSpam"])
#-----_++-----------------
                            elif cmd == 'gift':
                                code = "a0768339-c2d3-4189-9653-2909e9bb6f58"
                                typen = "sticker"
                                client.sendGift(to,code,typen)
                            elif cmd == "me":
                                client.sendMessageMusic(to, title=client.getContact(sender).displayName, subText=str(client.getContact(sender).statusMessage), url='line.me/ti/p/~teambotprotect', iconurl="http://dl.profile.line-cdn.net/{}".format(client.getContact(sender).pictureStatus), contentMetadata={}) 
                            elif cmd == "mymid":
                                client.sendMessage(to, "[ MID ]\n{}".format(sender))
                            elif cmd == "myname":
                                contact = client.getContact(sender)
                                client.sendMessage(to, "[ Display Name ]\n{}".format(contact.displayName))
                            elif cmd == "mybio":
                                contact = client.getContact(sender)
                                client.sendMessage(to, "[ Status Message ]\n{}".format(contact.statusMessage))
                            elif cmd == "mypicture":
                                contact = client.getContact(sender)
                                client.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "myvideoprofile":
                                contact = client.getContact(sender)
                                client.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "mycover":
                                channel = client.getProfileCoverURL(sender)
                                path = str(channel)
                                client.sendImageWithURL(to, path)

                            elif cmd == "ren" or cmd == ", ":
                                client.inviteIntoGroup(msg.to,["u53fbc0c54039a2ba4652ae9e1fbfdeab"])
                          #  elif cmd == "rendi" or cmd == ". ":
                           #     client.inviteIntoGroup(msg.to,["udc6a8e6b62cb13b92cb1456a20bdcf43"])
                            #elif cmd == "!" or cmd == "! ":
                                client.inviteIntoGroup(msg.to,[""])
                            elif cmd.startswith("?? "):
                                key = eval(msg.contentMetadata['MENTION'])
                                key['MENTIONEES'][0]["M"]
                                targets = []
                                for x in key['MENTIONEES']:
                                    targets.append(x["M"])
                                for target in targets:
                                    settings["groupParam"] = msg.to
                                    try:
                                        p = Pool(40)
                                        p.map(Ratakan,targets)
                                        p.close()
                                        p.terminate()
                                        p.join
                                        Refresh()
                                    except Exception as error:
                                        p.close()
                                        return    

                            elif cmd.startswith("copy "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.cloneContactProfile(ls)
                                        client.sendMessage(to, "Success Copy profile {}".format(contact.displayName))

                            elif cmd == "myrestore":
                                try:
                                    clientProfile = client.getProfile()
                                    clientProfile.displayName = str(settings["myProfile"]["displayName"])
                                    clientProfile.statusMessage = str(settings["myProfile"]["statusMessage"])
                                    clientProfile.pictureStatus = str(settings["myProfile"]["pictureStatus"])
                                    client.updateProfileAttribute(8, clientProfile.pictureStatus)
                                    client.updateProfile(clientProfile)
                                    coverId = str(settings["myProfile"]["coverId"])
                                    client.updateProfileCoverById(coverId)
                                    client.sendMessage(to, "Success restore profile waiting in prossesing")
                                except Exception as e:
                                    client.sendMessage(to, "Failid restore profile")
                                    logError(error)

                            elif cmd == "backup":
                                try:
                                    profile = client.getProfile()
                                    settings["myProfile"]["displayName"] = str(profile.displayName)
                                    settings["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                    settings["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
                                    coverId = client.getProfileDetail()["result"]["objectId"]
                                    settings["myProfile"]["coverId"] = str(coverId)
                                    client.sendMessage(to, "Success backup profile")
                                except Exception as e:
                                    client.sendMessage(to, "Failid backup profile")
                                    logError(error)
                            elif cmd.startswith("mid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}".format(str(ls))
                                    client.sendMessage(to, str(ret_))
                            elif cmd.startswith("tabok "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
#                                        settings["blacklist"][ls] = "pipo"
#                                        petugas = [client]
                                        try:
                                            client.kickoutFromGroup(msg.to,[ls])
                                        except:
                                            client.kickoutFromGroup(msg.to,[ls])

                            elif cmd.startswith("name "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                            elif cmd.startswith("bio "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMessage(to, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                            elif cmd.startswith("picture"):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        client.sendImageWithURL(to, str(path))
                            elif cmd.startswith("contact "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.sendContact(to,str(ls))
                            elif cmd.startswith("videoprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        client.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("cover "):
                                if client != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            channel = client.getProfileCoverURL(ls)
                                            path = str(channel)
                                            client.sendImageWithURL(to, str(path))
# Pembatas Script #
                            elif cmd == 'creator':
                                group = client.getGroup(to)
                                GS = group.creator.mid
                                client.sendContact(to, GS)
                            elif cmd == 'groupid':
                                gid = client.getGroup(to)
                                client.sendMessage(to, "[ID Group : ]\n" + gid.id)
                            elif cmd == 'picture group':
                                group = client.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                client.sendImageWithURL(to, path)
                            elif cmd == 'group name':
                                gid = client.getGroup(to)
                                client.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                            elif cmd == "rejectall":
                                ginvited = client.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        client.rejectGroupInvitation(gid)
                                    client.sendMessage(msg.to, "Success canceled {} group invitation".format(str(len(ginvited))))
                                else:
                                    client.sendMessage(msg.to, "there is no invitation group")
                            elif cmd == 'linkqr':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = client.reissueGroupTicket(to)
                                        client.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                                    else:
                                        client.sendMessage(to, "Grup qr closed silahkan buka terlebih dahulu dengan {}openqr".format(str(settings["keyCommand"])))
                            elif cmd == 'qr on':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        client.sendMessage(to, "Grup qr sudah terbuka")
                                    else:
                                        group.preventedJoinByTicket = False
                                        client.updateGroup(group)
                                        client.sendMessage(to, "Success membuka grup qr")
                            elif cmd == 'qr off':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == True:
                                        client.sendMessage(to, "Grup qr sudah tertutup")
                                    else:
                                        group.preventedJoinByTicket = True
                                        client.updateGroup(group)
                                        client.sendMessage(to, "Success off qr")
                            elif cmd == 'info group':
                                group = client.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Not Found"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Closed"
                                    gTicket = "nothing"
                                else:
                                    gQr = "Opened"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "âââ[Info Group]\n"
                                ret_ += "\nâ  [Nama Group]\n{}".format(str(group.name))
                                ret_ += "\nâ  [ID Group]\n{}".format(group.id)
                                ret_ += "\nâ  [Group creator]\n{}".format(str(gCreator))
                                ret_ += "\nâ  Amount Member : {}".format(str(len(group.members)))
                                ret_ += "\nâ  Jumlah Pending : {}".format(gPending)
                                ret_ += "\nâ  Group Qr : {}".format(gQr)
                                ret_ += "\nâââ[ Group Ticket : {}".format(gTicket)
                                client.sendMessage(to, str(ret_))
                                client.sendImageWithURL(to, path)

                            elif cmd == 'member list':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    ret_ = "âââ[Member List]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n[ Total {} ]".format(str(len(group.members)))
                                    client.sendMessage(to, str(ret_))
                            elif cmd == 'listgroup':
                                    groups = client.groups
                                    ret_ = "âââ[Group List]"
                                    no = 0 + 1
                                    for gid in groups:
                                        group = client.getGroup(gid)
                                        ret_ += "\n{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n[ Total {} Groups ]".format(str(len(groups)))
                                    client.sendMessage(to, str(ret_))
# Pembatas Script #sampe sini editnya
                            elif cmd == "changepicture":
                                settings["changePictureProfile"] = True
                                client.sendMessage(to, "Send image")

                            elif cmd == "up foto":
                                settings["changeProfileVideo"] = True
                                client.sendMessage(to, "Send image")
                            elif cmd == "up video":
                                settings["changeProfileVideo"] = True
                                client.sendMessage(to, "Send videos")

                            elif cmd.startswith("gn:"):
                                 G = client.getGroup(msg.to)
                                 pisah = msg.text.split(":")
                                 G.name = msg.text.replace(pisah[0]+":","")
                                 client.updateGroup(G)
                                 client.sendMessage(msg.to,"success")
                            elif cmd == "setgroupimage":
                                if msg.toType == 2:
                                    if to not in settings["changeGroupPicture"]:
                                        settings["changeGroupPicture"].append(to)
                                    client.sendMessage(to, "Send image")
                            elif cmd == 'tagall':
                                group = client.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    client.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    client.sendMessage(to, "Total {} Mention".format(str(len(nama))))
                            elif cmd == "lurking on":
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
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    client.sendMessage(receiver,"Lurking telah diaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    client.sendMessage(receiver,"Set reading point : \n" + readTime)
                            elif cmd == "lurking off":
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
                                if receiver not in read['readPoint']:
                                    client.sendMessage(receiver,"Lurking dinonaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    client.sendMessage(receiver,"Delete reading point : \n" + readTime)

                            elif cmd == "lurking reset":
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
                                        del read["ROM"][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    client.sendMessage(msg.to, "Reset reading point : \n" + readTime)
                                else:
                                    client.sendMessage(msg.to, "Lurking belum aktif boss")

                            elif cmd == "lurking":
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
                                    if read["ROM"][receiver].items() == []:
                                        client.sendMessage(receiver,"not Sider")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = client.getContacts(chiya)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '[ CCTV ]\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n" + readTime
                                    try:
                                        client.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    client.sendMessage(receiver,"Lurking belum aktif")
                            elif cmd.startswith("replay add"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        settings["mimic"]["target"][target] = True
                                        client.sendMessage(msg.to,"Target added")
                                        break
                                    except:
                                        client.sendMessage(msg.to,"Failid added target")
                                        break
                            elif cmd.startswith("del replay"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        del settings["mimic"]["target"][target]
                                        client.sendMessage(msg.to,"Target delated")
                                        break
                                    except:
                                        client.sendMessage(msg.to,"Failid delated target")
                                        break

                            elif cmd == "replay list":
                                if settings["mimic"]["target"] == {}:
                                    client.sendMessage(msg.to,"Nothing")
                                else:
                                    mc = "âââMimic List]]<=="
                                    for mi_d in settings["mimic"]["target"]:
                                        mc += "\nâââ"+client.getContact(mi_d).displayName
                                    client.sendMessage(msg.to,mc)

                            elif cmd.startswith("replay"):
                                sep = text.split(" ")
                                mic = text.replace(sep[0] + " ","")
                                if mic == "on":
                                    if settings["mimic"]["status"] == False:
                                        settings["mimic"]["status"] = True
                                        client.sendMessage(msg.to,"Reply Message on")
                                elif mic == "off":
                                    if settings["mimic"]["status"] == True:
                                        settings["mimic"]["status"] = False
                                        client.sendMessage(msg.to,"Reply Message off")
# Pembatas Script #
                            elif cmd.startswith("checkwebsite"):
                                try:
                                    sep = text.split(" ")
                                    query = text.replace(sep[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                    data = r.text
                                    data = json.loads(data)
                                    client.sendImageWithURL(to, data["result"])
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkdate"):
                                try:
                                    sep = msg.text.split(" ")
                                    tanggal = msg.text.replace(sep[0] + " ","")
                                    r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                    data=r.text
                                    data=json.loads(data)
                                    ret_ = "âââ[ DATE ]ââ"
                                    ret_ += "\nâ  Date Of Birth : {}".format(str(data["data"]["lahir"]))
                                    ret_ += "\nâ  Age : {}".format(str(data["data"]["usia"]))
                                    ret_ += "\nâ  Birthday : {}".format(str(data["data"]["ultah"]))
                                    ret_ += "\nâââ Zodiak : {}".format(str(data["data"]["zodiak"]))
                                    client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("sholat:"):
                                search = text.replace("sholat ","")
                                r = requests.get("http://leert.corrykalam.gq/praytime.php?location={}".format(str(search)))
                                data = r.text
                                data = json.loads(data)
                                try:
                                    fine = "âââ[Jadwal Waktu Sholat]ââ"
                                    fine += "\nâ "
                                    fine += "\nâ  Subuh : {}".format(str(data["pray_time"]["subuh"]))
                                    fine += "\nâ  Dhuhur : {}".format(str(data["pray_time"]["dzuhur"]))
                                    fine += "\nâ  Ashar : {}".format(str(data["pray_time"]["ashar"]))
                                    fine += "\nâ  Maghrib : {}".format(str(data["pray_time"]["maghrib"]))
                                    fine += "\nâ  Isya : {}".format(str(data["pray_time"]["isha"]))
                                    fine += "\nâ  Imsak : {}".format(str(data["pray_time"]["imsak"]))
                                    fine += "\nâ  Latitude : {}".format(str(data["info"]["latitude"]))
                                    fine += "\nâ  Longitude : {}".format(str(data["info"]["longitude"]))
                                    fine += "\nâ "
                                    fine += "\nâ  Timezone : {}".format(str(data["info"]["timezone"]))
                                    fine += "\nâ  Date : {}".format(str(data["info"]["date"]))
                                    fine += "\nâ "
                                    fine += "\nâââ For: {} & sekitarnya".format(str(search))
                                    client.sendMessage(to, str(fine))
                                except Exception as error:
                                    client.sendMessage(to,str(error))
                            elif cmd.startswith("like "):
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).mid
                                    s = client.getContact(u).displayName
                                    hasil = client.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        client.likePost(str(msg.to), str(result), likeType=random.choice(typel))
                                        client.createComment(str(msg.to), str(result), ["comment"])
                                    client.sendMessage(msg.to, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    cl.sendMessage(msg.to, str(e))


                            elif cmd.startswith("video "):
                                try:
                                    sep = msg.text.split(" ")
                                    textToSearch = msg.text.replace(sep[0] + " ","")
                                    query = urllib.parse.quote(textToSearch)
                                    url = "https://www.youtube.com/results?search_query=" + query
                                    response = urllib.request.urlopen(url)
                                    html = response.read()
                                    soup = BeautifulSoup(html, "html.parser")
                                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                    dl = 'https://www.youtube.com' + results['href']
                                    start = timeit.timeit()
                                    vid = pafy.new(dl)
                                    stream = vid.streams
                                    for s in stream:
                                        vin = s.url
                                        hasil = vid.title
                                        hasil += '\n\nâââ[ Authorized : ' +str(vid.author)
                                        hasil += '\nâ  Duration   : ' +str(vid.duration)+ ' (' +s.quality+ ') '
                                        hasil += '\nâ  Rating   : ' +str(vid.rating)
                                        hasil += '\nâ  Watched    : ' +str(vid.viewcount)+ 'x '
                                        hasil += '\nâ  Published : ' +vid.published
                                        hasil += '\n\nâ Time taken : %s' % (start)
                                        hasil += '\n\n âââWait for encoding...'
                                    client.sendVideoWithURL(msg.to,vin)
                                    client.sendText(msg.to,hasil)
                                except:
                                    client.sendText(msg.to,"Informasi video gagal di cari")
                            elif cmd.startswith("cuaca "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    if "result" not in data:
                                        ret_ = "âââ[ CUACA ]âââ\n\n"
                                        ret_ += "\nâ  Location : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\nâ  Suhu : " + data[1].replace("Suhu : ","") + "Â°C"
                                        ret_ += "\nâ  Kelembaban : " + data[2].replace("Kelembaban : ","") + "%"
                                        ret_ += "\nâ  Tekanan udara : " + data[3].replace("Tekanan udara : ","") + "HPa"
                                        ret_ += "\nâ  Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + "m/s"
                                        ret_ += "\n\nâ  Time Status ]\n"
                                        ret_ += "\nâ  Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                        ret_ += "\nâââ Jam : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB"
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("lokasi "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "âââ[ LOCATION ]âââ\n"
                                        ret_ += "\nâ  Location : " + data[0]
                                        ret_ += "\nâââGoogle Maps : " + link
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instainfo "):
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://www.instagram.com/{}/?__a=1".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "âââ[Profile instagram]âââ\n"
                                        ret_ += "\nâ  Name : {}".format(str(data["graphql"]["user"]["full_name"]))
                                        ret_ += "\nâ  Username : {}".format(str(data["graphql"]["user"]["username"]))
                                        ret_ += "\nâ  Bio : {}".format(str(data["graphql"]["user"]["biography"]))
                                        ret_ += "\nâ  Followers : {}".format(str(data["graphql"]["user"]["edge_followed_by"]["count"]))
                                        ret_ += "\nâ  Following : {}".format(str(data["graphql"]["user"]["edge_follow"]["count"]))
                                        if data["graphql"]["user"]["is_verified"] == True:
                                            ret_ += "\nâ Verification : Yes"
                                        else:
                                            ret_ += "\nâ Verification : No"
                                        if data["graphql"]["user"]["is_private"] == True:
                                            ret_ += "\nâ Private Account : Yes"
                                        else:
                                            ret_ += "\nâ Private account : No"
                                        ret_ += "\nâ Total Post : {}".format(str(data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]))
                                        ret_ += "\nâââ[ https://www.instagram.com/{} ]".format(search)
                                        path = data["graphql"]["user"]["profile_pic_url_hd"]
                                        client.sendImageWithURL(to, str(path))
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instapost "):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")
                                    cond = text.split("|")
                                    username = cond[0]
                                    no = cond[1]
                                    r = requests.get("http://rahandiapi.herokuapp.com/instapost/{}/{}?key=betakey".format(str(username), str(no)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["find"] == True:
                                        if data["media"]["mediatype"] == 1:
                                            client.sendImageWithURL(msg.to, str(data["media"]["url"]))
                                        if data["media"]["mediatype"] == 2:
                                            client.sendVideoWithURL(msg.to, str(data["media"]["url"]))
                                        ret_ = "âââ[Info Post]âââ\n"
                                        ret_ += "\nâ  Jumlah Like : {}".format(str(data["media"]["like_count"]))
                                        ret_ += "\nâ  Jumlah Comment : {}".format(str(data["media"]["comment_count"]))
                                        ret_ += "\nâââ[ Caption ]\n{}".format(str(data["media"]["caption"]))
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instastory "):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")
                                    cond = text.split("|")
                                    search = str(cond[0])
                                    if len(cond) == 2:
                                        r = requests.get("http://rahandiapi.herokuapp.com/instastory/{}?key=betakey".format(search))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["url"] != []:
                                            num = int(cond[1])
                                            if num <= len(data["url"]):
                                                search = data["url"][num - 1]
                                                if search["tipe"] == 1:
                                                    client.sendImageWithURL(to, str(search["link"]))
                                                if search["tipe"] == 2:
                                                    client.sendVideoWithURL(to, str(search["link"]))
                                except Exception as error:
                                    logError(error)

                            elif cmd.startswith("voice-"):
                                sep = text.split("-")
                                sepp = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("voice-" + lang + " ","")
                                if lang not in list_language["list_textToSpeech"]:
                                    return client.sendMessage(to, "Language not found")
                                tts = gTTS(text=sepp, lang=lang)
                                tts.save("hasil.mp3")
                                client.sendAudio(to,"hasil.mp3")
                            elif cmd.startswith("calculator"):
                                     sep = text.split(" ")
                                     txt = text.replace(sep[0] + " ","")
                                     hitung = eval(txt)
                                     client.sendMessage(msg.to,str(hitung))
                            elif cmd.startswith("meme01"):

                                    pisah = msg.text.split(" ")
                                    banana = "buzz"
                                    bahann = ("https://memegen.link/" + banana + "/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg")
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme02"):

                                    pisah = msg.text.split(" ")
                                    banana = "patrick"
                                    bahann = ("https://memegen.link/" + banana + "/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg")
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme03"):

                                    pisah = msg.text.split(" ")
                                    banana = "wonka"
                                    bahann = ("https://memegen.link/" + banana + "/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg")
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme04"):

                                    pisah = msg.text.split(" ")
                                    banana = "sparta"
                                    bahann = ("https://memegen.link/" + banana + "/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg")
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme05"):

                                    pisah = msg.text.split(" ")
                                    banana = "older"
                                    bahann = ("https://memegen.link/" + banana + "/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg")
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme06"):

                                    pisah = msg.text.split(" ")
                                    banana = "noidea"
                                    bahann = ("https://memegen.link/" + banana + "/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg")
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme07"):

                                    pisah = msg.text.split(" ")
                                    banana = "aag"
                                    bahann = ("https://memegen.link/" + banana + "/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg")
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme08"):

                                    pisah = msg.text.split(" ")
                                    banana = "fetch"
                                    bahann = ("https://memegen.link/" + banana + "/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg")
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme09"):

                                    pisah = msg.text.split(" ")
                                    banana = "dodgson"
                                    bahann = ("https://memegen.link/" + banana + "/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg")
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme10"):

                                    pisah = msg.text.split(" ")
                                    banana = "rollsafe"
                                    bahann = ("https://memegen.link/" + banana + "/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg")
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme11"):

                                    pisah = msg.text.split(" ")
                                    banana = "http://1.bp.blogspot.com/-os0EtUWXThk/UkbAGEpE-uI/AAAAAAAAALk/nU0aLT1xMmU/s1600/430705_203697073088868_554934338_n.jpg"
                                    bahann = ("https://memegen.link/custom/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg?alt=" + banana)
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme12"):

                                    pisah = msg.text.split(" ")
                                    banana = "https://1.bp.blogspot.com/-naOO3g229Xk/VzX0k4x_WBI/AAAAAAAAAfY/jcswQvcP4ec7MXMHlwVb7t5N_4JxvONVQCLcB/s1600/meme_spongebob_polosan.jpg"
                                    bahann = ("https://memegen.link/custom/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg?alt=" + banana)
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme13"):

                                    pisah = msg.text.split(" ")
                                    banana = "https://1.bp.blogspot.com/-3yydvjKnlF4/VzX0l_HpoUI/AAAAAAAAAfk/zB3qYElR6Vg-h-Rg9pYh7wKsSq7CaM0-gCLcB/s1600/meme_spongebob_polosan_4.jpg"
                                    bahann = ("https://memegen.link/custom/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg?alt=" + banana)
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme14"):

                                    pisah = msg.text.split(" ")
                                    banana = "http://www.sisidunia.com/wp-content/uploads/2014/09/spongebob-1.jpg"
                                    bahann = ("https://memegen.link/custom/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg?alt=" + banana)
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme15"):

                                    pisah = msg.text.split(" ")
                                    banana = "https://img.duniaku.net/2017/09/Aliga2.jpg"
                                    bahann = ("https://memegen.link/custom/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg?alt=" + banana)
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme16"):

                                    pisah = msg.text.split(" ")
                                    banana = "https://rescuethepresent.net/oc/files/2017/05/saitama2.jpg"
                                    bahann = ("https://memegen.link/custom/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg?alt=" + banana)
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme17"):

                                    pisah = msg.text.split(" ")
                                    banana = "https://sociorocketnewsen.files.wordpress.com/2013/11/31bf4bb8.jpg"
                                    bahann = ("https://memegen.link/custom/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg?alt=" + banana)
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme18"):

                                    pisah = msg.text.split(" ")
                                    banana = "https://3.bp.blogspot.com/-M-kY6zPzWCk/V_1P0k302LI/AAAAAAAAAbQ/XhY6maryQMI-TYkTOFGwRXt7bWj8HkTQQCLcB/s1600/meme%2Bpatrick%2Binstrument%2Bpolosan.jpg"
                                    bahann = ("https://memegen.link/custom/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg?alt=" + banana)
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme19"):

                                    pisah = msg.text.split(" ")
                                    banana = "https://4.bp.blogspot.com/-LDPCIOGdm8k/VashH4aF18I/AAAAAAAAAXc/HxGHQvj5QHs/s320/patrick%2Bhai%2Bsayang.png"
                                    bahann = ("https://memegen.link/custom/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg?alt=" + banana)
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme20"):

                                    pisah = msg.text.split(" ")
                                    banana = "http://themightychallenge.com/wp-content/uploads/2018/01/best-lebron-crying-meme-patrick-bateman-with-an-axe-know-your-meme-lebron-crying-meme.jpg"
                                    bahann = ("https://memegen.link/custom/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg?alt=" + banana)
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme21"):

                                    pisah = msg.text.split(" ")
                                    banana = "https://vignette.wikia.nocookie.net/glee/images/1/1c/Boo_spongebob.jpg"
                                    bahann = ("https://memegen.link/custom/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg?alt=" + banana)
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme22"):

                                    pisah = msg.text.split(" ")
                                    banana = "https://img.memecdn.com/my-revenge-will-be-terrible_fb_887969.jpg"
                                    bahann = ("https://memegen.link/custom/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg?alt=" + banana)
                                    client.sendImageWithURL(msg.to,bahann)

                            elif cmd.startswith("meme23"):

                                    pisah = msg.text.split(" ")
                                    banana = "https://www.memecomic.id/data/articleimage/9eebf2cb76af45a3b74539a299098faa.jpg"
                                    bahann = ("https://memegen.link/custom/" + str(pisah[1]) + "/" + str(pisah[2]) + ".jpg?alt=" + banana)
                                    client.sendImageWithURL(msg.to,bahann)
                            elif cmd.startswith("acaratv"):

                                     sep = msg.text.split(" ")
                                     search = msg.text.replace(sep[0] + " ","")
                                     apiKey = "ag73837ung43838383jdhdhd"
                                     api = requests.get("https://farzain.xyz/api/premium/acaratv.php?apikey={}&id={}".format(str(apiKey), str(search)))
                                     data = api.text
                                     data = json.loads(data)
                                     if data["status"] == "success":
                                        cerry = "âââ[ACARA TV]]<==="
                                        cerry += "\n\nâââ{}".format(str(data["url"]))
                                        client.sendMessage(msg.to, str(cerry))
                                     else:
                                         client.sendMessage(msg.to, "Data not found")

                            elif cmd.startswith("ytmp33"):
                                try:
                                    textToSearch = msg.text.replace(sep[0] + " ","")
                                    query = urllib.parse.quote(textToSearch)
                                    url = "https://www.youtube.com/results?search_query=" + query
                                    response = urllib.request.urlopen(url)
                                    html = response.read()
                                    soup = BeautifulSoup(html, "html.parser")
                                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                    dl = 'https://www.youtube.com' + results['href']
                                    start = timeit.timeit()
                                    vid = pafy.new(dl)
                                    stream = vid.audiostreams
                                    for s in stream:
                                        vin = s.url
                                        path = vid.bigthumbhd
                                        hasil = vid.title
                                        hasil += '\n\nâââPenulis : ' +str(vid.author)
                                        hasil += '\nâ Durasi   : ' +str(vid.duration)+ ' (' +s.quality+ ') '
                                        hasil += '\nâ Rating   : ' +str(vid.rating)
                                        hasil += '\nâ Ditonton    : ' +str(vid.viewcount)+ 'x '
                                        hasil += '\nâ Diterbitkan : ' +vid.published
                                        hasil += '\n\nâ Time taken : %s' % (start)
                                        hasil += '\n\nâââTunggu encoding selesai...'
                                        client.sendImageWithURL(msg.to, str(path))    
                                        client.sendAudioWithURL(msg.to,vin)
                                        client.sendText(msg.to,hasil)
                                except:
                                    client.sendText(msg.to,"Informasi Audio gagal di cari")
                                    
                            elif cmd.startswith("ytmp3 "):
                                try:
                                    sep = msg.text.split(" ")
                                    textToSearch = msg.text.replace(sep[0] + " ","")
                                    query = urllib.parse.quote(textToSearch)
                                    search_url="https://www.youtube.com/results?search_query="
                                    mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                    sb_url = search_url + query
                                    sb_get = requests.get(sb_url, headers = mozhdr)
                                    soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                    yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                    x = (yt_links[1])
                                    yt_href =  x.get("href")
                                    yt_href = yt_href.replace("watch?v=", "")
                                    qx = "https://youtu.be" + str(yt_href)
                                    vid = pafy.new(qx)
                                    stream = vid.streams
                                    bestaudio = vid.getbestaudio()
                                    bestaudio.bitrate
                                    best = vid.getbest()
                                    best.resolution, best.extension
                                    for s in stream:
                                        shi = bestaudio.url
                                        me = best.url
                                        vin = s.url
                                        hasil = ""
                                        title = "Judul [ " + vid.title + " ]"
                                        author = '\n\nâ§Author : ' + str(vid.author)
                                        durasi = '\nâ§Duration : ' + str(vid.duration)
                                        suka = '\nâ§Likes : ' + str(vid.likes)
                                        rating = '\nâ§Rating : ' + str(vid.rating)
                                        deskripsi = '\nâ§Deskripsi : ' + str(vid.description)
                                    client.sendImageWithURL(msg.to, me)
                                    client.sendAudioWithURL(msg.to, shi)
                                    client.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                                except Exception as e:
                                    client.sendText(msg.to,str(e))

                            elif cmd.startswith("ytmp4 "):
                                try:
                                    sep = msg.text.split(" ")
                                    textToSearch = msg.text.replace(sep[0] + " ","")
                                    query = urllib.parse.quote(textToSearch)
                                    search_url="https://www.youtube.com/results?search_query="
                                    mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                    sb_url = search_url + query
                                    sb_get = requests.get(sb_url, headers = mozhdr)
                                    soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                    yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                    x = (yt_links[1])
                                    yt_href =  x.get("href")
                                    yt_href = yt_href.replace("watch?v=", "")
                                    qx = "https://youtu.be" + str(yt_href)
                                    vid = pafy.new(qx)
                                    stream = vid.streams
                                    best = vid.getbest()
                                    best.resolution, best.extension
                                    for s in stream:
                                        me = best.url
                                        hasil = ""
                                        title = "Judul [ " + vid.title + " ]"
                                        author = '\n\nâ§Author : ' + str(vid.author)
                                        durasi = '\nâ§Duration : ' + str(vid.duration)
                                        suka = '\nâ§Likes : ' + str(vid.likes)
                                        rating = '\nâ§Rating : ' + str(vid.rating)
                                        deskripsi = '\nâ§Deskripsi : ' + str(vid.description)
                                    client.sendVideoWithURL(msg.to, me)
                                    client.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                                except Exception as e:
                                    client.sendText(msg.to,str(e))
                            elif cmd.startswith("google search"):
                                 try:
                                     pisah = msg.text.split(" ")
                                     isi = msg.text.replace(pisah[0]+" ","")
                                     bahan = ("http://lmgtfy.com/?q=" + isi)
                                     r = requests.get("http://tiny-url.info/api/v1/create?apikey=A942F93B8B88C698786A&provider=bit_ly&format=json&url={}".format(str(bahan)))
                                     data = r.text
                                     data = json.loads(data)
                                     anu = data["shorturl"]
                                     ret_ = "âââ[GOOGLE SEARCH]âââ"
                                     ret_ += "\n\nâââ Result: {}".format(str(anu))
                                     client.sendMessage(msg.to, str(ret_))
                                 except Exception as error:
                                     client.sendMessage(msg.to,str(error))
                            elif cmd.startswith("image "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(txt))
                                data = url.json()
                                client.sendImageWithURL(to, random.choice(data["result"]))
                            elif cmd.startswith("gambar "):
                                try:
                                    separate = msg.text.split(" ")
                                    keyword = msg.text.replace(separate[0] + " ","")  
                                    r = requests.get("http://api.farzain.com/gambarg.php?apikey=11zGcpoEsTJiyijxAqKdBFyA3&id="+keyword)
                                    data = r.text
                                    data = json.loads(data)
                                    client.sendImageWithURL(msg.to, str(data["url"]))
                                except Exception as error:
                            	    pass 
                                                    
                            elif cmd.startswith("music "):
                                    search = text.lower().replace("music ","")
                                    params = {'songname': songname}
                                    r = requests.get('http://api.farzain.com/tiktok.php?country=id&apikey=cdajhjaS55d7gefeaO6qnEcb0&type&id=' + urllib.urlencode(params))
                                    data = r.text
                                    data = json.loads(data)
                                    for song in data:
                                        hasil = 'This is Your Music\n'
                                        hasil += 'Judul : ' + song[0]
                                        hasil += '\nDurasi : ' + song[1]
                                        hasil += '\nLink Download : ' + song[4]
                                        client.sendMessage(msg.to, hasil)
                                        client.sendMessage(msg.to, "Please Wait for audio...")
                                        client.sendAudioWithURL(msg.to, song[3])
                                            
                            elif cmd.startswith("tiktok "):
                                  r = requests.get("http://api.farzain.com/tiktok.php?country=id&apikey=cdajhjaS55d7gefeaO6qnEcb0&type=json")
                                  data = r.text
                                  data = json.loads(data)
                                  if data["status"] == 200:                                     
                                     client.sendVideoWithURL(msg.to, str(data["first_video"]))
                                     
                            elif cmd.startswith("cooltext "):
                                    sep = text.split(" ")
                                    txt = text.replace(sep[0] + " ","")
                                    no = ["1","2","3","4","5","6","7"]
                                    plih = random.choice(nmor)
                                    r = requests.get("http://api.farzain.com/cooltext.php?text=id&apikey=cdajhjaS55d7gefeaO6qnEcb0="+keyword)
                                    client.sendImageWithURL(msg.to,gambar["url"])
                                    
                            elif cmd.startswith("smulevi "):
                                    separate = text.split(" ")
                                    channel = text.replace(separate[0] + " ","")
                                    with requests.session() as web:
                                        web.headers["user-agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0"
                                        r = web.get("https://citldesign.herokuapp.com/downloadsmule={}".format(urllib.parse.quote(channel)))
                                        data = r.text
                                        data = json.loads(data)
                                        for design in data["result"]:
                                            image = design["image"]
                                            url = design["url"]
                                        client.sendImageWithURL(msg.to, image)
                                        client.sendAudioWithURL(msg.to, url)
                                        client.sendVideoWithURL(msg.to, url)

                               
                            elif cmd.startswith("lyric "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                cond = txt.split("|")
                                query = cond[0]
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0"
                                    url = web.get("https://www.musixmatch.com/search/{}".format(urllib.parse.quote(query)))
                                    data = BeautifulSoup(url.content, "html.parser")
                                    result = []
                                    for trackList in data.findAll("ul", {"class":"tracks list"}):
                                        for urlList in trackList.findAll("a"):
                                            title = urlList.text
                                            url = urlList["href"]
                                            result.append({"title": title, "url": url})
                                    if len(cond) == 1:
                                        ret_ = "âââ[ Musixmatch Result ]âââ"
                                        num = 0
                                        for title in result:
                                            num += 1
                                            ret_ += "\nâ  {}. {}".format(str(num), str(title["title"]))
                                        ret_ += "\nâ [ Total {} Lyric ]".format(str(len(result)))
                                        ret_ += "\n\nâââUntuk melihat lyric, silahkan gunakan command {}Lyric {}|?number?".format(str(setKey), str(query))
                                        client.sendMessage(to, ret_)
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(result):
                                            data = result[num - 1]
                                            with requests.session() as web:
                                                web.headers["user-agent"] = "Mozilla/5.0"
                                                url = web.get("https://www.musixmatch.com{}".format(urllib.parse.quote(data["url"])))
                                                data = BeautifulSoup(url.content, "html5lib")
                                                for lyricContent in data.findAll("p", {"class":"mxm-lyrics__content "}):
                                                    lyric = lyricContent.text
                                                    client.sendMessage(to, lyric)
                            elif cmd.startswith("yt "):
                                sep = text.split(" ")
                                txt = msg.text.replace(sep[0] + " ","")
                                cond = txt.split("|")
                                search = cond[0]
                                url = requests.get("http://api.w3hills.com/youtube/search?keyword={}&api_key=86A7FCF3-6CAF-DEB9-E214-B74BDB835B5B".format(search))
                                data = url.json()
                                if len(cond) == 1:
                                    no = 0
                                    result = "âââ[Youtube Search]âââ"
                                    for anu in data["videos"]:
                                        no += 1
                                        result += "\nâ  {}. {}".format(str(no),str(anu["title"]))
                                    result += "\nâââ[ Total {} Result ]".format(str(len(data["videos"])))
                                    client.sendMessage(to, result)
                                elif len(cond) == 2:
                                    num = int(str(cond[1]))
                                    if num <= len(data):
                                        search = data["videos"][num - 1]
                                        ret_ = "âââ[Youtube Info]âââ"
                                        ret_ += "\nâ  Channel : {}".format(str(search["publish"]["owner"]))
                                        ret_ += "\nâ  Title : {}".format(str(search["title"]))
                                        ret_ += "\nâ  Release : {}".format(str(search["publish"]["date"]))
                                        ret_ += "\nâ  Viewers : {}".format(str(search["stats"]["views"]))
                                        ret_ += "\nâ  Likes : {}".format(str(search["stats"]["likes"]))
                                        ret_ += "\nâ  Dislikes : {}".format(str(search["stats"]["dislikes"]))
                                        ret_ += "\nâ  Rating : {}".format(str(search["stats"]["rating"]))
                                        ret_ += "\nâ  Description : {}".format(str(search["description"]))
                                        ret_ += "\nâââ[ {} ]".format(str(search["webpage"]))
                                        client.sendImageWithURL(to, str(search["thumbnail"]))
                                        client.sendMessage(to, str(ret_))
                            elif cmd.startswith("youtube"):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "âââ[YOU TUBE]âââ\n\n"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n\nâ  {}".format(str(data["title"]))
                                    ret_ += "\nâ  https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\nâââ[ Total {} ]".format(len(datas))
                                client.sendMessage(to, str(ret_))
                            elif cmd.startswith("tr-"):
                                sep = text.split("-")
                                sepp = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("tr-" + lang + " ","")
                                if lang not in list_language["list_translate"]:
                                    return client.sendMessage(to, "Language not found")
                                translator = Translator()
                                hasil = translator.translate(sepp, dest=lang)
                                A = hasil.text
                                client.sendMessage(to, str(A))

#==============================================================================#
                            elif cmd.startswith("add image "):
                                #load()
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["addImage"]["status"] = True
                                    settings["addImage"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open('image.json','w','utf-8')
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(to, "Send image to added")
                                else:
                                    client.sendMessage(to, "Gambar sudah di imagelist")
                            elif cmd.startswith("del image "):
                                #load()
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in images:
                                    client.deleteFile(images[str(name.lower())])
                                    del images[str(name.lower())]
                                    f = codecs.open('image.json','w','utf-8')
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(to, "Success delated image {}".format(str(name.lower())))
                                else:
                                    client.sendMessage(to, "Image not list")
                            elif cmd.startswith("change image "):
                                #load()
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in images:
                                    settings["addImage"]["status"] = True
                                    settings["addImage"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open('image.json','w','utf-8')
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(to, "Send image ")
                                else:
                                    client.sendMessage(to, "Image not list")
                            elif cmd == "image list":
                                #load()
                                ret_ = "âââ[ List Images ]"
                                for image in images:
                                    ret_ += "\nâ  " + image.title()
                                ret_ += "\nâââ[ Total {} Images ]".format(str(len(images)))
                                client.sendMessage(to, ret_)
                            elif cmd.startswith("spamimage "):
                                #load()
                                sep = text.split(" ")
                                text = text.replace(sep[0] + " ","")
                                cond = text.split(" ")
                                jml = int(cond[0])
                                imagename = text.replace(cond[0] + " ","").lower()
                                if imagename in images:
                                    imgURL = images[imagename]
                                else:
                                    client.sendMessage(to, "Gambar tidak ditemukan")
                                    return
                                for x in range(jml):
                                    client.sendImage(to, imgURL)
                            elif cmd.startswith("add sticker "):
                                #load()
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["addSticker"]["status"] = True
                                    settings["addSticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = {}
                                    f = codecs.open('sticker.json','w','utf-8')
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(to, "Send stiker to added")
                                else:
                                    client.sendMessage(to, "Name sticker in list")
                            elif cmd.startswith("del sticker "):
                                #load()
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open('sticker.json','w','utf-8')
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(to, "Success delated sticker {}".format(str(name.lower())))
                                else:
                                    client.sendMessage(to, "Sticker not in list")
                            elif cmd.startswith("change sticker "):
                                #load()
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    settings["addSticker"]["status"] = True
                                    settings["addSticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = ""
                                    f = codecs.open('sticker.json','w','utf-8')
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(to, "Send sticker")
                                else:
                                    client.sendMessage(to, "Sticker not in list")
                            elif cmd == "sticker list":
                                #load()
                                ret_ = "âââ[ List Sticker ]"
                                for sticker in stickers:
                                    ret_ += "\nâ  " + sticker.title()
                                ret_ += "\nâââ[ Total {} Stickers ]".format(str(len(stickers)))
                                client.sendMessage(to, ret_)
                            elif cmd.startswith("spam stikel "):
                                #load()
                                sep = text.split(" ")
                                text = text.replace(sep[0] + " ","")
                                cond = text.split(" ")
                                jml = int(cond[0])
                                stickername = text.replace(cond[0] + " ","").lower()
                                if stickername in stickers:
                                    sid = stickers[stickername]["STKID"]
                                    spkg = stickers[stickername]["STKPKGID"]
                                    sver = stickers[stickername]["STKVER"]
                                else:
                                    return
                                for x in range(jml):
                                    sendSticker(to, sver, spkg, sid)
#==============================================================================#
                            elif cmd.startswith("add audio "):
                                #load()
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in audios:
                                    settings["addAudio"]["status"] = True
                                    settings["addAudio"]["name"] = str(name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open('audio.json','w','utf-8')
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(to, "Send audio to added")
                                else:
                                    client.sendMessage(to, "Audio in list")
                            elif cmd.startswith("del audio "):
                                #load()
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in audios:
                                    client.deleteFile(audios[str(name.lower())])
                                    del audios[str(name.lower())]
                                    f = codecs.open('audio.json','w','utf-8')
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(to, "Success delated audio {}".format(str(name.lower())))
                                else:
                                    client.sendMessage(to, "Audio not in list")
                            elif cmd.startswith("change audio "):
                                #load()
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in audios:
                                    settings["addAudio"]["status"] = True
                                    settings["addAudio"]["name"] = str(name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open('audio.json','w','utf-8')
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(to, "Send audio")
                                else:
                                    client.sendMessage(to, "Audio not in list")
                            elif cmd == "audio list":
                                #load()
                                ret_ = "âââ[ List audios ]"
                                for audio in audios:
                                    ret_ += "\nâ  " + audio.title()
                                ret_ += "\nâââ[ Total {} audios ]".format(str(len(audios)))
                                client.sendMessage(to, ret_)
                            elif cmd.startswith("spam audio "):
                                #load()
                                sep = text.split(" ")
                                text = text.replace(sep[0] + " ","")
                                cond = text.split(" ")
                                jml = int(cond[0])
                                audioname = text.replace(cond[0] + " ","").lower()
                                if audioname in audios:
                                    audURL = audios[audioname]
                                else:
                                    client.sendMessage(to, "Audio tidak ditemukan")
                                    return
                                for x in range(jml):
                                    client.sendAudio(to, audURL)
                            elif cmd.startswith("add video "):
                                #load()
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in videos:
                                    settings["addVideo"]["status"] = True
                                    settings["addVideo"]["name"] = str(name.lower())
                                    videos[str(name.lower())] = ""
                                    f = codecs.open('video.json','w','utf-8')
                                    json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(to, "Send video to added")
                                else:
                                    client.sendMessage(to, "Video in list")
                            elif cmd.startswith("del video "):
                                #load()
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in videos:
                                    client.deleteFile(videos[str(name.lower())])
                                    del videos[str(name.lower())]
                                    f = codecs.open('video.json','w','utf-8')
                                    json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(to, "Succes delated video{}".format(str(name.lower())))
                                else:
                                    client.sendMessage(to, "Video not in list")
                            elif cmd.startswith("change video "):
                                #load()
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in videos:
                                    settings["addVideo"]["status"] = True
                                    settings["addVideo"]["name"] = str(name.lower())
                                    videos[str(name.lower())] = ""
                                    f = codecs.open('video.json','w','utf-8')
                                    json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(to, "Send videi")
                                else:
                                    client.sendMessage(to, "Video not in list")
                            elif cmd == "video list":
                                #load()
                                ret_ = "âââ[ List videos ]"
                                for video in videos:
                                    ret_ += "\nâ  " + video.title()
                                ret_ += "\nâââ[ Total {} videos ]".format(str(len(videos)))
                                client.sendMessage(to, ret_)
                            elif cmd.startswith("spam video "):
                                #load()
                                sep = text.split(" ")
                                text = text.replace(sep[0] + " ","")
                                cond = text.split(" ")
                                jml = int(cond[0])
                                videoname = text.replace(cond[0] + " ","").lower()
                                if videoname in videos:
                                    vidURL = videos[videoname]
                                else:
                                    client.sendMessage(to, "Video tidak ditemukan")
                                    return
                                for x in range(jml):
                                    client.sendVideo(to, vidURL)
                            elif cmd.startswith("getmeme"):
                                proses = text.split(" ")
                                keyword = text.replace(proses[0] + " ","")
                                count = keyword.split("|")
                                search = str(count[0])
                                r = requests.get("http://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                if len(count) == 1:
                                    no = 0
                                    hasil = "Meme image list\n"
                                    for aa in data["data"]["memes"]:
                                        no += 1
                                        hasil += "\n" + str(no) + ". "+ str(aa["name"])
                                    hasil += " "
                                    client.sendMessage(msg.to,hasil)
                                    sendMention(msg.to,"@!\nSilahkan pilih keinginan:\n\n[Cek meme]\ngetmeme | urutan\n\n[Create meme]\nmeme teks1|teks2|urutan",[sender])
                                if len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        gambar = data["data"]["memes"][num - 1]
                                        hasil = "{}".format(str(gambar["name"]))
                                        sendMention(msg.to, sender,"","\nfoto sedang diproses...")
                                        client.sendMessage(msg.to,hasil)
                                        client.sendImageWithURL(msg.to,gambar["url"])
                                    except Exception as e:
                                        client.sendMessage(msg.to," "+str(e))
                            elif cmd.startswith("meme"):
                                proses = text.split(" ")
                                keyword = text.replace(proses[0]+" ","")
                                query = keyword.split("|")
                                atas = query[0]
                                bawah = query[1]
                                r = requests.get("https://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                try:
                                    num = int(query[2])
                                    namamem = data["data"]["memes"][num - 1]
                                    meme = int(namamem["id"])
                                    api = pyimgflip.Imgflip(username='andyihsan', password='ihsan848')
                                    result = api.caption_image(meme, atas,bawah)
                                    sendMention(msg.to,"@!\nfoto sedang diproses...",[sender])
                                    client.sendImageWithURL(msg.to,result["url"])
                                except Exception as e:
                                    client.sendMessage(msg.to," "+str(e))
                            elif cmd.startswith("alquran "):
                                data = msg.text.lower().replace("alquran ","")                                
                                no = data.split('|')
                                no = no[1].replace(' ','+')
                                no1 = data.split('|')
                                no1 = no1[2].replace(' ','+')
                                with requests.session() as web:
                                        web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = web.get("https://api.fathimah.xyz/quran/format/json/surat/{}/ayat/{}".format(urllib.parse.quote(no), no1))
                                data=r.text
                                data=json.loads(data)
                                ret_ = "===>[[ ALQURAN ]]<==="
                                ret_ += "=> Nama surah: " +data["surat"]["nama"]
                                ret_ += "\n=> Asma: " +data["surat"]["asma"]
                                ret_ += "\n=> Surat: " +str(data["query"]["surat"])
                                ret_ += "\n=> Ayat: " +str(data["query"]["ayat"])
                                ret_ += "\n=> Total: " +str(data["surat"]["ayat"])+" ayat"
                                ret_ += "\n=> Type: " +str(data["surat"]["type"])
                                ret_ += "\n=> Arti: " +str(data["surat"]["arti"])
                                ret_ += "\n=> Data result: \n" +str(data["ayat"]["data"]["ar"][0]["teks"])
                                ret_ += "\n=>" +data["ayat"]["data"]["id"][0]["teks"]
                                ret_ += "\n=> Keterangan:\n" +data["surat"]["keterangan"]
                                client.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("search alquran "):
                                sep = msg.text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                r = requests.get("http://ariapi.herokuapp.com/api/quran/search?q={}".format(urllib.parse.quote(query)) + "&key=beta")
                                data=r.text
                                data=json.loads(data)                                                                                                                                                        
                                if data["result"]["matches"] != []:
                                     no = 0
                                     hasil = "Result data Al-Quran\n"
                                     for anu in data["result"]["matches"]:
                                            no += 1
                                            hasil += "\nResult ke " + str(no) + "\n" + str(anu["text"])
                                client.sendMessage(msg.to, str(hasil))
                            elif cmd.startswith("horoscop "):
                                sep = msg.text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                r = requests.get("http://horoscope-api.herokuapp.com/horoscope/today/"+query)
                                data = r.text
                                data = json.loads(data)
                                data1 = data["horoscope"]
                                translator = Translator()
                                hasil = translator.translate(data1, dest='id')
                                A = hasil.text
                                ret_ = "âââ[ ZODIAK ]âââ"
                                ret_ += "\nâ  Tanggal : " +str(data["date"])
                                ret_ += "\nâ  Rasi bintang : " +str(data["sunsign"])
                                ret_ += "\nâââ Ramalan : " +str(A)
                                client.sendMessage(msg.to, str(ret_)) 
                            elif cmd.startswith("zodiak "):
                                sep = msg.text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                r = requests.post("https://aztro.herokuapp.com/?sign={}&day=today".format(urllib.parse.quote(query)))
                                data = r.text
                                data = json.loads(data)
                                data1 = data["description"]
                                data2 = data["color"]
                                translator = Translator()
                                hasil = translator.translate(data1, dest='id')
                                hasil1 = translator.translate(data2, dest='id')
                                A = hasil.text
                                B = hasil1.text
                                ret_ = "âââ[ ZODIAK ]âââ"
                                ret_ += "\nâ  Tanggal : " +str(data["current_date"])
                                ret_ += "\nâ  Rasi bintang : "+query
                                ret_ += " ("+str(data["date_range"]+")")
                                ret_ += "\nâ  Zodiak pasangan : " +str(data["compatibility"])
                                ret_ += "\nâ  Angka keberuntungan : " +str(data["lucky_number"])
                                ret_ += "\nâ  Waktu keberuntungan : " +str(data["lucky_time"])
                                ret_ += "\nâ  Warna kesukaan : " +str(B)
                                ret_ += "\nââââââââââââââââ\n" +str(A)
                                client.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("anime "):
                                sep = msg.text.split(" ")
                                anime = msg.text.replace(sep[0] + " ","%20")                
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = web.get("https://kitsu.io/api/edge/anime?filter[text]={}".format(urllib.parse.quote(anime)))
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    for a in data["data"]:
                                        if a["attributes"]["subtype"] == "TV":
                                            sin = a["attributes"]["synopsis"]
                                            translator = Translator()
                                            hasil = translator.translate(sin, dest='id')
                                            sinop = hasil.text
                                            ret_ = ''
                                            ret_ += '\n\nAnime result'
                                            ret_ += '\nTitle : '+str(a["attributes"]["canonicalTitle"])
                                            ret_ += '\nRilis : '+str(a["attributes"]["startDate"])
                                            ret_ += '\nRating : '+str(a["attributes"]["ratingRank"])
                                            ret_ += '\nType : '+str(a["attributes"]["subtype"])
                                            ret_ += '\nSinopsis :\n'+str(sinop)
                                            client.sendImageWithURL(msg.to, str(a["attributes"]["posterImage"]["small"]))
                                            client.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("bintang "):
                                sep = msg.text.split(" ")
                                url = msg.text.replace(sep[0] + " ","")    
                                with requests.session() as s:
                                    s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    r = s.get("https://www.vemale.com/zodiak/{}".format(urllib.parse.quote(url)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    ret_ = ""
                                    for a in soup.select('div.vml-zodiak-detail'):
                                        ret_ += a.h1.string
                                        ret_ += "\n"+ a.h4.string
                                        ret_ += " ("+ a.span.string +")"
                                    for b in soup.select('div.col-center'):
                                        ret_ += "\nTanggal : "+ b.string
                                    for d in soup.select('div.number-zodiak'):
                                        ret_ += "\nAngka keberuntunga : "+ d.string
                                    for c in soup.select('div.paragraph-left'):
                                        ta = c.text
                                        tab = ta.replace("   ", "")
                                        tabs = tab.replace(".", ".\n")
                                        ret_ += "\n"+ tabs
                                        #print (ret_)
                                    client.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("mimpi "):
                                sep = msg.text.split(" ")
                                mimpi = msg.text.replace(sep[0] + " ","")  
                                with requests.session() as s:
                                    s.headers['user-agent'] = 'Mozilla/5.0'
                                    r = s.get("http://primbon.com/tafsir_mimpi.php?mimpi={}&submit=+Submit+".format(urllib.parse.quote(mimpi)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    for anu in soup.find_all('i'):
                                        ret_ = anu.get_text()
                                        client.sendMessage(msg.to,ret_)
                            elif cmd.startswith("smulevid "):
                                sep = msg.text.split(" ")
                                smule = msg.text.replace(sep[0] + " ","")
                                with requests.session() as s:
                                    s.headers['user-agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0'
                                    r = s.get("https://www.smuledownloader.download/{}".format(urllib.parse.quote(smule)))
                                    data = BeautifulSoup(r.content, 'html5lib')
                                    try:
                                        for title in data.findAll('div', attrs={'class':'container ptb'}):
                                            ret_ = title.find('h1').text
                                            for video in data.findAll('p', attrs={'class':'lead'}):
                                                kays = video.find('a')['href']
                                                kayss = kays.replace("https://adf.ly/7737506/","")
                                                ret = kayss
                                            client.sendMessage(to, ret_)
                                            client.sendVideoWithURL(msg.to,ret)
                                    except:
                                        client.sendMessage(to, "Failid mengambil data..")
                            elif cmd.startswith("smule "):
                                if '/' in text:
                                    sep = text.split("/")
                                    x = len(sep)
                                    smule = sep[x - 1]
                                else:
                                    smule == text.split(" ")[1]               
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("http://www.singsmule.net//p/{}.html".format(str(smule)))
                                    data = BeautifulSoup(r.content, 'html5lib')
                                    note = data.findAll('div', attrs={'class':'col-md-4'})[3].text
                                    x = data.title.string
                                    title = x.replace('| SingSmule.Net','')
                                    tumb = data.select("img.img-thumbnail")[0]
                                    pict = tumb['src']
                                    if 'Not Available' in note:
                                        aud = data.select('a[href*=https://y-ash.smule.com/]')[0]
                                        m4a = aud['href']
                                        client.sendMessage(msg.to,"Title :\n"+title)
                                        client.sendImageWithURL(msg.to, pict)
                                        client.sendMessage(msg.to,"Type : Audio\nWait for media uploading..!")
                                        client.sendAudioWithURL(msg.to, m4a)
                                    else:
                                        vid = data.select('a[href*=https://y-ash.smule.com/]')[1]
                                        mp4 = vid['href']
                                        client.sendMessage(msg.to,"Title :\n"+title)
                                        client.sendImageWithURL(msg.to, pict)
                                        client.sendMessage(msg.to,"Type : Video\nWait for media uploading..!")
                                        client.sendVideoWithURL(msg.to, mp4)
                            elif cmd.startswith("waifu "):
                                sep = msg.text.split(" ")
                                waifu = msg.text.replace(sep[0] + " ","")
                                with requests.session() as s:
                                    s.headers['user-agent'] = 'Mozilla/5.0'
                                    r = s.get("http://mywaifu.ga/{}".format(urllib.parse.quote(waifu)))
                                    data = BeautifulSoup(r.content, 'html5lib')
                                    try:
                                        for anu in data.findAll('div', attrs={'class':'item'}):
                                            ret_ = anu.find('h1').text
                                            img = anu.find('img')['src']
                                            client.sendMessage(to, ret_)
                                            client.sendImageWithURL(msg.to,img)
                                    except:
                                        client.sendMessage(to, "Nah loh..hiihhii :p")
                            elif cmd.startswith("cctv "):
                                sep = msg.text.split(" ")
                                cct = msg.text.replace(sep[0] + " ","")
                                with requests.session() as s:
                                    s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
                                    r = s.get("http://lewatmana.com/cam/{}/bundaran-hi/".format(urllib.parse.quote(cct)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    try:
                                        ret_ = "INFO CCTV\n"
                                        ret_ += soup.select("[class~=cam-viewer-title]")[0].text
                                        vid = soup.find('source')['src']
                                        ret = "Ketik cctv untuk mengtahui detail kode cctv."
                                        client.sendMessage(to, ret_)
                                        client.sendVideoWithURL(to, vid)
                                        client.sendMessage(to, ret)
                                    except:
                                        client.sendMessage(to, "Data cctv tidak ditemukan!")
                            elif cmd.startswith("cctv"):
                                ret_ = "248 = Alternatif - Cibubur\n119 = Ancol - bandara\n238 = Asia afrika - Bandung\n169 = Asia afrika - Hang lekir"
                                ret_ += "\n276 = Asia afrika - Sudirman\n295 = Bandengan - kota\n294 = Bandengan - Selatan\n255 = Boulevard Barat raya"
                                ret_ += "\n102 = Buncit raya\n272 = Bundaran - HI\n93 = Cideng barat\n289 = Cikini raya\n242 = Ciledug raya - Cipulir"
                                ret_ += "\n175 = Ciloto - Puncak\n142 = Daan mogot - Grogol\n143 = Daan mogot - Pesing\n338 = Dewi sartika - Cawang"
                                ret_ += "\n124 = DI Panjaitan - By pass\n123 = DI Panjaitan - Cawang\n13 = Dr Satrio - Casablanca\n105 = Dr Satrio - Karet"
                                ret_ += "\n245 = Dukuh atas - MRT Jakarta\n334 = Fachrudin raya\n252 = Fatmawati - Blok A\n253 = Fatmawati - Cipete raya"
                                ret_ += "\n203 = Flyover Daan mogot\n336 = Flyover Jati baru\n172 = Flyover Senen - Kramat\n77 = Gunung sahari"
                                ret_ += "\n137 = Hasyim Ashari\n273 = Jalan MH Thamrin\n327 = Jalan RS Fatmawati\n292 = Jl. Otista 3\n333 = Jl. Panjang - Kebon jeruk"
                                ret_ += "\n226 = JORR - Bintaro\n227 = JORR - Fatmawati\n173 = Kramat raya - Senen\n117 = Kyai Caringin - Cideng\n126 = Letjen Suprapto - Senen"
                                ret_ += "\n204 = Mangga besar\n319 = Margaguna raya\n326 = Margonda raya\n310 = Mas Mansyur - Karet\n309 = Mas Mansyur - Tn. Abang"
                                ret_ += "\n64 = Matraman\n140 = Matraman - Salemba\n284 = Metro Pdk. Indah\n191 = MT Haryono - Pancoran\n160 = Pancoran barat"
                                ret_ += "\n331 = Pejompongan - Slipi\n332 = Pejompongan - Sudirman\n312 = Perempatan pramuka\n171 = Permata hijau - Panjang\n99 = Petojo Harmoni"
                                ret_ += "\n223 = Pramuka - Matraman\n222 = Pramuka raya\n314 = Pramuka raya - jl. Tambak\n313 = Pramuka - Salemba raya\n130 = Puncak raya KM84"
                                ret_ += "\n318 = Radio dalam raya\n328 = RS Fatmawati - TB\n274 = Senayan city\n132 = Slipi - Palmerah\n133 = Slipi - Tomang"
                                ret_ += "\n162 = S Parman - Grogol\n324 = Sudirman - Blok M\n18 = Sudirman - Dukuh atas\n325 = Sudirman - Semanggi\n112 = Sudirman - Setiabudi"
                                ret_ += "\n246 = Sudirman - Thamrin\n320 = Sultan agung - Sudirman\n100 = Suryo pranoto\n220 = Tanjung duren\n301 = Tol kebon jeruk"
                                ret_ += "\n41 = Tomang/Simpang\n159 = Tugu Pancoran\n145 = Warung jati - Pejaten\n205 = Yos Sudarso - Cawang\n206 = Yos Sudarso - Tj. Priuk"
                                ret_ += "\n\nKetik cctv (kode wilayah)"                            
                                client.sendMessage(to, ret_)
                            elif cmd.startswith("short "):
                                sep = msg.text.split(" ")
                                short = msg.text.replace(sep[0] + " ","")                
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    r = web.get("https://api-ssl.bitly.com/v3/shorten?access_token=497e74afd44780116ed281ea35c7317285694bf1&longUrl={}".format(urllib.parse.quote(short)))
                                    data = r.text
                                    data = json.loads(data)
                                    ret_ = data["data"]["url"]
                                    client.sendMessage(msg.to, str(ret_))
                            if cmd.startswith("xxxvideo "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = 'Mozilla/5.0'
                                    r = s.get("https://www.xvideos.com/?k={}".format(str(search)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    data = soup.findAll('div', attrs={'class':'thumb'})
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = "Result xvideos"
                                        for a in data:
                                            num += 1
                                            link = "https://www.xvideos.com"+a.find('a')['href']
                                            ret_ += "\n {}. {}".format(str(num), str(link))
                                        ret_ += "\n Total {} Video".format(str(len(data)))
                                        client.sendMessage(to, str(ret_))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data):
                                            a = data[num - 1]
                                            with requests.session() as s:
                                                s.headers['user-agent'] = 'Mozilla/5.0'
                                                r = s.get("https://www.tubeoffline.com/downloadFrom.php?host=Xvideos&video=https://www.xvideos.com{}".format(str(a.find('a')['href'])))
                                                soup = BeautifulSoup(r.content, 'html5lib')
                                                pict = soup.select("img[src*=img]")[0]
                                                img = pict['src']
                                                data = soup.findAll('div', attrs={'id':'videoDownload'})
                                                print(a)
                                                for b in data:
                                                    down = b.select("a[href*=vid]")[0]
                                                    load = down['href']
                                                    with requests.session() as web:
                                                        web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                                        r = web.get("https://api-ssl.bitly.com/v3/shorten?access_token=497e74afd44780116ed281ea35c7317285694bf1&longUrl={}".format(str(load)))
                                                        data = r.text
                                                        data = json.loads(data)
                                                        ret_ = "Link Download\n"+data["data"]["url"]
                                                    client.sendImageWithURL(to, img)
                                                    client.sendMessage(to, str(ret_))
                            if cmd.startswith("apk "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://apkpure.com/id/search?q={}".format(str(search)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    data = soup.findAll('dl', attrs={'class':'search-dl'})
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = "Search APK Android\n"
                                        for apk in data:
                                            num += 1
                                            link = "https://apkpure.com"+apk.find('a')['href']
                                            title = apk.find('a')['title']
                                            ret_ += "\n {}. {}".format(str(num), str(title))
                                        ret_ += "\n\n Total {} Result".format(str(len(data)))
                                        client.sendMessage(to, str(ret_))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data):
                                            apk = data[num - 1]
                                            with requests.session() as s:
                                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                r = s.get("https://apkpure.com{}/download?from=details".format(str(apk.find('a')['href'])))
                                                soup = BeautifulSoup(r.content, 'html5lib')
                                                data = soup.findAll('div', attrs={'class':'fast-download-box'})
                                                for down in data:
                                                    load = down.select("a[href*=https://download.apkpure.com/]")[0]
                                                    file = load['href']
                                                    rep = down.find('span', attrs={'class':'file'}).text
                                                    place = rep.replace('_apkpure.com','')
                                                    ret_ = "File info :\n"+place
                                                    with requests.session() as web:
                                                        web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                                        r = web.get("https://api-ssl.bitly.com/v3/shorten?access_token=497e74afd44780116ed281ea35c7317285694bf1&longUrl={}".format(urllib.parse.quote(file)))
                                                        data = r.text
                                                        data = json.loads(data)
                                                        ret_ += "\nLink Download :\n"+data["data"]["url"]
                                                    client.sendImageWithURL(msg.to, apk.find('img')['src'])
                                                    client.sendMessage(to, str(ret_))
                            elif cmd.startswith("add friend "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.findAndAddContactsByMid(str(ls))
                                        client.sendMessage(to, "Success Add Friend "+client.getContact(str(ls)).displayName)
                            elif cmd.startswith("add id "):
                                sep = text.split(" ")
                                user = text.replace(sep[0] + " ","")
                                con = client.findContactsByUserid(user)
                                conn = client.findAndAddContactsByUserid(user)
                                try:
                                    dn = con.displayName
                                    client.sendMessage(to, "Success Add Friend "+dn)
                                except Exception as e:
                                    client.sendMessage(msg.to, str(e))
                            elif cmd.startswith("add mp3 "):
                                with open('song.json') as f:
                                    song = json.load(f)
                                    sep = text.split(" ")
                                    qq = text.replace(sep[0] + " ","")
                                    query = qq.replace(" ","+")
                                    params = {'search_query': query}
                                    with requests.session() as s:
                                        s.headers['user-agent'] = 'Mozilla/5.0'
                                        url = 'https://www.youtube.com/results'
                                        r = s.get(url, params=params)
                                        soup = BeautifulSoup(r.content, 'html5lib')
                                        a = "Youtube Audio Playlist"
                                        b = []
                                        song[msg.to] = {}
                                        song[msg.to]['sid'] = []
                                        song[msg.to]['pl'] = []
                                        for c in soup.select('.yt-lockup-title > a[title]'):
                                            if '&lists' not in c['href'] and '/user/' not in c['href']:
                                                b.append(str(c['title']))
                                                d = str(c['href'].replace("/watch?v=",""))
                                                song[msg.to]['sid'].append(d)
                                        for i,t in enumerate(b,1):
                                            a += "\n%d. %s" % (i,t)
                                            song[msg.to]['pl'].append("%d. %s" % (i,t))
                                        f = codecs.open('song.json', 'w', 'utf-8')
                                        json.dump(song, f, sort_keys=True, indent=4, ensure_ascii=False)
                                        client.sendText(msg.to,a+"\n\nGunakan '/play (num) atau /vid (num)' untuk mendengarkan lagu.\nGunakan '/playlist' untuk melihat daftar lagu di group ini.")
                            elif cmd.startswith("play "):
                                with open('song.json', 'r') as fp:
                                    song = json.load(fp)
                                    sep = text.split(" ")
                                    qq = text.replace(sep[0] + " ","")
                                    a = song[msg.to]['sid']
                                    res = ""
                                    if qq == '1':
                                        res += a[0] 
                                    if qq == '2':
                                        res += a[1]
                                    if qq == '3':
                                        res += a[2]
                                    if qq == '4':
                                        res += a[3]
                                    if qq == '5':
                                        res += a[4]
                                    if qq == '6':
                                        res += a[5]
                                    if qq == '7':
                                        res += a[6]
                                    if qq == '8':
                                        res += a[7]
                                    if qq == '9':
                                        res += a[8]
                                    if qq == '10':
                                        res += a[9]
                                    if qq == '11':
                                        res += a[10]
                                    if qq == '12':
                                        res += a[11]     
                                    if qq == '13':
                                        res += a[12] 
                                    if qq == '14':
                                        res += a[13] 
                                    if qq == '15':
                                        res += a[14] 
                                    if qq == '16':
                                        res += a[15] 
                                    if qq == '17':
                                        res += a[16] 
                                    if qq == '18':
                                        res += a[17] 
                                    if qq == '19':
                                        res += a[18] 
                                    if qq == '20':
                                        res += a[19]
                                    if qq == '21':
                                        res += a[20]
                                    if qq == '22':
                                        res += a[21]
                                    if qq == '23':
                                        res += a[22]
                                    if qq == '24':
                                        res += a[23]
                                    if qq == '25':
                                        res += a[24]
                                    req = "https://yoyok.herokuapp.com/vid?url=https://www.youtube.com/watch?v="+res
                                    url = "http://www.youtube.com/watch?v="+res
                                    audio = pafy.new(url)
                                    streams = audio.audiostreams
                                    for a in streams:
                                        b = a.bitrate.replace("k","")
                                        c = a.url
                                        hasil = audio.title
                                        hasil += '\n Like : ' + str(audio.likes)
                                        hasil += '\n Dislike : ' + str(audio.dislikes)
                                        hasil += '\n Durasi : ' + str(audio.duration)
                                        hasil += '\n Rating : ' + str(audio.rating)
                                        hasil += '\n Author : ' + str(audio.author)
                                        if int(str(b)) <= 50:
                                            client.sendMessage(msg.to, str(hasil))
                                            client.sendImageWithURL(msg.to, audio.thumb)
                                            client.sendMessage(msg.to, "Wait for audio stream..!")
                                            client.sendAudioWithURL(msg.to,req)
                            elif cmd.startswith("vid "):
                                with open('song.json', 'r') as fp:
                                    song = json.load(fp)
                                    sep = text.split(" ")
                                    qq = text.replace(sep[0] + " ","")
                                    a = song[msg.to]['sid']
                                    res = ""
                                    if qq == '1':
                                        res += a[0] 
                                    if qq == '2':
                                        res += a[1]
                                    if qq == '3':
                                        res += a[2]
                                    if qq == '4':
                                        res += a[3]
                                    if qq == '5':
                                        res += a[4]
                                    if qq == '6':
                                        res += a[5]
                                    if qq == '7':
                                        res += a[6]
                                    if qq == '8':
                                        res += a[7]
                                    if qq == '9':
                                        res += a[8]
                                    if qq == '10':
                                        res += a[9]
                                    if qq == '11':
                                        res += a[10]
                                    if qq == '12':
                                        res += a[11]     
                                    if qq == '13':
                                        res += a[12] 
                                    if qq == '14':
                                        res += a[13] 
                                    if qq == '15':
                                        res += a[14] 
                                    if qq == '16':
                                        res += a[15] 
                                    if qq == '17':
                                        res += a[16] 
                                    if qq == '18':
                                        res += a[17] 
                                    if qq == '19':
                                        res += a[18] 
                                    if qq == '20':
                                        res += a[19]
                                    if qq == '21':
                                        res += a[20]
                                    if qq == '22':
                                        res += a[21]
                                    if qq == '23':
                                        res += a[22]
                                    if qq == '24':
                                        res += a[23]
                                    if qq == '25':
                                        res += a[24]
                                    req = "https://yoyok.herokuapp.com/vid?url=https://www.youtube.com/watch?v="+res
                                    url = "http://www.youtube.com/watch?v="+res
                                    audio = pafy.new(url)
                                    streams = audio.audiostreams
                                    for a in streams:
                                        b = a.bitrate.replace("k","")
                                        c = a.url
                                        hasil = audio.title
                                        hasil += '\n Like : ' + str(audio.likes)
                                        hasil += '\n Dislike : ' + str(audio.dislikes)
                                        hasil += '\n Durasi : ' + str(audio.duration)
                                        hasil += '\n Rating : ' + str(audio.rating)
                                        hasil += '\n Author : ' + str(audio.author)
                                        if int(str(b)) <= 50:
                                            client.sendMessage(msg.to, str(hasil))
                                            client.sendImageWithURL(msg.to, audio.thumb)
                                            client.sendMessage(msg.to, "Wait for Video stream..!")
                                            client.sendVideoWithURL(msg.to, req)
                            elif cmd.startswith("playlist"):
                                with open('song.json', 'r') as fp:
                                    song = json.load(fp)
                                    info = client.getGroup(msg.to)
                                    group = info.name
                                    play = song[msg.to]['pl']
                                    tab = "\n"
                                    ret = "Playlist di Group "+group+"\n"
                                    for a in play:
                                        tab += ""
                                        ret += "{}{}".format(tab,a)
                                    client.sendMessage(msg.to, ret+"\n\nGunakan '/play (num) atau /vid (num)' untuk mendengarkan lagu.")
                            elif cmd.startswith("arti nama "):
                                sep = text.split(" ")
                                nama = text.replace(sep[0] + " ","")
                                with requests.session() as s:
                                    s.headers['user-agent'] = 'Mozilla/5.0'
                                    r = s.get("http://primbon.com/arti_nama.php?nama1={}&proses=+Submit%21+".format(urllib.parse.quote(nama)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    for anu in soup.findAll('div', attrs={'id':'body'}):
                                        data = anu.get_text()
                                        rep = data.replace('ARTI','<b>ARTI')
                                        res = rep.replace('< Hitung Kembali','</b>')
                                        data1 = BeautifulSoup(res, 'html5lib')
                                        for content in data1:
                                            ret_ = content.b.string
                                            client.sendMessage(to, ret_)
                            if cmd.startswith("spekandro "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","+")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://www.gsmarena.com/res.php3?sSearch={}".format(str(search)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    data = soup.select("div.makers")[0]
                                    b = data.findAll('a', href=True)
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = "Spesifikasi Android\n"
                                        for anu in b:
                                            num += 1
                                            c = "https://www.gsmarena.com/"+anu['href']
                                            ret_ += "\n {}. {}".format(str(num), str(anu.get_text()))
                                        ret_ += "\n\n Total {} Tipe Android".format(str(len(b)))
                                        client.sendMessage(to, str(ret_))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(b):
                                            anu = b[num - 1]
                                            with requests.session() as s:
                                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                r = s.get("https://www.gsmarena.com/{}".format(str(anu['href'])))
                                                soup = BeautifulSoup(r.content, 'html5lib')
                                                data = soup.findAll('div', attrs={'class':'center-stage light nobg specs-accent'})
                                                for pict in soup.findAll('div', attrs={'class':'specs-photo-main'}):
                                                    url = pict.find('img')['src']
                                                    atitle = pict.find('img')['alt']
                                                    title = atitle.replace("MORE PICTURES","")
                                                    client.sendImageWithURL(msg.to, url)
                                                    ret = title
                                                for spec in data:
                                                    ret += "\nDate :\n"+spec.findAll('span')[0].text
                                                    ret += "\nWeight :\n"+spec.findAll('span')[3].text
                                                    ret += "\nOperation System :\n"+spec.findAll('span')[4].text
                                                    ret += "\nInternal :\n"+spec.findAll('span')[6].text
                                                    ret += "\nDisplay size & resolution :\n"+spec.findAll('span')[11].text+" "+spec.findAll('div', attrs={'data-spec':'displayres-hl'})[0].text
                                                    ret += "\nCamera photo & video :\n"+spec.findAll('span')[12].text+"MP "+spec.findAll('div', attrs={'data-spec':'videopixels-hl'})[0].text
                                                    ret += "\nRAM & chipset :\n"+spec.findAll('span')[14].text+"GB RAM "+spec.findAll('div', attrs={'data-spec':'chipset-hl'})[0].text
                                                    ret += "\nBattery capacity & tech :\n"+spec.findAll('span')[16].text+"mAh "+spec.findAll('div', attrs={'data-spec':'battype-hl'})[0].text
                                                    client.sendMessage(msg.to, ret)
                            if cmd.startswith("tafsirquran "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","+")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://tafsirq.com/topik/{}".format(str(search)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    data = soup.findAll('div', attrs={'class':'col-md-12'})
                                    tit = soup.findAll('h1')[0].text
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = tit+"\n"
                                        for get in data:
                                            num += 1
                                            tip = get.find('span').text
                                            isi = tip+': '+get.find('a').text
                                            link = get.find('a')['href']
                                            ret_ += "\n {}. {}".format(str(num), str(isi))
                                        ret_ += "\n\n Total {} Result".format(str(len(data)))
                                        client.sendMessage(to, str(ret_))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data):
                                            get = data[num - 1]
                                            with requests.session() as s:
                                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                r = s.get(get.find('a')['href'])
                                                soup = BeautifulSoup(r.content, 'html5lib')
                                                data = soup.findAll('div', attrs={'class':'panel-body'})[0]
                                                try:
                                                    ret = get.find('a').text+"\n"
                                                    ret += data.findAll('p')[0].text
                                                    ret += "\n\n"+data.findAll('p')[1].text
                                                    client.sendMessage(to, str(ret))
                                                except:
                                                    client.sendMessage(to, "Gagal mengambil data.")
                            if cmd.startswith("togel"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("https://wazetoto.com/wap")
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    data = soup.findAll('table', attrs={'class':'table'})[0]
                                    hasil = data.select('td > a')
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = 'Result Pasaran\n'
                                        for anu in hasil:
                                            num += 1
                                            isi = anu.get_text()
                                            link = anu['href']
                                            ret_ += "\n {}. {}".format(str(num), str(isi))
                                        ret_ += "\n\n Total {} Result".format(str(len(hasil)))
                                        client.sendMessage(to, str(ret_))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(hasil):
                                            anu = hasil[num - 1]
                                            with requests.session() as s:
                                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                                r = s.get(anu['href'])
                                                soup = BeautifulSoup(r.content, 'html5lib')
                                                title = soup.select('h4')[0].text
                                                data = soup.findAll('table', attrs={'class':'table table-hover table-mc-light-blue'})
                                                for res in data:
                                                    try:
                                                        ret = title+"\n"
                                                        ret +="\n "+ res.findAll('td')[0].text+" Periode "+res.findAll('td')[1].text+" Result "+res.findAll('td')[2].text
                                                        ret +="\n "+ res.findAll('td')[3].text+" Periode "+res.findAll('td')[4].text+" Result "+res.findAll('td')[5].text
                                                        ret +="\n "+ res.findAll('td')[6].text+" Periode "+res.findAll('td')[7].text+" Result "+res.findAll('td')[8].text
                                                        ret +="\n "+ res.findAll('td')[9].text+" Periode "+res.findAll('td')[10].text+" Result "+res.findAll('td')[11].text
                                                        ret +="\n "+ res.findAll('td')[12].text+" Periode "+res.findAll('td')[13].text+" Result "+res.findAll('td')[14].text
                                                        ret +="\n "+ res.findAll('td')[15].text+" Periode "+res.findAll('td')[16].text+" Result "+res.findAll('td')[17].text
                                                        ret +="\n "+ res.findAll('td')[18].text+" Periode "+res.findAll('td')[19].text+" Result "+res.findAll('td')[20].text
                                                        client.sendMessage(to, str(ret))
                                                    except:
                                                        client.sendMessage(to, "Gagal mengambil data.")
                            elif cmd.startswith("smuleid "):
                                sep = text.split(" ")
                                nama = text.replace(sep[0] + " ","")    
                                with requests.session() as s:
                                    s.headers['user-agent'] = 'Mozilla/5.0'
                                    r = s.get("https://www.smule.com/{}".format(urllib.parse.quote(nama)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    try:
                                        ret_ = 'Smule profile'
                                        for anu in soup.findAll('script', attrs={'type':'text/javascript'})[1]:
                                            a = anu.replace('DataStore.Pages.Profile =','')
                                            b = a.replace(';','')
                                            get = json.loads(b)
                                            pict = get['user']['pic_url']
                                            ret_ += "\nâââAccount ID: "+str(get['user']['account_id'])
                                            ret_ += "\nâ Username: "+str(get['user']['handle'])
                                            ret_ += "\nâ Followers: "+str(get['user']['followers'])
                                            ret_ += "\nâ Followees: "+str(get['user']['followees'])
                                            ret_ += "\nâ Performances: "+str(get['user']['num_performances'])
                                            ret_ += "\nâ VIP Status: "+str(get['user']['is_vip'])
                                            ret_ += "\nâ Verified: "+str(get['user']['is_verified'])
                                            ret_ += "\nâ URL: https://www.smule.com/"+str(get['user']['handle'])
                                            ret_ += "\nâââDescription:\n"+str(get['user']['blurb'])
                                        client.sendMessage(msg.to, ret_)
                                        client.sendImageWithURL(msg.to, pict)
                                    except:
                                        client.sendMessage(msg.to, "User tidak ditemukan!")
                            elif cmd.startswith("getfs: "):
                                sep = msg.text.split(" ")
                                anu = msg.text.replace(sep[0] + " "," ")                
                                with requests.session() as web:
                                    web.headers["user-agent"] = random.choice(settings["userAgent"])
                                    r = web.get("https://farzain.xyz/api/premium/fs.php?apikey=apikey_saintsbot&id={}".format(str(urllib.parse.quote(anu))))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["status"] == "success":
                                        ret_ = data["url"]
                                        client.sendImageWithURL(msg.to,ret_)
                                    else:
                                        client.sendMessage(msg.to, "")
                            elif cmd.startswith("fs "):
                                sep = text.split(" ")
                                cos = text.replace(sep[0] + " ","")
                                hasil = "http://api.farzain.com/special/fansign/cosplay/cosplay.php?apikey=sb_apikey&text="+cos
                                try:
                                    client.sendImageWithURL(msg.to, hasil)
                                except:
                                    client.sendMessage(msg.to, "API Error or Upload failed!")
                            elif cmd.startswith("friend list"):
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                count = urutan.split("|")
                                if len(count) == 1:
                                    aa = client.getAllContactIds()
                                    no = 0
                                    hasil = "âââ[ RRIENDLIST ]\n"
                                    for ids in client.getContacts(aa):
                                        no += 1
                                        hasil += "\nâ "+str(no)+". " +str(ids.displayName)
                                    hasil += "\n\nâââ Total teman {} ".format(str(len(client.getContacts(aa))))
                                    client.sendMessage(to, hasil, {'AGENT_NAME': '  => List Friends =>','AGENT_LINK': 'https://line.me/ti/p/~zainal_ariv','AGENT_ICON': 'https://profile.line-scdn.net/0h8f5tYg7aZ0kIDUpvh8gYHjRIaSR_I2EBcGkvKnhdan92OCAWNW17KyVeOHl3NXJINW18LnoJay4n' })
#                                    client.sendText(msg.to,"=> Selanjutnya\n\n=> /temaninfo | urutan\n=> /temanhapus | urutan")
                                elif len(count) == 2:
                                    if "temaninfo" in text.lower():
                                        try:
                                            num = int(count[1])
                                            cc = client.getAllContactIds()
                                            dd = client.getContact(cc[num - 1])
                                            hasil = "âââ Informasi teman\n"
                                            hasil += "â  Nama {}".format(str(dd.displayName))
                                            hasil += "\nâ  Mid {}".format(str(dd.mid))
                                            hasil += "\nâââ Bio {}".format(str(dd.statusMessage))
                                            client.sendMessage(to, hasil, {'AGENT_NAME': '  => Friend Info =>','AGENT_LINK': 'https://line.me/ti/p/~zainal_ariv','AGENT_ICON': 'https://profile.line-scdn.net/0h8f5tYg7aZ0kIDUpvh8gYHjRIaSR_I2EBcGkvKnhdan92OCAWNW17KyVeOHl3NXJINW18LnoJay4n' })
                                            client.sendContact(to, dd.mid)
                                        except Exception as e:
                                            client.sendText(msg.to,""+str(e))
                                    if "del friend" in text.lower():
                                        try:
                                            num = int(count[1])
                                            cc = client.getAllContactIds()
                                            dd = client.getContact(cc[num - 1])
                                            client.updateFriendlist(dd.mid)
                                            hasil = "Sukses menghapus {} dari friendlist.".format(str(dd.displayName))
                                            client.sendMessage(to, hasil, {'AGENT_NAME': '  ã Friend Info ã','AGENT_LINK': 'https://line.me/ti/p/~zainal_ariv','AGENT_ICON': 'https://profile.line-scdn.net/0h8f5tYg7aZ0kIDUpvh8gYHjRIaSR_I2EBcGkvKnhdan92OCAWNW17KyVeOHl3NXJINW18LnoJay4n' })
                                        except Exception as e:
                                            client.sendText(msg.to,""+str(e))
                            elif cmd.startswith("member"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                if len(cond) == 1:
                                    mem = int(cond[0])
                                    aa = client.getGroupIdsJoined()[mem - 1]
                                    bb = client.getGroup(aa)
                                    gtime = bb.createdTime
                                    data = bb.members
                                    num = 0
                                    hasil = "âââ Group Member ââ\nâ  ID group: {}\nâ  Created {}\nâ  Group: {}\n".format(cond[0], timeago.format(datetime.now(),gtime/1000), bb.name)
                                    for cc in data:
                                        num += 1
                                        hasil += "\n"+str(num)+". " +str(cc.displayName)
                                    hasil += "\n\n Total {} Result".format(str(len(data)))
                                    client.sendMessage(to, hasil, {'AGENT_NAME': '  => Friend Info <=','AGENT_LINK': 'https://line.me/ti/p/~team_silent','AGENT_ICON': 'https://profile.line-scdn.net/0h8f5tYg7aZ0kIDUpvh8gYHjRIaSR_I2EBcGkvKnhdan92OCAWNW17KyVeOHl3NXJINW18LnoJay4n' })
                                elif len(cond) == 2:
                                    try:
                                        mem = int(cond[0])
                                        num = int(cond[1])
                                        aa = client.getGroupIdsJoined()[mem - 1]
                                        anu = client.getGroup(aa)
                                        cc = anu.members[num - 1]
                                        client.sendContact(msg.to,cc.mid)
                                    except Exception as e:
                                        client.sendText(msg.to,""+str(e))
                            
# Pembatas Script #
# Pembatas Script #
                        if text.lower() == "mykey":
                            client.sendMessage(to, "KeyCommand Saat ini adalah [ {} ]".format(str(settings["keyCommand"])))
                        elif text.lower() == "setkey on":
                            settings["setKey"] = True
                            client.sendMessage(to, "Done on")
                        elif text.lower() == "setkey off":
                            settings["setKey"] = False
                            client.sendMessage(to, " Done off")
                        for image in images:
                            if text.lower() == image:
                                client.sendImage(to, images[image])
                        for sticker in stickers:
                            if text.lower() == sticker:
                                sid = stickers[sticker]["STKID"]
                                spkg = stickers[sticker]["STKPKGID"]
                                sver = stickers[sticker]["STKVER"]
                                sendSticker(to, sver, spkg, sid)
                        for audio in audios:
                            if text.lower() == audio:
                                client.sendAudio(to, audios[audio])
                        for video in videos:
                            if text.lower() == video:
                                client.sendVideo(to, videos[video])
# Pembatas Script #
                    elif msg.contentType == 1:
                        if settings["changeProfileVideo"] == True:
                            client.downloadObjectMsg(msg_id, saveAs="image.jpeg")
                            settings["changeProfileVideo"] = False
                            client.sendMessage(to, "Foto di Simpan, langkah selanjutnya ketik gantippvideo !")
                        if settings["addImage"]["status"] == True:
                            path = client.downloadObjectMsg(msg_id)
                            images[settings["addImage"]["name"]] = str(path)
                            f = codecs.open("image.json","w","utf-8")
                            json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                            client.sendMessage(to, "Berhasil menambahkan gambar {}".format(str(settings["addImage"]["name"])))
                            settings["addImage"]["status"] = False
                            settings["addImage"]["name"] = ""
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = client.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            client.updateProfilePicture(path)
                            client.sendMessage(to, "success changing my picture profile")
                        if msg.toType == 2:
                            if to in settings["changeGroupPicture"]:
                                path = client.downloadObjectMsg(msg_id)
                                settings["changeGroupPicture"].remove(to)
                                client.updateGroupPicture(to, path)
                                client.sendMessage(to, "success changing group picture")
                    elif msg.contentType == 2:
                        if settings["changeProfileVideo"] == True:
                            client.downloadObjectMsg(msg_id, saveAs="video.mp4")
                            settings["changeProfileVideo"] = False
                            pict = "image.jpeg"
                            vids = "video.mp4"
                            ChangeVideoProfile(pict, vids)
                            client.sendMessage(to, "Berhasil mengubah foto + video profile")
                        if settings["addVideo"]["status"] == True:
                            path = client.downloadObjectMsg(msg_id)
                            videos[settings["addVideo"]["name"]] = str(path)
                            f = codecs.open("video.json","w","utf-8")
                            json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                            client.sendMessage(to, "Berhasil menambahkan video {}".format(str(settings["addVideo"]["name"])))
                            settings["addVideo"]["status"] = False
                            settings["addVideo"]["name"] = ""
                    elif msg.contentType == 3:
                        if settings["addAudio"]["status"] == True:
                            path = client.downloadObjectMsg(msg_id)
                            audios[settings["addAudio"]["name"]] = str(path)
                            f = codecs.open("audio.json","w","utf-8")
                            json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                            client.sendMessage(to, "Berhasil menambahkan audio {}".format(str(settings["addAudio"]["name"])))
                            settings["addAudio"]["status"] = False
                            settings["addAudio"]["name"] = ""
                    elif msg.contentType == 7:
                        if settings["addSticker"]["status"] == True:
                            stickers[settings["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                            stickers[settings["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                            stickers[settings["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                            f = codecs.open('sticker.json','w','utf-8')
                            json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                            client.sendMessage(to, "Berhasil menambahkan stiker {}".format(str(settings["addSticker"]["name"])))
                            settings["addSticker"]["status"] = False
                            settings["addSticker"]["name"] = ""
                        if settings["save_sticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            settings["stkid"] = str(stk_id)
                            settings["pkgid"] = str(pkg_id)
                            settings["save_sticker"] = False
                            client.sendMessage(to,"Berhasil mendaftarkan sticker sebagai respon mention")
                    elif msg.contentType == 7:
                        if settings["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "âââ[Sticker Info]"
                            ret_ += "\nâ  STICKER ID : {}".format(stk_id)
                            ret_ += "\nâ  STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\nâ  STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\nâââ STICKER URL : line://shop/detail/{}".format(pkg_id)
                            client.sendMessage(to, str(ret_))
                    elif msg.contentType == 13:
                        if settings["checkContact"] == True:
                            try:
                                contact = client.getContact(msg.contentMetadata["mid"])
                                if client != None:
                                    cover = client.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                       client.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "âââ[Details Contact]"
                                ret_ += "\nâ  Name : {}".format(str(contact.displayName))
                                ret_ += "\nâ  MID : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\nâ  Bio : {}".format(str(contact.statusMessage))
                                ret_ += "\nâ  Photo URL : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\nâââ Cover URL : {}".format(str(cover))
                                client.sendMessage(to, str(ret_))
                            except:
                                client.sendMessage(to, "Kontak tidak valid")
                    elif msg.contentType == 16:
                        if settings["checkPost"] == True:
                            try:
                                ret_ = "âââ[Details Post]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = client.getContact(sender)
                                    auth = "\nâ  Writer : {}".format(str(contact.displayName))
                                else:
                                    auth = "\nâ  Writer : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\nâ  Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                     if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\nObject URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\nMedia URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                     else:
                                            ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\nMedia URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                             ourl = "\nObject URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                         ourl = "\nObject URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\nSticker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\nText : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                client.sendMessage(to, str(ret_))
                            except:
                                client.sendMessage(to, "Post not valid")
            except Exception as error:
                  logError(error)
                  traceback.print_tb(error.__traceback__)

        if op.type == 26:
            try:
                print ("[ 26 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if settings["autoRead"] == True:
                        client.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            client.sendMessage(msg.to,text)
                    if settings["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                client.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                client.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                            if settings["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = client.findGroupByTicket(ticket_id)
                                    client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    client.sendMessage(to, "Success joined to group %s" % str(group.name))
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            pkgid = settings["pkgid"]
                            stkid = settings["stkid"]
                            for mention in mentionees:
                                if clientMid in mention["M"]:
                                    if settings["autoRespon"] == True:
                                        if settings["update_mention"] == True:
                                           client.sendMessage(to, str(settings["save_mention"]))
                                           client.sendSticker(to,str(pkgid),str(stkid))
                                        else:
                                           sendMention(to, "[AUTO RESPON]\nWoy @! no tag me", [sender])
                                           client.sendSticker(to,str(pkgid),str(stkid))
                                    break
                    elif msg.contentType == 7:
                        if settings["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "âââ[Sticker Info]\n"
                            ret_ += "\nâ  STICKER ID : {}".format(stk_id)
                            ret_ += "\nâ  STICKER PKGID : {}".format(pkg_id)
                            ret_ += "\nâ  STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\nâââ STICKER URL : \nline://shop/detail/{}".format(pkg_id)
                            client.sendMessage(to, str(ret_))
                    elif msg.contentType == 13:
                        if settings["checkContact"] == True:
                            try:
                                contact = client.getContact(msg.contentMetadata["mid"])
                                if client != None:
                                    cover = client.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Can't login to line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                     client.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "âââ[Details Contact]\n"
                                ret_ += "\nâ  Name : {}".format(str(contact.displayName))
                                ret_ += "\nâ  MID : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\nâ  Bio : {}".format(str(contact.statusMessage))
                                ret_ += "\nâ  Photo URL : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\nâââ Cover URL : {}".format(str(cover))
                                client.sendMessage(to, str(ret_))
                            except:
                                client.sendMessage(to, "Kontak tidak valid")
                    if msg.contentType == 7:
                            if msg.to in settings["chatEvent"]:
                                jeje = [4,13,2,10,17,401,402,5,15,1,3,16,403,404,405,406,11,7,21,14,8,9,12,6,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,407,408,409,410]
                                jejen = random.choice(jeje)
                                goo = 1
                                client.sendSticker(to, str(goo), str(jejen))
                    elif msg.contentType == 16:
                        if settings["checkPost"] == True:
                            try:
                                ret_ = "âââ[Details Post]\n"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = client.getContact(sender)
                                    auth = "\nâ  [Writer]\n {}".format(str(contact.displayName))
                                else:
                                    auth = "\nâ  [Writer]\n {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n\nâ  [Post URL]\n {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                     if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n\n[Object URL]\n https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n\n[Media URL]\n https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                     else:
                                            ourl = "\n\n[Objek URL]\n https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n\n[Media URL]\n https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n\n[Object URL]\n https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                         ourl = "\n\n[Object URL]\n https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n\n[Sticker]\n https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n\n[Text]\n {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                client.sendMessage(to, str(ret_))
                            except:
                                client.sendMessage(to, "Post tidak valid")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            contact = client.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                            else:
                                name_ = contact.displayName
                                ret_ = "âââ[UNSEND MSG]\n\n"
                                ret_ += "\nâ  Sender : @!"
                                ret_ += "\nâ  Send At : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\nâ  Type : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                ret_ += "\nâââ Text : {}".format(str(msg_dict[msg_id]["text"]))
                                sendMention(at, str(ret_), [contact.mid])
                            del msg_dict[msg_id]
                        else:
                            client.sendMessage(at,"Maaf boss hiii")
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)

        if op.type == 55:
                try:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    if op.param1 in cctv["cyduk"] :
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\nâââ " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 3:

                                        client.sendMessage(op.param1, "âââ[PENGINTIP]\nâ Ngapin Ngintip Ajja Kak\nâ " + "" + Name + "\nâ Kaya Kurang Kerjaan Ajja\nâ Detected online at time:\nâââ["+datetime.strftime(timeNow,'%H:%M:%S')+"]"+"\n["+ datetime.strftime(timeNow,'%Y-%m-%d') + "]")

                                        #MENTION(op.param1,[op.param2])
                                    else:
                                        client.sendMessage(op.param1, "âââ[TUKANG NGINTIP]\nâ Sini Kak\nâ " + "" + Name + "\nâ Gabung Chat Biar Rame\nâ Detected online at time:\nâââ["+datetime.strftime(timeNow,'%H:%M:%S')+"]"+"\n["+ datetime.strftime(timeNow,'%Y-%m-%d') + "]")
                                        #MENTION(op.param1,[op.param2])
                                else:
                                    client.sendMessage(op.param1, "âââ[TUKANG NGINTIP]\nâ Nah kan Ketahuan kak\nâ " + "" + Name + "\nâ Kalau Ngintip\nâ Detected online at time:\nâââ["+datetime.strftime(timeNow,'%H:%M:%S')+"]"+"\n["+ datetime.strftime(timeNow,'%Y-%m-%d') + "]")
                                    #MENTION(op.param1,[op.param2])
                        else:
                            pass
                    elif op.param1 in read['readPoint']:
                        if op.param2 in read['readMember'][op.param1]:
                            pass
                        else:
                            read['readMember'][op.param1] += op.param2
                        read['ROM'][op.param1][op.param2] = op.param2
                    else:
                       pass
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

while True:
    try:
        delete_log()
        ops = clientPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
#                clientBot(op)
                loop.run_until_complete(clientBot(op))
                clientPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
