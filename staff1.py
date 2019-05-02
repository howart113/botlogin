#import LINEPY
#from LINEPY import *
from linepy import *
from akad.ttypes import *
from tmp.petunjuk import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from datetime import datetime, timedelta, date
from random import randint
from tmp.MySplit import *
from tmp.zalgos import zalgos
from tmp.Instagram import InstagramScraper
from multiprocessing import Pool, Process
from io import StringIO
import selenium.webdriver as webdriver
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as pesan
import time, random, sys, json, null, codecs, html5lib ,shutil ,threading, glob, re, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
loop = asyncio.get_event_loop()
#======================================================================================
botStart = time.time()
#======================================================================================
try:
    with open('token1.txt','r') as tokens:
        token = tokens.read()
    print(str(token))
except Exception as e:
    gonebot = LINE()
gonebot = LINE(token)
gonebot.log("Auth Token : " + str(gonebot.authToken))
gonebot.log("Timeline Token : " + str(gonebot.tl.channelAccessToken))
#====================================================================================
#====================================================================================
myMid = gonebot.profile.mid
gonebotPoll = OEPoll(gonebot)
gonebotProfile = gonebot.getProfile()
gonebotMID = gonebot.getProfile().mid
bot = [gonebotMID]
#====================================================================================
mulai = time.time()
#====================================================================================
lastseen = {
    "find": {},
    "username": {}
}
kuciyose = {'mimic':{},'thread':{},'MakeWaterColor':{'s1':False,'s2':False,'s3':False},'DrawImage':False,'DrawMissing':{'t1':'','t2':'','t3':'','t4':False},'MakeMeme':False,'tos':{},'talkblacklist':{'tos':{}},"GN":""}
#====================================================================================
#====================================================================================
Bots = [myMid]
zxcvzx = myMid
heheOpen = codecs.open('basic.json','r','utf-8')
settingsOpen = codecs.open("temp.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
stickers1Open = codecs.open("sticker1.json","r","utf-8")
stickers2Open = codecs.open("sticker2.json","r","utf-8")
wait = json.load(heheOpen)
stickers = json.load(stickersOpen)
stickers1 = json.load(stickers1Open)
stickers2 = json.load(stickers2Open)
settings = json.load(settingsOpen)
msg_image={}
msg_video={}
msg_sticker={}
msgdikirim = {}
msgditerima = {}
unsendchat = {}
msg_dict = {}
temp_flood = {}
groupName = {}
numlist= {}
groupImage = {}
kuciyose = {}
protectname = []
wbanlist = []
groupName = {}
groupImage = {}
kuciyose = {}
protectqr = []
protectkick = []
protecARoin = []
protectinvite = []
protectcancel = []
oepoll = OEPoll(gonebot)
Ariff = gonebotMID
#====================================================================================
with open('protectcancel.json', 'r') as fp:
    protectcancel = json.load(fp)  
with open('protectinvite.json', 'r') as fp:
    protectinvite = json.load(fp)
#====================================================================================
wait["myProfile"]["displayName"] = gonebotProfile.displayName
wait["myProfile"]["statusMessage"] = gonebotProfile.statusMessage
wait["myProfile"]["pictureStatus"] = gonebotProfile.pictureStatus
cont = gonebot.getContact(gonebotMID)
wait["myProfile"]["videoProfile"] = cont.videoProfile
coverId = gonebot.getProfileDetail()["result"]["objectId"]
wait["myProfile"]["coverId"] = coverId
#====================================================================================
settings = {
    "autoblock": True,
    "autoLeave": True,
    "lang": "JP",
    "tag": False,
    "pict": False,
    "server": "VPS",
    "ilstpict": {},
    "tagsticker": False,
    "addSticker": {
        "name": "",
        "status": False,
    },
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "tag": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "lv": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "wc": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "add": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "join2": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
        }
    },
}

RfuProtect = {
    "autoblock": True,
    "autoLeave": True,
}

norak = {
    "detectTemplate": False,
}

nissa = {
    "addTikel2": {
        "name": "",
        "status": False
        },
}

anyun = {
    "addTikel": {
        "name": "",
        "status": False
        },
}

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

tes = {
    "Message": {},
    "msg": {},
}

tes2 = {
    "Message2": {},
    "msg2": {},
}

peler = { 
    "receivercount": 0,
    "sendcount": 0
}

read = { 
    "readMember": {},
    "readPoint": {}
}

hoho = {
    "savefile": False,
    "namefile": "",
}
temp = {"te": "#FFFFFF","t": "#6600CC"}
temptag = {
    "stealtag": True,
    "pesanya": "ยังไม่มีข้อความตอบแทค",
}

tagadd = {
    "add": "ยินดีที่ได้รู้จักนะครับ 😃\nรับแอดละน้า. >_<",
    "wctext": "ยินดีต้อนรับเข้ากลุ่มนะครับ 😃",
    "lv": "บ๊ายบาย >< ขอให้เธอโชคดีงับ >_<",
}

