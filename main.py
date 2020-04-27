#!/bin/python
# coded by sCuby07
# Buset bro lu mau recode?

class Simsimi:

	def __init__(self, url, nekot):
		self.url = url
		self.nekot = nekot

	def chatbot(self):
		you = input('\x1b[32;1m[\x1b[37m!\x1b[32;1m]\x1b[37m Your Name : ');print('\n')
		while True:
			try:
				self.ask = input('{}{}{} : '.format(ijo,you,putih))
				self.api = requests.get(self.url.format(self.ask)).text
				zx = json.loads(self.api)["simsimi_talk_set"]
				anonk = random.choice(zx["answers"])
				yuhuu = anonk["sentence"]
				print("{}SimSimi {}: {}".format(merah,putih,yuhuu))
			except KeyboardInterrupt:
				exit('{}SimSimi {}: Kaka jahat tinggalin simi:('.format(merah,putih))

	def login(self):
		os.system('clear')
		data.banner()
		print('''
\x1b[32;1m  [\x1b[37m1\x1b[32;1m]\x1b[37m Get Token
\x1b[32;1m  [\x1b[37m2\x1b[32;1m]\x1b[37m Login Tools
\x1b[32;1m  [\x1b[37m3\x1b[32;1m]\x1b[37m Report Bug \x1b[32;1m(\x1b[37mWhatsApp\x1b[32;1m)
\x1b[32;1m  [\x1b[37m4\x1b[32;1m]\x1b[37m Exit\n''')
		pil = int(input('\x1b[32;1m[\x1b[37m?\x1b[32;1m]\x1b[37m Choice : '))
		if pil == 1:
			os.system('xdg-open https://semawur.com/DB4rd;python main.py')
		elif pil == 2:
			os.system('clear')
			data.banner()
			self.token = input('\n\x1b[32;1m[\x1b[37m!\x1b[32;1m]\x1b[37m Token : ')
			self.ambil_token = requests.get(self.nekot).text
			ryu = re.findall('<div class=".*?">(.*?)</div>', self.ambil_token)
			if self.token == ryu[2]:
				self.chatbot()
			else:
				print('\x1b[31mToken Not Found!\x1b[37m')
		elif pil == 3:
			os.system('xdg-open https://wa.me/62895611982226;python main.py')
		elif pil == 4:
			exit(random.choice(["HEH ASU LU MAU GUA PUKUL?","BERTUMBUK KITA!!!"]))

try:
	import requests, json, re, os, random
	from data import data
	from base64 import *
	ijo = '\x1b[32;1m'
	putih = '\x1b[37m'
	merah = '\x1b[31m'
	run = Simsimi('https://secureapp.simsimi.com/v1/simsimi/talkset?uid=287126054&av=6.8.9.4&lc=id&cc=&tz=Asia%2FJakarta&os=a&ak=pNfLbeQT%2B0cnFY8YHQb7CNHowpg%3D&message_sentence={}&normalProb=8&isFilter=1&talkCnt=2&talkCntTotal=2&reqFilter=1&session=XZzaduTVCSqa6vMtuyFhGv9eCXiyWwKJVETZjpQjc2oLPGBN2XtpzcKRFhLukHd6EAYVWMiSGuPzQV5Vwcdmwz14&triggerKeywords=%5B%5D', b16decode('68747470733A2F2F706173746562696E2E636F6D2F634D6835626E7164'))
	run.login()
except requests.exceptions.ConnectionError:
	print('%sSimSimi %s: Nyalahin datanya kak'% (merah,putih))
