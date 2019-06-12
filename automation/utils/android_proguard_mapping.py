#encoding=utf-8
import os
import re

class AndroidProguardMapping:

    def __init__(self, proguardFile=None):
        self.mappingTable = None

        if proguardFile != None and os.path.isfile(proguardFile):
            self.mappingTable = open(proguardFile, 'r').read()

    def getId(self, proguardResId):
        realId = proguardResId

        if self.mappingTable != None:
            realId = re.findall("R.id." + "(.*)""'", re.findall(
                "R.id." + proguardResId + " -> " + "(.*)", self.mappingTable).__str__())[0]

        return realId
