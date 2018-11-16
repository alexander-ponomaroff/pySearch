#jrkong's command line searcher

from urllib.parse import quote
import urllib
import argparse
import webbrowser

argparser = argparse.ArgumentParser()
argparser.add_argument("-s", action="append", help="Takes a query to search for and searches it.", nargs="*")
argparser.add_argument("-e", "--engine", help="Changes the name or alias of a search engine and sets it as the search engine for the session", nargs="+")
argparser.add_argument("-d", "--domain", help="Changes the domain extention", nargs="+")

args = argparser.parse_args()

class Search:
    def __init__(self, searchIn = None, engineIn = "yahoo", domainIn = "com"):
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
        self.buildQuery()
        self.url = "http://www." + self.engine + "." + self.domain + self.searchString + self.searchQuery
    #end of link building

    def openBrowser(self):
        webbrowser.open_new_tab(self.url)        
    #end of openBrowser()
    
    def buildQuery(self):
        if self.engine == "amazon":
            self.searchString = "/s/keywords="
            self.searchQuery = "%20".join(self.searchRaw)
        elif self.engine == "twitter":
            self.searchQuery = " ".join(self.searchRaw)
        elif self.engine == "yandex":
            self.searchString = "/search/?text="
            self.searchQuery = "+".join(self.searchRaw)
        elif self.engine == "duckduckgo":
            self.searchString = "/?q="
            self.searchQuery = "+".join(self.searchRaw)
        elif self.engine == "archive":
            self.searchString = "/search.php?query="
            self.searchQuery = "+".join(self.searchRaw)
            self.domain = "org"
        elif self.engine == "boardreader":
            self.searchString = "/s/"
            self.searchQuery = "+".join(self.searchRaw)+".html"
        elif self.engine == "ask":
            self.searchString = "/web?q="
            self.searchQuery = "+".join(self.searchRaw)
        elif self.engine == "facebook":
            self.searchString = "/search/str/"
            self.searchQuery = "+".join(self.searchRaw)+"/keywords_search"
        elif self.engine == "yahoo":
            self.searchString = "/search?p="
            self.searchQuery = "+".join(self.searchRaw)
            self.engine = "search.yahoo"
        else:
            self.searchQuery = "+".join(self.searchRaw)
        #end of search exceptions
        
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
