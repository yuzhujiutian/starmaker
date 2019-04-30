# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FS = Tools.Tools().FindSource
# ----------
# Hot Topics页面
# ----------

# HotTopics页面-Title-Text([0]English_text=Hot Topics)
HotTopicsPage_Title_Text_ClaS = "android.widget.TextView"

# HotTopics页面-HotTopics_TopicsName
Source_HotTopicsPage_HotTopics_TopicsName_IDS = "topic_name"
HotTopicsPage_HotTopics_TopicsName_IDS = package + FS(Source_HotTopicsPage_HotTopics_TopicsName_IDS)







