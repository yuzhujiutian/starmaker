# coding=utf-8
#from Utils.GetDevicesInfo import GetPackages
from Utils import Tools
package = Tools.Tools().package()
FindSource = Tools.Tools().FindSource
# ----------
# 启动模块
# ----------

# 开屏广告
Source_OpenAdd_Link_ID = "fl_adcontainer_activity_splash"
OpenAdd_Link_ID = package + FindSource(Source_OpenAdd_Link_ID)

# 开屏广告倒计时
Source_OpenAdd_Time_Btn = "launch_timing_count"
OpenAdd_Time_Btn = package + FindSource(Source_OpenAdd_Time_Btn)

# Skip——跳过开屏
Source_Skip_OpenAdd_Btn_ID = "launch_timing_text"
Skip_OpenAdd_Btn_ID = package + FindSource(Source_Skip_OpenAdd_Btn_ID)

# 登录页——Tips（text="sing with 50,000,000+ music lovers"）
Source_StartUpHome_Tips_ID = "tv_welcome"
StartUpHome_Tips_ID = package + FindSource(Source_StartUpHome_Tips_ID)

# 登录页——说明（text=You agree to our Terms of Service & Privacy Policy）
Source_StartUpHome_Explain_ID = "tv_policy"
StartUpHome_Explain_ID = package + FindSource(Source_StartUpHome_Explain_ID)

# 登录页——Email 登录按钮
Source_Email_LogIn_Btn_ID = "img_login_left"
Email_LogIn_Btn_ID = package + FindSource(Source_Email_LogIn_Btn_ID)
Email_LogIn_Btn_R = [0.368, 0.86, 500]

# 登录页——Phone 登录按钮
Source_Phone_LogIn_Btn_ID = "img_login_middle"
Phone_LogIn_Btn_ID = package + FindSource(Source_Phone_LogIn_Btn_ID)

# 登录页——G+ 登录按钮
Source_Google_LogIn_Btn_ID = "img_login_right"
Google_LogIn_Btn_ID = package + FindSource(Source_Google_LogIn_Btn_ID)

# 登录页——Facebook 登录按钮
Source_FB_LogIn_Btn_ID = "rl_login_top"
FB_LogIn_Btn_ID = package + FindSource(Source_FB_LogIn_Btn_ID)
