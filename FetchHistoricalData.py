import requests

print('Please enter a date of your choice with this format => YYYY-MM-DD :')
date=input()
print('Please enter one or multiple cryptocurrency symbols "separated with comma please" :')
symbol=input()
print('Please enter your preferred target currency :')
trgt=input()

api='4976d29d2ffb43259ac94f12ff54646d'
url = 'http://api.coinlayer.com/date? access_key = 4976d29d2ffb43259ac94f12ff54646d &symbols = symbol &target=trgt'
params = {'access_key': api, 'YYYY-MM-DD': 'date','symbols': symbol,'target': trgt}
r = requests.get('https://api.coinlayer.com/date', params = params)
convcoin = r.json()
print (convcoin) 
