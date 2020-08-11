import csv, requests
import matplotlib.pyplot as plt
import numpy as np
from date import *
# Store basic demographic data by state
censusdata = []
censusdatafields = []
with open('population.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    censusdatafields = next(csvreader)
    index = 0
    for row in csvreader:
        censusdata.append([row[0][1:]])
        censusdata[index].extend([int(row[1].replace(',','')), int(row[2].replace(',','')), float(row[3])])
        index+=1

# Use arbitrary file to get important parameters
initial_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/06-14-2020.csv'
initial_data = requests.get(initial_url)
lines = initial_data.text.split('\n')
covid_datafields = lines[0].split(',')
field_dict = {}
for i in range(len(covid_datafields)):
    field_dict[covid_datafields[i]] = i

states = []
notstates = ['American Samoa', 'Diamond Princess', 'District of Columbia', 'Grand Princess', 'Guam', 'Northern Mariana Islands', 'Puerto Rico', 'Virgin Islands', 'Recovered', '']
state_dict = {}
statecounter = 0
for i in range(1, len(lines)):
    provincestate = lines[i].split(',')[0]
    if not provincestate in notstates:
        states.append(provincestate)
        state_dict[provincestate] = statecounter
        statecounter += 1

# Get important data from all files
(month, day, year) = (4, 12, 2020)
base_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/'
day_url = base_url + url_format(month, day, year) + '.csv'
day_data = requests.get(day_url, 'r')

covid_data = []
daycount = 0
while day_data.status_code == 200:
    # print(day)
    covid_data.append([])
    lines = day_data.text.split('\n')
    for i in range(1, len(lines)):
        statedata = lines[i].split(',')
        if len(statedata) > 1 and statedata[0] not in notstates:
            covid_data[daycount].append([
                statedata[field_dict.get('People_Hospitalized', -1)],
                statedata[field_dict.get('Deaths', -1)]
            ])
    print(len(covid_data))


    
    daycount+=1
    (month, day, year) = next_date(month, day, year)
    day_url = base_url + url_format(month, day, year) + '.csv'
    day_data = requests.get(day_url, 'r')

x1, x2, y1, y2 = range(len(covid_data)), range(len(covid_data)), [], []
for i in range(len(covid_data)):
    y1.append(int(covid_data[i][state_dict.get('Massachusetts', -1)][0]))
    y2.append(int(covid_data[i][state_dict.get('Massachusetts', -1)][1]))

plt.yticks(np.arange(0, 100000, 10000))

plt.plot(x1,y1,label='hospitalizations')
plt.plot(x2,y2,label='deaths')

plt.title('Hospitalizations vs. Deaths in Massachusetts')
plt.xlabel('Days after 4/12/20')
plt.legend()


plt.savefig('images/massachusetts.png')
plt.show()


