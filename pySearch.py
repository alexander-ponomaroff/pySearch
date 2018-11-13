#jrkong's command line searcher

import urllib
import argparse
import webbrowser
import platform
import subprocess

argparser = argparse.ArgumentParser()
argparser.add_argument("-s", action="append", help="Takes a query to search for and searches it.", nargs="*")
argparser.add_argument("-e", "--engine", help="Changes the name or alias of a search engine and sets it as the search engine for the session", nargs="+")
argparser.add_argument("-d", "--domain", help="Changes the domain extention", nargs="+")

args = argparser.parse_args()

class Search:
    def __init__(self, searchIn = None, engineIn = "google", domainIn = "ca"):
        self.searchRaw = searchIn
        self.searchQuery = ""
        self.engine = engineIn
        self.domain = domainIn
        self.url = ""
        self.searchString = "/search?q="
    #end of constructor

    #set search engine
    def setEngine(self, engineIn):
        self.engine = engineIn
    #end of setEngine

    #set domain engine
    def setDomain(self, domainIn):
        self.domain = domainIn
    #end of setdomain
    
    #set search Query
    def setQuery(self, searchIn):
        self.searchRaw = searchIn
    #end of setQuery

    def buildLink(self):
        if self.engine == "amazon":
            self.searchString = "/s/keywords="
            self.searchQuery = "%20".join(self.searchRaw)
        elif self.engine == "twitter":
            self.searchQuery = " ".join(self.searchRaw)
        else:
            self.searchQuery = "+".join(self.searchRaw)
        #end of search exceptions
        print(self.ping())
        self.url = "http://www." + self.engine + "." + self.domain + self.searchString + self.searchQuery
    #end of link building

    def ping(self):
    
        popularDomains = ["ca", "com", "de", "cn", "net", "uk", "org", "info",
                          "nl", "eu", "ru"]
    
        # Checks if the operating system is windows
        param = '-n' if platform.system().lower()=='windows' else '-c'
    
        command = ['ping', param, '1', self.engine + "." + self.domain]
    
        if subprocess.call(command) != 0:
            
            for dom in popularDomains:
                
                command = ['ping', param, '1', self.engine + "." + dom]
                
                if subprocess.call(command) == 0:
                    self.domain = dom
                    return "The domain you entered didn't work! Here's one that works: " + dom
        else:
            return "The domain you entered worked!"

    def openBrowser(self):
        webbrowser.open_new_tab(self.url)
    #end of openBrowser()
#end of Query

searchObj = Search()

if args.engine is not None:
    searchObj.setEngine(args.engine[0])

if args.domain is not None:
    searchObj.setDomain(args.domain[0])
#end of cmd args handling

for search in args.s:
    searchObj.setQuery(search)
    searchObj.buildLink()
    searchObj.openBrowser()

