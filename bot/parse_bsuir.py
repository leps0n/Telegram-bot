import requests

URL_teacher = 'https://journal.bsuir.by/api/v1/employees'
URL_schedule = 'https://journal.bsuir.by/api/v1/studentGroup/schedule?studentGroup=830501'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.77 YaBrowser/20.11.0.817 Yowser/2.5 Safari/537.36'}
def get_html(url, params=None):
    response = requests.get(url, headers=HEADERS, params=params)
    return response

def parse_teacher():
    str = 'Анисимов Владимир Яковлевич'
    list = str.split(' ')
    flag = 0
    response=get_html(URL_teacher)
    if get_html(URL_teacher).ok:
        for i in range(815):
            if response.json()[i]['lastName'] == list[0]:
                flag = flag + 1
            if response.json()[i]['firstName'] == list[1]:
                flag = flag + 1
            if response.json()[i]['middleName'] == list[2]:
                flag = flag + 1
            if flag == 3:
                print('Должность: '+response.json()[i]['rank']+'\nКафедра: '+''.join(response.json()[i]['academicDepartment']))
            flag = 0
            i = i + 1

def parse_schedule():
    response = get_html(URL_schedule)
    global schedule
    lis = list()
    if get_html(URL_schedule).ok:
        # print(response.json())
        for k in range(0,5):
            lis.append(response.json()['schedules'][k]['weekDay'] + ' | Номер недели: ' + str(response.json()['currentWeekNumber']))
            for i in range(0,len(response.json()['schedules'][k]['schedule'])):
                for j in range(0,len(response.json()['schedules'][k]['schedule'][i]['weekNumber'])):
                    if response.json()['schedules'][k]['schedule'][i]['weekNumber'][j] == response.json()['currentWeekNumber']:
                        string = str(response.json()['schedules'][k]['schedule'][i]['subject']+
                            ' | '+response.json()['schedules'][k]['schedule'][i]['lessonType']+
                            ' | '+''.join(response.json()['schedules'][k]['schedule'][i]['auditory'])+
                            ' | '+response.json()['schedules'][k]['schedule'][i]['lessonTime']
                            )
                        lis.append(string)
            lis.append('\n')
    schedule = '\n'.join(lis)
    return schedule
parse_schedule()