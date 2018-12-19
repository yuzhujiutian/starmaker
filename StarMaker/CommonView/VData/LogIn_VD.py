# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FindSource = Tools.Tools().FindSource
gms = "com.google.android"
FS = package + FindSource
# ----------
# 登录模块
# ----------

# ----------
# 1>Email 登录
# ----------

# Email 登录弹窗——登录
EmailWindow_LogIn_Btn_Class = "android.widget.TextView"

# Email 登录弹窗——注册
EmailWindow_SignUp_Btn_Class = "android.widget.TextView"

# Email 登录——账号输入框
Email_Username_Box_Class = "android.widget.EditText"

# Email 登录——清空账号
Source_Email_Clear_EmailBox_Btn_ID = "img_input_delete"
Email_Clear_EmailBox_Btn_ID = FS(Source_Email_Clear_EmailBox_Btn_ID)

# Email 登录-清空密码
Source_Email_Clear_PWDBox_Btn_ID = "img_input_delete"
Email_Clear_PWDBox_Btn_ID = FS(Source_Email_Clear_PWDBox_Btn_ID)

# Email 登录——清空
# 1.当输入账号、密码其中一项时，使用Email_Clear_UsernameBox_Btn_ID/Email_Clear_PWDBox_Btn_ID
# 2.当输入账号且输入密码时，使用Email_Clear_Class[]，清空账号[1]/清空密码[2]
Email_Clear_Class = "android.widget.EditText"

# Email 账号错误（不能为空：Your email cannot be empty./邮箱未注册：This Email is not registered yet, please Sign Up now.）
Source_Email_Username_Error_ID = "tv_warning"
Email_Username_Error_ID = FS(Source_Email_Username_Error_ID)

# Email 密码错误（不能为空：Your password cannot be empty./密码错误：Username or password is incorrect）
Source_Email_Password_Error_ID = "tv_warning"
Email_Password_Error_ID = FS(Source_Email_Password_Error_ID)

# Email 账号/密码错误
# 1.当账号、密码其中一项报错时，使用Email_Username_Error_ID/Email_Password_Error_ID
# 2.当账号报错且密码报错时，使用Email_Clear_Class[]，账号错误[1]/密码错误[2]
Email_UPError_Class = "android.widget.TextView"

# Email 账号未注册——Sign Up（ACP）
Email_Username_SignUpNow_ACP = [0.715, 0.254, 500]

# Email 登录——密码输入框
Email_Password_Box_Class = "android.widget.EditText"

# Email 登录——显示密码
Source_Email_ShowPassword_Btn_ID = "img_input_visibility"
Email_ShowPassword_Btn_ID = FS(Source_Email_ShowPassword_Btn_ID)

# Email 确认登录——提交账号密码验证
Source_LogIn_Confirm_Btn_ID = "btw_email_confirm"
LogIn_Confirm_Btn_ID = FS(Source_LogIn_Confirm_Btn_ID)

# Email 忘记密码
Source_Email_ForgotPassword_Link_ID = "tv_email_forget_password"
Email_ForgotPassword_Link_ID = FS(Source_Email_ForgotPassword_Link_ID)

# ----------
# 2>Phone 登录
# ----------

# 预选手机号弹窗——Title(text=选择要登录的帐号以继续：)
Phone_PreselectionTitle_ID = gms + ".gms:id/credentials_hint_picker_title"

# 预选手机号——首个手机号
PhonePhone_PreselectionFirstNumber_ID = gms + ".gms:id/credential_primary_label"

# 预选手机号——以上都不是
PhonePhone_PreselectionCancel_ID = gms + ".gms:id/cancel"

# PhoneHome Tips (text=输入手机号/请输入发送到{number}的验证码/)
Source_PhoneHome_Tips_ID = "com_accountkit_title"
PhoneHome_Tips_ID = FS(Source_PhoneHome_Tips_ID)

# PhoneHome Describe（text=轻触下一步通过 Account Kit powered by Facebook 验证你的帐户。即使没有 Facebook 帐户，你也可以使用 Account Kit。你可通过手机短信接收手机号验证码。此过程可能产生短信和流量资费。详细了解 Facebook 如何使用你的信息。）
Source_PhoneHome_Describe_ID = "com_accountkit_text"
PhoneHome_Describe_ID = FS(Source_PhoneHome_Describe_ID)

# Phone 当前选择国家国旗（点击可拉起切换弹窗，text="🇨🇳"）
Source_Phone_NowCountryCode_ID = "country_code"
Phone_NowCountryCode_ID = FS(Source_Phone_NowCountryCode_ID)

# Phone 输入手机号
Source_Phone_input_ID = "com_accountkit_phone_number"
Phone_input_ID = FS(Source_Phone_input_ID)
# Phone_input_Class = "android.widget.EditText"

