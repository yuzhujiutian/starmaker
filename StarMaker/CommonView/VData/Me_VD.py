# coding=utf-8
from StarMaker.Utils.GetDevicesInfo import DevicesInfo
from StarMaker.Utils.reSource import get_mapping_from_file

package = DevicesInfo().package()
mapping_dict = get_mapping_from_file()
gms = "com.google.android"

# ----------
# StartMaker的Me页面
# ----------
# 首页Me的个人经验值
MePage_Tab_MeExperience_Class = "android.widget.TextView"

# My Level 的返回到Me页面
Source_Mylevel_BackButton_Class = "android.widget.ImageButton"