ProfileMe = {
    "myProfile": {
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "PictureMe": "",
    "NameMe": "",
}
#====================================================================================
with open("temp.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("basic.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
#======================แจ้งเตือน============================================================
Notify = "ueb552d5cde140643b7604a3486ce9f6e"
gonebot.findAndAddContactsByMid(Notify)
gonebot.sendMessage(Notify,"เข้าสู่ระบบสำเร็จ")
lgncall = ""
keyword = {}
try:
    with open('keyword.json', 'r',encoding="utf_8_sig") as fpsave:
        keyword = json.load(fpsave)
    print("file keyword Go!!!")
except:
    print("Couldn't file keyword")
#=========================เวลาออน===========================================================
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)   
#====================================================================================    
def redtube(to):
    numb = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    a = requests.get("https://api.boteater.vip/redtube?page={}".format(random.choice(numb)))
    a = json.loads(a.text)
    ret = []
    for i in a['result']:
        data = {"messages": [{"type": "video","originalContentUrl": i['dl'],"previewImageUrl": i['img']}]}
        sendCarousel(to,data)
def picFinder(name):    
        try:
            rgram = requests.get('http://www.instagram.com/{}'.format(name))
            rgram.raise_for_status()
            selenaSoup=BeautifulSoup(rgram.text,'html.parser')
            pageJS = selenaSoup.select('script')
            for i, j in enumerate(pageJS):
                pageJS[i]=str(j)
            picInfo = sorted(pageJS,key=len, reverse=True)[0]
            allPics = json.loads(str(picInfo)[52:-10])['entry_data']['ProfilePage'][0]
            return allPics
        except requests.exceptions.HTTPError:
            return '\t \t ### ACCOUNT MISSING ###'
def igsearch(msg,wait,pesan):
        to = msg.to
        msg.text = pesan
        text = msg.text.split(' ')[1]
        data = picFinder(text)
        if len(msg.text.split(' ')) == 2:
            try:
                asd = data['graphql']['user']
                data = instagramku(msg,wait,text,asd)
                sendCarousel(msg.to,data)
            except:
                text = traceback.format_exc()
                return gonebot.sendMessage(to,"Status: 404\nReason: Instagram {}".format(text))
        if(pesan.startswith('instagram post ') and len(pesan.split(' ')) == 3):
            try:
                k = InstagramScraper()
                results = k.profile_page_recent_posts('https://www.instagram.com/{}/?hl=id'.format(msg.text.split(' ')[2]))
                try:
                    ret_ = []
                    for i in results:
                        url = i['thumbnail_src']
                        ret_.append({"type": "bubble","hero": {"type": "image","url": url,"size": "full","aspectRatio": "1:1","aspectMode": "fit",},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Post Detail","uri": "{}instagram%20post%20{}%20{}".format(wait["ttt"],msg.text.split(" ")[2],len(ret_))}},],}})
                    k = len(ret_)//10
                    for aa in range(k+1):
                        data = {"messages": [{"type": "flex","altText": "Noob sent a flex.","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                        sendCarousel(to,data)
                except Exception as e:
                    traceback.print_tb(e.__traceback__)
            except Exception as e:
                ee = traceback.format_exc()
                return gonebot.sendMessage(to,'{}'.format(e))
        if(pesan.startswith('instagram post ') and len(pesan.split(' ')) == 4):
            k = InstagramScraper()
            results = k.profile_page_recent_posts('https://www.instagram.com/{}/?hl=id'.format(msg.text.split(' ')[2]))
            ret = []
            no = 0
            for i in results:
                no += 1
                ret.append(i['shortcode'])
            url = requests.get('https://www.instagram.com/p/{}'.format(ret[int(msg.text.split(' ')[3])]))
            soup = BeautifulSoup(url.text, 'html.parser')
            z = soup.find('body')
            y = z.find('script')
            v = y.text.strip().replace('window._sharedData =', '').replace(';', '')
            d = json.loads(v)
            ret_ = []
            e = d['entry_data']['PostPage'][0]['graphql']['shortcode_media']
            if 'edge_sidecar_to_children' in e:
                like = e['edge_media_preview_like']['count']
                caption = e['edge_media_to_caption']['edges']
                for zz in caption:
                    anu = zz['node']['text']
                comment = e['edge_media_to_comment']['count']
                bla = e['edge_media_to_comment']
                for ib in bla['edges']:
                    komen = ib['node']['text']
                    usrname = ib['node']['owner']['username']
                for a in e['edge_sidecar_to_children']['edges']:
                    if a['node']['is_video'] == True:
                        prev = a['node']['display_url']
                        vid = a['node']['video_url']
                        view = a['node']['video_view_count']
                    else:
                        pict = a['node']['display_url']
                    try:
                        ret_.append({"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "INSTAGRAM POST","weight": "bold"}]},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Send Video","uri": "line://app/1602687308-GXq4Vvk9?type=video&ocu={}&piu={}".format(vid,prev)}},]},"hero": {"type": "image","url": prev,"size": "full","aspectRatio": "1:1","aspectMode": "fit"},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "POST INFO","weight": "bold","size":"md","margin":"md"},{"type":"separator","color":"#000000"},{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Caption","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(anu),"color": "#262423","size": "sm","wrap": True,"flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Likes","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(like)),"color": "#262423","size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Comment","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(comment)),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "From","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "@{}".format(usrname),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Text","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(komen),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "View count","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(view)),"color": "#262423","wrap": True,"size": "sm","flex": 5}]}]}]}})
                    except:
                        ret_.append({"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "INSTAGRAM POST","weight": "bold"}]},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Send Image","uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(pict)}},]},"hero": {"type": "image","url": pict,"size": "full","aspectRatio": "1:1","aspectMode": "fit"},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "POST INFO","weight": "bold","size":"md","margin":"md"},{"type":"separator","color":"#000000"},{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Caption","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(anu),"color": "#262423","size": "sm","wrap": True,"flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Likes","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(like)),"color": "#262423","size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Comment","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(comment)),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "From","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "@{}".format(usrname),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Text","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(komen),"color": "#262423","wrap": True,"size": "sm","flex": 5}]}]}]}})
                k = len(ret_)//10
                for aa in range(k+1):
                    data = {"messages": [{"type": "flex","altText": "Noob sent a flex.","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                    sendCarousel(to,data)
            else:
                like = e['edge_media_preview_like']['count']
                caption = e['edge_media_to_caption']['edges']
                for zz in caption:
                    anu = zz['node']['text']
                comment = e['edge_media_to_comment']['count']
                bla = e['edge_media_to_comment']
                for ib in bla['edges']:
                    komen = ib['node']['text']
                    usrname = ib['node']['owner']['username']
                if e['is_video'] == True:
                    durasi = e['video_duration']
                    view = e['video_view_count']
                    ret_.append({"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "INSTAGRAM POST","weight": "bold"}]},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Send Video","uri": "line://app/1602687308-GXq4Vvk9?type=video&ocu={}&piu={}".format(e['video_url'],e['display_url'])}},]},"hero": {"type": "image","url": e['display_url'],"size": "full","aspectRatio": "1:1","aspectMode": "fit"},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "POST INFO","weight": "bold","size":"md","margin":"md"},{"type":"separator","color":"#000000"},{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Caption","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(anu),"color": "#262423","size": "sm","wrap": True,"flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Likes","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(like)),"color": "#262423","size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Comment","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(comment)),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "From","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "@{}".format(usrname),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Text","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(komen),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "View count","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(view)),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Duration","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{} Second".format(humanize.intcomma(durasi)),"color": "#262423","wrap": True,"size": "sm","flex": 5}]}]}]}})
                else:
                    ret_.append({"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "INSTAGRAM POST","weight": "bold"}]},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Send Image","uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(e['display_url'])}},]},"hero": {"type": "image","url": e['display_url'],"size": "full","aspectRatio": "1:1","aspectMode": "fit"},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "POST INFO","weight": "bold","size":"md","margin":"md"},{"type":"separator","color":"#000000"},{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Caption","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(anu),"color": "#262423","size": "sm","wrap": True,"flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Likes","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(like)),"color": "#262423","size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Comment","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(comment)),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "From","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "@{}".format(usrname),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Text","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(komen),"color": "#262423","wrap": True,"size": "sm","flex": 5}]}]}]}})
                k = len(ret_)//10
                for aa in range(k+1):
                    data = {"messages": [{"type": "flex","altText": "Noob sent a flex.","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                    sendCarousel(to,data)
        if(pesan.startswith('instagram story ')):
            a = requests.get("https://rest.farzain.com/api/ig_story.php?id={}&apikey=aguzzzz748474848&beta".format(msg.text.split(' ')[2])).text
            a = json.loads(a)
            ret_ = []
            s = [c for c in a['pict_url']]
            for b in a['video_url']:
                print(b)
                if b == 'None':
                    pass
                ret_.append({"type": "bubble","hero": {"type": "image","url": "https://boteater.vip/jpg-5quup28a.jpg","size": "full","aspectRatio": "1:1","aspectMode": "fit",},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Send Video","uri": "line://app/1602687308-GXq4Vvk9?type=video&ocu={}&piu=https://image.freepik.com/free-vector/instagram-icon_1057-2227.jpg".format(b)}},],}})
            k = len(ret_)//10
            for aa in range(k+1):
                data = {"messages": [{"type": "flex","altText": "Noob sent a flex.","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                sendCarousel(to,data)
def blekedok(t:int=None):
    r = requests.get('https://www.webtoons.com/id/genre')
    soup = BeautifulSoup(r.text,'html5lib')
    data = soup.find_all(class_='card_lst')
    return data
def WebtoonDrama(msg,wait,pesan):
    msg.text = pesan
    drama = msg.text.split(' ')[1]
    text = msg.text
    for a in DramaEnak(drama,text,msg.to,blekedok(drama),wait):sendCarousel(msg.to,a)
def samehadakuget(h):
    if h == '1':r = requests.get('https://www.samehadaku.tv/')
    else:r = requests.get('https://www.samehadaku.tv/page/{}'.format(h))
    soup = BeautifulSoup(r.text,'html5lib')
    data = soup.find_all(class_='post-title')
    del data[0]
    del data[14:]
    return data
def samehadakulist(to,msg,wait,pesan):
    msg.text = pesan
    h = pesan.split(" ")[2]
    data = samehadakuget(h)
    b = ' 「 Samehadaku 」'
    if len(pesan.split(" ")) == 3:
        if int(h) == 1:no = 0
        else:no = (int(h)-1)*14
        for c in data:
            no+=1
            b+= '\n{}. {}'.format(no,c.find('a').text)
        b+= '\n    Example Samehadaku page {} 1'.format(h)
        gonebot.sendMessage(msg.to,b)
    if len(pesan.split(" ")) == 4:
        if int(pesan.split(' ')[2]) == 1:g = int(pesan.split(' ')[3])-1
        else:g = int(pesan.split(' ')[3])-1;g = (((int(pesan.split(' ')[2])*14-14)//(int(pesan.split(' ')[2])-1))-(-int(pesan.split(' ')[3])+14*int(pesan.split(' ')[2])))-1
        r = requests.get(data[g].find('a').get('href'))
        soup = BeautifulSoup(r.text,'html5lib')
        data1 = soup.find(class_='download-eps')
        b += '\nTitle: {} \n\n  |  Donwloader  |'.format(data[g].find('a').text)
        for ss in data1.find_all('li'):
            b+= '\n\n  - {}'.format(ss.text.strip().split('UF')[0])
            no=0
            for dd in ss.find_all('a'):
                no+=1
                b+= '\n    {}. {} {}'.format(no,dd.text,dd.get('href').replace('http://www.',''))
        b+= '\n\n | Info Download |\nUF = UpFile, CU = Cloud User\nGD = Google Drive\nZS = Zippy Share, SC = Sendit Cloud\nMU = Mega UP'
        gonebot.sendMessage(msg.to,b)
        gonebot.sendImageWithURL(msg.to,soup.find_all('img')[2]['src'],data[g].find('a').text)
def webtoon(to,msg,wait):
    data = webtoonk(msg,wait)
    sendCarousel(to,data)
def youtube(to,wait):
    data = {
        "messages": [
            {
                "type": "flex",
                "altText": "Noob sent a template.",
                "contents": {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://pixelstalk.net/wp-content/uploads/2016/05/Youtube-Wallpapers-HD-kids-620x349.jpg",
                        "size": "full",
                        "aspectRatio": "1:1",
                        "aspectMode": "fit",
                        "size": "full"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "contents": [
                            {
                                "type": "text",
                                "text": "YOUTUBE",
                                "weight": "bold",
                                "size": "md",
                                "margin": "md"
                            },
                            {
                                "type": "separator",
                                "color": "#000000",
                            },
                            {
                                 "type": "box",
                                 "layout": "baseline",
                                 "margin": "md",
                                 "contents": [
                                     {
                                         "type": "text",
                                         "text": "| Type |",
                                         "weight": "bold",
                                         "size": "md",
                                         "margin": "md",
                                         "align": "center"
                                     }
                                 ]
                             },
                             {
                                 "type": "box",
                                 "layout": "baseline",
                                 "margin": "md",
                                 "contents": [
                                     {
                                         "type": "text",
                                         "text": "- AUDIO",
                                         "flex": 1,
                                         "size": "md",
                                         "margin": "md"
                                     },
                                     {
                                         "type": "text",
                                         "text": "- SEARCH",
                                         "flex": 1,
                                         "size": "md",
                                         "margin": "md"
                                     },
                                 ]
                             },
                             {
                                 "type": "box",
                                 "layout": "baseline",
                                 "margin": "md",
                                 "contents": [
                                     {
                                         "type": "text",
                                         "text": " ",
                                         "flex": 1,
                                         "size": "md",
                                         "margin": "md"
                                     },
                                     {
                                         "type": "text",
                                         "text": "- INFO",
                                         "size": "md",
                                         "margin": "md",
                                         "flex": 3,
                                     }
                                 ]
                             },
                             {
                                 "type": "box",
                                 "layout": "baseline",
                                 "margin": "md",
                                 "contents": [
                                     {
                                         "type": "text",
                                         "text": "- VIDEO",
                                         "flex": 1,
                                         "size": "md",
                                         "margin": "md"
                                     },
                                     {
                                         "type": "text",
                                         "text": "- DOWNLOAD",
                                         "flex": 1,
                                         "size": "md",
                                         "margin": "md"
                                     },
                                 ]
                             },
                             {
                                 "type": "separator",
                                 "color": "#000000",
                             },
                             {
                                 "type": "box",
                                 "layout": "baseline",
                                 "margin": "md",
                                 "contents": [
                                     {
                                         "type": "text",
                                         "text": " ",
                                         "flex": 1,
                                         "size": "md",
                                         "margin": "md",
                                     },
                                     {
                                         "type": "text",
                                         "text": "| Command's |",
                                         "size": "md",
                                         "margin": "md",
                                         "flex": 3,
                                         "weight": "bold"
                                     }
                                 ]
                             },
                             {
                                 "type": "separator",
                                 "color": "#000000",
                             },
                             {
                                 "type": "box",
                                 "layout": "baseline",
                                 "margin": "md",
                                 "contents": [
                                     {
                                         "type": "text",
                                         "text": 'youtube <type> <url>',
                                         "flex": 0,
                                         "size": "md",
                                         "margin": "md",
                                     },
                                 ]
                             },
                             {
                                 "type": "separator",
                                 "color": "#000000",
                             }
                         ]
                     },
                     "footer": {
                         "type": "box",
                         "layout": "vertical",
                         "spacing": "sm",
                         "contents": [
                             {
                                 "type": "button",
                                 "style": "link",
                                 "height": "sm",
                                 "action": {
                                     "type": "uri",
                                     "label": "Example",
                                     "uri": "{}youtube%20search%20j.fla".format(wait['ttt'])
                                 }                                                   
                             },
                             {
                                 "type": "spacer",
                                 "size": "sm",
                             }
                         ],
                         "flex": 0
                     }
                 }
             }
         ]
     }
    h = sendCarousel(to,data)
    return h
def imagegoogle(to,wait,pesan):
    a = image_search(gonebot.adityasplittext(pesan))
    b = random.choice([a[:10],a[10:20],a[20:30],a[30:40],a[40:50],a[50:60],a[60:70],a[70:80]])
    a = b
    ret_ = []
    gimagesa(a,ret_)
    k = len(ret_)//10
    for aa in range(k+1):
        data = {"messages": [{"type": "flex","altText": "google image","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
        h = sendCarousel(to,data)
    return h
def image_search(query):
    images = gonebot.adityarequestweb('https://api.eater.pw/googleimg/{}'.format(query))
    return images['result']
def anunanu(to,s,wait,j=''):
    try:
        if j == '':
            data = {"messages": [{"type": "image","originalContentUrl": s,"previewImageUrl": s,"sentBy":{"label":"</> Noob Coder","iconUrl":"https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),"linkUrl":"line://nv/profilePopup/mid=u0b401cfefcc3b77c02abcc5816204aa2"}}]}
        else:
            data = {"messages": [{"type": "image","originalContentUrl": s,"previewImageUrl": s,"animated":True,"extension":"gif","sentBy":{"label":"</> Noob Coder","iconUrl":"https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),"linkUrl":"line://nv/profilePopup/mid=u0b401cfefcc3b77c02abcc5816204aa2"}}]}
        sendCarousel(to,data)
    except Exception as e:
        print(e)
def anuanu(to,s,wait,j=''):
    try:
        if j == '':
            data = {"messages": [{"type": "video","originalContentUrl": s,"previewImageUrl": s}]}
        else:
            data = {"messages": [{"type": "video","originalContentUrl": s,"previewImageUrl": s}]}
        sendCarousel(to,data)
    except Exception as e:
        print(e)
#====================================================================================
def restartBot():
    os.system("clear")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def load():
    global stickers
    global stickers1
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
    with open("sticker1.json","r") as fp:
        stickers1 = json.load(fp)        
def backupData():
    try:
        backup = wait
        f = codecs.open('basic.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers1
        f = codecs.open('sticker1.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers2
        f = codecs.open('sticker2.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        print(error)
        return False
#====================================================================================
def kntl(to,hehe):
    data = {"messages": [{"type": "text","text": hehe,"sentBy":{"label":"</> Noob Coder","iconUrl":"https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),"linkUrl":"line://nv/profilePopup/mid=u0b401cfefcc3b77c02abcc5816204aa2"}}]}
    sendCarousel(to,data)
#====================================================================================
def command(text):
    pesan = text.lower()
    return pesan
#=====================================================================

#=====================================================================
def entod_in(to, mid):
    try:
        gonebot.kickoutFromGroup(to, [mid])
        gonebot.findAndAddContactsByMid(mid)
        gonebot.inviteIntoGroup(to, [mid])
        gonebot.cancelGroupInvitation(to,[mid])
    except Exception as e:
        print(e)
def removeCmd(pesan, text):
	rmv = len(pesan)
	return text[rmv:]
#=====================================================================
def google_url_shorten(url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAzrJV41pMMDFUVPU0wRLtxlbEU-UkHMcI'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    return resp['id'].replace("https://","")
def cytmp4(url):
    import pafy
    vid = pafy.new(url,basic=False)
    result = vid.streams[-1]
    return result.url
def cytmp3(url):
    import pafy
    vid = pafy.new(url,basic=False)
    result = vid.audiostreams[-1]
    return result.url
#=====================================================================
def sendMessageCustom(to, text, icon , name):
    RhyN = {
        'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    gonebot.sendMessage(to, text, contentMetadata=RhyN)
#=====================================================================
def YoutubeTempat(wait,to,meta,dfghj,links,linkss):
    return {"messages": [{"type": "flex","altText": "Youtube","contents": {"type": "bubble","header": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "Youtube","weight": "bold","color": "#aaaaaa","size": "sm"}]},"hero": {"type": "image","url": meta['thumbnail'],"size": "full","aspectRatio": "20:13","aspectMode": "fit","action": {"type": "uri","uri": dfghj}},"body": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Title","color": "#aaaaaa","size": "sm","flex": 1},{"type": "text","text": "{}".format(meta['title']),"color": "#262423","wrap": True,"size": "sm","flex": 5}]}]}]},"footer": {"type": "box","layout": "horizontal","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Send Video","uri": "line://app/1602687308-GXq4Vvk9?type=video&ocu={}&piu={}".format(links,meta['thumbnail'])}},{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Send Audio","uri": "line://app/1602687308-GXq4Vvk9?type=audio&link={}".format(linkss)}}],"flex": 0}}}]}
def sendCarousel(to,col):
    col = json.dumps(col)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1632242027-drK8Q1KZ', xyzz)
    token = gonebot.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=col, headers=headers)
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1632242027-drK8Q1KZ', xyzz)
    token = gonebot.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1632242027-drK8Q1KZ', xyzz)
    token = gonebot.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendflex(to, data):
    n1 = LiffChatContext(to)
    n2 = LiffContext(chat=n1)
    view = LiffViewRequest('1632242027-drK8Q1KZ', n2)
    token = gonebot.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
#=====================================================================
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            gonebot.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def listgroup(to,wait,msg):
    try:
        gid = gonebot.getGroupIdsJoined()
        sd = gonebot.getGroups(gid)
        ret = " 「 Groups 」"
        no = 0
        total = len(gid)
        cd = "\n\n• Trigger: [<|>|-|num]\n> • < Remote Mention\n   •  groups (numb) tag <trigger>\n> • < Remote Kick\n   •  groups (numb) kick <trigger>\n> • < Leave Groups\n   •  leave groups <trigger>\n> • < Get QR\n   • qr groups <trigger>\n> • < Unsent\n   • groups (numb) unsent (numb)\n> • < Cek Member\n   •  groups (numb)\n   •  groups (numb) mem <trigger>"
        for G in sd:
            member = len(G.members)
            no += 1
            ret += "\n{}. {} | {}".format(no, G.name[0:20], member)
        ret += cd
        k = len(ret)//10000
        for aa in range(k+1):
            gonebot.sendMessage(to,'{}'.format(ret[aa*10000 : (aa+1)*10000]),msgid=msg.id)
    except Exception as e:
        print(e)
#=====================================================================
#=====================================================================
def sendMention(to, mid, firstmessage='', lastmessage=''):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        try:
            gonebot.sendMessage(to, text, {'MSG_SENDER_NAME': gonebot.getContact(mid).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + gonebot.getContact(mid).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as e:
            gonebot.sendMessage(to, text, {'MSG_SENDER_NAME': gonebot.getContact("u0b401cfefcc3b77c02abcc5816204aa2").displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + gonebot.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        print(error)
def tagdia(to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@RhyNRyuKenzo "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        try:
            gonebot.sendMessage(to, textx, {'AGENT_LINK': 'https://line.me/R/ti/p/2Axnr-JD8L','AGENT_ICON': "http://dl.profile.line-cdn.net/" + gonebot.getProfile().picturePath,'MSG_SENDER_NAME': gonebot.getContact(ps).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + gonebot.getContact(ps).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as e:
            try:
                gonebot.sendMessage(to, textx, {'AGENT_LINK': 'https://line.me/R/ti/p/2Axnr-JD8L','AGENT_ICON': "http://dl.profile.line-cdn.net/" + gonebot.getProfile().picturePath,'MSG_SENDER_NAME': gonebot.getContact(to).displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + gonebot.getContact(to).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
            except Exception as e:
                gonebot.sendMessage(to, textx, {'AGENT_LINK': 'https://line.me/R/ti/p/2Axnr-JD8L','AGENT_ICON': "http://dl.profile.line-cdn.net/" + gonebot.getProfile().picturePath,'MSG_SENDER_NAME': gonebot.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + gonebot.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#=====================================================================
#=====================================================================
def sendPhone(to, mid):
    a = gonebot.getContact(mid)
    contentMetadata = {
        'vCard': 'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:ANDROID 8.13.3 Android OS 4.4.4\r\nFN:\\'+a.displayName+'\nTEL;TYPE=mobile:'+a.statusMessage+'\r\nN:?;\\,\r\nEND:VCARD\r\n',
        'displayName': a.displayName
    }
    gonebot.sendMessage(to, '', contentMetadata, 13)
def sendStickers(to, sver, spkg, sid):
    contentMetadata = {
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    gonebot.sendMessage(to, '', contentMetadata, 7)
def sendSticker(to, mid, sver, spkg, sid):
    contentMetadata = {
        'MSG_SENDER_NAME': gonebot.getContact(mid).displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + gonebot.getContact(mid).pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    gonebot.sendMessage(to, '', contentMetadata, 7)
#=====================================================================
#=====================================================================
def autoresponuy(to,msg,wait):
    to = msg.to
    if msg.to not in wait["GROUP"]['AR']['AP']:
        return
    if msg.to in wait["GROUP"]['AR']['S']:
        gonebot.sendMessage(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
    if(wait["GROUP"]['AR']['P'][msg.to] in [""," ","\n",None]):
        return
    if '@!' not in wait["GROUP"]['AR']['P'][msg.to]:
        wait["GROUP"]['AR']['P'][msg.to] = '@!'+wait["GROUP"]['AR']['P'][msg.to]
    nama = gonebot.getGroup(msg.to).name
    sd = gonebot.waktunjir()
    gonebot.sendMention(msg.to,wait["GROUP"]['AR']['P'][msg.to].replace('greeting',sd).replace(';',nama),'',[msg._from]*wait["GROUP"]['AR']['P'][msg.to].count('@!'))
#=====================================================================
#=====================================================================
def restoreProfile():
    profile = gonebot.getProfile()
    profile.displayName = wait['myProfile']['displayName']
    profile.statusMessage = wait['myProfile']['statusMessage']
    if wait['myProfile']['videoProfile'] == None:
        path = gonebot.downloadFileURL('http://dl.profile.line-cdn.net/' + wait['myProfile']['pictureStatus'], 'path')
        gonebot.updateProfile(profile)
        gonebot.updateProfilePicture(path)
    else:
        gonebot.updateProfile(profile)
        pict = gonebot.downloadFileURL('http://dl.profile.line-cdn.net/' + wait['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = gonebot.downloadFileURL( 'http://dl.profile.line-cdn.net/' + wait['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = wait['myProfile']['coverId']
    gonebot.updateProfileCoverById(coverId)
def cloneProfile(mid):
    contact = gonebot.getContact(mid)
    if contact.videoProfile == None:
        gonebot.cloneContactProfile(mid)
    else:
        profile = gonebot.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        gonebot.updateProfile(profile)
        pict = gonebot.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = gonebot.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = gonebot.getProfileDetail(mid)['result']['objectId']
    gonebot.updateProfileCoverById(coverId)
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = gonebot.genOBSParams({'oid': gonebotMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = gonebot.server.postContent('{}/talk/vp/upload.nhn'.format(str(gonebot.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        gonebot.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
def changeProfileVideo(to):
    if wait['changeProfileVideo']['picture'] == None:
        return gonebot.sendMessage(to, "Photos not found")
    elif wait['changeProfileVideo']['video'] == None:
        return gonebot.sendMessage(to, "Videos not found")
    else:
        path = wait['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = gonebot.genOBSParams({'oid': gonebot.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = gonebot.server.postContent('{}/talk/vp/upload.nhn'.format(str(gonebot.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return gonebot.sendMessage(to, "Failed update Profile video")
        path_p = wait['changeProfileVideo']['picture']
        wait['changeProfileVideo']['status'] = False
        gonebot.updateProfilePicture(path_p, 'vp')
#=====================================================================
#=====================================================================
def NoteCreate(to,pesan,msg):
    h = []
    s = []
    if pesan == 'mentionnote':
        sakui = gonebot.getProfile()
        group = gonebot.getGroup(msg.to);nama = [contact.mid+'||//{}'.format(contact.displayName) for contact in group.members];nama.remove(sakui.mid+'||//{}'.format(sakui.displayName))
        data = nama
        k = len(data)//20
        for aa in range(k+1):
            nos = 0
            if aa == 0:dd = '╭「 Mention Note 」─';no=aa
            else:dd = '├「 Mention Note 」─';no=aa*20
            msgas = dd
            for i in data[aa*20 : (aa+1)*20]:
                no+=1
                if no == len(data):msgas+='\n╰{}. @'.format(no)
                else:msgas+='\n│{}. @'.format(no)
            msgas = msgas
            for i in data[aa*20 : (aa+1)*20]:
                gg = []
                dd = ''
                for ss in msgas:
                    if ss == '@':
                        dd += str(ss)
                        gg.append(dd.index('@'))
                        dd = dd.replace('@',' ')
                    else:
                        dd += str(ss)
                s.append({'type': "RECALL", 'start': gg[nos], 'end': gg[nos]+1, 'mid': str(i.split('||//')[0])})
                nos +=1
            h = gonebot.createPostGroup(msgas,msg.to,holdingTime=None,textMeta=s)
    else:
        pesan = pesan.replace('create note ','')
        if 'MENTION' in msg.contentMetadata.keys()!= None:
            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
            mentionees = mention['MENTIONEES']
            no = 0
            for mention in mentionees:
                ask = no
                nama = str(gonebot.getContact(mention["M"]).displayName)
                h.append(str(pesan.replace('create note @{}'.format(nama),'')))
                for b in h:
                    pesan = str(b)
                gg = []
                dd = ''
                for ss in pesan:
                    if ss == '@':
                        dd += str(ss)
                        gg.append(dd.index('@'))
                        dd = dd.replace('@',' ')
                    else:
                        dd += str(ss)
                s.append({'type': "RECALL", 'start': gg[no], 'end': gg[no]+1, 'mid': str(mention["M"])})
                no +=1
        h = gonebot.createPostGroup(pesan,to,holdingTime=None,textMeta=s)
def cekmentions(to,wait,pesan):
    try:
        if to in wait['ROM']:
            moneys = {}
            for a in wait['ROM'][to].items():
                moneys[a[0]] = [a[1]['msg.id'],a[1]['waktu'],a[1]['metadata'],a[1]['text']] if a[1] is not None else idnya
            sort = sorted(moneys)
            sort.reverse()
            sort = sort[0:]
            msgas = ' 「 Mention Me 」'
            if pesan == "mentionme":
                try:
                    if to in wait['ROM']:
                        h = []
                        no = 0
                        for m in sort:
                            h.append(m)
                            no+=1
                            msgas+= '\n{}. @!{}x'.format(no,len(moneys[m][0]))
                        gonebot.sendMention(to, msgas,' 「 Mention Me 」\n', h)
                except:
                    try:
                        msgas = 'Sorry @!In {} nothink get a mention'.format(gonebot.getGroup(to).name)
                        gonebot.sendMention(to, msgas,' 「 Mention Me 」\n', [gonebot.getProfile().mid])
                    except:
                        msgas = 'Sorry @!In Chat @!nothink get a mention'
                        gonebot.sendMention(to, msgas,' 「 Mention Me 」\n', [gonebot.getProfile().mid,to])
            if pesan.startswith('cek mention '):
                if len(pesan.split(" ")) == 3:
                    asd = sort[int(pesan.split(" ")[2])-1]
                    nol = 0
                    msgas+= '\n - @! {}x Mention'.format(len(moneys[asd][0]))
                    h = [asd]
                    try:
                        for kucing in range(len(moneys[asd][3])):
                            nol+=1
                            if moneys[asd][3][kucing].count('@!') >= 21:
                                if nol == 1:msgas+= '\n{}. {}\nJust Tagall Or Spam Tag > 20 Tag'.format(nol,humanize.naturaltime(datetime.fromtimestamp(moneys[asd][1][kucing]/1000)))
                                else:msgas+= '\n\n{}. {}\nJust Tagall Or Spam Tag > 20 Tag'.format(nol,humanize.naturaltime(datetime.fromtimestamp(moneys[asd][1][kucing]/1000)))
                            else:
                                for hhh in eval(moneys[asd][2][kucing]['MENTION'])["MENTIONEES"]:
                                    h.append(hhh['M'])
                                if nol == 1:msgas+= '\n{}. {}\n{}\nline://nv/chatMsg?chatId={}&messageId={}\n'.format(nol,humanize.naturaltime(datetime.fromtimestamp(moneys[asd][1][kucing]/1000)),moneys[asd][3][kucing],to,moneys[asd][0][kucing])
                                else:msgas+= '\n\n{}. {}\n{}\nline://nv/chatMsg?chatId={}&messageId={}\n'.format(nol,humanize.naturaltime(datetime.fromtimestamp(moneys[asd][1][kucing]/1000)),moneys[asd][3][kucing],to,moneys[asd][0][kucing])
                        dd = len(msgas.split('@!'))
                        k = dd//20
                        no=0
                        for a in range(k+1):
                            gg = ''
                            for b in msgas.split('@!')[a*20 : (a+1)*20]:
                                no+=1
                                if a == 0:
                                    if no == len(msgas.split('@!')):gg+= b
                                    else:gg+= b+'@!'
                                else:
                                    if no == a+20:gg+= b.replace('\n','')+'@!'
                                    else:
                                        if no == len(msgas.split('@!')):gg+= b
                                        else:gg+= b+'@!'
                            gonebot.sendMention(to, gg,' 「 Mention Me 」\n', h[a*20 : (a+1)*20])
                        del wait['ROM'][to][asd]
                    except Exception as e:gonebot.sendMessage(to,'ERROR {}'.format(e))
        else:
            try:
                msgas = 'Sorry @!In {} nothing get a mention'.format(gonebot.getGroup(to).name)
                gonebot.sendMention(to, msgas,' 「 Mention Me 」\n', [gonebot.getProfile().mid])
            except:
                msgas = 'Sorry @!In Chat @!nothing get a mention'
                gonebot.sendMention(to, msgas,' 「 Mention Me 」\n', [gonebot.getProfile().mid,to])
    except Exception as error:
        print(error)
def albumNamaGrup(to,wait,pesan):
    ha = gonebot.getGroupAlbum(to)
    if pesan == 'get album':
        a = [a['title'] for a in ha['result']['items']];c=[a['photoCount'] for a in ha['result']['items']]
        b = '╭「 Album Group 」'
        no=0
        for i in range(len(a)):
            no+=1
            if no == len(a):b+= '\n╰{}. {} | {}'.format(no,a[i],c[i])
            else:b+= '\n│{}. {} | {}'.format(no,a[i],c[i])
        gonebot.sendMessage(to,"{}".format(b))
    if pesan.startswith('get album '):
        try:
            a = pesan.split(' ')
            selection = MySplit(a[3],range(1,len(ha['result']['items'])+1))
            print(selection)
            for i in selection.parse():
                try:
                    b = random.randint(0,999)
                    s = gonebot.getImageGroupAlbum(to,ha['result']['items'][int(a[2])-1]['id'], ha['result']['items'][int(a[2])-1]['recentPhotos'][i-1]['oid'], returnAs='path', saveAs='{}.png'.format(b))
                    print(s)
                    gonebot.sendImage(to,'{}.png'.format(b))
                    os.remove('{}.png'.format(b))
                except:continue
        except Exception as e:print(e)
    else:
        a = pesan.split(' ')
        if len(a) == 5:
            wait["Images"]['anu']=ha['result']['items'][int(a[3])-1]['id']
            wait['ChangeGDP'] = True
            gonebot.sendMessage(to," 「 Album 」\nSend a Picture for add to album")
#=====================================================================
#=====================================================================
async def gonebotBot(op):
    global pb1
    global lgncall
    try:
        timeis = time.localtime()
        a = time.strftime('%H:%M:%S', timeis)
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoblock"] == True:
                gonebot.blockContact(op.param1)           
                gonebot.sendMessage(Notify,"มีคนแอดตัวนี้มา  contact ด้านล่างนี้เลย")
                gonebot.sendMessage(Notify, None, contentMetadata={'mid': op.param1}, contentType=13)
        if op.type == 5:
            if wait["autoAdd"] == True:
              if op.param2 in gonebotMID:
                  return
              gonebot.sendMessage(Notify,"มีคนแอดตัวนี้มา  contact ด้านล่างนี้เลย")
              gonebot.sendMessage(Notify, None, contentMetadata={'mid': op.param1}, contentType=13)
              gonebot.findAndAddContactsByMid(op.param1)
              gonebot.sendMessage(op.param1,"{}".format(tagadd["add"]))
              msgSticker = settings["messageSticker"]["listSticker"]["add"]
              if msgSticker != None:
                  sid = msgSticker["STKID"]
                  spkg = msgSticker["STKPKGID"]
                  sver = msgSticker["STKVER"]
                  sendSticker(op.param1, sver, spkg, sid)
              print ("[ 5 ] AUTO ADD")
         
#=====================================================================
        if op.type == 13:
            if gonebot.getProfile().mid in op.param3:
                if settings["autoLeave"] == True:
                    gonebot.acceptGroupInvitation(op.param1)
                    ginfo = gonebot.getGroup(op.param1)
                    gonebot.leaveGroup(op.param1)
  #              else:
   #                 gonebot.acceptGroupInvitation(op.param1)
    #                ginfo = gonebot.getGroup(op.param1)
#=====================================================================
#        if op.type == 13:
 #           if gonebot.getProfile().mid in op.param3:
   #             if wait["autoJoin"] == True:
    #                G = gonebot.getCompactGroup(op.param1)
     #               if len(G.members) <= wait["Members"]:
      #                  gonebot.acceptGroupInvitation(op.param1)
       #                 gonebot.leaveGroup(op.param1)
        #            else:
         #               gonebot.acceptGroupInvitation(op.param1)
#            if op.param2 in wait["owner"]:
 #               gonebot.acceptGroupInvitation(op.param1)
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                try:
                    group = gonebot.getGroup(op.param1)
                    group.preventedJoinByTicket = True
                    gonebot.updateGroup(group)
                    gonebot.kickoutFromGroup(op.param1,[op.param2])
                    group.preventedJoinByTicket = True
                    gonebot.updateGroup(group)
                except Exception as e:
                    group = gonebot.getGroup(op.param1)
                    group.preventedJoinByTicket = True
                    gonebot.kickoutFromGroup(op.param1,[op.param2])
                    gonebot.updateGroup(group)
#=====================================================================
        if op.type == 15:
          if settings["Leave"] == True:
            if op.param2 in gonebotMID:
                return
            ginfo = gonebot.getGroup(op.param1)
            contact = gonebot.getContact(op.param2)
            name = contact.displayName
            pp = contact.pictureStatus
            s = name + " " + tagadd["lv"]
            data = {
                "type": "flex",
                "altText": "มีคนออกกลุ่ม",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "body": {
                            "backgroundColor": '#6600CC'
                        },
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "{}".format(s),
                                "wrap": True,
                                "color": "#FFFFFF",
                                "gravity": "center",
                                "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
            data = {
                "type": "flex",
                "altText": "มีคนออกกลุ่ม",
                "contents": {
                    "type": "bubble",
                    "hero": {
                         "type":"image",
                         "url": "https://profile.line-scdn.net/" + str(pp),
                         "size":"full",
                         "action": {
                             "type": "uri",
                             "uri": "http://line.me/ti/p/~kiebotsiri"
                         }
                    },
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 15:
          if settings["lv"] == True:
              ginfo = gonebot.getGroup(op.param1)
              msg = settings["messageSticker"]["listSticker"]["lv"]
              if msg != None:
                  contact = gonebot.getContact(gonebotMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)  
        if op.type == 17:
          if settings["Welcome"] == True:
            if op.param2 in gonebotMID:
                return
            g = gonebot.getGroup(op.param1)
            contact = gonebot.getContact(op.param2)
            gname = g.name
            name = contact.displayName
            pp = contact.pictureStatus
            s = "〖 Group Welcome 〗\n"
            s += "\n• ชื่อกลุ่ม : {}".format(gname)
            s += "\n• ชื่อคนเข้ากลุ่ม : {}\n\n".format(name)
            s += tagadd["wctext"]
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "body": {
                            "backgroundColor": '#6600CC'
                        },
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "{}".format(s),
                                "wrap": True,
                                "color": "#FFFFFF",
                                "align": "center",
                                "gravity": "center",
                                "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    "hero": {
                         "type":"image",
                         "url": "https://profile.line-scdn.net/" + str(pp),
                         "size":"full",
                         "action": {
                             "type": "uri",
                             "uri": "http://line.me/ti/p/~kiebotsiri"
                         }
                    },
                }
            }
            sendTemplate(op.param1, data)

        if op.type == 17:
          if settings["Wc"] == True:
            if op.param2 in gonebotMID:
                return
            ginfo = gonebot.getGroup(op.param1)
            contact = gonebot.getContact(op.param2)
            cover = gonebot.getProfileCoverURL(op.param2)
            names = contact.displayName
            status = contact.statusMessage
            pp = contact.pictureStatus
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    'styles': {
                        "body": {
                            "backgroundColor": '#6600CC'
                        },
                     },
                     "hero": {
                         "type":"image",
                         "url": cover,
                         "size":"full",
                         "aspectRatio":"20:13",
                         "aspectMode":"cover"
                     },
                     "body": {
                         "type": "box",
                         "layout": "vertical",
                         "contents": [
                             {
                                 "type": "image",
                                 "url": "https://profile.line-scdn.net/" + str(pp),
                                 "size": "lg"
                             },
                             {
                                 "type":"text",
                                 "text":" "
                             },
                             {
                                 "type":"text",
                                 "text":"{}".format(names),
                                 "size":"xl",
                                 "weight":"bold",
                                 "color":"#FFFFFF",
                                 "align":"center"
                             },
                             {
                                 "type": "text",
                                 "text": status,
                                 "wrap": True,
                                 "align": "center",
                                 "gravity": "center",
                                 "color": "#FFFFFF",
                                 "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["wcsti2"] == True:
              ginfo = gonebot.getGroup(op.param1)
              msg = settings["messageSticker"]["listSticker"]["wc"]
              if msg != None:
                  contact = gonebot.getContact(gonebotMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)

        if op.type in [25, 26]:
            if op.type == 25: print ("[ 25 ] SEND MESSAGE")
            else: print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            isValid = True
            pesan = command(text)
            if isValid != False:
                if msg.toType == 0 and sender != gonebotMID: to = sender
                else: to = receiver
                if msg._from not in gonebotMID:
                  if wait["selfbot"] == True:
                    if msg._from in wait["blacklist"]:
                        gonebot.sendMention(to, "คุณติดดำผมอยู่นะครับ @! :)","",[msg._from])
                        gonebot.kickoutFromGroup(msg.to, [msg._from])
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    if settings["tag"] == True:
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if gonebotMID in mention["M"]:                      	
                                contact = gonebot.getContact(sender)
                                LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                                LINKVIDEO = "https://os.line.naver.jp/os/p/" + sender + "/vp"
                                data = {
                                    "type": "flex",
                                    "altText": "{} Send Flex".format(gonebot.getProfile().displayName),
                                    "contents": {
                                        "type": "bubble",
                                            'styles': {
                                                "header": {
                                                    "backgroundColor": '#ff00ff'
                                                },
                                                "body": {
                                                    "backgroundColor": '#99FFFF'
                                                },
                                                "footer": {
                                                    "backgroundColor": '#99FFFF'
                                                },
                                            },
                                        "header": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "{}".format(contact.displayName),
                                                    "weight": "bold",
                                                    "color": "#9900FF",
                                                    "size": "sm"
                                                }
                                            ]
                                        },
                                        "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                            "size": "full",
                                            "aspectRatio": "1:1",
                                            "aspectMode": "fit",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://nv/profilePopup/mid=u432466aa8e06c4f084820af51812abe1"
                                            }
                                        },
                                        "body": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "margin": "lg",
                                                    "spacing": "sm",
                                                    "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                {
                                                                    "type": "text",
                                                                    "text": "Name :",
                                                                    "color": "#9900FF",
                                                                    "size": "sm",
                                                                    "flex": 0
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": "{}".format(contact.displayName),
                                                                    "color": "#9900FF",
                                                                    "size": "sm",
                                                                    "flex": 1
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                {
                                                                   "type": "text",
                                                                    "text": "Status :",
                                                                    "color": "#9900FF",
                                                                    "size": "sm",
                                                                    "flex": 0
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": "{}".format(contact.statusMessage),
                                                                    "color": "#9900FF",
                                                                    "wrap": True,
                                                                    "size": "sm",
                                                                    "flex": 1
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "button",
                                                    "style": "link",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "☣ɢᴏɴᴇʙᴏᴛʟɪɴᴇ☣",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=video&ocu={}&piu={}".format(LINKVIDEO,LINKFOTO)
                                                    }                                                   
                                                },
                                                {
                                                    "type": "spacer",
                                                    "size": "sm",
                                                }
                                            ],
                                            "flex": 0
                                        }
                                    }
                                }
                                sendTemplate(to, data)
#==============================================================
                if msg.contentType == 0 and sender not in gonebotMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if settings["tagsticker"] == True:
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if gonebotMID in mention["M"]:
                                    #  contact = gonebot.getContact(gonebotMID)
                                   #   a = contact.displayName
                                      msg = settings["messageSticker"]["listSticker"]["tag"]
                                      if msg != None:
                                          contact = gonebot.getContact(gonebotMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendflex(to, data)
                                      else:
                                          contact = gonebot.getContact(gonebotMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+'ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendflex(to, data)

                if 'MENTION' in msg.contentMetadata.keys() != None:
                    if temptag["stealtag"] == True:
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if gonebotMID in mention["M"]:                       
                                contact = gonebot.getContact(sender)
                                start = time.time()
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)   
                                a = "วันที่"+ datetime.strftime(timeNow,'%d-%m-%Y')+"🇹🇭เวลา"+ datetime.strftime(timeNow,'%H:%M:%S')+"\n"
                                textnya = temptag["pesanya"]
                                LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                                LINKVIDEO = "https://os.line.naver.jp/os/p/" + sender + "/vp"
                                data = {
                                    "type": "flex",
                                    "altText": "มีผู้กล่าวถึงคุณ",
                                    "contents": {
                                        "type": "bubble",
                                            'styles': {
                                                "header": {
                                                    "backgroundColor": '#000000'
                                                },
                                                "body": {
                                                    "backgroundColor": '#000000'
                                                },
                                                "footer": {
                                                    "backgroundColor": '#000000'
                                                },
                                            },
                                        "footer":{
                                          "layout":"baseline","contents":[
                                    {
                                        "size":"xl",
                                        "url":"https://vishanu.co/wp-content/uploads/2018/02/flag-round-250.png","type":"icon"
                                    },
                                    {
                                        "text":"☣ɢᴏɴᴇʙᴏᴛʟɪɴᴇ☣",
                                        "size":"md",
                                        "wrap":True,
                                        "weight":"bold",
                                        "align":"center",
                                        "color":"#FFFFFF",
                                 "action":{
                                        "uri":"https://line.me/ti/p/~" + gonebot.profile.userid,
                                        "type":"uri"
                                 },
                                          "type":"text"
                                    }
                                  ],
                                  "type":"box"
                                  },
                                 "body":{
                                        "spacing":"md",
                                         "layout":"vertical",
                                         "contents":[
                                  {
                                        "layout":"horizontal",
                                         "contents":[
                                   {
                                        "flex":0,
                                         "size":"sm",
                                         "aspectRatio":"1:1",
                                         "url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                         "gravity":"bottom",
                                         "type":"image",
                                         "aspectMode":"cover"
                                     }
                                     ],
                                        "margin":"md",
                                        "type":"box"
                                   },
                                   {
                                      "color":"#111111",
                                      "type":"separator"
                                   },
                                   {
                                     "layout":"vertical",
                                      "contents":[
                                   {
                                        "text":"ตอบแทคอัตโนมัติ",
                                        "size":"md",
                                        "align":"center",
                                        "weight":"bold",
                                        "color":"#00FF33",
                                        "type":"text"
                                   },
                                   {
                                        "color":"#111111",
                                        "type":"separator"
                                   },
                                   {
                                        "type": "text",
                                        "text": "{}".format(textnya),
                                        "wrap": True,
                                        "align": "start",
                                        "color": "#00FF33",
                                        "gravity": "center",
                                        "size": "sm"
                                   },
                                   {
                                        "color":"#111111",
                                        "type":"separator"
                                   },
                                   {
                                        "text":"AutoRespon",
                                        "size":"xxs",
                                        "wrap":True,
                                        "align":"end",
                                        "weight":"bold",
                                        "color":"#00FF33",
                                        "type":"text"
                                   },
                                   {
                                        "color":"#111111",
                                        "type":"separator"
                                   },
                                   {
                                        "type": "text",
                                        "text": "{}".format(a),
                                        "wrap": True,
                                        "align": "start",
                                        "color": "#00FF33",
                                        "gravity": "center",
                                        "size": "sm"
                                        }
                                     ],
                                        "type":"box"
                                        }
                                      ],
                                     "type":"box"
                                        },
                                     "type":"bubble"
                                    }
                                }
                                sendTemplate(to, data) 
                                
#==========================================================         
        if op.type in [25, 26]:
            if op.type == 25: print ("[ 25 ] SEND MESSAGE")
            else: print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            isValid = True
            pesan = command(text)
            if isValid != False:
                if msg.toType == 0 and sender != gonebotMID: to = sender
                else: to = receiver
                if msg.contentType == 16:
                    if msg.toType in [2,1,0]:
                        try:
                            if settings["autolike"] == True:                            
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                if purl[1] not in wait['postId']:
                                    gonebot.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                            if settings["autolike"] == True:    
                                gonebot.createComment(purl[0], purl[1], settings["commentPost"])
                                wait['postId'].append(purl[1])
                            else:
                                pass
                        except Exception as e:
                            if settings["autolike"] == True:
                                purl = msg.contentMetadata['postEndUrl'].split('homeId=')[1].split('&postId=')
                                if purl[1] not in wait['postId']:
                                    gonebot.likePost(msg._from, purl[1], random.choice([1001,1002,1003,1004,1005]))
                            if settings["autolike"] == True:    
                                gonebot.createComment(msg._from, purl[1], settings["commentPost"])
                                wait['postId'].append(purl[1])
                            else:pass
                            
#=====================================================================
        if op.type == 25:
            print("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            isValid = True
            pesan = command(text)
            if isValid != False:
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    try:
                        if msg.to not in wait['Unsend']:
                            wait['Unsend'][msg.to] = {'B':[]}
                        if msg._from not in [gonebotMID]:
                            return
                        wait['Unsend'][msg.to]['B'].append(msg.id)
                    except:pass                            
                if msg.contentType == 0: 
                    for sticker in stickers:
                        try:
                            if text.lower() == sticker:
                                sid = stickers[sticker]["STKID"]
                                spkg = stickers[sticker]["STKPKGID"]
                                sver = stickers[sticker]["STKVER"]
                                a = gonebot.shop.getProduct(packageID=int(spkg), language='ID', country='ID')
                                if a.hasAnimation == True:data = {"type": "template","altText": "{} sent a sticker.".format(gonebot.getProfile().displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png".format(sid),"size": "full","action": {"type": "uri","uri": "http://line.me/ti/p/zMankMvx69"}}]}}
                                else:data = {"type": "template","altText": "{} sent a sticker.".format(gonebot.getProfile().displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png".format(sid),"size": "full","action": {"type": "uri","uri": "http://line.me/ti/p/zMankMvx69"}}]}}
                                sendTemplate(to,data)
                        except Exception as e:
                            print(e)                        
                    for pesan in pesan.split(" # "):
                        if pesan == "..":
                            a = gonebot.downloadFileURL("https://webtoon-phinf.pstatic.net/20181116_55/1542356619393SexJ2_JPEG/15423566193481392290.jpg?type=q90", saveAs="aa.jpg")
                            gonebot.sendImageWithURL(to, "http://domain.com/image/https://webtoon-phinf.pstatic.net/20181116_55/1542356619393SexJ2_JPEG/15423566193481392290.jpg?type=q90")
                        if pesan == '.':
                            gonebot.sendAudio(to, 'tmp/bacot.mp3')
                        if pesan.startswith('tes '):
                            k = InstagramScraper()
                            a = int(pesan.split(' ')[1])
                            results = k.profile_page_recent_posts('https://www.instagram.com/awkarin')
                            ret = []
                            for i in results:
                                ret.append(i['shortcode'])
                            try:
                                url = requests.get('https://www.instagram.com/p/{}'.format(ret[a]))
                                soup = BeautifulSoup(url.text, 'html.parser')
                                a = soup.find('body')
                                b = a.find('script')
                                c = b.text.strip().replace('window._sharedData =', '').replace(';', '')
                                d = json.loads(c)
                                e = d['entry_data']['PostPage'][0]['graphql']['shortcode_media']
                                for i in e:print(e)
                                a = e['video_duration']
                                print(a)
                                b = e['video_view_count']
                                print(b)
                            except Exception as e:print(e)

                        if pesan.startswith("เชค "):
                            if msg._from in [gonebotMID]:
                                mmid = msg.text.replace("เชค ","")
                                gonebot.sendContact(to, mmid)
                        if pesan.startswith("footer "):
                            khie = text.split(" ")
                            hey = text.replace(khie[0] + " ", "")
                            text = "{}".format(hey)
                            data = {
                                "type": "text",
                                "text": "{}".format(text),
                                "sentBy": {
                                    "label": "{}".format(gonebot.getContact(gonebotMID).displayName),
                                    "iconUrl": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),
                                    "linkUrl": "line://ti/p/~samurai-_-"
                                }
                            }
                            sendTemplate(to, data)  
                        if pesan == "ตั้งค่า":
                            ret = "โปรดพิมพ์คำสั่ง: \n\n"
                            ret += "  • เปิดบล็อค\n" 
                            ret += "  • ปิดบล็อค\n"
                            ret += "  • เปิดแอด\n" 
                            ret += "  • ปิดแอด\n"
                            ret += "  • ตั้งแอด [text]\n" 
                            ret += "  • เปิดไลค์\n"
                            ret += "  • ปิดไลค์\n"
                            ret += "  • เปิดกันรัน\n"  
                            ret += "  • ปิดกันรัน\n" 
                            ret += "  • เปิดคนออก\n"
                            ret += "  • ปิดคนออก\n"
                            ret += "  • เปิดต้อนรับ\n"
                            ret += "  • ปิดต้อนรับ\n"
                            ret += "  • เปิดต้อนรับ2\n"
                            ret += "  • ปิดต้อนรับ2\n"
                            ret += "  • เปิดติ๊กคนออก\n"  
                            ret += "  • ปิดติ๊กคนออก\n" 
                            ret += "  • เปิดติ๊กคนเข้า\n" 
                            ret += "  • ปิดติ๊กคนเข้า\n" 
                            ret += "  • เปิดแทค1\n"    
                            ret += "  • ปิดแทค1\n" 
                            ret += "  • เปิดแทค2\n" 
                            ret += "  • ปิดแทค2\n" 
                            ret += "  • เปิดแทค3\n" 
                            ret += "  • ปิดแทค3\n" 
                            ret += "  • เปิดติ้กใหญ่\n" 
                            ret += "  • ปิดติ้กใหญ่\n" 
                            ret += "  • ตั้งติ้กคนแทค\n"
                            ret += "  • ลบติ้กคนแทค\n"
                            ret += "  • เชคแทค\n"
                            ret += "  • ตั้งแทค [text]\n"
                            ret += "  • ตั้งต้อนรับ [text]\n"
                            ret += "  • ตั้งคนออก [text]\n"
                            ret += "  • ตั้งติ๊กคนแทค\n"
                            ret += "  • ลบติ๊กคนแทค\n"
                            ret += "  • ตั้งติ๊กคนเข้า\n"
                            ret += "  • ลบติ๊กคนเข้า\n"
                            ret += "  • ตั้งติ๊กคนออก\n"  
                            ret += "  • ลบติ๊กคนออก\n"
                            ret += "  • ตั้งติ๊กคนแอด\n"    
                            ret += "  • ลบติ๊กคนแอด\n"                                       
                            ret += "  • detectunsend on/off\n"                       
                            ret += "  • prankcall notif on/off\n"
                            ret += "  • groupcall notif on/off\n"                            
                            ret += "  • responcall\n"
                            ret += "  • responcall msg set [text]\n"
                            ret += "  • fcg msg set [text]\n"
                            ret += "  • vcg msg set [text]\n"
                            ret += "  • live msg set [text]\n"                            
                            hello = "{}".format(str(ret))
                            cu = gonebot.getProfileCoverURL(gonebotMID)
                            image = str(cu)                            
                            data = {
                                    "type": "flex",
                                    "altText": "☣ɢᴏɴᴇʙᴏᴛʟɪɴᴇ☣",
                                        "contents": {
                                        "styles": {
                                        "body": {
                                        "backgroundColor": "#F5F5F5"
                                        },
                                        "footer": {
                                          "backgroundColor": "#000000"
                                        }
                                        },
                                            "type": "bubble",
                                                "hero": {
                                                    "type": "image",
                                                    "url": image,
                                                    "size": "full",
                                                    "aspectRatio": "20:13",
                                                    "aspectMode": "cover",
                                                },
                                            "body": {
                                            "contents": [
                                              {
                                                "contents": [
                                                  {
                                                    "url": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),
                                                    "type": "image"
                                                  },
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "text": "การตั้งค่าเปิด/ปิด",
                                                    "size": "xl",
                                                    "align": "center",
                                                    "color": "#FF0000",
                                                    "wrap": True,
                                                    "weight": "bold",
                                                    "type": "text"
                                                  }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "contents": [
                                                      {
                                                        "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                        "type": "icon",
                                                        "size": "md"
                                                      },
                                                      {
                                                        "text":"{}".format(str(ret)),
                                                        "size": "sm",
                                                        "margin": "none",
                                                        "color": "#6F4E37",
                                                        "wrap": True,
                                                        "weight": "regular",
                                                        "type": "text"
                                                      }
                                                    ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                                  }
                                                ],          
                                                "type": "box",
                                                "layout": "vertical"
                                              }
                                            ],
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "vertical"
                                        },
                                        "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "สนใจเช่าบอท คลิก",
                                                    "uri": "https://line.me/ti/p/~kieloveselfbot"
                                                }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                            sendflex(to, data)  
#                            data = {
 #                               "type": "text",
  #                              "text": "{}".format(str(ret)),
   #                             "sentBy": {
    #                                "label": "{}".format(gonebot.getContact(gonebotMID).displayName),
     #                               "iconUrl": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),
      #                              "linkUrl": "line://ti/p/~samurai-_-"
       #                         }
        #                    }
         #                   sendTemplate(to, data)   
                        if pesan == "ลูกเล่น":
                            ret = "พิมพ์คำสั่ง: \n\n"
                            ret += "  • clone\n" 
                            ret += "  • backupprofile\n"  
                            ret += "  • ไลค์ @\n"  
                            ret += "  • แชร์โพส @\n"   
                            ret += "  • อัพโพส [text]\n"  
                            ret += "  • ลิสกลุ่ม\n"                  
                            hello = "{}".format(str(ret))
                            cu = gonebot.getProfileCoverURL(gonebotMID)
                            image = str(cu)                            
                            data = {
                                    "type": "flex",
                                    "altText": "☣ɢᴏɴᴇʙᴏᴛʟɪɴᴇ☣",
                                        "contents": {
                                        "styles": {
                                        "body": {
                                        "backgroundColor": "#F5F5F5"
                                        },
                                        "footer": {
                                          "backgroundColor": "#000000"
                                        }
                                        },
                                            "type": "bubble",
                                                "hero": {
                                                    "type": "image",
                                                    "url": image,
                                                    "size": "full",
                                                    "aspectRatio": "20:13",
                                                    "aspectMode": "cover",
                                                },
                                            "body": {
                                            "contents": [
                                              {
                                                "contents": [
                                                  {
                                                    "url": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),
                                                    "type": "image"
                                                  },
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "text": "ลูกเล่นต่างๆ",
                                                    "size": "xl",
                                                    "align": "center",
                                                    "color": "#FF0000",
                                                    "wrap": True,
                                                    "weight": "bold",
                                                    "type": "text"
                                                  }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "contents": [
                                                      {
                                                        "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                        "type": "icon",
                                                        "size": "md"
                                                      },
                                                      {
                                                        "text":"{}".format(str(ret)),
                                                        "size": "sm",
                                                        "margin": "none",
                                                        "color": "#6F4E37",
                                                        "wrap": True,
                                                        "weight": "regular",
                                                        "type": "text"
                                                      }
                                                    ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                                  }
                                                ],          
                                                "type": "box",
                                                "layout": "vertical"
                                              }
                                            ],
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "vertical"
                                        },
                                        "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "สนใจเช่าบอท คลิก",
                                                    "uri": "https://line.me/ti/p/~kieloveselfbot"
                                                }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                            sendflex(to, data)  

                        if pesan == "ใหม่":
                            ret = "พิมพ์คำสั่ง: \n\n"
                            ret += "  • ประกาศ2\n"
                            ret += "  • ตั้งรูปประกาศ\n"
                            ret += "  • ประกาศ2 [text]\n"
                            ret += "  • ตั้งติ้ก1 [text]\n"   
                            ret += "  • ตั้งติ้ก [text]\n"                       
                            ret += "  • อัพชื่อ [text]\n"
                            ret += "  • อัพตัส [text]\n"                            
                            ret += "  • google [text]\n"
                            ret += "  • ยูทูป [text]\n"
                            ret += "  • ออก [text]\n"
                            ret += "  • footer [text]\n"
                            ret += "  • ตั้งคอมเม้น [text]\n"
                            ret += "  • เชคคอมเม้น [text]\n"
                            ret += "  • เพิ่มล้อเลียน @\n" 
                            ret += "  • ลบล้อเลียน @\n"
                            ret += "  • ลบเพื่อน @\n"
                            ret += "  • ล้างเพื่อน\n"
                            hello = "{}".format(str(ret))
                            cu = gonebot.getProfileCoverURL(gonebotMID)
                            image = str(cu)                            
                            data = {
                                    "type": "flex",
                                    "altText": "☣ɢᴏɴᴇʙᴏᴛʟɪɴᴇ☣",
                                        "contents": {
                                        "styles": {
                                        "body": {
                                        "backgroundColor": "#F5F5F5"
                                        },
                                        "footer": {
                                          "backgroundColor": "#000000"
                                        }
                                        },
                                            "type": "bubble",
                                                "hero": {
                                                    "type": "image",
                                                    "url": image,
                                                    "size": "full",
                                                    "aspectRatio": "20:13",
                                                    "aspectMode": "cover",
                                                },
                                            "body": {
                                            "contents": [
                                              {
                                                "contents": [
                                                  {
                                                    "url": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),
                                                    "type": "image"
                                                  },
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "text": "อัพเดทใหม่",
                                                    "size": "xl",
                                                    "align": "center",
                                                    "color": "#FF0000",
                                                    "wrap": True,
                                                    "weight": "bold",
                                                    "type": "text"
                                                  }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "contents": [
                                                      {
                                                        "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                        "type": "icon",
                                                        "size": "md"
                                                      },
                                                      {
                                                        "text":"{}".format(str(ret)),
                                                        "size": "sm",
                                                        "margin": "none",
                                                        "color": "#6F4E37",
                                                        "wrap": True,
                                                        "weight": "regular",
                                                        "type": "text"
                                                      }
                                                    ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                                  }
                                                ],          
                                                "type": "box",
                                                "layout": "vertical"
                                              }
                                            ],
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "vertical"
                                        },
                                        "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "สนใจเช่าบอท คลิก",
                                                    "uri": "https://line.me/ti/p/~kieloveselfbot"
                                                }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                            sendflex(to, data) 
                        if pesan == "โปรไฟล์":
                            ret = "พิมคำสั่ง:\n\n"
                            ret += "  • ไอดีเรา\n"
                            ret += "  • ชื่อเรา\n"
                            ret += "  • ตัสเรา\n"
                            ret += "  • รูปเรา\n"
                            ret += "  • รูปวีดีโอเรา\n"
                            ret += "  • ปกเรา\n"
                            hello = "{}".format(str(ret))
                            cu = gonebot.getProfileCoverURL(gonebotMID)
                            image = str(cu)                            
                            data = {
                                    "type": "flex",
                                    "altText": "☣ɢᴏɴᴇʙᴏᴛʟɪɴᴇ☣",
                                        "contents": {
                                        "styles": {
                                        "body": {
                                        "backgroundColor": "#F5F5F5"
                                        },
                                        "footer": {
                                          "backgroundColor": "#000000"
                                        }
                                        },
                                            "type": "bubble",
                                                "hero": {
                                                    "type": "image",
                                                    "url": image,
                                                    "size": "full",
                                                    "aspectRatio": "20:13",
                                                    "aspectMode": "cover",
                                                },
                                            "body": {
                                            "contents": [
                                              {
                                                "contents": [
                                                  {
                                                    "url": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),
                                                    "type": "image"
                                                  },
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "text": "โปรไฟล์",
                                                    "size": "xl",
                                                    "align": "center",
                                                    "color": "#FF0000",
                                                    "wrap": True,
                                                    "weight": "bold",
                                                    "type": "text"
                                                  }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "contents": [
                                                      {
                                                        "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                        "type": "icon",
                                                        "size": "md"
                                                      },
                                                      {
                                                        "text":"{}".format(str(ret)),
                                                        "size": "sm",
                                                        "margin": "none",
                                                        "color": "#6F4E37",
                                                        "wrap": True,
                                                        "weight": "regular",
                                                        "type": "text"
                                                      }
                                                    ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                                  }
                                                ],          
                                                "type": "box",
                                                "layout": "vertical"
                                              }
                                            ],
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "vertical"
                                        },
                                        "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "สนใจเช่าบอท คลิก",
                                                    "uri": "https://line.me/ti/p/~kieloveselfbot"
                                                }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                            sendflex(to, data)                             
                        if pesan == "ป้องกัน":
                            ret = "พิมคำสั่ง:\n\n"
                            ret += "  • กันลิ้ง เปิด/ปิด\n"
                            ret += "  • กันเชิญ เปิด/ปิด\n"
                            ret += "  • กันเตะ เปิด/ปิด\n"
                            ret += "  • กันยก เปิด/ปิด\n"
                            ret += "  • cb [ล้างดำ]\n"
                            ret += "  • bc [เชคดำ]\n"
                            hello = "{}".format(str(ret))
                            cu = gonebot.getProfileCoverURL(gonebotMID)
                            image = str(cu)                            
                            data = {
                                    "type": "flex",
                                    "altText": "☣ɢᴏɴᴇʙᴏᴛʟɪɴᴇ☣",
                                        "contents": {
                                        "styles": {
                                        "body": {
                                        "backgroundColor": "#F5F5F5"
                                        },
                                        "footer": {
                                          "backgroundColor": "#000000"
                                        }
                                        },
                                            "type": "bubble",
                                                "hero": {
                                                    "type": "image",
                                                    "url": image,
                                                    "size": "full",
                                                    "aspectRatio": "20:13",
                                                    "aspectMode": "cover",
                                                },
                                            "body": {
                                            "contents": [
                                              {
                                                "contents": [
                                                  {
                                                    "url": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),
                                                    "type": "image"
                                                  },
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "text": "ตั้งค่าป้องกัน",
                                                    "size": "xl",
                                                    "align": "center",
                                                    "color": "#FF0000",
                                                    "wrap": True,
                                                    "weight": "bold",
                                                    "type": "text"
                                                  }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "contents": [
                                                      {
                                                        "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                        "type": "icon",
                                                        "size": "md"
                                                      },
                                                      {
                                                        "text":"{}".format(str(ret)),
                                                        "size": "sm",
                                                        "margin": "none",
                                                        "color": "#6F4E37",
                                                        "wrap": True,
                                                        "weight": "regular",
                                                        "type": "text"
                                                      }
                                                    ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                                  }
                                                ],          
                                                "type": "box",
                                                "layout": "vertical"
                                              }
                                            ],
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "vertical"
                                        },
                                        "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "สนใจเช่าบอท คลิก",
                                                    "uri": "https://line.me/ti/p/~kieloveselfbot"
                                                }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                            sendflex(to, data)                          
                        if pesan == "แปลภาษา":
                            ret = "พิมคำสั่ง: แปลภาษา\n\n"
                            ret += "  • อินโด:[text]\n"
                            ret += "  • อังกิด:[text]\n"
                            ret += "  • ญี่ปุ่น:[text]\n"
                            ret += "  • Korea:[rext]\n"
                            ret += "  • ไทย:[rext]\n"
                            ret += "  • Arab:[text]"
                            hello = "{}".format(str(ret))
                            cu = gonebot.getProfileCoverURL(gonebotMID)
                            image = str(cu)                            
                            data = {
                                    "type": "flex",
                                    "altText": "☣ɢᴏɴᴇʙᴏᴛʟɪɴᴇ☣",
                                        "contents": {
                                        "styles": {
                                        "body": {
                                        "backgroundColor": "#F5F5F5"
                                        },
                                        "footer": {
                                          "backgroundColor": "#000000"
                                        }
                                        },
                                            "type": "bubble",
                                                "hero": {
                                                    "type": "image",
                                                    "url": image,
                                                    "size": "full",
                                                    "aspectRatio": "20:13",
                                                    "aspectMode": "cover",
                                                },
                                            "body": {
                                            "contents": [
                                              {
                                                "contents": [
                                                  {
                                                    "url": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),
                                                    "type": "image"
                                                  },
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "text": "ชุดแปลภาษา",
                                                    "size": "xl",
                                                    "align": "center",
                                                    "color": "#FF0000",
                                                    "wrap": True,
                                                    "weight": "bold",
                                                    "type": "text"
                                                  }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "contents": [
                                                      {
                                                        "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                        "type": "icon",
                                                        "size": "md"
                                                      },
                                                      {
                                                        "text":"{}".format(str(ret)),
                                                        "size": "sm",
                                                        "margin": "none",
                                                        "color": "#6F4E37",
                                                        "wrap": True,
                                                        "weight": "regular",
                                                        "type": "text"
                                                      }
                                                    ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                                  }
                                                ],          
                                                "type": "box",
                                                "layout": "vertical"
                                              }
                                            ],
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "vertical"
                                        },
                                        "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "สนใจเช่าบอท คลิก",
                                                    "uri": "https://line.me/ti/p/~kieloveselfbot"
                                                }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                            sendflex(to, data) 
                        if pesan == "!me":
                        	gonebot.reissueUserTicket()
                        	contact = gonebot.getContact(gonebotMID)
                        	RatXfo = random.choice(["#000000"])
                        	RatXfo2 = random.choice(["#FFFFFF"])
                        	data = {
                                    "type":"flex",
                                    "altText": "Me",
                                    "contents":
                                    {
                                    "type":"bubble",
                                    "footer":
                                    {
                                        "type":"box",
                                        "layout":"horizontal",
                                        "contents":
                                        [
                                    {
                                        "color":RatXfo2,
                                        "size":"xs",
                                        "wrap":True,
                                        "action":
                                            {
                                                "type":"uri",
                                                "uri":"line://app/1602687308-GXq4Vvk9?type=profile"
                                            },
                                                "type":"text",
                                                "text":"Me",
                                                "align":"center",
                                                "weight":"bold"
                                            },
                                        {
                                            "type":"separator",
                                            "color":RatXfo2
                                            },
                                        {
                                            "color":RatXfo2,
                                            "size":"xs",
                                            "wrap":True,
                                            "action":
                                                {
                                                    "type":"uri",
                                                    "uri":"http://line.me/ti/p/" + gonebot.getUserTicket().id
                                                },
                                                    "type":"text",
                                                    "text":"ADD ME",
                                                    "align":"center",
                                                    "weight":"bold"
                                                }
                                            ]
                                        },
                                            "styles":
                                            {
                                            "footer":
                                            {
                                            "backgroundColor":RatXfo
                                            },
                                            "body":
                                            {
                                            "backgroundColor":"#FAEBD7"
                                            }
                                        },
                                            "body":
                                            {
                                                "type":"box",
                                                "contents":
                                                [
                                            {
                                                "type":"box",
                                                "contents":
                                            [
                                        {
                                            "type":"separator",
                                            "color":RatXfo
                                        },
                                        {
                                            "aspectMode":"cover",
                                            "gravity":"bottom",
                                            "aspectRatio":"1:1",
                                            "size":"sm",
                                            "type":"image",
                                            "url":"https://media.tenor.com/images/74a2b4b0fc38bc87c81f68b0bb24572d/tenor.gif"
                                        },
                                        {
                                            "type":"separator",
                                            "color":RatXfo
                                        },
                                        {
                                            "type":"image",
                                            "aspectMode":"cover",
                                            "aspectRatio":"1:1",
                                            "size":"sm",
                                            "url":"https://66.media.tumblr.com/aa99c2153d464c2fa0ff2ec55e889a56/tumblr_o00uzj1ma91u1bxt2o1_500.gif"
                                            },
                                            {
                                                "type":"separator",
                                                "color":RatXfo
                                            },
                                            {
                                                "type":"image",
                                                "aspectMode":"cover",
                                                "aspectRatio":"1:1",
                                                "size":"sm",
                                                "url":"https://media.tenor.com/images/91d0b45d95b27080c4d0d1175d586533/tenor.gif"
                                            },
                                            {
                                                "type":"separator",
                                                "color":RatXfo
                                            },
                                            {
                                                "type":"image",
                                                "aspectMode":"cover",
                                                "aspectRatio":"1:1",
                                                "size":"sm",
                                                "url":"https://i.redd.it/u9ugbmg7t4h11.gif"
                                            },
                                            {
                                                "type":"separator",
                                                "color":RatXfo
                                            }
                                            ],
                                                "layout":"vertical",
                                                "spacing":"none",
                                                "flex":1
                                            },
                                            {
                                                "type":"separator",
                                                "color":RatXfo
                                            },
                                            {
                                                "type":"box",
                                                "contents":
                                            [
                                        {
                                            "type":"separator",
                                            "color":RatXfo
                                            },
                                        {
                                            "color":"#413877",
                                            "size":"md",
                                            "wrap":True,
                                            "type":"text",
                                            "text":"ชื่อ🔗",
                                            "weight":"bold"
                                            },
                                        {
                                            "type":"separator",
                                            "color":RatXfo
                                            },
                                        {
                                            "color":"#413877",
                                            "size":"md",
                                            "wrap":True,
                                            "type":"text",
                                            "text":"{}".format(contact.displayName),
                                            "weight":"bold"
                                            },
                                        {
                                            "type":"separator",
                                            "color":RatXfo
                                            },
                                        {
                                            "color":RatXfo,
                                            "size":"xs",
                                            "wrap":True,
                                            "type":"text",
                                            "text":"สถานะโปรไฟล์:",
                                            "weight":"bold"
                                            },
                                        {
                                            "type":"text",
                                            "text":"{}".format(contact.statusMessage),                                            
                                            "size":"xxs",
                                            "wrap":True,
                                            "color":"#e00f0f"
                                        }
                                    ],
                                        "layout":"vertical",
                                        "flex":2
                                        }
                                    ],
                                        "layout":"horizontal",
                                        "spacing":"md"
                                    },
                                        "hero":
                                    {
                                        "aspectMode":"cover",
                                        "margin":"xxl",
                                        "aspectRatio":"20:13",
                                        "size":"full",
                                        "type":"image",
                                        "url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                                    }
                                 }
                            }
                        	sendflex(to, data)    
                        if pesan == "คท":
                        	contact = gonebot.getContact(gonebotMID)
                        	cu = gonebot.getProfileCoverURL(gonebotMID)
                        	image = str(cu)                            
                        	data = {
                                    "type": "flex",
                                    "altText": "<ME>",
                                        "contents": {
                                        "styles": {
                                        "body": {
                                        "backgroundColor": "#F5F5F5"
                                        },
                                        "footer": {
                                          "backgroundColor": "#000000"
                                        }
                                        },
                                            "type": "bubble",
                                                "hero": {
                                                    "type": "image",
                                                    "url": image,
                                                    "size": "full",
                                                    "aspectRatio": "20:13",
                                                    "aspectMode": "cover",
                                                },
                                            "body": {
                                            "contents": [
                                              {
                                                "contents": [
                                                  {
                                                    "url": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),
                                                    "type": "image"
                                                  },
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "text": "ชื่อ:{}".format(contact.displayName),
                                                    "size": "xl",
                                                    "align": "center",
                                                    "color": "#FF0000",
                                                    "wrap": True,
                                                    "weight": "bold",
                                                    "type": "text"
                                                  }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                              },
                                              {
                                                "type": "separator",
                                                "color": "#DC143C"
                                              },
                                              {
                                                "contents": [
                                                  {
                                                    "contents": [
                                                      {
                                                        "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                        "type": "icon",
                                                        "size": "md"
                                                      },
                                                      {
                                                        "text":"สเตตัส:\n{}".format(contact.statusMessage),
                                                        "size": "sm",
                                                        "margin": "none",
                                                        "color": "#6F4E37",
                                                        "wrap": True,
                                                        "weight": "regular",
                                                        "type": "text"
                                                      }
                                                    ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                                  }
                                                ],          
                                                "type": "box",
                                                "layout": "vertical"
                                              }
                                            ],
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "vertical"
                                        },
                                        "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "สนใจเช่าบอท คลิก",
                                                    "uri": "https://line.me/ti/p/~kieloveselfbot"
                                                }
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ],
                                    "flex": 0
                                    }
                                }
                            }
                        	sendflex(to, data)                                                                                                                                                                                       
                        if pesan.startswith("wallpaper "):
                            query = removeCmd("wallpaper ",text)
                            cond = query.split("|")
                            search = str(cond[0])
                            result = requests.get("https://api.eater.pw/wallp/{}".format(str(search)))
                            data = result.text
                            data = json.loads(data)
                            print(data)
                            if data["result"] != []:
                                ret_ = []
                                for i in data["result"]:
                                    url = i['link']
                                    ret_.append({"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "HD WALLPAPER","weight": "bold"}]},"hero": {"type": "image","url": url,"size": "full","aspectRatio": "2:1","aspectMode": "fit"},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "TAP ON THE BUTTON","weight": "bold","size":"md","margin":"md"},{"type":"separator","color":"#000000"}]},"footer": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "horizontal","contents": [{"type": "button","flex": 2,"style": "primary","color": "#FF2B00","height": "sm","action": {"type": "uri","label": "LINK","uri": "{}{}".format(wait['ttt'],url)}}, {"flex": 3,"type": "button","margin": "sm","style": "primary","color": "#097500","height": "sm","action": {"type": "uri","label": "SEND IMAGE","uri": "line://app/1602687308-GXq4Vvk9?type=image&img="+url}}]}]}})
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {"messages": [{"type": "flex","altText": "Noob sent a flex.","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                                    sendCarousel(to,data)
                        if pesan.startswith("google "):
                            spl = re.split("google ",msg.text,flags=re.IGNORECASE)
                            if spl[0] == "":
                                if spl[1] != "":
                                    try:
                                        gonebot.sendMessage(to,"Searching ..")
                                        resp = BeautifulSoup(requests.get("https://www.google.co.th/search",params={"q":spl[1],"gl":"th"}).content,"html.parser")
                                        text = "Google:\n\n"
                                        for el in resp.findAll("h3",attrs={"class":"r"}):
                                            try:
                                                tmp = el.a["class"]
                                                continue
                                            except:
                                                pass
                                            try:
                                                if el.a["href"].startswith("/search?q="):
                                                    continue
                                            except:
                                                continue
                                            text += el.a.text+"\n"
                                            text += str(el.a["href"][7:]).split("&sa=U")[0]+"\n\n"
                                        text = text[:-2]
                                        gonebot.sendMessage(to,str(text))
                                    except Exception as e:
                                        print(e)                                    
                        if(pesan.startswith('ดึงวีดีโอ ') or pesan.startswith('youtube audio ') or pesan.startswith('youtube info ')):
                            try:
                                texts = gonebot.adityasplittext(pesan,'s').split("|")
                                print(texts)
                                a = gonebot.adityarequestweb("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q="+texts[0]+"&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8")
                                if len(texts) == 1:dfghj = gonebot.adityasplittext(msg.text,'s').replace('https://youtu.be/','').replace('youtube video ','').replace('youtube audio ','').replace('youtube info ','').replace('https://www.youtube.com/watch?v=','');meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                if len(texts) >= 2:dfghj = a["items"][int(texts[1])-1]["id"]['videoId'];dfghj = 'https://www.youtube.com/watch?v='+a["items"][int(texts[1])-1]["id"]['videoId'];meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                if pesan.startswith('youtube info '):
                                    if(len(texts) == 1):dfghj = gonebot.adityasplittext(msg.text,'s').replace('youtu.be/','youtube.com/watch?v=').replace('info ','');meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                    if(len(texts) == 2):dfghj = 'https://www.youtube.com/watch?v='+a["items"][int(texts[1])-1]["id"]['videoId'];meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                    if meta['description'] == '':hjk = ''
                                    else:hjk = '\nDescription:\n{}'.format(meta['description'])
                                    t = ' 「 Youtube 」\nTitle: {}{}\n\nLike: {}  Dislike: {}\nViewers: {}'.format(meta['title'],hjk,humanize.intcomma(meta['like_count']),humanize.intcomma(meta['dislike_count']),humanize.intcomma(meta['view_count']))
                                    kntl(to,t)
                                    s = meta['thumbnail']
                                    anunanu(to,s,wait)
                                if(pesan.startswith("youtube video ") or pesan.startswith("youtube audio ")):
                                    kk = random.randint(0,999)
                                    if(len(texts) == 1):dfghj = gonebot.adityasplittext(msg.text,'s').replace('youtu.be/','youtube.com/watch?v=').replace('audio ','').replace('video ','');meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                    if len(texts) == 2:dfghj = 'https://www.youtube.com/watch?v='+a["items"][int(texts[1])-1]["id"]['videoId'];print(dfghj);meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                    hhhh = ' 「 Youtube 」\nJudul: {}\nDuration: {}\nEx: {}\nStatus: Waiting... For Upload'.format(meta['title'],meta['duration'],'1270*720')
                                    kntl(to,hhhh)
                                    links = cytmp4(dfghj);links = 'https://'+google_url_shorten(links)
                                    linkss = cytmp3(dfghj);linkss = 'https://'+google_url_shorten(linkss)
                                    sendCarousel(to,YoutubeTempat(wait,to,meta,dfghj,links,linkss))
                                    if(pesan.startswith("youtube video ")):sendCarousel(to,{"messages": [{"type": "video","altText": "YouTube","originalContentUrl": links,"previewImageUrl": meta['thumbnail']}]})
                                    if(pesan.startswith("youtube audio ")):sendCarousel(to,{"messages": [{"type": "audio","altText": "YouTube","originalContentUrl": linkss,"duration": meta['duration']*1000}]})
                            except Exception as e:gonebot.sendMessage(to, str(e))
                        if pesan.startswith("ยูทูป "):
                            a = gonebot.adityarequestweb("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q="+gonebot.adityasplittext(pesan,'s')+"&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8")
                            if a["items"] != []:
                                no = 0
                                ret_ = []
                                for music in a["items"]:
                                    no += 1
                                    ret_.append({"type": "bubble","header": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "Youtube","weight": "bold","color": "#aaaaaa","size": "sm"}]},"hero": {"type": "image","url": 'https://i.ytimg.com/vi/{}/maxresdefault.jpg'.format(music['id']['videoId']),"size": "full","aspectRatio": "20:13","aspectMode": "fit","action": {"type": "uri","uri": 'https://www.youtube.com/watch?v=' +music['id']['videoId']}},"body": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Title","color": "#aaaaaa","size": "sm","flex": 1},{"type": "text","text": "{}".format(music['snippet']['title']),"color": "#262423","wrap": True,"size": "sm","flex": 5}]}]}]},"footer": {"type": "box","layout": "horizontal","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Page","uri": 'https://www.youtube.com/watch?v=' +music['id']['videoId']}},{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Video","uri": "{}youtube%20video%20https://www.youtube.com/watch?v={}".format(wait['ttt'],music['id']['videoId'])}},{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Audio","uri": "{}youtube%20audio%20https://www.youtube.com/watch?v={}".format(wait['ttt'],music['id']['videoId'])}},],}})
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {"messages": [{"type": "flex","altText": "Noob sent a template.","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                                    sendCarousel(to,data)
                            else:
                                gonebot.sendMessage(to,"Type: Search Youtube Video\nStatus: "+str(self.adityasplittext(msg.text,'s'))+" not found")

                        if pesan == "backupprofile":
                            try:
                                restoreProfile()
                                gonebot.sendContact(to,gonebotMID)
                                gonebot.sendMessage(to, "Profile has been Backup")
                            except Exception as e:
                                gonebot.sendMessage(to, "[ ERROR ]")
                                gonebot.sendMessage(to, str(e))

                        elif msg.text.lower().startswith("ตั้งต้อนรับ "):
                              text_ = removeCmd("ตั้งต้อนรับ", text)
                              try:
                                  tagadd["wctext"] = text_
                                  sa = "「 ตั้งต้อนรับ 」\nคือ : " + text_
                                  data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "gonebot Botline", "iconUrl": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u266f0d1211f905b2ca386024d9d4e165"}}
                                  sendTemplate(to,data)
                              except:
                                  gonebot.sendMessags(to,"Done. >_<")
                        elif msg.text.lower().startswith("ตั้งคนออก "):
                                    text_ = removeCmd("ตั้งคนออก", text)
                                    try:
                                        tagadd["lv"] = text_
                                        gonebot.sendMessage(to,"「 ตั้งคนออก 」\nคือ : " + text_)
                                    except:
                                        gonebot.sendMessage(to,"สำเเร็จแล้ว")
                        elif msg.text.lower().startswith("ตั้งแอด "):
                              text_ = removeCmd("ตั้งแอด", text)
                              try:
                                  tagadd["add"] = text_
                                  sa = "「 ตั้งแอด 」\nคือ : " + text_
                                  data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "gonebot Botline", "iconUrl": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=u266f0d1211f905b2ca386024d9d4e165"}}
                                  sendTemplate(to,data)
                              except:
                                  gonebot.sendMessags(to,"Done. >_<")                                
                        if text.lower() == "เชค":
                            add = tagadd["add"]
                            wc = tagadd["wctext"]
                            lv = tagadd["lv"]
                            gonebot.generateReplyMessage(msg.id)
                            gonebot.sendReplyMessage(msg.id, to, "ข้อความแอด :\n"+str(add)+"\n\nข้อความต้อนรับ :\n"+str(wc)+"\n\nข้อความคนออก :\n"+str(lv))

                        if text.lower() == "เปิดต้อนรับ":
                            settings["Welcome"] = True
                            gonebot.sendMessage(to, "เปิดแล้ว ...")
                        if text.lower() == "ปิดต้อนรับ":
                            settings["Welcome"] = False
                            gonebot.sendMessage(to,"ปิดแล้ว ...")
                        if text.lower() == "เปิดต้อนรับ2":
                            settings["Wc"] = True
                            gonebot.sendMessage(to,"เปิดแล้ว ....")
                        if text.lower() == "ปิดต้อนรับ2":
                            settings["Wc"] = False
                            gonebot.sendMessage(to,"ปิดแล้ว ....")
                        if text.lower() == "เปิดคนออก":
                            settings["Leave"] = True
                            gonebot.sendMessage(to,"เปิดแล้ว ....")
                        if text.lower() == "ปิดคนออก":
                            settings["Leave"] = False
                            gonebot.sendMessage(to,"ปิดแล้ว ...")
                        if text.lower() == "เปิดติ๊กคนออก":
                            settings["lv"] = True
                            gonebot.sendMessage(to,"เปิดแล้ว ...")
                        if text.lower() == "ปิดติ๊กคนออก":
                            settings["lv"] = False
                            gonebot.sendMessage(to,"ปิดแล้ว ...")
                        if text.lower() == "เปิดติ๊กคนเข้า":
                            settings["wcsti2"] = True
                            gonebot.sendMessage(to,"เปิดแล้ว ...")
                        if text.lower() == "ปิดติ๊กคนเข้า":
                            settings["wcsti2"] = False
                            gonebot.sendMessage(to,"ปิดแล้ว ....")
                        if text.lower() == "เปิดแทค3":
                            settings["tagsticker"] = True
                            gonebot.sendMessage(to,"เปิดแล้ว ...")
                        if text.lower() == "ปิดแทค3":
                            settings["tagsticker"] = False
                            gonebot.sendMessage(to,"ปิดแล้ว .....")                            

                        elif 'กันลิ้ง' in msg.text:
                           if msg._from in gonebotMID:
                              spl = msg.text.replace('กันลิ้ง ','')
                              if spl == 'เปิด':
                                  if msg.to in protectqr:
                                       msgs = "ป้องกัน URL ถูกเปิดใช้งานอยู่แล้ว"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = gonebot.getGroup(msg.to)
                                       msgs = "ป้องกัน URL เปิดใช้งาน\nIn Group : " +str(ginfo.name)
                                  gonebot.sendMessage(msg.to, "「STATUS PROTECT URL」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = gonebot.getGroup(msg.to)
                                         msgs = "ป้องกัน URL ปิดใช้งาน\nIn Group : " +str(ginfo.name)
                                    else:
                                         msgs = "ป้องกัน URL ปิดใช้งานอยู่แล้ว"
                                    gonebot.sendMessage(msg.to, "「STATUS PROTECT URL」\n" + msgs)  

                        elif 'กันเตะ' in msg.text:
                           if msg._from in gonebotMID:
                              spl = msg.text.replace('กันเตะ ','')
                              if spl == 'เปิด':
                                  if msg.to in protectkick:
                                       msgs = "ป้องกันเตะ ถูกเปิดใช้งานอยู่แล้ว"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = gonebot.getGroup(msg.to)
                                       msgs = "ป้องกันเตะ เปิดใช้งาน\nIn Group : " +str(ginfo.name)
                                  gonebot.sendMessage(msg.to, "「STATUS PROTECT URL」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectkick:
                                         protectkick.append(msg.to)
                                         ginfo = gonebot.getGroup(msg.to)
                                         msgs = "ป้องกันเตะ ปิดใช้งาน\nIn Group : " +str(ginfo.name)
                                    else:
                                         msgs = "ป้องกันเตะ ปิดใช้งานอยู่แล้ว"
                                    gonebot.sendMessage(msg.to, "「STATUS PROTECT URL」\n" + msgs)                                      

                        elif 'กันเชิญ' in msg.text:
                           if msg._from in gonebotMID:
                              spl = msg.text.replace('กันเชิญ ','')
                              if spl == 'เปิด':
                                  if msg.to in protectinvite:
                                       msgs = "ป้องกันสมาชิกเชิญ ถูกเปิดใช้งานอยู่แล้ว"
                                  else:
                                       protectinvite[msg.to] = True
                                       f=codecs.open('protectinvite.json','w','utf-8')
                                       json.dump(protectinvite, f, sort_keys=True, indent=4,ensure_ascii=False)	
                                       ginfo = gonebot.getGroup(msg.to)
                                       msgs = "ป้องกันสมาชิกเชิญ เปิดใช้งาน\nIn Group : " +str(ginfo.name)
                                  gonebot.sendMessage(msg.to, "「STATUS PROTECT URL」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectinvite:
                                         del protectinvite[msg.to]
                                         f=codecs.open('protectinvite.json','w','utf-8')
                                         json.dump(protectinvite, f, sort_keys=True, indent=4,ensure_ascii=False)	
                                         ginfo = gonebot.getGroup(msg.to)
                                         msgs = "ป้องกันสมาชิกเชิญ ปิดใช้งาน\nIn Group : " +str(ginfo.name)
                                    else:
                                         msgs = "ป้องกันสมาชิกเชิญ ปิดใช้งานอยู่แล้ว"
                                    gonebot.sendMessage(msg.to, "「STATUS PROTECT URL」\n" + msgs) 

                        elif 'กันยก' in msg.text:
                           if msg._from in gonebotMID:
                              spl = msg.text.replace('กันยก ','')
                              if spl == 'เปิด':
                                  if msg.to in protectcancel:
                                       msgs = "ป้องกันยกเชิญ ถูกเปิดใช้งานอยู่แล้ว"
                                  else:
                                       protectcancel[msg.to] = True
                                       f=codecs.open('protectcancel.json','w','utf-8')
                                       json.dump(protectcancel, f, sort_keys=True, indent=4,ensure_ascii=False)	
                                       ginfo = gonebot.getGroup(msg.to)
                                       msgs = "ป้องกันยกเชิญ เปิดใช้งาน\nIn Group : " +str(ginfo.name)
                                  gonebot.sendMessage(msg.to, "「STATUS PROTECT URL」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in protectcancel:
                                         del protectcancel[msg.to]
                                         f=codecs.open('protectcancel.json','w','utf-8')
                                         json.dump(protectcancel, f, sort_keys=True, indent=4,ensure_ascii=False)	
                                         ginfo = gonebot.getGroup(msg.to)
                                         msgs = "ป้องกันยกเชิญ ปิดใช้งาน\nIn Group : " +str(ginfo.name)
                                    else:
                                         msgs = "ป้องกันยกเชิญ ปิดใช้งานอยู่แล้ว"
                                    gonebot.sendMessage(msg.to, "「STATUS PROTECT URL」\n" + msgs)                                                                                                       

                        if pesan.startswith("ดำ "):
                          if wait["selfbot"] == True:
                            if msg._from in gonebotMID:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           gonebot.sendMessage(msg.to,"เพิ่มบัญชีดำสำเร็จแล้ว")
                                       except:
                                           pass

                        if pesan.startswith("ขาว "):
                          if wait["selfbot"] == True:
                            if msg._from in gonebotMID:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           gonebot.sendMessage(msg.to,"ลบบัญชีดำสำเร็จแล้ว")
                                       except:
                                           pass                                

                        if pesan == "bc":
                          if wait["selfbot"] == True:
                            if msg._from in gonebotMID:
                              if wait["blacklist"] == {}:
                                    gonebot.sendMessage(msg.to,"ไม่พบคนติดดำ")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = gonebot.getContact(i)
                                        gonebot.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        if pesan == "cb":
                          if wait["selfbot"] == True:
                            if msg._from in gonebotMID:
                              wait["blacklist"] = {}
                              ragets = gonebot.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              gonebot.sendMessage(to,"ล้างดำหมดแล้ว " +mc)  

                        if pesan == 'ล้างห้อง':
                            if msg.toType != 2: return gonebot.sendMessage(to, 'ไม่สามารถเตะสมาชิกทั้งหมดได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
                            group = gonebot.getGroup(to)
                            if not group.members:
                                return gonebot.sendMessage(to, 'ไม่สามารถเตะสมาชิกทั้งหมดได้\nไม่มีคนไห้เตะ')
                            for member in group.members:
                                if member.mid == myMid:
                                    continue
                                try:
                                    gonebot.kickoutFromGroup(to, [member.mid])
                                except TalkException as talk_error:
                                    return gonebot.sendMessage(to, 'ไม่สามารถเตะสมาชิกทั้งหมดได้เนื่องจาก `%s`' % talk_error.reason)
                                time.sleep(0.8)
                            gonebot.sendMessage(to, 'เตะสมาชิกทั้งหมด, จำนวน %i คน' % len(group.members))  

                        if pesan == "บัญชีกลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in gonebotMID:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +gonebot.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +gonebot.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +gonebot.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +gonebot.getGroup(group).name + "\n"                                    
                                gonebot.sendMessage(msg.to,"❧ รายการกลุ่มที่ป้องกัน\n\n❦ ป้องกันสมาชิกเปิดลิ้ง :\n"+ma+"\n❧ ป้องกันสมาชิกเตะ :\n"+mb+"\n❧ ป้องกันคนเข้า :\n"+md+"\n❧ ป้องกันสมาชิกยกเชิญ:\n"+mc+"\n❧ ป้องกันสมาชิกเชิญ :\n"+me+"\nจำนวน「%s」กลุ่มที่เปิดป้องกัน" %(str(len(protectqr)+len(protectkick)+len(protectcancel)+len(protectinvite))))
                                                                  
                        if pesan == 'square':
                            a = gonebot.getJoinedSquares()
                            squares = a.squares
                            txt2 = '「 Squares 」\n'
                            for s in range(len(squares)):
                                txt2 += "\n"+str(s+1)+". "+str(squares[s].name)
                            txt2 += "\n\nTotal {} Squares.".format(str(len(squares)))
                            txt2 += "\n\nUsage : Square [num]"
                            gonebot.generateReplyMessage(msg.id)
                            gonebot.sendReplyMessage(msg.id, to,str(txt2))
                        if pesan.startswith("square"):
                            number = removeCmd("square",text)
                            squares = gonebot.getJoinedSquares().squares
                            ret_ = "「 Square 」\n"
                            try:
                                square = squares[int(number)-1]
                                path = "http://dl.profile.line-cdn.net/" + square.profileImageObsHash
                                ret_ += "\n1. Name : {}".format(str(square.name))
                                ret_ += "\n2. Description: {}".format(str(square.desc))
                                ret_ += "\n3. ID Square : {}".format(str(square.mid))
                                ret_ += "\n4. Link : {}".format(str(square.invitationURL))
                                gonebot.sendImageWithURL(to, path)
                                gonebot.generateReplyMessage(msg.id)
                                gonebot.sendReplyMessage(msg.id, to,str(ret_))
                            except Exception as error:
                                gonebot.sendMessage(to, str(error))
                        if pesan.startswith("clone "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    cloneProfile(ls)
                                    gonebot.sendContact(to,gonebotMID)
                                    gonebot.sendMention(to, "「 Clone 」\nType: Clone Profile\nTarget: @!\nStatus: Succes..","",[ls])
                        if pesan == "คำสั่ง":
                            sender_profile = gonebot.getContact(sender)
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
                                        "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "contents": [
                                                    {
                                                    "url": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),
                                                    "type": "image"
                                                },
                                            ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#DC143C"
                                            },
                                            {                                                
                                                "contents": [
                                                    {
                                                    "text": "คำสั่งพื้นฐาน1",
                                                    "size": "xl",
                                                    "align": "center",
                                                    "color": "#FF0000",
                                                    'flex': 1,
                                                    "weight": "bold",
                                                    "type": "text"
                                                    }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#DC143C"
                                            },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " ใหม่",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                            },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " ตั้งต่า",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                            },
                                            {                                            
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " แปลภาษา",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " เชคค่า",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                            },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " ป้องกัน",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " เปิดอ่าน",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                            },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " อ่าน",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " ปิดอ่าน",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                            },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Bc [text]",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "☣ɢᴏɴᴇʙᴏᴛʟɪɴᴇ☣",
                                                        "align": "center",
                                                        "color": "#FFFFFF",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "md",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
                                        "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "contents": [
                                                    {
                                                    "url": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),
                                                    "type": "image"
                                                },
                                            ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#DC143C"
                                            },
                                            {                                                
                                                "contents": [
                                                    {
                                                    "text": "คำสั่งพื้นฐาน2",
                                                    "size": "xl",
                                                    "align": "center",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "bold",
                                                    "type": "text"
                                                    }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#DC143C"
                                            },
                                            {    
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " ดำ [@]",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " ขาว [@]",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Friend",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"                                                
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " .ประกาศ [text]",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Memegen",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " เตะ [@]",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Gcall",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " คท",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " !me",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "☣ɢᴏɴᴇʙᴏᴛʟɪɴᴇ☣",
                                                        "align": "center",
                                                        "color": "#FFFFFF",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "md",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
                                        "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "contents": [
                                                    {
                                                    "url": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),
                                                    "type": "image"
                                                },
                                            ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#DC143C"
                                            },
                                            {                                                
                                                "contents": [
                                                    {
                                                    "text": "คำสั่งพื้นฐาน3",
                                                    "size": "xl",
                                                    "align": "center",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "bold",
                                                    "type": "text"
                                                    }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#DC143C"
                                            },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " แทค",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " เปิดลิ้ง",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " ปิดลิ้ง",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " ขอลิ้ง",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Spam",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " บอกหมุด: [text]",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": "  ปักหมุด",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " ลบหมุด",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://media1.tenor.com/images/0350558b3ce1c2a9818b6ae1a6200a77/tenor.gif",
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " ลิสหมุด",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#a30404",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "☣ɢᴏɴᴇʙᴏᴛʟɪɴᴇ☣",
                                                        "align": "center",
                                                        "color": "#FF33FF",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                            data = {
                                "type": "flex",
                                "altText": "☣ɢᴏɴᴇʙᴏᴛʟɪɴᴇ☣",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)                                                                                                                                                                                                                                                    
               #         if pesan == 'ออน':
                #            eltime = time.time() - mulai
                 #           bot = "" +waktu(eltime)
                  #          a = (bot)
                   #         data = {
                    #            "type": "text",
                     #           "text": "{}".format(a),
                      #          "sentBy": {
                       #             "label": "{}".format(gonebot.getContact(gonebotMID).displayName),
                        #            "iconUrl": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),
                         #           "linkUrl": "line://nv/profilePopup/mid=u432466aa8e06c4f084820af51812abe1"
                          #      }
                           # }
                            #sendTemplate(to,data) 
                #        if pesan == "speed":
                #            start = time.time()
                #            gonebot.sendMessage("u8356f84ac11d24464fb797227e573c20", "Testing..")
                #            elapsed_time = time.time() - start
                #            took = time.time() - start
                #            a = " 「 Speed 」\nType: Speed♪\n - Took : %.3fms♪\n - Taken: %.10f♪" % (took,elapsed_time)
                #            data = {
                #                "type": "text",
                #                "text": "{}".format(a),
                #                "sentBy": {
                #                    "label": "{}".format(gonebot.getContact(gonebotMID).displayName),
                #                    "iconUrl": "https://obs.line-scdn.net/{}".format(gonebot.getContact(gonebotMID).pictureStatus),
                #                    "linkUrl": "line://nv/profilePopup/mid=u432466aa8e06c4f084820af51812abe1"
                #                }
                #            }
                #            sendTemplate(to,data)                            
                        if pesan.startswith(".ประกาศ ") and sender == gonebotMID:
                            txt = removeCmd(".ประกาศ", text)
                            groups = gonebot.getGroupIdsJoined()
                            for group in groups:
                                gonebot.sendMessage(group, "「 อนุญาติแอดมินกลุ่ม 」\n\n{}".format(str(txt)))
                                time.sleep(1)
                            gonebot.sendMessage(to, "ทำการเสร็จเรียบร้อยแล้วจำนวน {} กลุ่ม".format(str(len(groups))))                                                                        
                        if pesan == 'me':
                            a = gonebot.getProfile().displayName
                            c = 'line://nv/profilePopup/mid=u432466aa8e06c4f084820af51812abe1'
                            b = "https://obs.line-scdn.net/" + gonebot.getContact(gonebotMID).pictureStatus
                            d = gonebotMID
                            e = gonebot.getProfile().statusMessage
                            contact = gonebot.getContact(gonebotMID)
                            if contact.videoProfile == None:
                                link = "https://obs.line-scdn.net/" + gonebot.getContact(gonebotMID).pictureStatus
                            else:
                                link = "line://app/1606644641-DAwvRm5p?type=video&ocu=https://obs.line-scdn.net/" + gonebot.getContact(gonebotMID).pictureStatus + '/vp&piu=https://obs.line-scdn.net/' + gonebot.getContact(gonebotMID).pictureStatus
                            profilesku(a,b,c,d,e,link,wait,to)
                        if pesan == "gcall" or pesan.startswith('gcall '):
                            if msg._from in [gonebotMID]:
                                if len(pesan.split(' ')) <= 1:
                                    a = "╭───「 Gcall 」─\n│    | Command |  \n│Get Gcall\n│  Key: GetGroupCall\n│Spam Gcall\n│  Key: Gcall [num|@]\n│NotifCall\n│  Key: GroupCall Notif:[on|off]\n│  Key: ResponCall:[on|off]\n"
                                    a += "│PrankCall\n│  Key: PrankCall notif:[on|off]\n│PrankCall Message\n│  Key: fcg msg set [enter|text]\n│  Key: vcg msg set [enter|text]\n│  Key: live msg set [enter|text]\n╰──────"
                                    kntl(to, str(a))
                                else:
                                    if msg.toType == 2:
                                        j = int(pesan.split(' ')[1])
                                        a = [gonebot.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                        if 'MENTION' in msg.contentMetadata.keys()!=None:
                                            key = eval(msg.contentMetadata["MENTION"])
                                            key1 = key["MENTIONEES"][0]["M"]
                                            nama = [key1]
                                            b = [gonebot.call.inviteIntoGroupCall(to,nama,mediaType=2) for b in a];gonebot.sendMention(to, '「 Gcall 」\n@!has been spammed with {} amount of call♪'.format(j),'',[key1])
                                        else:
                                            group = gonebot.getGroup(to);nama = [contact.mid for contact in group.members];b = [gonebot.call.inviteIntoGroupCall(to,nama,mediaType=2) for b in a]
                                            gonebot.sendMention(to, ' 「 Gcall 」\n@!spammed with {} amount of call to all member♪'.format(j),'',[msg._from])
                                    if msg.toType == 1:
                                        j = int(pesan.split(' ')[1])
                                        a = [gonebot.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                        group = gonebot.getRoom(to);nama = [contact.mid for contact in group.contacts];b = [gonebot.call.inviteIntoGroupCall(to,nama,mediaType=2) for b in a]
                                        gonebot.sendMention(to, ' 「 Gcall 」\n@!spammed with {} amount of call to all member♪'.format(j),'',[msg._from])
#=====================================================================
#=====================================================================
                        if pesan == "prankcall notif:on" and msg.toType == 2:
                            if to not in wait["notificationCallPrank"]:
                                wait["notificationCallPrank"].append(to)
                                gonebot.sendMessage(to, " 「 Group Call 」\nNotification Prank Call set to on♪")
                            else:
                                gonebot.sendMessage(to, " 「 Group Call 」\nNotification Prank Call already on♪")
                        if pesan == "prankcall notif:off" and msg.toType == 2:
                            if to in wait["notificationCallPrank"]:
                                wait["notificationCallPrank"].remove(to)
                                gonebot.sendMessage(to, " 「 Group Call 」\nNotification Prank Call set to off♪")
                            else:
                                gonebot.sendMessage(to, " 「 Group Call 」\nNotification Prank Call set already off♪")
                        if pesan == "groupcall notif:on" and msg.toType == 2:
                            if to not in wait["notificationCall"]:
                                wait["notificationCall"].append(to)
                                gonebot.sendMessage(to, " 「 Group Call 」\nNotification GroupCall set to on♪")
                            else:
                                gonebot.sendMessage(to, " 「 Group Call 」\nNotification GroupCall already on♪")
                        if pesan == "groupcall notif:off" and msg.toType == 2:
                            if to in wait["notificationCall"]:
                                wait["notificationCall"].remove(to)
                                gonebot.sendMessage(to, " 「 Group Call 」\nNotification GroupCall set to off♪")
                            else:
                                gonebot.sendMessage(to, " 「 Group Call 」\nNotification GroupCall already off♪")
                        if pesan == "responcall:off" and sender == gonebotMID:
                            if wait["responCall"] == True:
                                wait["responCall"] = False
                                gonebot.sendMessage(to, " 「 Respon Call 」\nNotification Receive Call set to off♪")
                            else:
                                gonebot.sendMessage(to, " 「 Respon Call 」\nNotification Receive Call already off♪")
                        if pesan == "responcall:on" and sender == gonebotMID:
                            if wait["responCall"] == False:
                                wait["responCall"] = True
                                gonebot.sendMessage(to, " 「 Respon Call 」\nNotification Receive Call set to on♪")
                            else:
                                gonebot.sendMessage(to, " 「 Respon Call 」\nNotification Receive Call set to on♪")
                        if pesan.startswith("responcall msg set"):
                            if len(pesan.split("\n")) >= 2:
                                wait["pesanCall"] = pesan.replace(pesan.split("\n")[0]+"\n","").replace('|','@!')
                                gonebot.sendMessage(to," 「 ResponCall 」\nRespon Receive Call message has been set to:\n" + wait["pesanCall"])
                        if pesan.startswith("fcg msg set") and msg.toType == 2:
                            if len(pesan.split("\n")) >= 2:
                                wait["prankCall"]["audio"] = pesan.replace(pesan.split("\n")[0]+"\n","").replace('|','@!')
                                gonebot.sendMessage(to," 「 PrankCall 」\nPrankCall Audio message has been set to:\n" + wait["prankCall"]["audio"])
                        if pesan.startswith("vcg msg set") and msg.toType == 2:
                            if len(pesan.split("\n")) >= 2:
                                wait["prankCall"]["video"] = pesan.replace(pesan.split("\n")[0]+"\n","").replace('|','@!')
                                gonebot.sendMessage(to," 「 PrankCall 」\nPrankCall Video message has been set to:\n" + wait["prankCall"]["video"])
                        if pesan.startswith("live msg set") and msg.toType == 2:
                            if len(pesan.split("\n")) >= 2:
                                wait["prankCall"]["live"] = pesan.replace(pesan.split("\n")[0]+"\n","").replace('|','@!')
                                gonebot.sendMessage(to," 「 PrankCall 」\nPrankCall Live message has been set to:\n" + wait["prankCall"]["live"])
#=====================================================================
                        if pesan == "เปิดแทค1":
                            if settings["tag"] == True:
                                msgs=" 「 Steal Tag 」\nเปิดตอบกลับคนแทค1"
                            else:
                                msgs=" 「 Steal Tag 」\nเปิดตอบกลับคนแทค1"
                                settings["tag"] = True
                            gonebot.sendMessage(to, msgs)
                        if pesan == "ปิดแทค1":
                            if settings["tag"] == False:
                                msgs=" 「 Steal Tag 」\nปิดตอบกลับคนแทค1"
                            else:
                                msgs=" 「 Steal Tag 」\nปิดตอบกลับคนแทค1"
                                settings["tag"] = False
                            gonebot.sendMessage(to, msgs)
  
                        if pesan == "เปิดกันรัน":
                            if settings["autoLeave"] == True:
                                msgs=" 「 Steal leave 」\nเปิดกินห้องรันเรียบร้อยแล้ว"
                            else:
                                msgs=" 「 Steal leave 」\nเปิดกินห้องรันเรียบร้อยแล้ว"
                                settings["autoLeave"] = True
                            gonebot.sendMessage(to, msgs)
                        if pesan == "ปิดกันรัน":
                            if settings["autoLeave"] == False:
                                msgs=" 「 Steal leave 」\nปิดกินห้องรันเรียบร้อยแล้ว"
                            else:
                                msgs=" 「 Steal leave 」\nปิดกินห้องรันเรียบร้อยแล้ว"
                                settings["autoLeave"] = False
                            gonebot.sendMessage(to, msgs)  
                        if pesan == "เปิดแทค2":
                            if temptag["stealtag"] == True:
                                msgs=" 「 Steal Tag 」\nเปิดตอบกลับคนแทค2"
                            else:
                                msgs=" 「 Steal Tag 」\nเปิดตอบกลับคนแทค2"
                                temptag["stealtag"] = True
                            gonebot.sendMessage(to, msgs)
                        if pesan == "ปิดแทค2":
                            if temptag["stealtag"] == False:
                                msgs=" 「 Steal Tag 」\nปิดตอบกลับคนแทค2"
                            else:
                                msgs=" 「 Steal Tag 」\nปิดตอบกลับคนแทค2"
                                temptag["stealtag"] = False
                            gonebot.sendMessage(to, msgs)    
                        if pesan == 'เปิดไลค์':
                            if msg._from in [gonebotMID]:
                                settings['autolike'] = True
                                gonebot.sendMessage(to, "เปิดออโต้ไลค์แล้ว")                            
                        if pesan == 'ปิดไลค์':
                            if msg._from in [gonebotMID]:
                                settings['autolike'] = False
                                gonebot.sendMessage(to, "ปิดออโต้ไลค์แล้ว") 
                        if pesan == 'เปิดบล็อค':
                            if msg._from in [gonebotMID]:
                                settings['autoblock'] = True
                                gonebot.sendMessage(to, "เปิดออโต้บล็อคแล้ว")                            
                        if pesan == 'ปิดบล็อค':
                            if msg._from in [gonebotMID]:
                                settings['autoblock'] = False
                                gonebot.sendMessage(to, "ปิดออโต้บล็อคแล้ว")  
                        if pesan == 'เปิดแอด':
                            if msg._from in [gonebotMID]:
                                wait['autoAdd'] = True
                                gonebot.sendMessage(to, "เปิดออโต้แอดแล้ว")                            
                        if pesan == 'ปิดแอด':
                            if msg._from in [gonebotMID]:
                                wait['autoAdd'] = False
                                gonebot.sendMessage(to, "ปิดออโต้แอดแล้ว")                                 

                        if pesan == 'เปิดติ้กใหญ่':
                            if msg._from in [gonebotMID]:
                                settings['Sticker'] = True
                                gonebot.sendMessage(to, "Sticker to on")                            
                        if pesan == 'ปิดติ้กใหญ่':
                            if msg._from in [gonebotMID]:
                                settings['Sticker'] = False   
                                gonebot.sendMessage(to, "Sticker to off")                                                                                
#====================================================================================                            
#=====================================================================
                        elif pesan == "เชคแทค":
                              try:
                                  gonebot.sendMessage(to,str(temptag["pesanya"]))
                              except:
                                  gonebot.sendMessage(to,"「 เกิดข้อผิดพลาด 」")

                        elif pesan.startswith('ตั้งแทค ') and sender == gonebotMID:
                                data = msg.text[len("ตั้งแทค"):].strip()
                                try:
                                    temptag["pesanya"] = data
                                    time.sleep(0.1)
                                    gonebot.sendMessage(to,"「 ตั้งข้อความตอบแทคเรียบร้อย 」")
                                    time.sleep(0.1)
                                    gonebot.sendMessage(to,"ข้อความตอบแทคของคุณ :\n" + data)
                                except:
                                    gonebot.sendMessage(to,"「 เกิดข้อผิดพลาด 」")   

                        elif pesan == "เชคคอมเม้น":
                              try:
                                  gonebot.sendMessage(to,str(settings["commentPost"]))
                              except:
                                  gonebot.sendMessage(to,"「 เกิดข้อผิดพลาด 」")

                        elif pesan.startswith('ตั้งคอมเม้น ') and sender == gonebotMID:
                                data = msg.text[len("ตั้งคอมเม้น"):].strip()
                                try:
                                    settings["commentPost"] = data
                                    time.sleep(0.1)
                                    gonebot.sendMessage(to,"「 ตั้งคอมเม้นเรียบร้อย 」")
                                    time.sleep(0.1)
                                    gonebot.sendMessage(to,"คอมเม้นของคุณ :\n" + data)
                                except:
                                    gonebot.sendMessage(to,"「 เกิดข้อผิดพลาด 」")                                                                                                                                         
#=====================================================================
                        if pesan == "รีบอท":
                            if msg._from in [gonebotMID]:
                                gonebot.sendMessage(to, "Restarting...♪")
                                restartBot()
#=====================================================================
                        if pesan.startswith("อินโด:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=in&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                gonebot.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)

                        if pesan.startswith("อังกิด:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=en&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                gonebot.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        if pesan.startswith("ญี่ปุ่น:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ja&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                gonebot.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        if pesan.startswith("ไทย:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=th&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                gonebot.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        if pesan.startswith("arab:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ar&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                gonebot.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        if pesan.startswith('zalgo '):
                            def zalgo(text):return zalgoname().zalgofy(gonebot.mainsplit(text))
                            gonebot.sendMessage(to, zalgo(text))                            
                        if pesan == "randomname":
                            r=requests.get("http://uinames.com/api/")
                            data=r.text
                            data=json.loads(data)
                            hasil = "Random Name :\n\n"
                            hasil += "Name: " + str(data["name"])                                              
                            hasil += "\nLastName: " + str(data["surname"])
                            hasil += "\nGender: " + str(data["gender"])
                            hasil += "\nCountry: " + str(data["region"])      
                            gonebot.generateReplyMessage(msg.id)
                            gonebot.sendReplyMessage(msg.id,to,str(hasil))
                        if pesan.startswith("jawa:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=jw&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                gonebot.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        if pesan.startswith("kaskus "):
                            query = cmd.replace("kaskus ","")
                            cond = query.split("|")
                            search = str(cond[0])
                            result = requests.get("https://api.bayyu.net/kaskus-hotthread/?apikey=c28c944199384f191335f1f8924414fa839350d&page={}".format(str(search)))
                            data = result.text
                            data = json.loads(data)
                            if len(cond) == 1:
                                num = 0
                                ret_ = " 「 Kaskus 」\nType: Search Kaskus"
                                for kus in data["hot_threads"]:
                                    num += 1
                                    ret_ += "\n{}. {}".format(str(num), str(kus["title"]))                                  
                                ret_ += "\n\nExample: {} Kaskus {}|1".format(str(setKey), str(search))
                                gonebot.sendMessage(to, str(ret_))
                            elif len(cond) == 2:
                                num = int(cond[1])
                                if num <= len(data["hot_threads"]):
                                    kaskus = data["hot_threads"][num - 1]
                                    result = requests.get("https://api.bayyu.net/kaskus-hotthread/?apikey=c28c944199384f191335f1f8924414fa839350d&page={}".format(str(search)))
                                    data = result.text
                                    data = json.loads(data)
                                    if data["hot_threads"] != []:
                                        ret_ =" 「 Kaskus 」\nType: Detail Kaskus"
                                        ret_ += "\n   Description: {}".format(str(kaskus["detail"]))                                            
                                        ret_ += "\n   {}".format(str(kaskus["link"]))
                                        gonebot.sendImageWithURL(to, str(kaskus["img"]))
                                        gonebot.sendMessage(to, str(ret_))
#=====================================================================
                        if pesan == "detectunsend on":unsendon(to,wait,msg,kuciyose)
                        if pesan == "detectunsend off":unsendoff(to,wait,msg,kuciyose)
#=====================================================================
                        if pesan == "steal" and sender == gonebotMID:gonebot.sendMessage(to, "╭───「 Steal 」─\n│    | Command |  \n│Get Profile Picture\n│  Key: steal pp [@]\n│Get Cover Picture\n│  Key: steal cover [@]\n│Get ID\n│  Key: getid, getid [@|num]\n╰──────")
                        if pesan == 'friendlist' and sender == gonebotMID:
                            a = gonebot.refreshContacts();gonebot.datamention(to,'List Friend',a)
                        if pesan.startswith('เพิ่มล้อเลียน '):
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in wait['target']:
                                        wait['target'].append(target)
                                        gonebot.sendMessage(to," 「 Mimiclist 」\nType: AddML\nStatus: Succes...")
                            else:pass
                        if pesan.startswith('ลบล้อเลียน '):
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                    print(x["M"])
                                for target in targets:
                                    print(target)
                                    if target in wait['target']:
                                        wait['target'].remove(target)
                                        gonebot.sendMessage(to," 「 Mimiclist 」\nType: DelML\nStatus: Succes...")
                            else:pass
                        if pesan.startswith("ลบเพื่อน ") and sender == gonebotMID:
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                    gonebot.datamentions(to,'Friendlist',targets,'DELFL',wait,ps='\n├ Type: Delete Friendlist')
                            else:
                                anu = gonebot.refreshContacts()
                                gonebot.deletefriendnum(to, wait, pesan)
                        elif pesan == "ล้างเพื่อน":
                            n = len(gonebot.getAllContactIds())
                            try:
                                gonebot.clearContacts()
                            except: 
                                pass
                            t = len(gonebot.getAllContactIds())
                            gonebot.generateReplyMessage(msg.id)
                            gonebot.sendReplyMessage(msg.id, to,"Type: Friendlist\n • Detail: Clear Contact\n • Before: %s Friendlist\n • After: %s Friendlist\n • Total removed: %s Friendlist\n • Status: Succes.."%(n,t,(n-t)))
#=====================================================================
                        if pesan == 'ขอลิ้ง':
                            if msg.toType == 2:
                                group = gonebot.getGroup(to)
                                if group.preventedJoinByTicket == False:
                                    ticket = gonebot.reissueGroupTicket(to)
                                    gonebot.sendMessage(to, "「 ลิ้งกลุ่มนี้สามารถนำไปใช้ได้ 」 \nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                                        
                        if pesan == 'เปิดลิ้ง':
                            if msg.toType == 2:
                                group = gonebot.getGroup(to)
                                if group.preventedJoinByTicket == False:
                                    gonebot.sendMessage(to, "「 ลิ้งกลุ่มเปิดอยู่ กรุณาพิม ขอลิ้ง 」")
                                else:
                                    group.preventedJoinByTicket = False
                                    gonebot.updateGroup(group)
                                    gonebot.sendMessage(to, "「 เปิดลิ้งกลุ่มเรียบร้อย 」")
                                        
                        if pesan == 'ปิดลิ้ง':
                            if msg.toType == 2:
                                group = gonebot.getGroup(to)
                                if group.preventedJoinByTicket == True:
                                    gonebot.sendMessage(to, "「 ลิ้งกลุ่มปิดอยู่แล้วเจ้านาย 」")
                                else:
                                    group.preventedJoinByTicket = True
                                    gonebot.updateGroup(group)
                                    gonebot.sendMessage(to, "「 ปิดลิ้งกลุ่มเรียบร้อย 」")

                        if pesan.startswith("เตะ ") and sender == gonebotMID:
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"] [0] ["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        gonebot.kickoutFromGroup(msg.to,[target])                           
                                    except:
                                        gonebot.sendMessage(msg.to,"บัคแล้วเตะไม่ได้ครับท่าน")

                        elif "Spam " in msg.text:
                            txt = msg.text.split(" ")
                            jmlh = int(txt[2])
                            teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                            tulisan = jmlh * (teks+"\n")
                            if txt[1] == "on":
                                if jmlh <= 100000:
                                    for x in range(jmlh):
                                        gonebot.sendMessage(msg.to, teks)
                                else:
                                    gonebot.sendMessage(msg.to, "Out of Range!")
                            elif txt[1] == "off":
                                if jmlh <= 100000:
                                    gonebot.sendMessage(msg.to, tulisan)
                                else:
                                    gonebot.sendMessage(msg.to, "Out Of Range!")
                        if text.lower() == "mid" or text.lower() == "ไอดีเรา":
                            gonebot.generateReplyMessage(msg.id)
                            gonebot.sendReplyMessage(msg.id, to,gonebotMID)
                        elif text.lower() == "myname" or text.lower() == "ชื่อเรา":
                                    h = gonebot.getContact(gonebotMID)
                                    gonebot.generateReplyMessage(msg.id)
                                    gonebot.sendReplyMessage(msg.id, to, "「 ชื่อของคุณ 」\n"+str(h.displayName))
                        elif text.lower() == "mybio" or text.lower() == "ตัสเรา":
                                    h = gonebot.getContact(gonebotMID)
                                    gonebot.generateReplyMessage(msg.id)
                                    gonebot.sendReplyMessage(msg.id, to, "「 ตัสของคุณ 」\n"+str(h.statusMessage))
                        elif text.lower() == "mypicture" or text.lower() == "รูปเรา":
                                    h = gonebot.getContact(gonebotMID)
                                    image = "http://dl.profile.line-cdn.net/" + h.pictureStatus
                                    gonebot.generateReplyMessage(msg.id)
                                    gonebot.sendReplyImageWithURL(msg.id, to, image)
                        elif text.lower() == "myvideo" or text.lower() == "รูปวีดีโอเรา":
                                    h = gonebot.getContact(gonebotMID)
                                    if h.videoProfile == None:
                            	        return gonebot.sendMessage(to, "คุณไม่ได้ใส่รูปวีดีโอ >_<")
                                    gonebot.generateReplyMessage(msg.id)
                                    gonebot.sendReplyVideoWithURL(msg.id, to,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                        elif text.lower() == "mycover" or text.lower() == "ปกเรา":
                                    h = gonebot.getContact(gonebotMID)
                                    cu = gonebot.getProfileCoverURL(gonebotMID)
                                    image = str(cu)
                                    gonebot.generateReplyMessage(msg.id)
                                    gonebot.sendReplyImageWithURL(msg.id, to, image)                                    
#==============================================================================#
                        if text.lower() == "ประกาศ2":
                            s="**วิธีใช้ =°=\n1.พิม'ตั้งรูปประกาศ'ก่อน\n2.พิม'เชครูปประกาศ'เพื่อดูรูป\n3.กรอกคำที่จะประกาศ + idline"
                            gonebot.sendMessage(to,s)
                        if text.lower() == "ตั้งรูปประกาศ":
                            settings["pict"] = True
                            gonebot.sendMessage(to,"กรุณาส่งรูปที่จะตั้งลงมา")
                        if text.lower() == "เชครูปประกาศ":
                            path = settings["listpict"]
                            gonebot.sendImage(to, path)
                        elif msg.text.lower().startswith("ประกาศ2 "):
                                    delcmd = msg.text.split(" ")
                                    get = msg.text.replace(delcmd[0]+" ","").split("/")
                                    kw = get[0]
                                    ans = get[1]
                                    groups = gonebot.getGroupIdsJoined()
                                    path = settings["listpict"]
                                    for group in groups:
                                        sa = "「 ประกาศ 」\n\n{}".format(str(kw))
                                        data = {"type": "flex","altText": "มาอ่านเอาสิ","contents": {"type": "bubble","body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": sa,"wrap": True,"align": "center","size": "md"},{  "type":"text","text":" "},{"type":"button","style":"primary","color":"#ee1289","action": {"type": "uri","label": "> ติดต่อเรา <","uri": "line://ti/p/~{}".format(ans),}}]}}}
                                        sendTemplate(group, data)
                                        gonebot.sendImage(group, str(path))
                                    gonebot.sendMessage(to, "ส่งคำประกาศเสร็จแล้ว จำนวน {} กลุ่ม".format(str(len(groups))))                                    
#=====================================================================
                        if pesan == 'แทค':
                            if msg._from in [gonebotMID]:
                                try:group = gonebot.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(gonebot.getProfile().mid)
                                except:group = gonebot.getRoom(to);nama = [contact.mid for contact in group.contacts]
                                gonebot.datamention(to,'Mention',nama)
                        elif pesan.startswith('mentionname ') and sender == gonebotMID:
                            texst = gonebot.adityasplittext(pesan)
                            gs = gonebot.getGroup(to)
                            c = ['{}:-:{}'.format(a.displayName,a.mid) for a in gs.members]
                            c.sort()
                            b = []
                            for s in c:
                                if texst in s.split(':-:')[0].lower():b.append(s.split(':-:')[1])
                            gonebot.datamention(to,'Mention By Name',b)
                        if pesan == "mentionall -s" and sender == gonebotMID:
                            gonebot.unsendMessage(msg_id)
                            try:
                                group = gonebot.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members];nama.remove(gonebot.getProfile().mid)
                                k = len(nama)//20
                                for a in range(k+1):
                                    try:
                                        if a == 0:gonebot.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[:20],pl=0,ps='╭「 Mention 」─',pg='MENTIONALLUNSED',pt=nama)
                                        else:gonebot.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[a*20 : (a+1)*20],pl=a*20,ps='├「 Mention 」─',pg='MENTIONALLUNSED',pt=nama)
                                    except Exception as e:
                                        print(e)
                            except:
                                try:
                                    if a == 0:gonebot.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[:20],pl=0,ps='╭「 Mention 」─',pg='MENTIONALLUNSED',pt=nama)
                                    else:gonebot.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[a*20 : (a+1)*20],pl=a*20,ps='├「 Mention 」─',pg='MENTIONALLUNSED',pt=nama)
                                except:group = gonebot.getRoom(msg.to);nama = [contact.mid for contact in group.contacts]
                                k = len(nama)//20
                                for a in range(k+1):
                                    if a == 0:gonebot.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[:20],pl=0,ps='╭「 Mention 」─',pg='MENTIONALLUNSED',pt=nama)
                                    else:gonebot.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[a*20 : (a+1)*20],pl=a*20,ps='├「 Mention 」─',pg='MENTIONALLUNSED',pt=nama)
                        elif pesan.startswith('mention ') and sender == gonebotMID:
                            if msg.toType == 0:
                                gonebot.datamention(to,'Spam',[to]*int(pesan.split(" ")[1]))
                            elif msg.toType == 2:
                                gs = gonebot.getGroup(to)
                                nama = [contact.mid for contact in gs.members]
                                try:
                                    if 'MENTION' in msg.contentMetadata.keys()!=None:gonebot.datamention(to,'Spam',[eval(msg.contentMetadata["MENTION"])["MENTIONEES"][0]["M"]]*int(pesan.split(" ")[1]))
                                    else:texst = gonebot.adityasplittext(pesan)
                                    gs = gonebot.getGroup(to)
                                    nama = [contact.mid for contact in gs.members];nama.remove(gonebot.getProfile().mid)
                                    c = ['{}:-:{}'.format(a.displayName,a.mid) for a in gs.members]
                                    c.sort()
                                    b = []
                                    for s in c:
                                        if len(texst) == 1:dd = s[len(texst)-1].lower()
                                        else:dd = s[:len(texst)].lower()
                                        if texst in dd:b.append(s.split(':-:')[1])
                                    gonebot.datamention(to,'Mention By Abjad',b)
                                except:gonebot.adityaarchi(wait,'Mention','',to,gonebot.adityasplittext(msg.text),msg,'\n├Group: '+gs.name[:20],nama=nama)
#=====================================================================
#=====================================================================
                        if pesan == 'เชคค่า':
                            if msg._from in [gonebotMID]:
                                txt = "การตั้งค่า :"
                                txt += "\n"
                                if wait["autoAdd"] == True:txt += "\n- ออโต้แอด: เปิดใช้งาน"
                                else:txt += "\n- ออโต้แอด: ปิดใช้งาน"
                                if wait["autoJoin"] == True:txt += "\n- ออโต้มุดลิ้ง: เปิดใช้งาน"
                                else:txt += "\n- ออโต้มุดลิ้ง: ปิดใช้งาน" 
                                if settings["autoblock"] == True:txt += "\n- ออโต้บล็อค: เปิดใช้งาน"
                                else:txt += "\n- ออโต้บล็อค: ปิดใช้งาน"
                                if settings["autoLeave"] == True:txt += "\n- กินห้องรัน: เปิดใช้งาน"
                                else:txt += "\n- กินห้องรัน: ปิดใช้งาน"
                                if settings["Leave"] == True:txt += "\n- ข้อความคนออก: เปิดใช้งาน"
                                else:txt += "\n- ข้อความคนออก: ปิดใช้งาน"
                                if settings["lv"] == True:txt += "\n- สติ๊กเกอร์คนออก: เปิดใช้งาน"
                                else:txt += "\n- สติ๊กเกอร์ออก: ปิดใช้งาน"
                                if settings["Welcome"] == True:txt += "\n- ข้อความคนเข้า: เปิดใช้งาน"
                                else:txt += "\n- ข้อความคนเข้า: ปิดใช้งาน" 
                                if settings["Wc"] == True:txt += "\n- ข้อความคนเข้า2: เปิดใช้งาน"
                                else:txt += "\n- ข้อความคนเข้า2: ปิดใช้งาน"  
                                if settings["wcsti2"] == True:txt += "\n- สติ๊กเกอร์คนเข้า: เปิดใช้งาน"
                                else:txt += "\n- สติ๊กเกอร์คนเข้า: ปิดใช้งาน" 
                                if settings["tag"] == True:txt += "\n- ตอบกลับคนแทค1: เปิดใช้งาน"
                                else:txt += "\n- ตอบกลับคนแทค1: ปิดใช้งาน"
                                if temptag["stealtag"] == True:txt += "\n- ตอบกลับคนแทค2: เปิดใช้งาน"
                                else:txt += "\n- ตอบกลับคนแทค2: ปิดใช้งาน"
                                if settings["tagsticker"] == True:txt += "\n- สติ๊กเกอร์คนแทค: เปิดใช้งาน"
                                else:txt += "\n- สติ๊กเกอร์คนแทค: ปิดใช้งาน"
                                if settings["Sticker"] == True:txt += "\n- สติ๊กเกอร์ใหญ่: เปิดใช้งาน"
                                else:txt += "\n- สติ๊กเกอร์ใหญ่: ปิดใช้งาน"

                                data = {
                                    "type": "flex",
                                    "altText": "{}".format(txt),
                                    "contents": {
                                        "type": "bubble",
                                        "styles": {
                                            "body": {
                                                "backgroundColor": '#ffffff'
                                            },
                                        },
                                        "body": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": txt,
                                                    "color": "#CD1076",
                                                    "align": "center",
                                                    "weight": "bold",
                                                    "size": "xxl"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "{}".format(txt),
                                                    "wrap": True,
                                                    "color": "#ee1289",
                                                    "gravity": "center",
                                                    "size": "md"
                                                },
                                            ]
                                        },
                                    }
                                }
                                sendTemplate(to, data)                                                
#====================================================================================
#====================================================================================
                        if pesan == "lurk" and msg.toType == 2:
                            if msg._from in [gonebotMID]:
                                if 'lurkauto' not in wait:wait['lurkauto'] = False
                                if wait['lurkauto'] == False:sd = "\n│Lurk Auto: OFF"
                                else:sd = "\n│Lurk Auto: ON"
                                if to in wait['readPoint']:
                                    a = "\n│Lurk State: ON"+sd
                                else:
                                    a = "\n│Lurk State: OFF"+sd
                                if to in wait["lurkp"]:
                                    if wait["lurkp"][to] == {}:
                                        b='\n╰Lurk People: None'
                                        h="╭「 Lurk 」─\n"+a+"\n│    | Command |  \n│Lurk Point\n│   lurk on\n│   lurk auto on\n│Lurk Del\n│   lurk off\n│   lurk auto off\n│Lurk Cek\n│   lurk result"
                                        gonebot.sendMessage(to,h+b)
                                    else:
                                        h= "╭「 Lurk 」─\n"+a+"\n│    | Command |  \n│Lurk Point\n│   lurk on\n│   lurk auto on\n│Lurk Del\n│   lurk off\n│   lurk auto off\n│Lurk Cek\n│   lurk result\n│Lurk People: {}".format(len(wait["lurkp"][to]))
                                        no=0
                                        hh = []
                                        for c in wait["lurkp"][to]:
                                            no+=1
                                            hh.append(c)
                                            if no == len(wait["lurkp"][to]):h+= '\n╰ {}. @!'.format(no)
                                            else:h+= '\n│ {}. @!'.format(no)
                                        gonebot.sendMention(to,h,'',hh)
                                else:
                                    b='\n╰Lurk People: None'
                                    h="╭「 Lurk 」─\n│    | Command |  \n│Lurk Point\n│   lurk on\n│   lurk auto on\n│Lurk Del\n│   lurk off\n│   lurk auto off\n│Lurk Cek\n│   lurk result" 
                                    gonebot.sendMessage(to,h+b)
                        if pesan == "เปิดอ่าน" and msg.toType == 2:
                            if msg._from in [gonebotMID]:
                                if to in wait['readPoint']:
                                    gonebot.sendMessage(to, " 「 Lurk 」\nเปิดดูคนอ่านแล้ว")
                                else:
                                    try:
                                        wait['readPoint'][to] = msg.id;wait['setTime'][to] = {};wait["ROM1"][to] = {}
                                    except:
                                        pass
                                    wait['readPoint'][to] = msg.id;wait['setTime'][to] = {};wait['ROM1'][to] = {}
                                    gonebot.sendMessage(to, " 「 Lurk 」\nเปิดดูคนอ่านแล้ว")
                        if pesan == "ปิดอ่าน" and msg.toType == 2:
                            if msg._from in [gonebotMID]:
                                if to not in wait['readPoint']:
                                    gonebot.sendMessage(to, " 「 Lurk 」\nปิดดูคนอ่านแล้ว")
                                else:
                                    try:
                                        del wait['readPoint'][to];wait['setTime'][to] = {};wait['ROM1'][to] = {}
                                    except:
                                        pass
                                    gonebot.sendMessage(to, " 「 Lurk 」\nปิดดูคนอ่านแล้ว")
                        if pesan == "อ่าน" and msg.toType == 2:
                            if msg._from in [gonebotMID]:
                                if to in wait['readPoint']:
                                    try:
                                        anulurk(to,wait)
                                        wait['setTime'][to]  = {}
                                    except:gonebot.sendMessage(to,'「 Lurkers 」\n ไม่มีคนอ่าน')
                                else:gonebot.sendMessage(to, " 「 Lurk 」\nLurk point not on♪")
                        if pesan == "lurk auto on" and msg.toType == 2:
                            if msg._from in [gonebotMID]:
                                if to in wait['readPoint']:
                                    if wait['lurkauto'] == True:gonebot.sendMessage(to, " 「 Lurk 」\nLurk already set♪")
                                else:
                                    try:
                                        wait['readPoint'][to] = msg.id;wait['setTime'][to] = {};wait['ROM1'][to] = {}
                                    except:
                                        pass
                                    wait['readPoint'][to] = msg.id;wait['setTime'][to] = {};wait['ROM1'][to] = {}
                                    wait['lurkauto'] = True
                                    gonebot.sendMessage(to, " 「 Lurk 」\nLurk point set♪")
                        if pesan == "lurk auto off" and msg.toType == 2:
                            if msg._from in [gonebotMID]:
                                if wait['lurkauto'] == False:
                                    gonebot.sendMessage(to, " 「 Lurk 」\nLurk auto already off♪")
                                else:
                                    wait['lurkauto'] = False
                                    gonebot.sendMessage(to, " 「 Lurk 」\nLurk auto point off♪")
                        if pesan.startswith("lurk on ") and msg.toType == 2:
                            if msg._from in [gonebotMID]:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    targets = key["MENTIONEES"][0]["M"]
                                    if targets in wait['readPoints']:
                                        gonebot.sendMention(to, " 「 Lurk 」\nLurk in @! already active",'',[targets])
                                    else:
                                        try:
                                            del wait['readPoints'][targets];del wait['lurkt'][to];del wait['lurkp'][to][targets]
                                        except:
                                            pass
                                        wait['readPoints'][targets] = msg.id
                                        if to not in wait['lurkt']:
                                            wait['lurkt'][to] = {}
                                            wait['lurkp'][to] = {}
                                        if targets not in wait['lurkp'][to]:
                                            wait['lurkp'][to][targets] = {}
                                            wait['lurkt'][to][targets] = {}
                                        gonebot.sendMention(to, " 「 Lurk 」\nLurk in @! set to active",'',[targets])
                        if pesan.startswith("ปิดอ่าน ") and msg.toType == 2:
                            if msg._from in [gonebotMID]:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    targets = key["MENTIONEES"][0]["M"]
                                    if targets not in wait['readPoints']:
                                        gonebot.sendMention(to, " 「 Lurk 」\nLurk in @! already mute",'',[targets])
                                    else:
                                        try:
                                            del wait['readPoints'][targets];del wait['lurkp'][to][targets];del wait["lurkt"][to][targets]
                                        except:
                                            pass
                                        gonebot.sendMention(to, " 「 Lurk 」\nLurk in @! set to mute",'',[targets])
                        if pesan.startswith("lurk result ") and msg.toType == 2:
                            if msg._from in [gonebotMID]:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    targets = key["MENTIONEES"][0]["M"]
                                    if targets in wait['readPoints']:
                                        try:
                                            chiya = []
                                            for rom in wait["lurkp"][to][targets].items():
                                                chiya.append(rom[1])
                                                print(rom[1])
                                            k = len(chiya)//20
                                            for a in range(k+1):
                                                if a == 0:gonebot.mentionmention(to=to,wait=wait,text='',dataMid=chiya[:20],pl=0,ps='╭「 Lurkers 」─',pg='SIDERMES',pt=chiya)
                                                else:gonebot.mentionmention(to=to,wait=wait,text='',dataMid=chiya[a*20 : (a+1)*20],pl=a*20,ps='├「 Lurkers 」─',pg='SIDERMES',pt=chiya)
                                            wait['lurkt'][to][targets] = {};wait['lurkp'][to][targets] = {}
                                        except:gonebot.sendMention(to, "No recent data for @!","",[targets])
                                    else:gonebot.sendMention(to, " 「 Lurk 」\nLurk in @! not active",'',[targets])
                        if pesan.startswith("lastseen ") and msg.toType == 2:
                            if msg._from in [gonebotMID]:
                                if 'MENTION' in msg.contentMetadata.keys() != None:
                                    names = re.findall(r'@(\w+)', msg.text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    for mention in mentionees:
                                        if mention['M'] in lastseen["find"]:
                                            gonebot.sendMention(to, "@!{}".format(lastseen["username"][mention['M']]), '', [mention['M']])
                                        else:
                                            gonebot.sendMention(to, "Oops!!\nI can't found @!","", [mention['M']])

#====================================================================================
                        if pesan == "animequotes" and sender == gonebotMID:
                            with requests.session() as web:
                                web.headers["user-agent"] = "Mozilla/5.0"
                                url = web.get("https://rest.farzain.com/api/animequotes.php?apikey=aguzzzz748474848&beta").text
                                url = json.loads(url)
                                a = "╭「 AnimeQuotes 」─\n│"
                                a += "Anime: {}".format(url["result"]["anime"])
                                a += "\n│Author: {}".format(url["result"]["author"])
                                a += "\n╰Quote's: \n{}".format(url["result"]["quote"])
                                kntl(to, str(a))
                        if pesan == "images" and sender == gonebotMID:
                            a = "╭───「 Image 」─\n│    | Command |  \n│Fansign\n│  Key:  cosplay [name]\n│  Key:  viloid [name]\n│Arts\n│  Key:  retro [text text text]\n│  Key:  graffity [text text]\n│"
                            a += "  Key:  light graffity [enter|text]\n│  Key:  neon graffity [enter|text]\n╰──────"
                            kntl(to,str(a))
                        if pesan.startswith('neon graffity') and sender == gonebotMID:
                            s = gonebot.downloadFileURL('https://rest.farzain.com/api/photofunia/neon_sign.php?text='+str(pesan.split('\n')[1])+'&apikey=aguzzzz748474848&beta',saveAs='anu.png')
                            gonebot.sendImage(to, 'anu.png')
                            os.remove('anu.png')
                        if pesan.startswith('graffity ') and sender == gonebotMID:
                            s = 'https://rest.farzain.com/api/photofunia/graffiti_wall.php?text1='+str(pesan.split(' ')[1])+'&text2='+str(pesan.split(' ')[2])+'&apikey=aguzzzz748474848&beta'
                            anunanu(to,s,wait)
                        if pesan.startswith('light graffity') and sender == gonebotMID:
                            s = gonebot.downloadFileURL('http://api.farzain.com/photofunia/light_graffiti.php?text='+str(pesan.split('\n')[1])+'&apikey=aguzzzz748474848&beta',saveAs='anu.png')
                            gonebot.sendImage(to, 'anu.png')
                            os.remove('anu.png')
                        if pesan.startswith('retro ') and sender == gonebotMID:
                            s = gonebot.downloadFileURL('http://api.farzain.com/photofunia/retro.php?text1='+str(pesan.split(' ')[1])+'&text2='+str(pesan.split(' ')[2])+'&text3='+str(pesan.split(' ')[3])+'&apikey=aguzzzz748474848&beta', saveAs='anu.png')
                            gonebot.sendImage(to, 'anu.png')
                            os.remove('anu.png')
                        if pesan.startswith('tts ') and sender == gonebotMID:
                            gonebot.unsendMessage(msg.id)
                            name = pesan.replace('tts ','')
                            a = 'https://rest.farzain.com/api/tts.php?id={}&apikey=aguzzzz748474848&beta'.format(name)
                            gonebot.sendAudioWithURL(to,str(a))
                        if pesan == 'randomquotes' and sender == gonebotMID:
                            a = requests.get('https://rest.farzain.com/api/motivation.php?apikey=aguzzzz748474848&beta').text
                            a = json.loads(a)
                            ret = "╭「 Quotes 」─\n│"
                            ret += "Author: {}".format(a["result"]["by"])
                            ret += "\n╰Quote's: {}".format(a["result"]["quotes"])
                            kntl(to, str(ret))
                        if pesan.startswith("ออก "):
                            proses = text.split(" ")
                            ng = text.replace(proses[0] + " ","")
                            gid = gonebot.getGroupIdsJoined()
                            for i in gid:
                                h = gonebot.getGroup(i).name
                                if h == ng:
                                    gonebot.leaveGroup(i) 

                        if "บอกหมุด: " in msg.text:
                            bctxt = msg.text.replace("บอกหมุด: ", "")
                            a = gonebot.getGroupIdsJoined()
                            for manusia in settings["bc"]:
                                if manusia in a:
                                    gonebot.sendMessage(manusia,(bctxt))
                                    time.sleep(0.1)
                            gonebot.sendMessage(to,"「 ส่งกลุ่มที่ปักหมุดแล้ว 」")   

                        if pesan == 'ลิสหมุด':
                            a = gonebot.getGroupIdsJoined()
                            ret_ = " ══[รายชื่อกลุ่ม]══"
                            num = 1
                            for manusia in settings["bc"]:
                                if manusia in a:
                                    group = gonebot.getGroup(manusia)
                                    ret_ += "\n {}. {} | {}".format(str(num), str(group.name), str(len(group.members)))
                                    num=(num+1)					
                            gonebot.sendMessage(to, str(ret_))

                        if pesan == 'ปักหมุด':
                            settings["bc"][receiver] = True
                            gonebot.sendMessage(receiver,"「 ปักหมุดกลุ่มนี้เรียบร้อย 」")
								
                        if pesan == 'ลบหมุด':
                            try:
                                del settings["bc"][receiver]
                                gonebot.sendMessage(receiver,"「 ลบหมุดออกเรียบร้อย 」")
                            except:
                                gonebot.sendMessage(receiver,"「 ลบหมุดออกเรียบร้อย 」")                           

                        if pesan.startswith("อัพชื่อ "):
                            string = removeCmd("อัพชื่อ", text)
                            if len(string) <= 10000000000:
                                pname = gonebot.getContact(sender).displayName
                                profile = gonebot.getProfile()
                                profile.displayName = string
                                gonebot.updateProfile(profile)
                                gonebot.sendMessage(to, "「 Update Name 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))
                        if pesan.startswith("อัพตัส "):
                            string = removeCmd("อัพตัส", text)
                            if len(string) <= 10000000000:
                                pname = gonebot.getContact(sender).statusMessage
                                profile = gonebot.getProfile()
                                profile.statusMessage = string
                                gonebot.updateProfile(profile)
                                gonebot.sendMessage(to, "「 Update Status 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))                        
                        if pesan.startswith('เพลง ') and sender == gonebotMID:
                            name = pesan.replace('เพลง ','')
                            a = requests.get('https://rest.farzain.com/api/joox.php?id={}&apikey=aguzzzz748474848&beta'.format(name))
                            data = json.loads(a.text)
                            try:
                                a = "╭「 Music 」─\n│"
                                a += " Artist: {}\n│".format(data["info"]["penyanyi"])
                                a += " Title: {}\n".format(data["info"]["judul"])
                                a += "│ Album: {}\n╰ Lyric:\n{}".format(data["info"]["album"],data["lirik"].replace("\nCreated By Faraaz\n",""))
                                gonebot.sendMessage(to, str(a))
                                gonebot.sendAudioWithURL(to, data["audio"]["mp3"])
                                s = data["gambar"]
                                anunanu(to,s,wait)
                            except Exception as e:
                                print(e)
                        if pesan.startswith("cosplay ") and sender == gonebotMID:
                            name = pesan.replace("cosplay ","")
                            s = "https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=aguzzzz748474848&beta&text={}".format(name)
                            anunanu(to,s,wait)
                        if pesan.startswith("viloid ") and sender == gonebotMID:
                            name = pesan.replace("viloid ","")
                            s = "https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=aguzzzz748474848&beta&text={}".format(name)
                            anunaun(to,s,wait)
                        if pesan == "quranlist" and sender == gonebotMID:
                            data = gonebot.adityarequestweb("http://api.alquran.cloud/surah")
                            if data["data"] != []:
                                no = 0
                                ret_ = "╭──「 Al-Qur'an 」"
                                for music in data["data"]:
                                    no += 1
                                    if no == len(data['data']):ret_ += "\n╰{}. {}".format(no,music['englishName'])
                                    else:ret_ += "\n│{}. {}".format(no,music['englishName'])
                                gonebot.generateReplyMessage(msg.id)
                                gonebot.sendReplyMessage(msg.id, to,ret_)
                        if pesan.startswith("qur'an ") and sender == gonebotMID:
                            data = gonebot.adityarequestweb("http://api.alquran.cloud/surah/{}".format(gonebot.adityasplittext(pesan)))
                            if len(pesan.split(' ')) == 1:
                                if data["data"] != []:
                                    no = 0
                                    ret_ = "╭──「 Al-Qur'an 」"
                                    for music in data["data"]:
                                        no += 1
                                        if no == len(data['data']):ret_ += "\n╰{}. {}".format(no,music['englishName'])
                                        else:ret_ += "\n│{}. {}".format(no,music['englishName'])
                                    kntl(msg.to,ret_)
                            if len(pesan.split(' ')) == 2:
                                try:
                                    no = 0
                                    ret_ = " 「 Al-Qur'an 」\nSurah: {}".format(data['data']['englishName'])
                                    for music in data["data"]["ayahs"]:
                                        no += 1
                                        ret_ += "\n{}. {}".format(no,music['text'])
                                    k = len(ret_)//10000
                                    for aa in range(k+1):
                                        kntl(msg.to,'{}'.format(ret_[aa*10000 : (aa+1)*10000]))
                                except:kntl(msg.to," 「 Al-Qur'an 」\nI can't found surah number {}".format(gonebot.adityasplittext(pesan)))
                            if len(pesan.split(' ')) == 3:
                                try:
                                    nama = data["data"]["ayahs"]
                                    selection = MySplit(gonebot.adityasplittext(pesan,'s'),range(1,len(nama)+1))
                                    k = len(nama)//100
                                    text = " 「 Al-Qur'an 」\nSurah: {}".format(data['data']['englishName'])
                                    no = 0
                                    for i in selection.parse():
                                        no+= 1
                                        text+= "\n{}. {}".format(i,nama[i-1]['text'])
                                    k = len(text)//10000
                                    for aa in range(k+1):
                                        kntl(msg.to,'{}'.format(text[aa*10000 : (aa+1)*10000]))
                                except:
                                    kntl(msg.to," 「 Al-Qur'an 」\nI can't found surah number {}".format(gonebot.adityasplittext(pesan)))
#====================================================================================
                        elif pesan == "autojoin" and sender == gonebotMID:
                            if wait["autoJoin"] == True:a = "Enabled"
                            else:a = "Disabled"
                            if wait["Members"]:
                                b = "{}".format(int(wait["Members"]))
                            else:b = "0"
                            gonebot.generateReplyMessage(msg.id)
                            gonebot.sendReplyMessage(msg.id, to, "「 Auto Join 」\nEvent Trigger:\n Autojoin: "+a+"\n Stage: "+b+"\n\nCommand:\n Autojoin\n • Usage: autojoin on|off\n • Usage: autojoin set 「numb」")
                        elif pesan.startswith("autojoin set ") and sender == gonebotMID:
                            wait["Members"] = int(pesan.split(" ")[2])
                            gonebot.sendMessage(msg.to, " 「 Autojoin 」\nType: Minim Members\nStatus: Success Set\nTo: {} Members".format(wait["Members"]))
                        elif pesan == "autojoin on" and sender == gonebotMID:
                            if wait['autoJoin'] == True:
                                msgs=" 「 Auto Join 」\nAuto Join already set to ENABLED♪"
                            else:
                                msgs=" 「 Auto Join 」\nAuto Join has been set to ENABLED♪"
                                wait['autoJoin']=True
                            gonebot.sendMessage(msg.to, msgs)
                        elif pesan == "autojoin off" and sender == gonebotMID:
                            if wait['autoJoin'] == False:
                                msgs=" 「 Auto Join 」\nAuto Join already set to DISABLED♪"
                            else:
                                msgs=" 「 Auto Join 」\nAuto Join has been set to DISABLED♪"
                                wait['autoJoin']=False
                            gonebot.sendMessage(msg.to, msgs)
#====================================================================================
#====================================================================================
                        elif pesan == "getreader" and sender == gonebotMID:
                            if wait["readerPesan"] is not None:ret = " 「 Get Reader 」\nGetreader Message : " + str(wait["readerPesan"])
                            else:ret = " 「 Getreader 」\nGetreader Message: None"
                            b = wait["messageSticker"]["listSticker"]["readerSticker"]
                            a = b["STKPKGID"]
                            anu = gonebot.shop.getProduct(packageID=int(a), language='ID', country='ID')
                            if wait['messageSticker']['listSticker']['readerSticker']['status'] == True:ret += "\nGetreader sticker "+anu.title
                            else:ret += ''
                            try:
                                ret += "\n\n Command:\n"
                                ret += "Getreader on|off\nAdd|Del getreaderSticker\nGetreader msg set [text]"
                                gonebot.generateReplyMessage(msg.id)
                                gonebot.sendReplyMessage(msg.id, to, ret)
                            except Exception as e:
                                gonebot.sendMessage(to, str(e))
                        elif pesan == "add getreadersticker" and sender == gonebotMID:
                            wait["messageSticker"]["addStatus"] = True
                            wait["messageSticker"]["addName"] = "readerSticker"
                            gonebot.sendMessage(to, " 「 Getreader 」\nType: Add getreader Sticker\nStatus: Sent a sticker...")
                        elif pesan == "del getreadersticker" and sender == gonebotMID:
                            wait["messageSticker"]["listSticker"]["readerSticker"]["status"] = False
                            gonebot.sendMessage(to, " 「 Getreader 」\nType: Del getreader Sticker\nStatus: Success....")
                        elif pesan.startswith("getreader msg set ") and sender == gonebotMID:
                            text_ = removeCmd("getreader msg set", text)
                            try:
                                wait["readerPesan"] = text_
                                gonebot.sendMessage(to," 「 Getreader 」\nChanged to : " + text_)
                            except:
                                gonebot.sendMessage(to," 「Getreader 」\nFailed to replace message")
                        elif pesan == "getreader on" and sender == gonebotMID:
                            wait["getReader"][receiver] = []
                            gonebot.sendMessage(to, "Getreader set to on.")
                        elif pesan == "getreader off" and sender == gonebotMID:
                            if receiver in wait["getReader"]:
                                del wait["getReader"][receiver]
                                gonebot.sendMessage(to, "Getreader set to off.")
#====================================================================================

#====================================================================================
                        elif msg.text.lower()== "ตั้งติ๊กคนแทค":
                            settings["messageSticker"]["addStatus"] = True
                            settings["messageSticker"]["addName"] = "tag"
                            gonebot.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                        elif msg.text.lower() == "ลบติ๊กคนแทค":
                            settings["messageSticker"]["listSticker"]["tag"] = None
                            gonebot.sendMessage(to, "ลบสติกเกอรคนแทคแล้ว")                            
                        elif msg.text.lower()== "ตั้งติ๊กคนเข้า":
                            settings["messageSticker"]["addStatus"] = True
                            settings["messageSticker"]["addName"] = "wc"
                            gonebot.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                        elif msg.text.lower() == "ลบติ๊กคนเข้า":
                            settings["messageSticker"]["listSticker"]["wc"] = None
                            gonebot.sendMessage(to, "ลบสติกเกอรคนเข้าแล้ว")
                        elif msg.text.lower()== "ตั้งติ๊กคนออก":
                            settings["messageSticker"]["addStatus"] = True
                            settings["messageSticker"]["addName"] = "lv"
                            gonebot.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                        elif msg.text.lower() == "ลบติ๊กคนออก":
                            settings["messageSticker"]["listSticker"]["lv"] = None
                            gonebot.sendMessage(to, "ลบสติกเกอรคนออกแล้ว")
                        elif msg.text.lower()== "ตั้งติ๊กคนแอด":
                            settings["messageSticker"]["addStatus"] = True
                            settings["messageSticker"]["addName"] = "add"
                            gonebot.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                        elif msg.text.lower() == "ลบติ๊กคนแอด":
                            settings["messageSticker"]["listSticker"]["add"] = None
                            gonebot.sendMessage(to, "ลบสติกเกอรคนแอดแล้ว")
#=====================================================================
                        elif pesan.startswith("ตั้งติ้ก ") and sender == gonebotMID:
                            load()
                            name = removeCmd("ตั้งติ้ก ",text)
                            name = name.lower()
                            if name not in stickers:
                                wait["addSticker"]["status"] = True
                                wait["addSticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = {}
                                f = codecs.open('sticker.json','w','utf-8')
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                gonebot.sendMessage(to, "Type: Stickers\n • Detail: Add sticker\n • Status: Send sticker..")
                            else:
                                gonebot.sendMessage(to, "Type: Stickers\n • Detail: Add sticker\n • Status: Failed, Sticker name already in list..")
                        elif pesan.startswith("ลบติ้ก ") and sender == gonebotMID:
                            load()
                            name = removeCmd("ลบติ้ก ",text)
                            name = name.lower()
                            if name in stickers:
                                del stickers[str(name.lower())]
                                f = codecs.open('sticker.json','w','utf-8')
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                gonebot.sendMessage(to, "Type: Sticker\n • Detail: Delete sticker\n • Status: Succes delete Sticker {}".format(str(name.lower())))
                            else:
                                gonebot.sendMessage(to, "Type: Sticker\n • Detail: Delete sticker\n • Status: Failed, Sticker name not in list")
                        elif pesan.startswith("เปลี่ยนติ้ก ") and sender == gonebotMID:
                            load()
                            name = removeCmd("เปลี่ยนติ้ก ",text)
                            name = name.lower()
                            if name in stickers:
                                wait["addSticker"]["status"] = True
                                wait["addSticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = ""
                                f = codecs.open('sticker.json','w','utf-8')
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                gonebot.sendMessage(to, "Type: Stickers\n • Detail: Change sticker\n • Status: Send sticker..")
                            else:
                                gonebot.sendMessage(to, "Type: Stickers\n • Detail: Change sticker\n • Status: Failed, Sticker not in list..")

                        elif pesan.startswith("ตั้งติ้ก1 ") and sender == gonebotMID:
                            load()
                            name = removeCmd("ตั้งติ้ก1 ",text)
                            name = name.lower()
                            if name not in stickers1:
                                wait["addSticker1"]["status"] = True
                                wait["addSticker1"]["name"] = str(name.lower())
                                stickers1[str(name.lower())] = {}
                                f = codecs.open('sticker1.json','w','utf-8')
                                json.dump(stickers1, f, sort_keys=True, indent=4, ensure_ascii=False)
                                gonebot.sendMessage(to, "Type: Stickers\n • Detail: Add sticker\n • Status: Send sticker..")
                            else:
                                gonebot.sendMessage(to, "Type: Stickers\n • Detail: Add sticker\n • Status: Failed, Sticker name already in list..")
                        elif pesan.startswith("ลบติ้ก1 ") and sender == gonebotMID:
                            load()
                            name = removeCmd("ลบติ้ก1 ",text)
                            name = name.lower()
                            if name in stickers1:
                                del sticker1[str(name.lower())]
                                f = codecs.open('sticker1.json','w','utf-8')
                                json.dump(stickers1, f, sort_keys=True, indent=4, ensure_ascii=False)
                                gonebot.sendMessage(to, "Type: Sticker\n • Detail: Delete sticker\n • Status: Succes delete Sticker {}".format(str(name.lower())))
                            else:
                                gonebot.sendMessage(to, "Type: Sticker\n • Detail: Delete sticker\n • Status: Failed, Sticker name not in list")
                        elif pesan.startswith("เปลี่ยนติ้ก1 ") and sender == gonebotMID:
                            load()
                            name = removeCmd("เปลี่ยนติ้ก1 ",text)
                            name = name.lower()
                            if name in stickers1:
                                wait["addSticker1"]["status"] = True
                                wait["addSticker1"]["name"] = str(name.lower())
                                stickers1[str(name.lower())] = ""
                                f = codecs.open('sticker1.json','w','utf-8')
                                json.dump(stickers1, f, sort_keys=True, indent=4, ensure_ascii=False)
                                gonebot.sendMessage(to, "Type: Stickers\n • Detail: Change sticker\n • Status: Send sticker..")
                            else:
                                gonebot.sendMessage(to, "Type: Stickers\n • Detail: Change sticker\n • Status: Failed, Sticker not in list..")                                
                        elif pesan == "liststicker":
                            load()
                            ret_ = "「 Sticker List 」\n"
                            for sticker in stickers:
                                ret_ += "\n" + sticker.title()
                            ret_ += "\n\nTotal {} Stickers".format(str(len(stickers)))
                            gonebot.generateReplyMessage(msg.id)
                            gonebot.sendReplyMessage(msg.id, to, ret_)
                        elif pesan == "list sticker1":
                            load()
                            ret_ = "「 Sticker List 」\n"
                            for sticker in stickers1:
                                ret_ += "\n" + sticker.title()
                            ret_ += "\n\nTotal {} Stickers".format(str(len(stickers1)))
                            gonebot.generateReplyMessage(msg.id)
                            gonebot.sendReplyMessage(msg.id, to, ret_)                            
#=====================================================================
                        if pesan == 'cleartmp':
                            wait['ROM'] = {}
                            wait['ROM1'] = {}
                            wait['Unsend'] = {}
                            wait['getReader'] = {}
                            wait['setTime'] = {}
                            wait['lurkp'] = {}
                            wait['lurkt'] = {}
                            wait['postId'] = []
                            gonebot.sendMessage(to, "Refresh...")                            
#=====================================================================
                        if pesan.startswith('getid ') and sender == gonebotMID:
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                gonebot.getinformations(to,key1,wait)
                            else:
                                if pesan.startswith('getid '):
                                    if len(pesan.split(' ')) == 2:
                                        a = gonebot.getGroupIdsJoined()
                                        gonebot.getinformation(to,a[int(pesan.split(' ')[1])-1],wait)
                                if pesan == 'getid':gonebot.getinformation(to,gonebot.getContact(to).mid,wait)
                        if pesan.startswith('get vid '):
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                contact = gonebot.getContact(key1).pictureStatus
                                s = "https://obs.line-scdn.net/" + contact
                                sendCarousel(to,{"messages": [{"type": "video","altText": "VideoProfile","originalContentUrl": 'https://tinyurl.com/y8og3or5',"previewImageUrl": s}]})
                        if pesan.startswith('steal pp ') or pesan.startswith('steal vid ') or pesan == 'steal pp' or pesan == 'steal vid' or pesan == 'my pp' or pesan == 'my vid' or pesan.startswith('steal cover') or pesan == 'steal cover' or pesan == 'my cover' and sender == gonebotMID:
                            if msg._from in [gonebotMID]:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                else:
                                    if pesan == 'steal pp' or pesan == 'steal vid' or pesan == 'steal cover':key1 = to
                                    if pesan == 'my pp' or pesan == 'my cover' or pesan == 'my vid':key1 = gonebotMID
                                if pesan.startswith('steal pp ') or pesan.startswith('steal vid ') or pesan == 'steal pp' or pesan == 'steal vid' or pesan == 'my pp' or pesan == 'my vid':
                                    try:contact = gonebot.getContact(key1)
                                    except:contact = gonebot.getGroup(key1)
                                    s = "https://obs.line-scdn.net/" + contact.pictureStatus
                                    if pesan == 'my vid' or pesan == 'steal vid' or pesan.startswith('steal vid '):
                                        if contact.videoProfile != None:
                                            sendCarousel(to,{"messages": [{"type": "video","altText": "YouTube","originalContentUrl": s+'/vp',"previewImageUrl": s}]})
                                    if pesan == 'steal pp' or pesan == 'my pp' or pesan.startswith('steal pp '):
                                        anunanu(to,s,wait)
                                    else:
                                        path = gonebot.getProfileCoverURL(key1)
                                        s = str(path)
                                        gonebot.generateReplyMessage(msg.id)
                                        anunanu(to,s,wait)
                            else:
                                pass
                        if pesan == 'steal cover' or pesan == 'my cover' or pesan.startswith('steal cover ') and sender == gonebotMID:
                            if msg._from in [gonebotMID]:
                                if pesan == 'steal cover' and msg.toType == 0:
                                    path = gonebot.getProfileCoverURL(to)
                                    s = str(path)
                                    gonebot.generateReplyMessage(msg.id)
                                    anunanu(to,s,wait)
                                if pesan == 'my cover':
                                    path = gonebot.getProfileCoverURL(gonebotMID)
                                    s = str(path)
                                    gonebot.generateReplyMessage(msg.id)
                                    anunanu(to,s,wait)
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = gonebot.getProfileCoverURL(ls)
                                        s = str(path)
                                        gonebot.generateReplyMessage(msg.id)
                                        anunanu(to,s,wait)
 #=====================================================================  
                        if pesan == "บัญชี":
                            contact = gonebot.getContact(gonebotMID)
                            LINKFOTO = "https://os.line.naver.jp/os/p/" + gonebotMID
                            LINKVIDEO = "https://os.line.naver.jp/os/p/" + gonebotMID + "/vp"
                            data = {
                                "type": "flex",
                                "altText": "{} Send Flex".format(gonebot.getProfile().displayName),
                                "contents": {
                                    "type": "bubble",
                                        'styles': {
                                            "header": {
                                                "backgroundColor": '#333333'
                                            },
                                            "body": {
                                                "backgroundColor": '#33CCCC'
                                            },
                                            "footer": {
                                                "backgroundColor": '#33FF33'
                                            },
                                        },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                        "size": "full",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "fit",
                                        "action": {
                                            "type": "uri",
                                            "uri": "http://line.me/ti/p/~kiebotsiri"
                                        }
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "margin": "lg",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": " เลขที่บัญชี :",
                                                                "color": "#FFFFFF",
                                                                "size": "sm",
                                                                "flex": 0
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "020098794250",
                                                                "color": "#FFFFFF",
                                                                "size": "sm",
                                                                "flex": 1
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "ธนาคาร: ",
                                                                "color": "#FFFFFF",
                                                                "size": "sm",
                                                                "flex": 0
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "ธ.ก.ส",
                                                                "color": "#FFFFFF",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 1
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "ชื่อบัญชี: ",
                                                                "color": "#FFFFFF",
                                                                "size": "sm",
                                                                "flex": 0
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "นาย ดำรง จิตรวงศ์นันท์",
                                                                "color": "#FFFFFF",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 1
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "วอเลท/โทร",
                                                                "color": "#FFFFFF",
                                                                "size": "sm",
                                                                "flex": 0
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "0971810252",
                                                                "color": "#FFFFFF",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 1
                                                            } 
                                                        ]
                                                    }
                                                ] 
                                            }
                                        ]
                                    },                                                                                                    
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "สนใจเช่าบอท คลิกที่นี่",
                                                    "uri": "http://line.me/ti/p/~kiebotsiri"
                                                }                                                   
                                            },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }
                                        ],
                                        "flex": 0
                                    }
                                }
                            }
                            sendTemplate(to, data)                                 
#=====================================================================                                        
                        if pesan == "ออน":
                            eltime = time.time() - mulai
                            bot = "" +waktu(eltime)
                            a = (bot) 
                            LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                            LINKVIDEO = "https://os.line.naver.jp/os/p/" + sender + "/vp"                            
                            data = {
                                "type": "flex",
                                "altText": "{}".format(a),
                                "contents": {
                                    "type": "bubble",
                                        'styles': {
                                            "header": {
                                                "backgroundColor": '#00BFFF'
                                             },
                                            "footer": {
                                                "backgroundColor": '#33FF33'                                               
                                            },
                                        },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "margin": "lg",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text":  "{}".format(a),
                                                                "color": "#00FF00",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 1    
                                                            } 
                                                        ]
                                                    }
                                                ] 
                                            }
                                        ]
                                    },                                                                                                    
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "สนใจเช่าบอท คลิกที่นี่",
                                                    "uri": "http://line.me/ti/p/~kiebotsiri"
                                                }                                                   
                                            },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }
                                        ],
                                        "flex": 0
                                    }
                                }
                            }
                            sendTemplate(to, data) 
#=====================================================================                             
                        if pesan == "สปีด":
                            start = time.time()
                            gonebot.sendMessage("u8356f84ac11d24464fb797227e573c20", "ทดสอบความเร็ว")
                            elapsed_time = time.time() - start
                            took = time.time() - start
                            a = " 「 สปีดบอท 」\nความเร็วปิง♪\n - Took : %.3fms♪\nความเร็วสปีด: %.10f♪" % (took,elapsed_time)
                            LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                            LINKVIDEO = "https://os.line.naver.jp/os/p/" + sender + "/vp"                            
                            data = {
                                "type": "flex",
                                "altText": "BotSpeed",
                                "contents": {
                                    "type": "bubble",
                                    "hero": {
                                        "type":"image",
                                        "url":"https://i.pinimg.com/originals/f8/c8/70/f8c8701da82c73db661668e32446d880.jpg",
                                        "size": "full",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "fit"
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": a,
                                                "wrap": True,
                                                "color":"#363636",
                                                "align": "center",
                                                "gravity": "center",
                                                "size": "md"
                                            },
                                        ]
                                    }
                                }
                            }
                            sendTemplate(to, data)
#=====================================================================                            
                        if pesan.startswith("เขียน"):
                            khie = text.split(" ")
                            hey = text.replace(khie[0] + " ", "")
                            text = "{}".format(hey)
                            contact = gonebot.getContact(sender)
                            LINKFOTO = "https://os.line.naver.jp/os/p/" + gonebotMID
                            LINKVIDEO = "https://os.line.naver.jp/os/p/" + gonebotMID + "/vp"                            
                            data = {
                                "type": "flex",
                                "altText": "This is flex",
                            "contents": {
                                "type": "bubble",
                                    'styles': {
                                        "header": {
                                            "backgroundColor": '#FFE4E1'
                                        },
                                        "footer": {
                                            "backgroundColor": '#FFE4E1'
                                                },
                                            },
                                "header": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                            #"url": "https://sv1.picz.in.th/images/2019/01/29/TkB2nV.gif",
                                            "size": "full",
                                            "aspectRatio": "1:1",
                                            "aspectMode": "fit",
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "margin": "lg",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "baseline",
                                                    "spacing": "sm",
                                                    "contents": [
                                                                                                  {
                                                            "type": "text",
                                                            "text":  "{}".format(text),
                                                            "color": "#FF00FF",
                                                            "wrap": True,
                                                            "align": "start",
                                                            "size": "md",
                                                            "gravity": "center",
                                                            #"flex": 1    
                                                            } 
                                                        ]
                                                    }
                                                ] 
                                            }
                                        ]
                                    },                                                                                                    
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "สนใจเช่าบอท คลิกที่นี่",
                                                    "uri": "http://line.me/ti/p/~kiebotsiri"
                                                }                                                   
                                            },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }
                                        ],
                                        "flex": 0
                                    }
                                }
                            }
                            sendTemplate(to, data) 
#=====================================================================                              
                        if pesan.startswith("bc "):                          
                            txt =  text.split(" ")
                            matt = text.replace(txt[0] + " ","")
                            chat = "{}".format(matt)
                            groups = gonebot.getGroupIdsJoined()
                            contact = gonebot.getContact(sender)
                            LINKFOTO = "https://os.line.naver.jp/os/p/" + gonebotMID
                            LINKVIDEO = "https://os.line.naver.jp/os/p/" + gonebotMID + "/vp"
                            for gr in groups:
                                data = {
                                    "type": "flex",
                                    "altText": "This is flex",
                                "contents": {
                                    "type": "bubble",
                                        'styles': {
                                            "header": {
                                                "backgroundColor": '#000000'
                                            },
                                            "footer": {
                                                "backgroundColor": '#000000'
                                                 },
                                              },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                         #       "type": "image",
                                          #      "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                                #"url": "https://sv1.picz.in.th/images/2019/01/29/TkB2nV.gif",
                                           #     "size": "full",
                                            #    "aspectRatio": "1:1",
                                             #   "aspectMode": "fit",
                                            #},
                                            #{
                                                "type": "box",
                                                "layout": "vertical",
                                                "margin": "lg",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                                                                  {
                                                                "type": "text",
                                                                "text":  "{}".format(chat),
                                                                "color": "#FF6633",
                                                                "wrap": True,
                                                                "align": "start",
                                                                "size": "md",
                                                                "gravity": "center",
                                                                #"flex": 1    
                                                            } 
                                                        ]
                                                    }
                                                ] 
                                            }
                                        ]
                                    },                                                                                                    
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "md",
                                        "contents": [
                                        {
                                         "type": "button",
                                         "style": "primary",
                                         "color": "#FF3399",
                                         "action": {
                                           "type": "uri",
                                           "label": "สนใจเช่าบอท ได้ที่นี่",
                                           "uri": "http://line.me/ti/p/~kiebotsiri"
                                         }                                                   
                                            },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }
                                        ],
                                        "flex": 0
                                    }
                                }
                            }
                                bcTemplate(gr, data)   
                            gonebot.sendMessage(to, "ทำการเสร็จเรียบร้อยแล้วจำนวน {} กลุ่ม".format(str(len(groups))))                                                                        
#=====================================================================
   
                        if pesan == "เชลบอท":
                            gifnya = ['https://sv1.picz.in.th/images/2019/02/07/TU6ZiP.jpg']
                            data = {
                                "type": "template",
                                "altText": "KhieWasHere",
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [{
                                        "imageUrl": "{}".format(random.choice(gifnya)),
                                        "action": {
                                            "type": "uri",
                                            "uri": "https://line.naver.jp/ti/p/~{}".format(gonebot.getProfile().userid),
                                            "area": {
                                                "x": 520,
                                                "y": 0,
                                                "width": 520,
                                                "height": 1040
                                            }
                                        }
                                    }]
                                }
                            }
                            sendTemplate(to, data)                                                  
                        if pesan.startswith("food "):
                                query = removeCmd("food", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []                                	
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "I'm hungry",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
#=====================================================================
                        if pesan.startswith('spam 1 ') and sender == gonebotMID:
                            try:
                                j = int(pesan.split(' ')[2])
                                a = [gonebot.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                h = [kntl(to,b) for b in a];kntl(to, '「 Spam 」\nTarget has been spammed with {} amount of messages♪'.format(j))
                            except:pass
                        if pesan.startswith('pc ') and sender == gonebotMID:
                            try:
                                j = int(pesan.split(' ')[1])
                                a = [gonebot.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    nama = gonebot.getContact(key1).displayName
                                    anu = gonebot.getContact(key1)
                                    if len(pesan.split("\n")) >= 2:
                                        mid  = "{}".format(key1)
                                        text = "{}".format(str(pesan.replace(pesan.split("\n")[0]+"\n","")))
                                        icon = "http://dl.profile.line.naver.jp/{}".format(anu.pictureStatus)
                                        name = "{}".format(anu.displayName)
                                        b = [sendMessageCustom(key1, text, icon, name) for b in a];gonebot.sendMention(to, '「 Spam 」\n@!has been spammed with {} amount of messages♪'.format(j),'',[key1])
                            except Exception as e:print(e)
                        if pesan.startswith('spam 2 ') and sender == gonebotMID:
                            if msg.toType == 0:
                                j = int(pesan.split(' ')[2])
                                a = [gonebot.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                b = [gonebot.giftmessage(to) for b in a];gonebot.sendMessage(to, '「 Spam 」\nTarget has been spammed with {} amount of messages♪'.format(j))
                            else:
                                j = int(pesan.split(' ')[2])
                                a = [gonebot.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    nama = [key1]
                                    b = [gonebot.giftmessage(key1) for b in a];gonebot.sendMention(to, '「 Spam 」\n@!has been spammed with {} amount of gift♪'.format(j),'',[key1])
                        if pesan.startswith('spam 3 ') and sender == gonebotMID:
                            j = int(pesan.split(' ')[2])
                            a = [gonebot.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                            try:group = gonebot.getGroup(to);nama = [contact.mid for contact in group.members];b = [gonebot.sendContact(to,random.choice(nama)) for b in a]
                            except:nama = [to,to];b = [gonebot.sendContact(to,random.choice(nama)) for b in a]
                        if pesan.startswith('spam 4 ') and sender == gonebotMID:
                            j = int(pesan.split(' ')[2])
                            text = pesan.replace('spam 4 {} '.format(j),'')
                            anu = [gonebot.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                nama = [key1]
                                if pesan.startswith(" "):gss = 7
                                else:gss = 7
                                msg.contentMetadata = {'AGENT_LINK': 'line://ti/p/~{}'.format(gonebot.getProfile().userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + gonebot.getProfile().picturePath,'AGENT_NAME': ' 「 SPAM MENTION 」','MENTION': str('{"MENTIONEES":' + json.dumps([{'S':str(int(key['S'])-gss-len(pesan.split(' ')[2])-1+13), 'E':str(int(key['E'])-gss-len(pesan.split(' ')[2])-1+13), 'M':key['M']} for key in eval(msg.contentMetadata["MENTION"])["MENTIONEES"]]) + '}')}
                                msg.text = pesan[gss+1+len(pesan.split(' ')[2]):].replace(pesan[gss+1+len(pesan.split(' ')[2]):],' 「 Mention 」\n{}'.format(pesan[gss+1+len(pesan.split(' ')[2]):]))
                                b = [gonebot.sendMessages(msg) for b in anu]
                            if msg.toType == 0:
                                b = [gonebot.sendMention(to, "{}".format(text),"",[to]) for a in range(j)]
#=====================================================================
#=====================================================================
                        if pesan == "ลบรัน" and sender == gonebotMID:
                            ginvited = gonebot.getGroupIdsInvited()
                            if ginvited != [] and ginvited != None:
                                for gid in ginvited:
                                    gonebot.rejectGroupInvitation(gid)
                                gonebot.sendMessage(to, "ทำการลบห้องรันจำนวน 「 {} 」ห้อง".format(str(len(ginvited))))
                            else:
                                gonebot.sendMessage(to, "ไม่มีห้องรันแล้วครับ")
                        if pesan.startswith("myname") and sender == gonebotMID:
                            profile = gonebot.getProfile()
                            if len(pesan.split(" ")) <= 2 or len(pesan.split("\n")) <= 1:gonebot.sendMention(to,'@!','',[gonebot.getProfile().mid])
                            if len(pesan.split("\n")) >= 2:
                                profiles = gonebot.getProfile()
                                profile = gonebot.getProfile()
                                profile.displayName = msg.text.replace(msg.text.split("\n")[0]+"\n","")
                                if 'zalgo' in pesan:wait['myProfile']['displayName'] = zalgos().zalgofy(profile.displayName)
                                else:wait['myProfile']['displayName'] = profile.displayName
                                gonebot.updateProfileAttribute(2, wait['myProfile']['displayName'])
                                gonebot.sendMessage(to," 「 Profile 」\nType: Change Display Name\nStatus: Success\nFrom: "+profiles.displayName+"\nTo: "+wait['myProfile']['displayName'])
                        if pesan.startswith("mybio") and sender == gonebotMID:
                            profile = gonebot.getProfile()
                            if len(pesan.split(" ")) <= 1 or len(pesan.split("\n")) <= 1:gonebot.sendMessage(to,profile.statusMessage)
                            if len(pesan.split("\n")) >= 2:
                                profile.statusMessage = msg.text.replace(msg.text.split("\n")[0]+"\n","")
                                wait['myProfile']['statusMessage'] = profile.statusMessage
                                gonebot.updateProfileAttribute(16, profile.statusMessage)
                                gonebot.sendMessage(to," 「 Profile 」\nType: Change a status message\n" + profile.statusMessage+"\nStatus: Success change status message")
                        if pesan == "changedp" and sender == gonebotMID:
                            wait["changePicture"] = True
                            gonebot.sendMessage(to, "「 Profile 」\nType: Change Profile Picture♪\nStatus: Sent a picture..♪")
                        if pesan == "changedp video" and sender == gonebotMID:
                            wait['changeProfileVideo']['status'] = True
                            wait['changeProfileVideo']['stage'] = 1
                            gonebot.sendMessage(to, "「 Profile 」\nType: Change Video Profile♪\nStatus: Sent a video..♪")
                        if pesan == "changedp group" and sender == gonebotMID:
                            if msg.toType == 2:
                                if to not in wait["changeGroupPicture"]:
                                    wait["changeGroupPicture"].append(to)
                                gonebot.sendMessage(to, "「 Profile 」\nType: Change Profile Picture♪\nStatus: Sent a picture..♪")
                        if pesan == "mimic on":mimicon(to,wait)
                        if pesan == "mimic off":mimicoff(to,wait)
                        if pesan.startswith("changemy video") and sender == gonebotMID:
                            link = removeCmd("changemy video",text)
                            print(link)
                            contact = gonebot.getContact(gonebotMID)
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            a = subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            gonebot.sendMessage(to, "「 Profile 」\nType: Change Video Profile♪\nStatus: Downloading...♪")
                            pict = gonebot.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            time.sleep(2)
                            changeVideoAndPictureProfile(pict, vids)
                            gonebot.generateReplyMessage(msg.id)
                            gonebot.sendMessage(to, "「 Profile 」\nType: Change Video Profile♪\nStatus: Succes...♪")
                            os.remove("TeamAnuBot.mp4")
                        if pesan == 'ลิสกลุ่ม' or pesan.startswith('groups'):
                            if msg._from in [gonebotMID]:
                                if len(pesan.split(' ')) <= 1:
                                    listgroup(to,wait,msg)
                                else:
                                    gid = gonebot.getGroupIdsJoined()
                                    group = gonebot.getGroup(gid[int(pesan.split(' ')[1])-1])
                                    nama = [a.mid for a in group.members];nama.remove(gonebotMID)
                                    if len(pesan.split(" ")) == 2:
                                        total = "Local ID: {}".format(int(pesan.split(' ')[1]))
                                        gonebot.datamention(to,'List Member',nama,'\n├Group: '+group.name[:20]+'\n├'+total)
                                    if len(pesan.split(" ")) == 4:
                                        if pesan.startswith('groups '+pesan.split(' ')[1]+' mem '):gonebot.getinformations(to,nama[int(pesan.split(' ')[3])-1],wait);
                                        if pesan.startswith('groups '+pesan.split(' ')[1]+' tag '):gonebot.adityaarchi(wait,'Mention','tag',gid[int(pesan.split(' ')[1])-1],pesan.split(' ')[3],to,"\n├Group: {}\n├Local ID: {}".format(group.name[:20],int(pesan.split(' ')[1])),nama=nama)
                                        if pesan.startswith('groups '+pesan.split(' ')[1]+' kick '):gonebot.adityaarchi(wait,'Kick Member','kick',gid[int(pesan.split(' ')[1])-1],pesan.split(' ')[3],to,"\n├Group: {}\n├Local ID: {}".format(group.name[:20],int(pesan.split(' ')[1])),nama=nama)
                                        if pesan.startswith('groups '+pesan.split(' ')[1]+' unsent'):
                                            a = gid[int(pesan.split(' ')[1])-1]
                                            j = int(pesan.split(' ')[3])
                                            a = [gonebot.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                            h = wait['Unsend'][gid[int(pesan.split(' ')[1])-1]]['B']
                                            for b in h[:j]:
                                                print(b)
                                                try:
                                                    gonebot.unsendMessage(b)
                                                    wait['Unsend'][gid[int(pesan.split(" ")[1])-1]]['B'].remove(b)
                                                except Exception as e:print(e)
                        if pesan.startswith("leave groups ") and sender == gonebotMID:
                            if msg.toType in [0,1,2]:
                                gid = gonebot.getGroupIdsJoined()
                                if len(pesan.split(" ")) == 3:
                                    selection = MySplit(pesan.split(' ')[2],range(1,len(gid)+1))
                                    k = len(gid)//100
                                    for a in range(k+1):
                                        if a == 0:eto='╭「 Leave Group 」─'
                                        else:eto='├「 Leave Group 」─'
                                        text = ''
                                        no = 0
                                        for i in selection.parse()[a*100 : (a+1)*100]:
                                            gonebot.leaveGroup(gid[i - 1])
                                            no+=1
                                            if no == len(selection.parse()):text+= "\n╰{}. {}".format(i,gonebot.getGroup(gid[i - 1]).name)
                                            else:text+= "\n│{}. {}".format(i,gonebot.getGroup(gid[i - 1]).name)
                                        gonebot.sendMessage(to,eto+text)
                        if pesan.startswith('ไลค์ '):
                            if msg._from in ['u1e3f103c12b0b5bb347b825523344db6',gonebotMID] and msg.toType == 2:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    try:
                                        a = gonebot.getHomeProfile(key1)
                                        for i in a['result']['feeds']:
                                            if i['post']['postInfo']['liked'] == False:
                                                try:
                                                    gonebot.likePost(i['post']['userInfo']['mid'],i['post']['postInfo']['postId'],random.choice([1001,1002,1003,1004,1005]))
                                                    gonebot.createComment(i['post']['userInfo']['mid'],i['post']['postInfo']['postId'],""+wait['autoLike']['comment'])
                                                except Exception as e:
                                                    gonebot.sendMessage(to, str(e))
                                                    print('liked')
                                            else:
                                                 pass
                                        gonebot.sendMessage(to, "Like done..")
                                    except Exception as e:
                                        gonebot.sendMessage(to, str(e))
                        if pesan.startswith('create note ') and sender == gonebotMID:
                            if msg._from in [gonebotMID]:
                                pesan = pesan.replace('create note ','')
                                NoteCreate(to,pesan,msg)
                        if pesan == "mentionnote" and sender == gonebotMID:
                            if msg._from in [gonebotMID]:
                                NoteCreate(to,pesan,msg)
                        if pesan.startswith('ยก ') and sender == gonebotMID:
                            gonebot.unsendMessage(msg.id)
                            j = int(pesan.split(' ')[1])
                            a = [gonebot.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                            if len(pesan.split(' ')) == 2:
                                h = wait['Unsend'][msg.to]['B']
                                n = len(wait['Unsend'][msg.to]['B'])
                                for b in h[:j]:
                                    try:
                                        gonebot.unsendMessage(b)
                                        wait['Unsend'][msg.to]['B'].remove(b)
                                    except:pass
                                t = len(wait['Unsend'][msg.to]['B'])
                            if len(pesan.split(' ')) >= 3:h = [gonebot.unsendMessage(gonebot.sendMessage(to,gonebot.adityasplittext(pesan,'s')).id) for b in a]
                        if pesan == 'get album' or pesan.startswith('get album '):
                            if msg._from in [gonebotMID]:
                                albumNamaGrup(to,wait,pesan)
                        if pesan == "get note":
                            try:
                                if msg._from in [gonebotMID]:
                                    data = gonebot.getGroupPost(to)
                                    if data['result'] != []:
                                        try:
                                            no = 0
                                            b = []
                                            a = " 「 Groups 」\nType: Get Note"
                                            for i in data['result']['feeds']:
                                                b.append(i['post']['userInfo']['writerMid'])
                                                try:
                                                    for aasd in i['post']['contents']['textMeta']:b.append(aasd['mid'])
                                                except:pass
                                                no += 1
                                                gtime = i['post']['postInfo']['createdTime']
                                                try:g = i['post']['contents']['text'].replace('@','@!')
                                                except:g="None"
                                                if no == 1:sddd = '\n'
                                                else:sddd = '\n\n'
                                                a +="{}{}. Penulis : @!\nDescription: {}\nTotal Like: {}\nCreated at: {}\n".format(sddd,no,g,i['post']['postInfo']['likeCount'],humanize.naturaltime(datetime.fromtimestamp(gtime/1000)))
                                            a +="Status: Success Get "+str(data['result']['homeInfo']['postCount'])+" Note"
                                            gonebot.sendMention(to,a,'',b)
                                        except Exception as e:
                                            return gonebot.sendMessage(to,"「 Auto Respond 」\n"+str(e))
                            except Exception as e:print(e)
                        if pesan.startswith("get note "):
                            try:
                                if msg._from in [gonebotMID]:
                                    data = gonebot.getGroupPost(to)
                                    try:
                                        music = data['result']['feeds'][int(pesan.split(' ')[2]) - 1]
                                        b = [music['post']['userInfo']['writerMid']]
                                        try:
                                            for a in music['post']['contents']['textMeta']:b.append(a['mid'])
                                        except:pass
                                        try:
                                            g= "\n\nDescription:\n"+str(music['post']['contents']['text'].replace('@','@!'))
                                        except:
                                            g=""
                                        a="\n   Total Like: "+str(music['post']['postInfo']['likeCount'])
                                        a +="\n   Total Comment: "+str(music['post']['postInfo']['commentCount'])
                                        gtime = music['post']['postInfo']['createdTime']
                                        a +="\n   Created at: "+str(humanize.naturaltime(datetime.fromtimestamp(gtime/1000)))
                                        a += g
                                        zx = ""
                                        zxc = " 「 Groups 」\nType: Get Note\n   Penulis : @!"+a
                                        try:
                                            gonebot.sendMention(to,zxc,'',b)
                                        except Exception as e:
                                            gonebot.sendMessage(to, str(e))
                                        try:
                                            for c in music['post']['contents']['media']:
                                                params = {'userMid': gonebot.getProfile().mid, 'oid': c['objectId']}
                                                s = gonebot.server.urlEncode(gonebot.server.LINE_OBS_DOMAIN, '/myhome/h/download.nhn', params)
                                                if 'PHOTO' in c['type']:
                                                    try:
                                                        anunanu(to,s,wait)
                                                    except:pass
                                                else:
                                                    pass
                                                if 'VIDEO' in c['type']:
                                                    try:
                                                        anuanu(to,s,wait)
                                                    except:pass
                                                else:
                                                    pass
                                        except:
                                            pass
                                    except Exception as e:
                                        return gonebot.sendMessage(to,"「 Auto Respond 」\n"+str(e))
                            except Exception as e:print(e)
                        if pesan.startswith('cek mention ') or pesan == 'mentionme':
                            if msg._from in [gonebotMID]:
                                cekmentions(to,wait,pesan)
                        if pesan.startswith("แชร์โพส "):
                            if msg._from in [gonebotMID]:
                                j = int(pesan.split(' ')[2])
                                a = [gonebot.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        lists.append(mention["M"])
                                    for ls in lists:
                                        try:
                                            e = gonebot.getHomeProfile(ls)
                                            for i in e['result']['feeds']:
                                                b = i['post']['postInfo']['postId']
                                                f = [gonebot.sendPostToTalk(to,b) for g in a]
                                        except Exception as e:
                                            gonebot.sendMention(to, "Oops!! User @!doesn't have post/privacy not in public","",[ls])
                        if pesan == 'youtube':
                            try:
                                youtube(to,wait)
                            except Exception as e:print(e)
                                #gonebot.generateReplyMessage(msg.id)
                                #gonebot.sendReplyMessage(msg.id, to, "╭───「 Youtube 」─\n│    | Command |  \n│Event Triggred\n│  [query|numb|link]\n│Youtube list\n│  Key: Youtube search [query]\n│Youtube audio\n│  Key: Youtube audio <trigger>\n│Youtube video\n│  Key: Youtube video <trigger>\n│Youtube file\n│  Key: Youtubefile mp3 <trigger>\n│  Key: Youtubefile mp4 <trigger>\n│Youtube info\n│  Youtube info <trigger>\n╰──────")
                        if pesan.startswith("อัพโพส"):
                            if msg._from in [gonebotMID]:
                                try:
                                    texts = str(msg.text.replace(msg.text.split("\n")[0]+"\n",""))
                                    try:
                                        f = gonebot.createPost(texts)
                                        gonebot.sendPostToTalk(to,f["result"]["feed"]["post"]["postInfo"]["postId"])
                                    except Exception as e: 
                                        gonebot.sendMessage(to, str(e))
                                except Exception as e:
                                    gonebot.sendMessage(to, str(e))
                        if pesan.startswith('.talk'):
                            if msg._from in [gonebotMID]:
                                gonebot.unsendMessage(msg.id)
                                j = int(pesan.split(' ')[1])
                                a = [gonebot.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                if 'MENTION' in msg.contentMetadata.keys() != None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        anu = gonebot.getContact(ls)
                                        ps = "{}".format(ls)
                                        if len(pesan.split(" ")) >= 5000:
                                            mid = "{}".format(ls)
                                            icon = "http://dl.profile.line.naver.jp/{}".format(anu.pictureStatus)
                                            name = "{}".format(anu.displayName)
                                            tagdia(to, " 「 Auto Respons 」\n@!",ps,[ls])
                                            scont(to, mid, icon, name)
                                        if len(pesan.split("\n")) >= 2:
                                            mid  = "{}".format(ls)
                                            text = "{}".format(str(msg.text.replace(msg.text.split("\n")[0]+"\n","")))
                                            icon = "http://dl.profile.line.naver.jp/{}".format(anu.pictureStatus)
                                            name = "{}".format(anu.displayName)
                                            b = [sendMessageCustom(to, text, icon, name) for b in a]
                        if "/ti/g/" in msg.text:
                            try:
                                if wait["autoJoin"] == True:
                                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                    links = link_re.findall(msg.text)
                                    n_links=[]
                                    for l in links:
                                        n_links.append(l)
                                    for ticket_id in n_links:
                                        group=gonebot.findGroupByTicket(ticket_id)
                                        g = gonebot.getGroup(group.id)
                                        if len(g.members) >= wait['Members']:
                                            gonebot.acceptGroupInvitationByTicket(group.id,ticket_id)
                                        else:pass
                            except Exception as e:print(e)

                    for sticker in stickers1:
                        if text.lower() == sticker:
                            sid = stickers1[sticker]["STKID"]
                            data = {
                                "type": "template",
                                "altText": "KhieWasHere",
                                "baseSize": {
                                    "height": 1040,
                                    "width": 1040
                                },
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [{
                                        "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png".format(sid),
                                        "action": {
                                            "type": "uri",
                                            "uri": "https://line.naver.jp/ti/p/~{}".format(gonebot.getProfile().userid),
                                            "area": {
                                                "x": 520,
                                                "y": 0,
                                                "width": 520,
                                                "height": 1040
                                            }
                                        }
                                    }]
                                }
                            }
                            sendTemplate(to, data)


#=====================================================================                            
#========================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != gonebot.profile.mid:
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
#========================================================================
            elif msg.contentType == 7: # Content type is sticker
                if settings['Sticker']:
                    if 'STKOPT' in msg.contentMetadata:
                        contact = gonebot.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
                    else:
                        contact = gonebot.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
            elif msg.contentType == 1:
                if settings["pict"] == True:
                    path = gonebot.downloadObjectMsg(msg_id)
                    settings["pict"] = False
                    settings["listpict"] = str(path)
                    gonebot.sendMessage(to, "Done...")                                                
#=====================================================================  
                                         
                if msg.contentType == 1:
                    print(msg)
                    if wait["changePicture"] == True and sender == gonebotMID:
                        try:
                            if 'DOWNLOAD_URL' not in msg.contentMetadata:
                                path = gonebot.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id, 'path')
                            else:
                                path = gonebot.downloadFileURL(msg.contentMetadata['DOWNLOAD_URL'], 'path')
                        except:
                            path = gonebot.downloadObjectMsg(msg.id)
                        wait["changePicture"] = False
                        gonebot.updateProfilePicture(path)
                        gonebot.sendMessage(to, " 「 Profile 」\nType: Change Profile Picture♪\nStatus: Succes...♪")
                    if wait['changeProfileVideo']['status'] == True and sender == gonebotMID:
                        try:
                            if 'DOWNLOAD_URL' not in msg.contentMetadata:
                                path = gonebot.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id, 'path')
                            else:
                                path = gonebot.downloadFileURL(msg.contentMetadata['DOWNLOAD_URL'], 'path')
                        except:
                            path = gonebot.downloadObjectMsg(msg_id, saveAs="tmp/pict.bin")
                        if wait['changeProfileVideo']['stage'] == 1:
                            wait['changeProfileVideo']['picture'] = path
                            gonebot.sendMessage(to, " 「 Profile 」\nType: Change Video Profile♪\nStatus: Sent a video...♪")
                            wait['changeProfileVideo']['stage'] = 2
                        elif wait['changeProfileVideo']['stage'] == 2:
                            wait['changeProfileVideo']['picture'] = path
                            changeProfileVideo(to)
                            gonebot.sendMessage(to, " 「 Profile 」\nType: Change Video Profile♪\nStatus: Succes...♪")
                    if msg.toType == 2:
                        if to in wait["changeGroupPicture"] and sender == gonebotMID:
                            path = gonebot.downloadObjectMsg(msg_id, saveAs="tmp/pict.png")
                            wait["changeGroupPicture"].remove(to)
                            gonebot.updateGroupPicture(to, path)
                            gonebot.sendMessage(to, " 「 Group 」\nType: Change Group Picture♪\nStatus: Succes...♪")
                            os.remove("tmp/pict.png")
                        if to in wait['GROUP']['WM']['AP']:
                            if wait['GROUP']['WM']['status'] == True:
                                path = gonebot.downloadObjectMsg(msg.id)
                                wait['GROUP']['WM']['pict'][to] = str(path)
                                gonebot.sendMessage(to, " 「 Welcome Picture 」\nWelcome picture has been updated..")
                                wait['GROUP']['WM']['status'] = False
                if msg.contentType == 2:
                    print(msg)
                    if wait['changeProfileVideo']['status'] == True and sender == gonebotMID:
                        try:
                            if 'DOWNLOAD_URL' not in msg.contentMetadata:
                                path = gonebot.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id, 'path')
                            else:
                                path = gonebot.downloadFileURL(msg.contentMetadata['DOWNLOAD_URL'], 'path')
                        except:
                            path = gonebot.downloadObjectMsg(msg.id)
                        if wait['changeProfileVideo']['stage'] == 1:
                            wait['changeProfileVideo']['video'] = path
                            gonebot.sendMessage(to, " 「 Profile 」\nType: Change Video Profile♪\nStatus: Sent a picture♪")
                            wait['changeProfileVideo']['stage'] = 2
                        elif wait['changeProfileVideo']['stage'] == 2:
                            wait['changeProfileVideo']['video'] = path
                            changeProfileVideo(to)
                            gonebot.sendMessage(to, " 「 Profile 」\nType: Change Video Profile♪\nStatus: Succes...♪")
                if msg.contentType == 6:
                    if msg.toType == 2 and msg._from not in gonebotMID:
                        ps = msg._from
                        if to in wait["notificationCall"]:
                            b = msg.contentMetadata['GC_EVT_TYPE']
                            c = msg.contentMetadata["GC_MEDIA_TYPE"]
                            if c == "VIDEO" and b == "S":
                                a = '╭「 Group Call 」'
                                a += "\n│Group {} call".format(c)
                                a += "\n│in Group: {}".format(gonebot.getGroup(to).name)
                                a += "\n│CreatedTime: {}".format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)))
                                a += "\n╰Host: @!"
                                gonebot.sendMention(to, str(a),"",[msg._from])
                            if c == 'AUDIO' and b == "S":
                                a = '╭「 Group Call 」'
                                a += "\n│Group {} call".format(c)
                                a += "\n│in Group: {}".format(gonebot.getGroup(to).name)
                                a += "\n│CreatedTime: {}".format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)))
                                a += "\n╰Host: @!"
                                gonebot.sendMention(to, str(a),"",[msg._from])
                            if c == 'LIVE' and b == 'S':
                                a = '╭「 Live 」'
                                a += "\n│Group {}".format(c)
                                a += "\n│in Group: {}".format(gonebot.getGroup(to).name)
                                a += "\n│CreatedTime: {}".format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)))
                                a += "\n╰Host: @!"
                                gonebot.sendMention(to, str(a),"",[msg._from])
                            else:
                                mills = int(msg.contentMetadata["DURATION"])
                                seconds = (mills/1000)%60
                                if c == "VIDEO" and b == "E":
                                    a = '╭「 Group Call 」'
                                    a += "\n│Group {} call".format(c)
                                    a += "\n│in Group: {}".format(gonebot.getGroup(to).name)
                                    a += "\n│Duration: {} Sec".format(seconds)
                                    a += "\n╰Host: @!"
                                    gonebot.sendMention(to, str(a),"",[msg._from])
                                if c == "AUDIO" and b == "E":
                                    a = '╭「 Group Call 」'
                                    a += "\n│Group {} call".format(c)
                                    a += "\n│in Group: {}".format(gonebot.getGroup(to).name)
                                    a += "\n│Duration: {} Sec".format(seconds)
                                    a += "\n╰Host: @!"
                                    gonebot.sendMention(to, str(a),"",[msg._from])
                                if c == "LIVE" and b == "E":
                                    a = '╭「 Live 」'
                                    a += "\n│Group {}".format(c)
                                    a += "\n│in Group: {}".format(gonebot.getGroup(to).name)
                                    a += "\n│Duration: {} Sec".format(seconds)
                                    a += "\n╰Host: @!"
                                    gonebot.sendMention(to, str(a),"",[msg._from])
                        if to in wait["notificationCallPrank"]:
                            b = msg.contentMetadata['GC_EVT_TYPE']
                            c = msg.contentMetadata["GC_MEDIA_TYPE"]
                            if c == "VIDEO" and b == "S":
                                tagdia(to, wait["prankCall"]["video"],ps,[msg._from])
                            if c == 'AUDIO' and b == "S":
                                tagdia(to, wait["prankCall"]["audio"],ps,[msg._from])
                            if c == 'LIVE' and b == 'S':
                                tagdia(to, wait["prankCall"]["live"],ps,[msg._from])

                    if msg.contentType == 7:
                        if settings["messageSticker"]["addStatus"] == True:
                            name = settings["messageSticker"]["addName"]
                            if name != None and name in settings["messageSticker"]["listSticker"]:
                                settings["messageSticker"]["listSticker"][name] = {
                                    "STKID": msg.contentMetadata["STKID"],
                                    "STKVER": msg.contentMetadata["STKVER"],
                                    "STKPKGID": msg.contentMetadata["STKPKGID"]
                                }
                                gonebot.sendMessage(to, "Success Added " + name)
                            settings["messageSticker"]["addStatus"] = False
                            settings["messageSticker"]["addName"] = None
                        if settings["addSticker"]["status"] == True:
                            stickers[settings["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                            stickers[settings["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                            stickers[settings["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                            f = codecs.open('sticker.json','w','utf-8')
                            json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                            gonebot.sendMessage(to, "Success Added sticker {}".format(str(settings["addSticker"]["name"])))
                            settings["addSticker"]["status"] = False
                            settings["addSticker"]["name"] = ""
                    if msg.contentType == 7:
                        if settings["Sticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "╔══[ Sticker Info ]"
                            ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                            ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                            ret_ += "\n╚══[ Finish ]"
                            gonebot.sendMessage(to, str(ret_))      
                                                                                                    
                    if wait["addSticker"]["status"] == True and sender == gonebotMID:
                        stickers[wait["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[wait["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[wait["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        kntl(msg.to, " 「 Sticker 」\nName: "+a.title+"\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                        wait["addSticker"]["status"] = False
                        wait["addSticker"]["name"] = ""
                    if wait["addSticker1"]["status"] == True and sender == gonebotMID:
                        stickers1[wait["addSticker1"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers1[wait["addSticker1"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers1[wait["addSticker1"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker1.json','w','utf-8')
                        json.dump(stickers1, f, sort_keys=True, indent=4, ensure_ascii=False)
                        kntl(msg.to, " 「 Sticker 」\nName: "+a.title+"\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                        wait["addSticker1"]["status"] = False
                        wait["addSticker1"]["name"] = ""                        
                    if wait['sendSticker'] == True:
                        if msg._from in ["u40a63634c91d10f01a3ebcd36a7f8d94"]:
                            sid = msg.contentMetadata['STKID']
                            spkg = msg.contentMetadata['STKPKGID']
                            sver = msg.contentMetadata['STKVER']
                            name = gonebot.getContact(msg._from).displayName
                            pict = gonebot.getContact(msg._from).pictureStatus
                            group = gonebot.getGroupIdsJoined()
                            for i in group:
                                try:
                                    sendSticker(i, name, pict, sver, spkg, sid)
                                except Exception as e:
                                    try:
                                        sendSticker(i, name, gonebot.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").pictureStatus, sver, spkg, sid)
                                    except Exception as e:
                                        gonebot.sendMessage(to,  "Gua ngga ada stickernya :v")
                            wait['sendSticker'] = False
                        else:gonebot.sendMessage(to, "Gua ga ada stickernya :v")   
#===================================================================== 
        if op.type == 11:
            if op.param1 in protectqr:
                    try:
                        if gonebot.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in gonebotMID:
                                gonebot.reissueGroupTicket(op.param1)
                                X = gonebot.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                gonebot.updateGroup(X)
                                gonebot.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in gonebotMID:
                    try:
                        invitor = op.param2
                        gotinvite = []
                        if "\x1e" in op.param3:
                            gotinvite = op.param3.split("\x1e")
                        else:
                            gotinvite.append(op.param3)                        
                        for u in gotinvite:
                            wait["blacklist"][op.param2] = True
                            gonebot.cancelGroupInvitation(op.param1,[op.param3])
                            gonebot.kickoutFromGroup(op.param1,[op.param2])  
                    except:
                        pass    
        if op.type == 32:
            if op.param2 not in gonebotMID:
                pass
            if op.param1 in protectcancel:
                gonebot.kickoutFromGroup(op.param1,[op.param2])
                gonebot.findAndAddContactsByMid(op.param3)
                gonebot.inviteIntoGroup(op.param1,[op.param3])
                wait["blacklist"][op.param2] = True                                                   

        if op.type == 13:
            if op.param3 in wait["blacklist"]:
                if op.param2 not in gonebotMID:
                    gonebot.cancelGroupInvitation(op.param1,[op.param3])
                    gonebot.kickoutFromGroup(op.param1,[op.param2])
                    G = gonebot.getGroup(op.param1)	
                    G.preventedJoinByTicket = True		
                    gonebot.updateGroup(G)  

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in gonebotMID:
                    gonebot.kickoutFromGroup(op.param1,[op.param2])
                    G = gonebot.getGroup(op.param1)	
                    G.preventedJoinByTicket = True		
                    gonebot.updateGroup(G)	                    

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in gonebotMID:
                    wait["blacklist"][op.param2] = True
                    gonebot.kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass       

        if op.type == 19:
            if myMid in op.param3:
                if op.param2 in gonebotMID:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        gonebot.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                return

#=====================================================================                                         
        if op.type == 26:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            pesan = command(text)
            isValid = True
            if isValid != False:
                if msg.toType == 0 and sender != gonebotMID: to = sender
                else: to = receiver
                if msg.contentType == 0:
                    if 'MENTION' in msg.contentMetadata.keys() != None and msg._from not in gonebotMID and msg.toType == 2:
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        h = []
                        for mention in mentionees:
                            h.append(msg.text.replace(msg.text[int(mention["S"]):int(mention["E"])]+' ','@!').replace(msg.text[int(mention["S"]):int(mention["E"])],'@!'))
                        for mention in mentionees:
                            if mention["M"] in gonebotMID:
                                if to not in wait['ROM']:
                                    wait['ROM'][to] = {}
                                if msg._from not in wait['ROM'][to]:
                                    wait['ROM'][to][msg._from] = {}
                                if 'msg.id' not in wait['ROM'][to][msg._from]:wait['ROM'][to][msg._from]['msg.id'] = []
                                if 'waktu' not in wait['ROM'][to][msg._from]:wait['ROM'][to][msg._from]['waktu'] = []
                                if 'metadata' not in wait['ROM'][to][msg._from]:wait['ROM'][to][msg._from]['metadata'] = []
                                if 'text' not in wait['ROM'][to][msg._from]:wait['ROM'][to][msg._from]['text'] = []
                                wait['ROM'][to][msg._from]['msg.id'].append(msg.id)
                                wait['ROM'][to][msg._from]['waktu'].append(msg.createdTime)
                                wait['ROM'][to][msg._from]['metadata'].append(msg.contentMetadata)
                                wait['ROM'][to][msg._from]['text'].append(h[len(h)-1])
                                autoresponuy(to,msg,wait)
                                break
                if msg.contentType == 0:
                    if "/ti/g/" in text.lower():
                        if wait["autoJoin"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                   n_links.append(l)
                            for ticket_id in n_links:
                                group = gonebot.findGroupByTicket(ticket_id)
                                if len(group.members) >= wait["Members"]:
                                    gonebot.acceptGroupInvitationByTicket(group.id,ticket_id)
                                else:
                                    gonebot.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    gonebot.leaveGroup(group.id)

        if op.type == 65:
            try:
                msg = kuciyose['mimic'][op.param1][op.param2]['msg']
                if msg._from in wait["target"] and wait["status"] == True:
                    gonebot._unsendMessageReq += 1
                    gonebot.unsendMessage(kuciyose['mimic'][op.param1][op.param2]['s'])
            except:pass
            try:
                msg = kuciyose['tos'][op.param1][op.param2]['msg']
                if kuciyose['tos'][op.param1]['settingset'] == True:
                    if msg._from in kuciyose['talkblacklist']['tos']:
                        if kuciyose['talkblacklist']['tos'][msg._from]["expire"] == True:
                            return
                        elif time.time() - kuciyose['talkblacklist']['tos'][msg._from]["time"] <= 5:
                            kuciyose['talkblacklist']['tos'][msg._from]["flood"] += 1
                            if kuciyose['talkblacklist']['tos'][msg._from]["flood"] >= 10:
                                kuciyose['talkblacklist']['tos'][msg._from]["flood"] = 0
                                kuciyose['talkblacklist']['tos'][msg._from]["expire"] = True
                                gonebot.sendMention(msg.to, " 「 FLOOD 」\nFLOOD UNSEND DETECT, So sorry @! I will mute on 30second if unsend from you @!",'',[msg._from]*2)
                        else:
                            kuciyose['talkblacklist']['tos'][msg._from]["flood"] = 0
                            kuciyose['talkblacklist']['tos'][msg._from]["time"] = time.time()
                    else:
                        kuciyose['talkblacklist']['tos'][msg._from] = {"time": time.time(),"flood": 0,"expire": False}
                    if op.param2 in kuciyose['tos'][op.param1]:
                        kuciyose['GN'] = msg
                        if msg.toType == 0:
                            if msg._from != gonebot.getProfile().mid:
                                msg.to = msg._from
                            else:
                                msg.to = msg.to
                        else:
                            msg.to = msg.to
                        if msg.contentType == 0:dd = '\nType: Text'
                        else:dd= '\nType: {}'.format(ContentType._VALUES_TO_NAMES[msg.contentType])
                        aa = '\nCreatedTime: {}{}\nText:\n'.format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)),dd)
                        if msg.contentType == 0:
                            if 'MENTION' in msg.contentMetadata.keys() != None:
                                msg.text = ' 「 Unsend 」\nFrom: @GARA GANTENG '+aa+msg.text
                                gd = [{'S':str(0+len(' 「 Unsend 」\nFrom: ')), 'E':str(len('@RhyN GANTENG ')+len(' 「 Unsend 」\nFrom: ')), 'M':msg._from}]
                                for key in eval(msg.contentMetadata["MENTION"])["MENTIONEES"]:
                                    gd.append({'S':str(int(key['S'])+len(' 「 Unsend 」\nFrom: @RhyN GANTENG '+aa)), 'E':str(int(key['E'])+len(' 「 Unsend 」\nFrom: @GARA GANTENG '+aa)),'M':key['M']})
                                msg.contentMetadata = {'AGENT_LINK': 'line://ti/p/zMankMvx69','AGENT_NAME': ' 「 UNSEND DETECT 」',
                                'MENTION': str('{"MENTIONEES":' + json.dumps(gd) + '}')}
                                gonebot.sendMessages(msg)
                            else:
                                if msg.location != None:aa = aa.replace('Text','Location').replace('\nText:','');gonebot.sendMessages(msg)
                                if msg.text != None: asdd = msg.text
                                else:asdd = ''
                                gonebot.sendMention(op.param1,' 「 Unsend 」\nFrom: @! {}{}'.format(aa,asdd),'',[msg._from])
                        else:
                            a = ' 「 Unsend 」\nFrom: @!\nCreatedTime: {}{}'.format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)),dd)
                            try:
                                try:
                                    gonebot.sendMessages(msg)
                                except:
                                    agh = gonebot.shop.getProduct(packageID=int(msg.contentMetadata['STKPKGID']), language='ID', country='ID')
                                    if agh.hasAnimation == True:data = {"messages": [{"type":"image","originalContentUrl":'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/IOS/sticker_animation@2x.png',"previewImageUrl":'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/IOS/sticker_animation@2x.png',"animated":True,"extension":"gif","sentBy":{"label":"Mimic Sticker GIFs","iconUrl":'https://os.line.naver.jp/os/p/'+gonebotMID,"linkUrl":"line://ti/p/zMankMvx69"}}]}
                                    else:data = {"messages": [{"type": "image","originalContentUrl": 'https://os.line.naver.jp/os/p/'+gonebotMID,"previewImageUrl": 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/ANDROID/sticker.png;compress=true',"sentBy":{"label":"Mimic Sticker","iconUrl":'https://os.line.naver.jp/os/p/'+gonebotMID,"linkUrl":"line://ti/p/zMankMvx69"}}]}
                                    sendCarousel(to,data)
                            except:
                                pass
                            asdf = ' 「 Unsend 」\nFrom: @!\nCreatedTime: {}{}'.format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)),dd)
                            if msg.contentType == 1:
                                try:
                                    if msg.contentMetadata != {}:gonebot.sendGIF(op.param1,kuciyose['tos'][op.param1][op.param2]['path'])
                                except:
                                    gonebot.sendImage(op.param1,kuciyose['tos'][op.param1][op.param2]['path'])
                            if msg.contentType == 2:gonebot.sendVideo(op.param1,kuciyose['tos'][op.param1][op.param2]['path']);os.remove(kuciyose['tos'][op.param1][op.param2]['path'])
                            if msg.contentType == 3:gonebot.sendAudio(op.param1,kuciyose['tos'][op.param1][op.param2]['path']);os.remove(kuciyose['tos'][op.param1][op.param2]['path'])
                            if msg.contentType == 14:gonebot.sendFile(op.param1,kuciyose['tos'][op.param1][op.param2]['path'], file_name='',ct = msg.contentMetadata)
                            gonebot.sendMention(op.param1,asdf,'',[msg._from])
                        del kuciyose['tos'][op.param1][op.param2]
            except Exception as e:
                pass

        if op.type == 55:
            try:
                Name = gonebot.getContact(op.param2).mid
                group = gonebot.getGroup(op.param1).name
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
                readTime = timeNow.strftime('%H.%M')
                readTime2 = hr
                readTime3 = timeNow.strftime('%d') + "-" + bln + "-" + timeNow.strftime('%Y')
                lastseen["username"][Name] = "Was lastseen\nIn Group: ' " + group + " '\nTime: " + readTime + " WIB\nOn: " + readTime2 + ", " + readTime3
                lastseen['find'][op.param2] = True
            except Exception as e:
                print(e)
            if op.param1 in wait["getReader"] and op.param2 not in wait["getReader"][op.param1]:
                msgSticker = wait["messageSticker"]["listSticker"]["readerSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    try:
                        sendStk(op.param1, op.param2, sver, spkg, sid)
                    except Exception as e:
                        sendSticker2(op.param1, op.param2, sver, spkg, sid)
                if "@!" in wait["readerPesan"]:
                    msg = wait["readerPesan"].split("@!")
                    sendMention(op.param1, op.param2, msg[0], msg[1])
                else:
                    sendMention(op.param1, op.param2, "Gw", wait["readerPesan"])
                wait["getReader"][op.param1].append(op.param2)
            if op.param1 in wait['readPoint']:
                if op.param2 in wait['ROM1'][op.param1]:
                    wait['setTime'][op.param1][op.param2] = op.createdTime
                else:
                    wait['ROM1'][op.param1][op.param2] = op.param2
                    wait['setTime'][op.param1][op.param2] = op.createdTime
                    try:
                        if wait['lurkauto'] == True:
                            if len(wait['setTime'][op.param1]) % 5 == 0:
                                anulurk(op.param1,wait)
                    except:pass
            elif op.param2 in wait['readPoints']:
                wait['lurkt'][op.param1][op.param2][op.param3] = op.createdTime
                wait['lurkp'][op.param1][op.param2][op.param3] = op.param2
            else:pass
        backupData()
    except Exception as error:
        traceback.print_tb(error.__traceback__)
def unsendon(to,wait,msg,kuciyose):
    if 'tos' not in wait:wait['tos'] = {}
    if msg.to not in wait['tos']:wait['tos'][msg.to] = {}
    if 'settingset' not in wait['tos'][msg.to]:wait['tos'][msg.to]['settingset'] = False
    if wait['tos'][msg.to]['settingset'] == True:
        return gonebot.sendMessage(msg.to,' 「 Unsend 」\nUnsend Detection already Set ON')
    wait['tos'][msg.to]['settingset'] = True
    gonebot.sendMessage(msg.to,' 「 Unsend 」\nUnsend Detection Set ON')
def unsendoff(to,wait,msg,kuciyose):
    if 'tos' not in wait:wait['tos'] = {}
    if msg.to not in wait['tos']:wait['tos'][msg.to] = {}
    if 'settingset' not in wait['tos'][msg.to]:wait['tos'][msg.to]['settingset'] = False
    if wait['tos'][msg.to]['settingset'] == False:
        return gonebot.sendMessage(msg.to,' 「 Unsend 」\nUnsend Detection already Set OFF')
    del wait['tos'][msg.to]
    del kuciyose['tos'][msg.to]
    gonebot.sendMessage(msg.to,' 「 Unsend 」\nUnsend Detection Set OFF')
def anulurk(to, wait):
    moneys = {}
    for a in wait["setTime"][to].items():
        moneys[a[1]] = [a[0]] if a[1] is not None else idnya
    sort = sorted(moneys)
    sort = sort[0:]
    k = len(sort)//20
    for a in range(k+1):
        if a == 0:no= a;msgas = '╭「 Lurkers 」─'
        else:no = a*20;msgas = '├「 Lurkers 」─'
        h = []
        for i in sort[a*20 : (a+1)*20]:
            h.append(moneys[i][0])
            no+=1
            a = '{}'.format(humanize.naturaltime(datetime.fromtimestamp(i/1000)))
            if no == len(sort):msgas+='\n│{}. @!\n╰「 {} 」'.format(no,a)
            else:msgas+='\n│{}. @!\n│「 {} 」'.format(no,a)
        gonebot.sendMention(to, msgas,'', h)
def sendStk(to, mid, sver, spkg, sid):
    mid = gonebot.getContact(mid)
    contentMetadata = {
        'MSG_SENDER_NAME': mid.displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + mid.pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    gonebot.sendMessage(to, '', contentMetadata, 7)
def sendSticker2(to, mid, sver, spkg, sid):
    mid = gonebot.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5")
    contentMetadata = {
        'MSG_SENDER_NAME': mid.displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + mid.pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    gonebot.sendMessage(to, "", contentMetadata, 7)
#====================================================================================
def nhentai(to,msg,wait,pesan):
    try:
        msg.text = pesan
        lururl = 'https://domain.com/image/'
        if ' page ' not in msg.text:return
        if pesan.startswith('nhentai page '):
            k = pesan.split('page ')[1].split(' ')
            website = requests.get("https://nhentai.net?page={}".format(k[0]))
        else:
            h = pesan.split('page ')[0][len('nhentai '):]
            k = pesan.split('page ')[1].split(' ')
            website = requests.get("https://nhentai.net?page={}".format(h,k[0]))
        data = BeautifulSoup(website.content, "lxml")
        dataDoujins = []
        b = ' 「 Nhentai 」'
        ss = []
        hh = []
        gh = []
        gg = []
        ret_ = []
        for listAllDoujins in data.findAll("div", {"class":"container index-container"}):
            for getUrl in listAllDoujins.findAll("div", {"class":"gallery"}):
                for get in getUrl.find_all('a'):gh.append("https://nhentai.net{}".format(get.get('href')))
                for gets in getUrl.find_all('img'):
                    if 'https://t.nhentai.net/galleries/' in gets['src']:
                        gg.append(gets['src'])
                    else:
                        pass
            for getTitle in listAllDoujins.findAll("div", {"class":"caption"}):
                title = getTitle.text
                dataDoujins.append(title)
        if len(k) == 1:
            if int(k[0]) == 1:no = 0
            else:no = (int(k[0])-1)*25
            for c in range(0,len(dataDoujins)):
                no+=1
                ret_.append({"thumbnailImageUrl": lururl+gg[c],"imageSize": "contain","imageAspectRatio": "square","title": 'Rank {}'.format(no),"text": '{} '.format(dataDoujins[c][:55]),"actions": [{"type": "uri","label": "Go Page","uri": gh[c]}]})
            ks = len(ret_)//10
            for aa in range(ks+1):
                data = {"messages": [{"type": "template","altText": "Noob sent a template.","template": {"type": "carousel","columns": ret_[aa*10 : (aa+1)*10]}}]}
                aas = sendCarousel(to,data)
        if len(k) == 2:
            if int(k[0]) == 1:g = int(k[1])-1
            else:g = int(k[1])-1;g= (((int(k[0])*25-25)//(int(k[0])-1))-(-int(k[1])+25*int(k[0])))-1
            gonebot.sendMessage(to,' 「 Nhentai 」\nStatus: Uploading Doujin {} From nhentai'.format(dataDoujins[g]))
            website = requests.get("{}1/".format(gh[g]))
            data = BeautifulSoup(website.content, "lxml")
            for getJson in data.findAll("script")[2]:
                imgs = re.search(r"gallery\s*:\s*(\{.+\}),", getJson)
                imgs = json.loads(imgs.group(1))
                idx = imgs.get("media_id")
                images = []
                cdn = "https://i.nhentai.net/galleries/"
                ext = {"j": "jpg", "p": "png", "g": "gif"}
                for n, i in enumerate(imgs.get("images", {}).get("pages", [])):
                    hh = "{}{}/{}.{}".format(cdn, idx, n + 1, ext.get(i.get("t")))
                    ret_.append({"imageUrl": hh,"action": {"type": "uri","label": "View detail","uri": hh}})
                k = len(ret_)//10
                for aa in range(k+1):
                    data = {"messages": [{"type": "template","altText": "Noob sent a template.","template": {"type": "image_carousel","columns": ret_[aa*10 : (aa+1)*10]}}]}
                    sendCarousel(to,data)
                gonebot.sendMessage(to,' 「 Nhentai 」\nSuccess Send {} pict From Nhentai'.format(len(ret_)))
    except Exception as e:
        print(e)
def mimicon(to,wait):
    if wait['status'] == True:
        msgs=" 「 Mimic 」\nMimic already ENABLED♪"
    else:
        msgs=" 「 Mimic 」\nMimic set to ENABLED♪"
    wait["status"] = True
    gonebot.sendMessage(to,msgs)
def mimicoff(to,wait):
    kuciyose['GN'] = ''
    if wait['status'] == False:
        msgs=" 「 Mimic 」\nMimic already DISABLED♪"
    else:
        msgs=" 「 Mimic 」\nMimic set to DISABLED♪"
    wait["status"] = False
    gonebot.sendMessage(to,msgs)
#====================================================================================
def run():
    while True:
        backupData()
        try:
            ops = gonebotPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                    loop.run_until_complete(gonebotBot(op))
                    gonebotPoll.setRevision(op.revision)
        except Exception as error:
            traceback.print_tb(error.__traceback__)
if __name__ == "__main__":
    run()
