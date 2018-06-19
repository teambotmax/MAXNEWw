import requests,json

class send():
    def __init__(self, pnum):
        resp = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': pnum,'countryCode': 'TH','name': 'Noxtian','email': 'noxtian@noxt.cf','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
        print(resp.status_code)
        if resp.status_code == 200:
            self.responseNum = 0
        elif resp.status_code == 429:
            self.responseNum = 1
        else:
            self.responseNum = 2
