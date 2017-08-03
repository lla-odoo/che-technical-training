import urllib
import os
print(os.getcwd())
server_url = 'http://api1.odoo.com:5001/technical-training/?token='
token = raw_input('Could you insert your token? \n')
value = urllib.urlopen(server_url + token)
zip_file = open('./resources.zip', 'wr')
zip_file.write(value.read())
print('resources.zip downloaded')
zip_file.close()
os.system('unzip -o %s/resources.zip && mv %s/src/* %s/../../' % (os.getcwd(), os.getcwd(), os.getcwd()))
print('Files unzipped')
