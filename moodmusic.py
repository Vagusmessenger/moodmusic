import random, os, vlc, time, sys

musicDir = "/home/osmar/Music/moodmusic/"

print("How are you feeling, homie?")

valid_moods =[
"happy", 
"sad", 
"angry"]

happy_list =[
"Glad to hear it!", 
"Sweet!"]

sad_list = [
"Hope you feel better, man",
"Whatever happens, happens"]

angry_list = [
"Here's some loud and abrasive music"]

happypics = "/home/osmar/Pictures/moodmusic/happy/ocean.jpg"
sadpics = "/home/osmar/Pictures/moodmusic/sad/City.jpg"
angrypics = "/home/osmar/Pictures/moodmusic/angry/Riot.jpg"
default = "/home/osmar/Pictures/moodmusic/Space.png"


while True:
	mood = raw_input()
	if mood in valid_moods:
		if mood == 'happy':
			print(random.choice(happy_list))
			os.system("gsettings set org.gnome.desktop.background picture-uri file://" + happypics)
		elif mood == 'sad':
			print(random.choice(sad_list))
			os.system("gsettings set org.gnome.desktop.background picture-uri file://" + sadpics)	
		elif mood == 'angry':
			print(random.choice(angry_list))
			os.system("gsettings set org.gnome.desktop.background picture-uri file://"+ angrypics)
		mood = mood + "/"
		artist = random.choice(os.listdir(musicDir + mood))
		artist = artist + "/"
		song = random.choice(os.listdir(musicDir + mood + artist))
		song = vlc.MediaPlayer(musicDir + mood + artist + song)
		song.play()
		while True:
			print("Would you like to exit? [y/n]")
			response = raw_input()
			if response == 'y':
				os.system("gsettings set org.gnome.desktop.background picture-uri file://"+ default)
				print('Peace, homie')
				sys.exit()
			elif response == 'n':
				song.stop()
				song = random.choice(os.listdir(musicDir + mood + artist))
				song = vlc.MediaPlayer(musicDir + mood + artist + song)
				song.play()
			else: 
				print("Invalid response. Try again")

		
		time.sleep(1)
		songLength = song.get_length()
		timeRemaining = (songLength/1000) - 1
		time.sleep(song.get_length())

 		break
		
	else: 
		print("invalid mood")
		print("Valid moods:")
		for i in valid_moods:
				print(i)
		break
