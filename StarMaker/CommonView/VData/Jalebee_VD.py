# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FS = Tools.Tools().FindSource
# ----------
# Jalebee首页
# ----------
# Jalebee首页底部按钮([0]Home/[1]Party/[2]Message/[3]Me)
Source_Jalebee_MainTab_Common_IDS = "tab_name"
Jalebee_MainTab_Common_IDS = package + FS(Source_Jalebee_MainTab_Common_IDS)

# Jalebee首页内容Tab([0]FOLLOWING/[1]POPULAR)
Source_Jalebee_FeedTab_Common_IDS = "tv_tab_title"
Jalebee_FeedTab_Common_IDS = package + FS(Source_Jalebee_FeedTab_Common_IDS)
