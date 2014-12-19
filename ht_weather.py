from bs4 import BeautifulSoup
import re
import requests


def get_content(url):
    f = requests.get(url)
    content = f.text.encode("utf8", "ignore")
    return content


    
my_city = "Dhaka"
my_mode = "xml"
num_of_days = 3
url = "http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&mode={mode}&units=metric&cnt={num_days}".format(city = my_city, mode = my_mode, num_days = num_of_days)

info = get_content(url)
date = re.findall(r'<time day="(.*?)">',info)

temperature_dhaka = re.findall(r'<temperature (.*?) (.*?) (.*?) (.*?) (.*?) (.*?)/>', info)
humidity_dhaka = re.findall(r'<humidity value="(.*?)" ', info)




message = """
<html>
<head><title>Weather forecasting</title></head>
<body bgcolor="#00CED1">
<h1 align = center> This is a weather forecasting site</h1>
<h3> Weather forecast for %r is: </h3>
<ul>
<li>
temperature will be:  %r
</li>
<li>Humidity will be:  %r
</li>
</ul>
</br> </br>

<hr>


<h3> Weather forecast for %r is: </h3>
<ul>
<li>
temperature will be:  %r
</li>
<li>Humidity will be:  %r
</li>
</ul>
</br> </br>
<hr>


<h3> Weather forecast for %r is: </h3>
<ul>
<li>
temperature will be:  %r
</li>
<li>Humidity will be:  %r
</li>
</ul>
</br> </br>
<hr>
""" %(date[0],temperature_dhaka[0], humidity_dhaka[0],date[1],temperature_dhaka[1], humidity_dhaka[1],date[2],temperature_dhaka[2], humidity_dhaka[2])

f2 = open('ht_weather_display.html','w')
f2.write(message)
f2.close()

print "Yes, Successfully done your weather forecasting report"


    
    