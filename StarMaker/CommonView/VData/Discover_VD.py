# coding=utf-8
from StarMaker.Utils.GetDevicesInfo import DevicesInfo
from StarMaker.Utils.reSource import get_mapping_from_file

package = DevicesInfo().package()
mapping_dict = get_mapping_from_file()
gms = "com.google.android"


# ----------
# Discover
# ----------
# Discover页-功能入口-通用ID([0]Events/[1]SM Celeb/[2]SM Talent)
Source_DiscoverPage_FunctionEntry_Common_IDS = "txt_title"
DiscoverPage_FunctionEntry_Common_IDS = package + mapping_dict[Source_DiscoverPage_FunctionEntry_Common_IDS]
