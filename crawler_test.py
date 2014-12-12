from bs4 import BeautifulSoup
import requests
import os
import sys
import re
import time

# A function for making soup from a url
def make_soup(url):
    data = requests.get(url)
    content = data.text.encode("utf8", "ignore")
    soup = BeautifulSoup(content)
    return soup

#url = raw_input()
#get soup of desire url by calling function
soup = make_soup("http://joblist.bdjobs.com/jobsearch.asp?fcatId=8&icatId=")


#declare a list for storing job links
job_link = []
                    #print soup.find("div",attrs = {"class":"comp_name_text"}).text

#find the heading of jobs
titles= soup.findAll("div",attrs = {"class":"job_title_text"})
for item in titles:
    job_link.append('http://joblist.bdjobs.com/'+item.a['href']) #find the links of job

# now make soup all links of job and find the job description
while len(job_link) > 0:
    print len(job_link)
    next_url = job_link.pop(0)
    #print next_url
    soup2 = make_soup(next_url)
    job_des = soup2.findAll("div",attrs = {"class":"jr_text_d"})
    for item in job_des:
        txt= item.text.encode('cp850','replace').decode("utf8").strip()
        #print type(txt)
        print txt
