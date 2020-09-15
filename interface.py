import csv
from retrieval import DataGetter
from csvtranslator import *

print('Scraping data (this will take up to a minute)...')
dg = DataGetter()
print('Data ready!\n')


states = csvlist_to_list('general-data/states.csv')
datafields = csvlist_to_list('general-data/datafields.csv')

quit = False
while not quit:
    state = ''
    while not state in states:
        print('\nPlease enter a capitalized U.S. State (eg. "New York"): ')
        state = input()

    feature_num1 = 0
    feature_num2 = 0

    while not ((feature_num1-1) in range(6) and (feature_num2-1) in range(6) and not feature_num1 == feature_num2):
        print('\n_______________________________'
            '\n1.............Confirmed Cases',
            '\n2.............Recovered',
            '\n3.............Active'
            '\n4.............People Tested'
            '\n5.............People Hospitalized',
            '\n6.............Deaths',
            '\nPlease enter numbers for TWO DIFFERENT FEATURES (one argument per line):')
        feature_num1, feature_num2 = int(input()), int(input())

    print('\nEnter a filename for your graph PNG: ')
    out_filename = input()

    input_dict = {
        1: 'Confirmed',
        2: 'Recovered',
        3: 'Active',
        4: 'People_Tested',
        5: 'People_Hospitalized',
        6: 'Deaths'
    }

    dg.state_image(state, input_dict[feature_num1], input_dict[feature_num2], out_filename)

    print('\nGenerate another graph? (y/n)')
    if (input() == 'n'):
        quit = True

print('\nThanks for using COVID-simplified!')

exit(0)