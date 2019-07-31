# encoding=utf-8
import os
import re


class AndroidProGuardMapping:

    def __init__(self, ProGuardFile=None):
        self.mappingTable = None

        if ProGuardFile is not None and os.path.isfile(ProGuardFile):
            self.mappingTable = open(ProGuardFile, 'r').read()

    def getId(self, ProGuardFileResId):
        realId = ProGuardFileResId

        if self.mappingTable:
            realId = re.findall("R.id." + "(.*)""'", re.findall(
                "R.id." + ProGuardFileResId + " -> " + "(.*)", self.mappingTable).__str__())[0]

        return realId
