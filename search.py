
import urllib
import webbrowser

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
    
    def handleArgs(self, args):
        if args.engine is not None:
            self.setEngine(args.engine[0])

        if args.domain is not None:
            self.setDomain(args.domain[0])

        for search in args.s:
            self.setQuery(search)
            self.buildLink()
            self.openBrowser()
    #end of handleArgs
 
#end of Query
