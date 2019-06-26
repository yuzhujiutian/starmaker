# encoding=utf-8
import os
import re


class AndroidProGuardMapping:

    def __init__(self, ProGuardFile=None):
        self.mappingTable = None
        if ProGuardFile and os.path.isfile(ProGuardFile):
            self.mappingTable = open(ProGuardFile, 'r').read()

    def getId(self, ProGuardFileResId):
        realId = ProGuardFileResId
        try:
            if self.mappingTable:
                r_realId = re.findall("R.id." + "(.*)""'", re.findall(
                    "R.id." + realId + " -> " + "(.*)", self.mappingTable).__str__())[0]

                return r_realId
            else:
                return realId
        except:
            return realId
