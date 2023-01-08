import os
username = 'Jack'
#os.chdir('/home/computer/project/project')
#os.system("scrapy crawl project --nolog")
print('Hello ' + username)
print('Loading up your daily read .....')
urls = []
with open('/home/computer/urls.txt','r') as handle:
    urls = handle.readlines()
v = 1
for read in urls:
    print('['+str(v)+'] Article : ' + read + '  ')
    v += 1