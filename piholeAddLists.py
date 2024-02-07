import sys
import argparse
import requests
import os
import validators
from datetime import datetime
import sqlite3



PARAM_LIST = 'list'
PARAM_DELETE = 'delete'
PARAM_VERBOSE = 'verbose'


BLACKLIST_VALUE = 'b'
WHITELIST_VALUE = 'w'

PIHOLE_UPDATE_GRAVITY = 'pihole -g' 
PIHOLE_MANGEMENT_LISTS = "pihole -%s%s -nr %s > /dev/null"
PIHOLE_MAX_VALUES_ONETIME = 5000


GRAVITYDB="/etc/pihole/gravity.db"



def getListValuesFromCall(url):
    response = requests.get(url)
    print(str(response.status_code)+ " - "+ url)

    if response.status_code != 200:
        return []

    listValues = response.text.split("\n")
    return listValues


def getListsFromList(list):
    return getListValuesFromCall(list)



def getDomainsFromList(list):
    domainsListRaw = getListValuesFromCall(list)
    domainsList = []
    print("%d values from raw list" % (len(domainsListRaw)))
    for domain in domainsListRaw:
        if len(domain.strip()) > 0 and validators.domain(domain.strip()) == True:
            domainsList.append(domain.strip())

    return domainsList

def getGroupedDomains(domainsList):
    indexMin = 1
    indexMax = indexMin+PIHOLE_MAX_VALUES_ONETIME
    currentGroup = 1
    domainsListGrouped = []
    while indexMax-PIHOLE_MAX_VALUES_ONETIME < len(domainsList):
        arrayTemp = domainsList[indexMin:indexMax]
        domainsListGrouped.insert(currentGroup, ' '.join(arrayTemp))

        indexMin = indexMax+1
        indexMax = indexMin+PIHOLE_MAX_VALUES_ONETIME



    return domainsListGrouped

def main(argv):
    global isVerbose

    print('\n######### MANAGE BLACKLISTS AND WHITELISTS #########')

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--'+PARAM_LIST, help="list referencing every list to add", required=True)
    parser.add_argument('-d', '--'+PARAM_DELETE,   help="needs to display every HTTP call",  required=False, action='store_true')
    args = parser.parse_args()

    # CHECK IF DELETE OR ADD (DEFAULT)
    deleteNeeded = False
    if getattr(args, PARAM_DELETE):
        deleteNeeded = True
        print("----SUPPRESSION MODE ON ----\n")


    now = datetime.now()
    print("start = ", now)



    sqliteConnection = ''
    try:
        print('\n######### DATABASE CONNECTION #########')
        print(GRAVITYDB)
        sqliteConnection = sqlite3.connect(GRAVITYDB)
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")


    except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
            sys.exit()
 
    countErrors = 0
    for list in getListsFromList(getattr(args, PARAM_LIST)):

        
        # CHECK THE FORMAT 'w, url' or 'b, url'
        listValues = list.split(',')
    
        if len(listValues) == 2 and listValues[0] in [BLACKLIST_VALUE, WHITELIST_VALUE]:
        
            typeId = 1 if listValues[0] == 'b' else 0
            LinkList = listValues[1]

            # ALL DOMAINS FROM THE LIST WITHOUT EMPTY ONES
            domainsList = getDomainsFromList(LinkList)
            compteur = 0
            for domain in domainsList:
            
                sqlite_Query = ''
                if deleteNeeded == True:
                    sqlite_Query = 	"DELETE FROM domainlist WHERE domain = '%s' AND type = %d;" % (domain, typeId)
                elif deleteNeeded == False:
                    sqlite_Query = 	"INSERT INTO domainlist (domain, type, comment) VALUES ('%s', %d, '');" % (domain, typeId)
                    
                try:
                    cursor.execute(sqlite_Query)
                    compteur += 1
                except sqlite3.Error as error:
                    countErrors += 1
                    #print(domain+' is already in database')

                # "DELETE FROM domainlist WHERE domain = '${domain}' AND type = ${typeId};"
                # "INSERT INTO domainlist (domain,type,comment) VALUES ('${domain}',${typeId},'${comment}');"
            print("\nvalues updated : %d / %d" % (compteur, len(domainsList)))
            print("commit en cours")
            sqliteConnection.commit()	
            print("commit en done\n")
            


    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

    print('######### END OF MANAGING #########\n')



    print(' /!\\ NEED TO UPDATE GRAVITY /!\\ \n')


    now = datetime.now()
    print("end = ", now)

if __name__ == "__main__":
    main(sys.argv[1:])