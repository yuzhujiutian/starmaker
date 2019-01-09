# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FS = Tools.Tools().FindSource
gms = "com.google.android"


# ----------
# Search
# ----------
# Search页面-搜索-搜索框
Source_SearchPage_Search_SearchBox_ID = "imb_search"
SearchPage_Search_SearchBox_ID = package + FS(Source_SearchPage_Search_SearchBox_ID)


