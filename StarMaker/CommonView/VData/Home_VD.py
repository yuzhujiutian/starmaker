# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FindSource = Tools.Tools().FindSource
# ----------
# 首页
# ----------

# 首页顶部StarMaker标识
Source_HomePage_StarMaker_ID = "bc0"
HomePage_StarMaker_ID = package + FindSource(Source_HomePage_StarMaker_ID)

# ----------
# 1>首页引导
# ----------

# 首页 New Feature 引导（Only for your taste. Hope you love them.）
HomePage_NewFeature_AU = "new UiSelector().text(\"Only for your taste. Hope you love them.\")"
# HomePage_NewFeature_Class = "android.widget.TextView"

# 首页 Ranking 引导①（text="Ranking and Hashtag are moved here"）
Source_HomePage_Guide_ID = "content_tv"
HomePage_Guide_ID = package + FindSource(Source_HomePage_Guide_ID)

# ----------
# 2>首页五Tab
# ----------

# 首页Tab([0]feed流/[1]互娱页/[2]点唱页/[3]消息页/[4]个人页)
Home_Tab_Cla = "android.support.v7.app.ActionBar$Tab"
# Home_Tab_Cla = "android.support.v7.app.a$c"

# 选择发布类型([0]Album/[1]Camera/[2]Text/[3]Sing/[4]关闭)
PostType_ClaS = "android.widget.ImageView"
