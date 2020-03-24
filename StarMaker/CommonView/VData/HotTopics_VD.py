# coding=utf-8
from StarMaker.Utils.GetDevicesInfo import DevicesInfo
from StarMaker.Utils.reSource import get_mapping_from_file

package = DevicesInfo().package()
mapping_dict = get_mapping_from_file()
# ----------
# Hot Topics页面
# ----------

# HotTopics页面-Title-Text([0]English_text=Hot Topics)
HotTopicsPage_Title_Text_ClaS = "android.widget.TextView"

# HotTopics页面-HotTopics_TopicsName
Source_HotTopicsPage_HotTopics_TopicsName_IDS = "topic_name"
HotTopicsPage_HotTopics_TopicsName_IDS = package + mapping_dict[Source_HotTopicsPage_HotTopics_TopicsName_IDS]
