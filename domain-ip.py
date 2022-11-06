import argparse,sys,socket,colorama
from colorama import Fore, Back, Style


def main():#we use this function setup to maintain tidyness
	def argument_parsing():
		#here we crate the parser argument, we add in usage and description so users have a better understanding of the script
		parser = argparse.ArgumentParser(usage='python3 domain-ip.py', description="This script is made for finding the ip/ip's behind a domain, it also by default will print out the unique ip's seperately aswell.")
		domain_parser = argparse.ArgumentParser() # This is a small seperation this is our domain parser, this is seperated as i had to make seperate rules
		domain = parser.add_mutually_exclusive_group(required=True) #This makes one of the the options mandetory
		domain.add_argument('-domain', '--domain', '-d', '--d', help='This argument is for resolving the ips of a single domain.')
		domain.add_argument('--domain-list', '-dl', '--dl', help='This argument is for resolving the ips of a list of domains.')
		domain_args = domain_parser.parse_args([]) #Here we made it a simple call to a variable to parse arguments
		args = parser.parse_args() #Here we made it a simple call to a variable to parse arguments
		return args #returning args so wwe can call them later in the script
	args = argument_parsing()#we assign the returned value to a variable
	ip_list = []
	socket.setdefaulttimeout(10)#setting default timeout of our socket probes
	colorama.init(autoreset=True)#Initialize colorama
	if args.domain != None:#we check to see if the argument domain has been used
		address=args.domain#assigning the domain variable to one thats easier to list and makes more sense
		try:#here we try three times to connect
			ais = socket.getaddrinfo(address,0,0,0,0)
			pass
		except:
			try:
				ais = socket.getaddrinfo(address,0,0,0,0)
				pass
			except:
				try:
					ais = socket.getaddrinfo(address,0,0,0,0)
					pass
				except:#if none of the 3 probes are able to get a connection it marks the host as connection failed, which means its unreachable
					print(Fore.RED + 'Connection Failed!')
					sys.exit()
					pass
			pass
		for result in ais:#This will cycle through the output and grab all the ip's and add them to our predifined but empty list variable
			ip_list.append(result[-1][0])
			ip_list = list(set(ip_list))
		ip_list=[*set(ip_list)]
		print(Fore.BLUE + '\n[-] Host: ' + args.domain)#Here we print the domain for the user nicely to make it easy to keep track
		for ip in ip_list:#here we loop through and print all the ip's nicely to the user
			print(Fore.GREEN + ip)
			pass
	elif args.domain_list != None:#Checking to see if user supplied domain list
		domain_file = open(args.domain_list, "r")#here we open the file and assign it to a variable
		domains = domain_file.read().splitlines()#now we split the variable by new lines
		for domain in domains:#now we will loop through the domain file once again trying 3 times on each domain before having the connectin fail
			try:
				ais = socket.getaddrinfo(domain,0,0,0,0)
				pass
			except:
				try:
					ais = socket.getaddrinfo(domain,0,0,0,0)
					pass
				except:
					try:
						ais = socket.getaddrinfo(domain,0,0,0,0)
						pass
					except:
						print(Fore.RED + '\nConnection Failed!')
						pass
				pass
			for result in ais:#here we assign all the found ip's into one variable list we predifined as empty
				ip_list.append(result[-1][0])
				ip_list = list(set(ip_list))
			print(Fore.BLUE + '\n[-] Host: ' + domain)#print the host nice and neat for the user for easy logging
			for ip in ip_list:#print each ip nicely under the correct domain name for easy logging
				print(Fore.GREEN + ip)
				pass
		ip_list=[*set(ip_list)]#this lets us narrow it down to only unique results/no duplicates
		print(Fore.MAGENTA + '\n[+] Unique ips')
		for ip in ip_list:#here we print out the no duplicate list nicely for tthe user
			print(Fore.GREEN + ip)
			pass
	else:
		print(Fore.RED + 'Error!')#this is just incase the user slips by arg parse with no domain or domain list especified
		sys.exit()
	pass
main()
