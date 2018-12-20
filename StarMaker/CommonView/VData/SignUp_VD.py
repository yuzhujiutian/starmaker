# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
FS = DevicesInfo().package() + Tools.Tools().FindSource
gms = "com.google.android"
# ----------
# 注册模块
# ----------

# ----------
# 1>Email 注册
# ----------

# SignUp Tips（text=输入邮箱/"Verifying your email address …"/"Sent!"/"Open the email and confirm your email address"）
Source_SignUp_Tips_ID = "com_accountkit_title"
SignUp_Tips_ID = FS(Source_SignUp_Tips_ID)

# SignUp 选择账号以继续（accessibility id=Name）
Select_AN_IDS = gms + ".gmscredential_picker_options"

# SignUp 以上都不是
NoneOfThem_Btn_ID = gms + ".gmscancel"

# SignUp 输入框
Source_SignUp_Input_Box_ID = "com_accountkit_email"
SignUp_Input_Box_ID = FS(Source_SignUp_Input_Box_ID)

# SignUp 下一步
Source_SignUp_Next_Btn_ID = "com_accountkit_next_button"
SignUp_Next_Btn_ID = FS(Source_SignUp_Next_Btn_ID)

# SignUp 报错信息
Source_SignUp_InputEmail_Error_ID = "textinput_error"
SignUp_InputEmail_Error_ID = FS(Source_SignUp_InputEmail_Error_ID)

# SignUp 打开邮箱
Source_SignUp_OpenEmail_ID = "com_accountkit_check_email_button"
SignUp_OpenEmail_ID = FS(Source_SignUp_OpenEmail_ID)

# SignUp 重发邮件
Source_SignUp_ResendEmail_ID = "com_accountkit_retry_email_button"
SignUp_ResendEmail_ID = FS(Source_SignUp_ResendEmail_ID)

# Gmail 开启自动同步
Gmail_AutoSynchronization_ID = gms + ".gmconversation_tip_text"

# Gmail 选择会话
Gmail_SelectSession_IDS = gms + ".gmthread_list_view"

# Gmail 登录邮件——继续
Gmail_Confirm_Xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View"

# Gmail 登录邮件——Tips（message:"登录失败。"/"登录 Music App"/"你已登录"）
Gmail_ConfirmTips_Xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]"

# Gmail 登录邮件——登录/打开应用
Gmail_LogIn_Xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.widget.Button"


