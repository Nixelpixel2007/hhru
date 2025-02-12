import requests
import json
token = 'USERVSIE7MP6JNBL7RR95NU80S2OG2HPSMVSMTJUCKLKB34QVMEF1QTI91210F14'

headers = {'Authorization': f'Bearer {token}'}
list_vac = []

def vacancy():
    for i in range(200):
        params = {'page': i,
              'per_page': 20,
              'text': 'инженер',
              'employment': 'full',
              'schedule': 'fullDay',
              'currency':'RUR',
              'area':2,
              'experience':'between1And3'}
        response = requests.get('https://api.hh.ru/vacancies',headers=headers,params=params)
        response2 = json.loads(response.text)
        if 'items' in response2 :
            try:
                for z in range(len(response2['items'])):
                    if  ('инженер' in response2['items'][z]['professional_roles'][0]['name'].lower()
                        and response2['items'][z]['area']['name']=='Санкт-Петербург'
                        and 'инженер-эколог' not in response2['items'][z]['name'].lower()
                        and response2['items'][z]['professional_roles'][0]['id'] in ['48','174','46','47']):
                        list_vac.append(response2['items'][z]['id'])
                        print(response2['items'][z]['area']['name'])
                 #       print(response2['items'][z]['professional_roles'])
                        print('id vacancy',response2['items'][z]['id'],'z',z,'i',i)
                        print(response2['items'][z]['name'])
                        print(response2['items'][z]['alternate_url'])
                        print(response2['items'][z]['snippet']['requirement'])
                        print(response2['items'][z]['schedule']['name'])
                        print(response2['items'][z]['professional_roles'][0]['name'])
                        print(response.status_code)
                        print(response2['items'][z]['has_test'])
                        print(response2['items'][z]['salary'])
                        print('--------------------------------------')
            except: 'da'



def otclic():
    headers2 = {'Authorization': f'Bearer {token}',
           'HH-User-Agent': 'https://t.me/source_code'}


    for i in list_vac:

        params2 = {'resume_id':'b548ce02ff0b2f52c00039ed1f453950323641',
                   'vacancy_id':i,
                   'message':'Здравствуйте, заинтересовала Ваша вакансия, хотелось бы получить обратную связь'}
        response3 = requests.post('https://api.hh.ru/negotiations',headers=headers2,params=params2)
        print(response3.status_code)


vacancy() ### показывает вакансии
# otclic() # Если хочешь запустить отклик убери '#' перед otclic()



print(list_vac)   # список id вакансий по которым будет едти отклик
print(len(list_vac)) # кол-во найденных вакансий