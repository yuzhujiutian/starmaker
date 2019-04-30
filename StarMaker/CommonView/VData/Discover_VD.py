# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FS = Tools.Tools().FindSource
gms = "com.google.android"


# ----------
# Discover
# ----------
# Discover页-功能入口-通用ID([0]Events/[1]SM Celeb/[2]SM Talent)
Source_DiscoverPage_FunctionEntry_Common_IDS = "txt_title"
DiscoverPage_FunctionEntry_Common_IDS = package + FS(Source_DiscoverPage_FunctionEntry_Common_IDS)


