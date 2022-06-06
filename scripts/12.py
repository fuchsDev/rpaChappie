##
## automates the task of brave brownser
## 

# import the py libraries and files
from variables import *
from methods import *

# start workspace
noteBook() #check which laptop is in use
runBrave() #start the browser brave 
runUrl(linkWhats) #type the url
runUrl(linkTrello) #type the url
runUrl(linkGmail) #type the url

runUrl(linkLinx) #type the url
runLinxNewTab() #call method open newtab with linxseller in methods.py
loginLinxSeller(loginLinx, passwordLinx) #send variables to method in methods.py