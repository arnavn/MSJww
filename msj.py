import instabot
import time
import random
import os

def main():
	bot = instabot.Bot()
	bot.login()

	pauseseconds = random.randrange(60, 90, 1)
	os.system("cp msjww.jpg msjwwcopy.jpt")

	while(True):
		bot.upload_photo("msjwwcopy.jpg", caption="#msjww19")
		time.sleep(pauseseconds)
		pauseseconds = random.randrange(60, 90, 1)
		print("Waiting: ", pauseseconds)

		os.system("rm msjwwcopy.jpg.REMOVE_ME")
		os.system("cp msjww.jpg msjwwcopy.jpg")



if __name__ == "_main_":
	main()