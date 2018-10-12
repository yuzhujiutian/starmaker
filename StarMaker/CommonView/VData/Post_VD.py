# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FindSource = Tools.Tools().FindSource
# ----------
# 1>发布专辑
# ----------

# ----------
# 2>发布图片
# ----------

# ----------
# 3>发布短文
# ----------

# ----------
# 4>发布作品
# ----------

# 录制准备页——START
Source_RecordStart_ID = "record_btn"
RecordStart_ID = package + FindSource(Source_RecordStart_ID)
RecordStart_ID_R = [0.503, 0.882, 500]

# 录制页——剩余时间(text=03:36)
Source_RecordTime_ID = "record_time_tv"
RecordTime_ID = package + FindSource(Source_RecordTime_ID)

# 发布预览页——POST
Source_PostBtn_ID = "btn_post"
PostBtn_ID = package + FindSource(Source_PostBtn_ID)

# 发布编辑页——SEND
Source_EditSend_ID = "btn_next"
EditSend_ID = package + FindSource(Source_EditSend_ID)

# 评分页——DONE
Source_ScoreDone_ID = "tv_done"
ScoreDone_ID = package + FindSource(Source_ScoreDone_ID)

