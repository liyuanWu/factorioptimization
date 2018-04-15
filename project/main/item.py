import os
import json
from . import itemMetaConfig

class BaseItem(object):
    def __init__(self,json):
        self._json = json
        self.name = json[itemMetaConfig.ITEM_NAME]

    def getFieldWithKeys(self,keys=()):
        """
        currently only support to access dictionary
        """
        currentField = self._json
        for k in keys:
            try:
                currentField = currentField[k]
            except KeyError:
                print("Error accessing {} at {}: {} has no key {}".format(keys,k,currentField,k))
                break
        return currentField
    
    def __str__(self):
        return '<BaseItem:{}>'.format(self.name)

    def __repr__(self):
        return self.__str__()


class Item(BaseItem):
    def __init__(self,json):
        super().__init__(json)
        self.type = json[itemMetaConfig.ITEM_PROTOTYPE]

class BaseFactory(object):
    def __init__(self,loadDir,itemClass = BaseItem):
        self._allItemDict = {}
        allJsonFileList = filter(lambda s: os.path.splitext(s)[-1] == '.json' , os.listdir(loadDir))
        addDir = lambda s: os.path.join(loadDir,s)
        for jsonFileName in allJsonFileList:
            try:
                with open(addDir(jsonFileName),'r') as jsonFileIO:
                    j = json.load(jsonFileIO)
                    item = itemClass(j)
                    self._allItemDict[item.name] = item
            except Exception as e:
                print("{}: Failed to load {}".format(e,addDir(jsonFileName)))
                continue
        
    def __len__(self):
        return len(self._allItemDict)

    def getItem(self,name):
        if name in self._allItemDict:
            return self._allItemDict[name]
        else:
            return None

class ItemFactory(BaseFactory):
    def __init__(self):
        super().__init__(itemMetaConfig.ITEM_JSON_DIRECTORY,itemClass=Item)
        self._allTypeDict = {}
        for item in self._allItemDict.values():
            typeName = item.type
            if typeName in self._allTypeDict:
                self._allTypeDict[typeName].append(item)
            else:
                self._allTypeDict[typeName] = [item]

    def getItemWithType(self,typeName):
        if typeName in self._allTypeDict:
            return self._allTypeDict[typeName]
        else:
            return None

class TechFactory(BaseFactory):
    def __init__(self):
        super().__init__(itemMetaConfig.TECH_JSON_DIRECTORY)