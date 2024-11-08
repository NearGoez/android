import requests
from bs4 import BeautifulSoup as bs


s = requests.Session()



tutor_init = s.get('https://ipsdatax.com/tutor-login/')


login_payload = {'log': "DbenjaminDofus@gmail.com", 
                 'pwd': "214ff34fa"

        }

tutor_login = s.post(url = 'https://ipsdatax.com/tutor-login/', data = login_payload)

login_cookies = {
        'PHPSESSID'

        }

print(tutor_login.cookies)

