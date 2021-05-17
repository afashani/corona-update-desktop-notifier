import datetime
import time
import json
import urllib.request as request
from plyer import notification


with request.urlopen("https://www.hpb.health.gov.lk/api/get-current-statistical") as response:

#try:
#    getdata = requests.get("https://www.hpb.health.gov.lk/api/get-current-statistical")
#except:
#    print("You are offline!")

#print(getdata)  >>> <Response [200]>

    if response != None :
    #dataa = getdata.json()['success']
        source = response.read()
        m_dict = json.loads(source)
        while True:
            notification.notify(
                title = "COVID-19 Update on {}".format(datetime.date.today()),
                message = "Total Cases: {totalcases}\nToday Cases: {todaycases}\nTotal in Hospitals:{inhospital}\nTotal Deaths:{totaldeaths}\nTotal Recovered:{recovered}".format(
                        totalcases = m_dict["data"]["local_total_cases"],
                        todaycases = m_dict["data"]["local_new_cases"],
                        inhospital = m_dict["data"]["local_total_number_of_individuals_in_hospitals"],
                        totaldeaths = m_dict["data"]["local_deaths"],
                        recovered = m_dict["data"]["local_recovered"]

                ),
                app_name = "COVID ALERT",
                app_icon = "{}".format("D:\\PROJECTS\\covid_desktop_notifier\\alarm.ico"),
                timeout = 5,
                ticker = "COVID ALERT",
                toast = False,
            )
            time.sleep(60*60*6)