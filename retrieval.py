import csv, requests
import matplotlib.pyplot as plt
import numpy as np
import math
from date import *

class DataGetter:
    def __init__(self):
        # Store basic demographic data by state
        self.censusdata = []
        self.censusdatafields = []
        with open('general-data/population.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            self.censusdatafields = next(csvreader)
            index = 0
            for row in csvreader:
                self.censusdata.append([row[0][1:]])
                self.censusdata[index].extend([int(row[1].replace(',','')), int(row[2].replace(',','')), float(row[3])])
                index+=1

        # Use arbitrary file to get important parameters
        initial_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/06-14-2020.csv'
        initial_data = requests.get(initial_url)
        lines = initial_data.text.split('\n')
        self.covid_datafields = lines[0].split(',')
        self.field_dict = {}
        for i in range(len(self.covid_datafields)):
            self.field_dict[self.covid_datafields[i]] = i

        self.states = []
        notstates = ['American Samoa', 'Diamond Princess', 'District of Columbia', 'Grand Princess', 'Guam', 'Northern Mariana Islands', 'Puerto Rico', 'Virgin Islands', 'Recovered', '']
        self.state_dict = {}
        statecounter = 0
        for i in range(1, len(lines)):
            provincestate = lines[i].split(',')[0]
            if not provincestate in notstates:
                self.states.append(provincestate)
                self.state_dict[provincestate] = statecounter
                statecounter += 1

        # Get important data from all files
        (month, day, year) = (4, 12, 2020)
        base_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/'
        day_url = base_url + url_format(month, day, year) + '.csv'
        day_data = requests.get(day_url, 'r')

        self.covid_data = []
        daycount = 0
        while day_data.status_code == 200:
            print(daycount)
            self.covid_data.append([])
            lines = day_data.text.split('\n')
            for i in range(1, len(lines)):
                statedata = lines[i].split(',')
                if len(statedata) > 1 and statedata[0] not in notstates:
                    self.covid_data[daycount].append(statedata)
            daycount+=1
            (month, day, year) = next_date(month, day, year)
            day_url = base_url + url_format(month, day, year) + '.csv'
            day_data = requests.get(day_url, 'r')

        # print(self.covid_data[0])
        # CONFIRMED, HOSPITALIZATIONS, DEATHS, RECOVERED, ACTIVE, TESTED are important features
        # ['Province_State', 'Country_Region', 'Last_Update', 'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'FIPS', 'Incident_Rate', 'People_Tested', 'People_Hospitalized', 'Mortality_Rate', 'UID', 'ISO3', 'Testing_Rate', 'Hospitalization_Rate']
        
        
        # for st in self.states:
        #     x1, x2, y1, y2 = range(len(self.covid_data)), range(len(self.covid_data)), [], []
        #     for i in range(len(self.covid_data)):
        #         feature1_str = self.covid_data[i][self.state_dict.get(st, -1)][0]
        #         feature2_str = self.covid_data[i][self.state_dict.get(st, -1)][1]

        #         if feature1_str == '':
        #             feature1_num = y1[len(y1)-1] if len(y1) > 0 else 0
        #         else: 
        #             feature1_num = float(feature1_str)
        #         if feature2_str == '':
        #             feature2_num = y2[len(y2)-1] if len(y2) > 0 else 0
        #         else:
        #             feature2_num = float(feature2_str)
        #         y1.append(feature1_num)
        #         y2.append(feature2_num)

        #     max_value = max(max(y1), max(y2))

        #     plt.plot(x1,y1,label=feature1,color='blue')
        #     plt.plot(x2,y2,label=feature2,color='red')

        #     plt.title(feature1 + ' vs. ' + feature2 + ' in ' + st)
        #     plt.xlabel('Days after 4/12/20')
        #     plt.legend()
        #     plt.savefig('images/stategraphs/' + st.lower() + '.png')

        #     print(st)
        #     plt.clf()