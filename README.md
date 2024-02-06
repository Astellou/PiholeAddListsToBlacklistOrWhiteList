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
```


Help : 

```
  python piholeAddLists.py -h
````



Launch with list in parameters to add whitelist and blacklist :
```
python3 piholeAddLists.py -l https://raw.githubusercontent.com/Astellou/PiholeAddListsToBlacklistOrWhiteList/main/List.txt
```



Launch with list in parameters to delete whitelist and blacklist (-l -d) :
```
python3 piholeAddLists.py -l https://raw.githubusercontent.com/Astellou/PiholeAddListsToBlacklistOrWhiteList/main/List.txt -d
```


