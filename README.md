# Pihole Add Lists To Blacklist Or WhiteList

@Credits : #Example lists from https://github.com/Levi2288/AdvancedBlockList



Récupération du fichier : 
```
wget https://raw.githubusercontent.com/Astellou/PiholeAddListsToBlacklistOrWhiteList/main/piholeAddLists.py
```

Install python : 


```
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-requests
sudo apt-get install python3-validators
sudo apt install sqlite3
```


Help : 

```
/etc/pihole $ sudo -u pihole python3 python piholeAddLists.py -h
````



Launch where the database is located, by default /etc/pihole/
with list in parameters to add whitelist and blacklist :
```
/etc/pihole $ sudo -u pihole python3 piholeAddLists.py -l https://raw.githubusercontent.com/Astellou/PiholeAddListsToBlacklistOrWhiteList/main/List.txt
```



Launch with list in parameters to delete whitelist and blacklist (-l -d) :
```
/etc/pihole $ sudo -u pihole python3 piholeAddLists.py -l https://raw.githubusercontent.com/Astellou/PiholeAddListsToBlacklistOrWhiteList/main/List.txt -d
```


