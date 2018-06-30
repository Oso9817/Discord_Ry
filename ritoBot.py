from urllib.request import urlopen
import json, textwrap

class discord_rito():
    #d = grab_weather()
    def __init__(self, champEntry):
        #self.dummyID = None
        #self.dummyName = None
        self.ritokey = ''
        self.string = None
        self.allyRaw = None
        self.j = None
        self.tipsClean = None
        self.allyTips0 = str()
        self.summName = None
        self.skillP = None
        self.skillQ = None
        self.skillW = None
        self.skillE = None
        self.skillR = None
        self.skillKit = None      
        #self.getID()
        self.getChamp(champEntry)

    def requestUrl(self, url):
        response = urlopen(url)
        string = response.read().decode('utf-8')
        self.j = json.loads(string)

    
    #def getID(self, userName):
        #self.requestUrl('https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{0}?api_key=RGAPI-897e41cd-29a9-4711-952f-2f60fffad2b0'.format(userName))
        #self.dummyID = self.j['id']
        #self.dummyName = self.j['name']

    def getChamp(self, champEntry):
        self.requestUrl('https://na1.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&tags=allytips&tags=enemytips&tags=passive&tags=spells&dataById=false&api_key=' + self.ritokey)
        champEntry = champEntry.title()
        champEntry1 = champEntry
        champEntry = champEntry.replace(' ', '')
        if isinstance(champEntry, str):
            try:
                if champEntry == 'Wukong':
                    champEntry = 'MonkeyKing'
    
                if champEntry == 'Kogmaw':
                    champEntry = 'KogMaw'
    
                if champEntry == 'Reksai':
                    champEntry = 'RekSai'
            except Exception as msg:
                print('Something went wrong with the special champions {0}'.format(msg))

        if self.j['data'][champEntry]['key'] == champEntry:
            try:
                self.skillP = self.j['data'][champEntry]['passive']['sanitizedDescription']
                self.skillQ = self.j['data'][champEntry]['spells'][0]['sanitizedDescription']        
                self.skillW = self.j['data'][champEntry]['spells'][1]['sanitizedDescription']        
                self.skillE = self.j['data'][champEntry]['spells'][2]['sanitizedDescription']        
                self.skillR = self.j['data'][champEntry]['spells'][3]['sanitizedDescription']
                self.skillKit = "\n{0}\n P - {1}\n Q - {2}\n W - {3}\n E - {4}\n R - {5}".format(champEntry1, self.skillP, self.skillQ, self.skillW, self.skillE, self.skillR)
            except Exception as msg:
                print(msg)
            try:
                for i in range(0,len(self.j['data'][champEntry]['allytips'])):
                    self.allyTips0 += self.j['data'][champEntry]['allytips'][i].replace('.', '.\n').replace('!', '!\n').replace("\n ", "\n")
                wrapper = textwrap.TextWrapper(initial_indent=" ", subsequent_indent="    ")
                for line in wrapper.wrap(self.allyTips0):
                    print(line)
                self.allyTips1 = line
                
                self.allyTips0 = champEntry
                print(champEntry)

                    
            except Exception as e:
                raise e

            except Exception as e:
                raise e
discord_rito('Thresh')