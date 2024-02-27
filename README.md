# Pihole Add Lists To Blacklist Or WhiteList

@Credits : #Example lists from https://github.com/Levi2288/AdvancedBlockList

Goal ? Easily add list to blacklist and whitelite domains

Install dependecies : 

```
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-requests
sudo apt-get install python3-validators
sudo apt install sqlite3
```

go to the directory /etc/pihole: 
```
cd /etc/pihole
```


get the file : 
```
wget https://raw.githubusercontent.com/Astellou/PiholeAddListsToBlacklistOrWhiteList/main/piholeAddLists.py
```



Help : 

```
sudo -u pihole python3 python piholeAddLists.py -h
````



Launch where the database is located, by default /etc/pihole/
with list in parameters to add whitelist and blacklist :
```
sudo -u pihole python3 piholeAddLists.py -l https://raw.githubusercontent.com/Astellou/PiholeAddListsToBlacklistOrWhiteList/main/List.txt
```



Launch with -d in parameters to delete whitelist :
```
sudo -u pihole python3 piholeAddLists.py -l https://raw.githubusercontent.com/Astellou/PiholeAddListsToBlacklistOrWhiteList/main/List.txt -d
```