# Phone 下一步/继续
Source_Phone_Next_ID = "com_accountkit_next_button"
Phone_Next_ID = FS(Source_Phone_Next_ID)

# 验证码输入框——首个（1-6对应6个输入框）
Source_Code_FirstInputBox_ID = "com_accountkit_confirmation_code_1"
Code_FirstInputBox_ID = FS(Source_Code_FirstInputBox_ID)

# 未收到验证码
Source_Not_Received_Code_ID = "com_accountkit_retry_button"
Not_Received_Code_ID = FS(Source_Not_Received_Code_ID)

# 验证你的手机号{AreaCode}{PhoneNumber}
Source_Verify_Your_Number_ID = "com_accountkit_accountkit_verify_number"
Verify_Your_Number_ID = FS(Source_Verify_Your_Number_ID)

# 重发短信
Source_Recapture_Code_ID = "com_accountkit_resend_button"
Recapture_Code_ID = FS(Source_Recapture_Code_ID)

# ----------
# 3>G+ 登录
# ----------

# G+ google预选账号弹窗（text=为“StarMaker”选择帐号）
Google_PreselectionPopup_ID = gms + ".gms:id/title"

# G+ 添加账号
Google_AddAccountNumber_ID = gms + ".gms:id/add_account_chip_title"

# G+ 预选账号
Google_PreselectionAN_IDS = gms + ".gms:id/account_display_name"

# G+ 谷歌第三方登录页（text=登录(输入账号)/欢迎(输入密码)）
Google_AddLogInPage_Title_ID = "headingText"

# G+ 谷歌第三方登录——输入电子邮箱地址或电话号码
Google_AddLogInPage_InputAN_ID = "identifierId"

# G+ 添加账号下一步
Google_ANNext_ID = "identifierNext"

# G+ 添加账号报错信息
Google_AddAN_ErrorText_Xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[2]/android.view.View"

# G+ 谷歌第三方登录——显示账号（text=xinqiji871002@gmail.com）
Google_AddLogInPage_ShowAN_ID = "profileIdentifier"

# G+ 谷歌第三方登录——输入密码(class唯一)
Google_AddLogInPage_InputPWD_Class = "android.widget.EditText"

# G+ 输入密码下一步
Google_PWDNext_ID = "passwordNext"

# G+ 我同意
Google_ConsentNext_ID = "signinconsentNext"

# ----------
# 4>Facebook 登录——弹出弹窗（未安装FB）
# ----------

# Facebook 弹窗——h5_header 用于Find
FBPopup_Title_ID = "header"

# Facebook 弹窗——关闭弹窗(class唯一)
FBPopup_Close_Class = "android.widget.ImageView"

# Facebook 弹窗——输入账号
FBPopup_Email_ID = "m_login_email"

# Facebook 弹窗——输入密码
FBPopup_Password_ID = "m_login_password"

# Facebook 弹窗——登录
FBPopup_LogIn_ID = "u_0_5"

# Facebook 弹窗——继续
FBPopup_Continue_ID = "u_0_3"
FBPopup_Continue_R = [0.486, 0.781, 500]

# ----------
# 5>Facebook 登录——跳转页面（已安装FB）
# ----------

# Facebook 页面——预选账号title（text=轻触头像登录）用于Find
FBPage_Preselection_Title_Class = "android.widget.TextView"

# Facebook 页面——预选账号-登录另一账户
FBPage_Pre_LoginAnotherAccount_Text = "new UiSelector().text(\"登录另一帐户\")"

# Facebook 页面——输入账号
FBPage_inputAN_AID = "帐号"
# xpath = "//android.widget.EditText[@content-desc='帐号']"

# Facebook 页面——登录按钮(输入账号点一次，输入密码点一次)
FBPage_LogIn_AID = "登录点击"
# xpath = "//android.view.ViewGroup[@content-desc='登录点击']"

# Facebook 页面——输入密码
FBPage_inputPWD_AID = "密码"
# xpath = "//android.widget.EditText[@content-desc='密码']"

# ----------
# 6>快捷登录
# ----------

# 切换至快捷登录
Source_QuickLogin_Btn_ID = "img_back"
QuickLogin_Btn_ID = FS(Source_QuickLogin_Btn_ID)

# 切换至普通登录
Source_CommonLogin_Btn_ID = "tv_switch_login"
CommonLogin_Btn_ID = FS(Source_CommonLogin_Btn_ID)

# Development 开发者模式
Source_Development_Btn_ID = "img_star_maker"
Development_Btn_ID = FS(Source_Development_Btn_ID)

# 快速登录头像
Source_QuickLogin_Image_ID = "img_latest_avatar"
QuickLogin_Image_ID = FS(Source_QuickLogin_Image_ID)

# 快速登录用户名
Source_QuickLogin_StageName_ID = "tv_latest_name"
QuickLogin_StageName_ID = FS(Source_QuickLogin_StageName_ID)
