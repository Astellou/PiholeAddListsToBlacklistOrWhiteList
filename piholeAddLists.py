import sys
import argparse
import requests
import os

PARAM_LIST = 'list'
PARAM_DELETE = 'delete'
PARAM_VERBOSE = 'verbose'


BLACKLIST_VALUE = 'b'
WHITELIST_VALUE = 'w'

PIHOLE_UPDATE_GRAVITY = 'pihole -g' 
PIHOLE_MANGEMENT_LISTS = "pihole -%s%s -nr %s"


def getListsFromList(list):

    response = requests.get(list)
    print(str(response.status_code)+ " - "+ list+"\n")

    if response.status_code != 200:
        return []

    subList = response.text.split("\n")
    return subList

def getDomainsFromList(list):

    response = requests.get(list)
    print(str(response.status_code)+ " - "+ list+"\n")

    if response.status_code != 200:
        return []

    domainsList = response.text.split("\n")
    return domainsList

def main(argv):
    global isVerbose

    print('######### MANAGE BLACKLISTS AND WHITELISTS #########')

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--'+PARAM_LIST, help="list referencing every list to add", required=True)
    parser.add_argument('-d', '--'+PARAM_DELETE,   help="needs to display every HTTP call",  required=False, action='store_true')
    args = parser.parse_args()


    deleteNeeded = ''
    if getattr(args, PARAM_DELETE):
        deleteNeeded = ' -d'
        print("----SUPPRESSION MODE ON ----\n")

    for list in getListsFromList(getattr(args, PARAM_LIST)):

        listValues = list.split(',')
        if len(listValues) == 2 and listValues[0] in [BLACKLIST_VALUE, WHITELIST_VALUE]:
       
            BorWValue = listValues[0]
            LinkList = listValues[1]

            domainsList = getDomainsFromList(LinkList)
            for domain in domainsList:
                if len(domain.strip()) > 0:
                    command = PIHOLE_MANGEMENT_LISTS % (BorWValue, deleteNeeded, domain)
                    #print(command)
                    print(os.popen(command).read())
                    

    print('######### END OF MANAGING #########\n')

    print('######### UPDATE GRAVITY #########\n')
    print(os.popen(PIHOLE_UPDATE_GRAVITY).read()+"\n")
    print('######### END UPDATE GRAVITY #########\n')


    print('######### DONE :) #########\n')



if __name__ == "__main__":
    main(sys.argv[1:])