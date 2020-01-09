import requests 

api='4976d29d2ffb43259ac94f12ff54646d'
print('Please enter one or multiple cryptocurrency symbols "separated with comma please" :')
symbol=input()
print('Please enter a start date for your time frame with this format => YYYY-MM-DD :')
sdate=input()
print(' Please enter an end date for your time frame with this format => YYYY-MM-DD :')
edate=input()
print('Please enter your preferred target currency :')
trgt=input()
url = 'http://api.coinlayer.com/timeframe?access_key = 4976d29d2ffb43259ac94f12ff54646d &start_date = sdate &end_date = edate &symbols = symbol &target=trgt'


params = {'access_key': api, 'start_date': sdate,'end_date':edate, 'symbols': symbol,'target': trgt}
r = requests.get('http://api.coinlayer.com/timeframe', params = params)
convcoin = r.json()
print (convcoin) 
