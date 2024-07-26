import requests
import json
token = 'USERGSDPJEBU5CS60BJEMMC6J0JQLLAI87SFMARAIK3BAMFNFSGPN0KTO4QI4T6I'

headers = {'Authorization': f'Bearer {token}'}
list_vac = []

def vacancy():
    for i in range(5):
        params = {'page': i,
              'per_page': 20,
              'text': 'тестировщик',
              'employment': 'full',
              'schedule': 'remote',
              'professional_roles':124,
              'currency':'RUR',
              'experience':'between1And3'}
        response = requests.get('https://api.hh.ru/vacancies',headers=headers,params=params)
        response2 = json.loads(response.text)
        if 'items' in response2 :
            try:
                for z in range(len(response2['items'])):
                    if  (response2['items'][z]['professional_roles'][0]['name']=='Тестировщик'
                    and not response2['items'][z]['has_test']
                    and 'auto' not in response2['items'][z]['name'].lower()
                    and 'мобильн' not in response2['items'][z]['name'].lower()
                    and 'lead' not in response2['items'][z]['name'].lower()
                    and '1С' not in response2['items'][z]['name'].lower()
                    and 'авто' not in response2['items'][z]['name'].lower()
                    and 'mobile' not in response2['items'][z]['name'].lower()
                    and 'нагруз' not in response2['items'][z]['name'].lower()
                    and 'нагр' not in response2['items'][z]['snippet']['requirement'].lower()
                    and 'авто' not in response2['items'][z]['snippet']['requirement'].lower()
                    and 'мобиль' not in response2['items'][z]['snippet']['requirement'].lower()):
                        list_vac.append(response2['items'][z]['id'])
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
           'HH-User-Agent': 'https://vk.com/overhear'}


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