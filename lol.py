import requests, os, random, string

url = "https://alcaponerd.website//acesofacebook.php?api=1&lan=facebookapphk&ht=2"

email_address = ['@yahoo.com', '@gmail.com', '@hotmail.com', '@hotmail.co.uk', '@yahoo.co.uk', '@outlook.com', '@itunes.com']

chars = string.ascii_letters + string.digits + '!@#()^$£"*'

with open("names.txt", "r") as file:
	names = file.read().split()

with open("passwords.txt", "r") as file:
	passwords = file.read().split()
	
while True:
	name = random.choice(names)
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + random.choice(email_address)
	password = random.choice(passwords)
	password += ''.join(random.choice(chars) for i in range(random.randint(0,2)))

	requests.post(url, allow_redirects=False, data={
		"email" : username, 
		"pass" : password
		})
	print(username + " - " + password)
