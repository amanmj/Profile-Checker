import requests

codeforce = 'http://codeforces.com/profile/'
codechef = 'http://www.codechef.com/users/'
facebook = 'http://www.facebook.com/'
quora = 'http://www.quora.com/'
github = 'http://github.com/'

sites = [facebook,quora,codechef,codeforce,github]

def printChoices():
	print '1. Facebook'
	print '2. Quora'
	print '3. Codechef'
	print '4. Codeforces'
	print '5. Github'
	print '6. Check for all'

def checkSite(currentSite):
	r = requests.get(currentSite)
	if (r.status_code == 200):
		print 'Copy-paste url in web-browser'
		print currentSite
	else:
		print 'Check the username'
		print 'It is not found'

printChoices();
choice = int(raw_input('For which website you want to search the username?(Input the number of website): '))
x = raw_input('Enter the username : ')

if(choice > len(sites)+1):
	print 'Error 404!! Choice not available'
elif(choice == len(sites)+1):
	for site in sites:
		currentSite = site + x
		checkSite(currentSite)
else:
	currentSite = sites[choice-1] + x
	checkSite(currentSite)
