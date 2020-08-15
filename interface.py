import csv
from retrieval import DataGetter
from csvtranslator import *


def list_to_htmlselect(mylist, name):
    htmlstr = ''
    htmlstr += '<select name="' + name + '" id="' + name + '">'
    for item in mylist:
        htmlstr += '<option value=' + item + '>' + item + '</option>'
    htmlstr += '</select>'
    return htmlstr

# dg = DataGetter()

# with open('general-data/states.csv', 'r') as csvfile:
#      states = list(csv.reader(csvfile, delimiter=','))[0]

# print(states)

states = csvlist_to_list('general-data/states.csv')
datafields=csvlist_to_list('general-data/datafields.csv')
# list_to_csvlist(dg.covid_datafields, 'general-data/datafields.csv')

print('<label for="state">STATE:</label><br>')
print(list_to_htmlselect(states, 'state'))
print("<br><br>FEATURE 1<br>")
print(list_to_htmlselect(datafields, 'field'))
print("<br><br>FEATURE 2<br>")
print(list_to_htmlselect(datafields, 'field'))


# print("<select>")
# for st in states:
#     print("<option value=" + st + "> " + st + "</option>")
# print("</select>")

exit(0)
feature_str = "<select> <option value=> </select>"
print("FEATURE 1:")
print("FEATURE 2:")