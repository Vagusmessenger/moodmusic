import random, os, vlc, time, sys
def clear():
	os.system('clear')

clear()

skipcounter = 0

volumecounter = 1

musicDir = "/home/osmar/Music/moodmusic/"

valid_moods =[
"happy", 
"sad", 
"angry",
"tired"]

valid_responses =[
'skip', 
'peace',
'blast it',
'turn down']

happy_list =[
"Glad to hear it!", 
"Sweet!"]

sad_list = [
"Hope you feel better, man",
"Whatever happens, happens"]

angry_list = [
"Here's some loud and abrasive music"]

tired_list = [
"Sleep well", 
'Sweet dreams']

happypics = "/home/osmar/Pictures/moodmusic/happy/ocean.jpg"
sadpics = "/home/osmar/Pictures/moodmusic/sad/City.jpg"
angrypics = "/home/osmar/Pictures/moodmusic/angry/Riot.jpg"
tiredpics = "/home/osmar/Pictures/moodmusic/tired/night.jpg"
default = "/home/osmar/Pictures/moodmusic/Space.png"

mood ='change'

while True:
	print("How are you feeling, homie?")
	mood = raw_input()
	if mood in valid_moods:

		if mood == 'happy':
			clear()
			print(random.choice(happy_list))
			os.system("gsettings set org.gnome.desktop.background picture-uri file://" + happypics)

		elif mood == 'sad':
			clear()
			print(random.choice(sad_list))
			os.system("gsettings set org.gnome.desktop.background picture-uri file://" + sadpics)

		elif mood == 'angry':
			clear()
			print(random.choice(angry_list))
			os.system("gsettings set org.gnome.desktop.background picture-uri file://"+ angrypics)

		elif mood == 'tired' or 'sleepy':
			os.system("redshift -O 2500")
			clear()
			print(random.choice(tired_list))
			os.system("gsettings set org.gnome.desktop.background picture-uri file://"+ tiredpics)
			
		mood = mood + "/"
		artist = random.choice(os.listdir(musicDir + mood))
		artist = artist + "/"
		song = random.choice(os.listdir(musicDir + mood + artist))
		song = vlc.MediaPlayer(musicDir + mood + artist + song)
		song.play()

		while True:

			response = raw_input()
			if response == 'peace':
				clear()
				os.system("gsettings set org.gnome.desktop.background picture-uri file://"+ default)
				if mood == "tired/":
					os.system('redshift -x')
					clear()
				print('Peace, homie')
				sys.exit()

			elif response == 'skip':
				clear()
				song.stop()
				song = random.choice(os.listdir(musicDir + mood + artist))
				song = vlc.MediaPlayer(musicDir + mood + artist + song)
				song.play()
				skipcounter += 1
				if skipcounter == 3:
					print('Lighten up, will ya?')
				elif skipcounter == 5:
					print('Now you\'re just being ridiculous')
					skipcounter = 0
				else:
					print('Okay. Got it')

			elif response == 'boof':
				clear()
				print('You thought I was compooter? Hah! I Am Doggo. Heckin bamboozled')

			elif response == 'blast it':
				clear()
				print("You've got it")
				song.audio_set_volume(100)

			elif response == 'turn down':
				clear()
				print("No problem")
				song.audio_set_volume((80/volumecounter))
				volumecounter +=1
				if volumecounter == 5:
					volumecounter= 1

			elif response == 'help':
				print('Here are a few commands:\n'
					'skip: to play the next song \n'
					'peace: to exit\n'
					'blast it: to max the volume\n'
					'turn down: to lower the volume\n'
					'change: to change mood')

			elif response == 'mowr':
				clear()
				print('hello, kippen <3')
				#I love you, Shannon

			elif response == 'change':
				mood = 'change'
				clear()
				song.stop()
				os.system("gsettings set org.gnome.desktop.background picture-uri file://"+ default)
				print('Okay, no worries')
				break
				
			else: 
				print("Invalid response. Try again")
				print('Valid responses:')
				for i in valid_responses:
					print(i)
	elif mood == 'change':	
		continue

		time.sleep(1)
		songLength = song.get_length()
		timeRemaining = (songLength/1000) - 1
		time.sleep(song.get_length())

 		break		

 	elif mood == 'peace':
 		clear()
 		print('Peace, homie')
 		sys.exit()

	else: 
			print("Invalid mood")
			print("Valid moods:")
			for i in valid_moods:
				print(i)
			break
