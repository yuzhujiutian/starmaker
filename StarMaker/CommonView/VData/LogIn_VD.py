# coding=utf-8
from StarMaker.Utils.GetDevicesInfo import DevicesInfo
from StarMaker.Utils.reSource import get_mapping_from_file

package = DevicesInfo().package()
mapping_dict = get_mapping_from_file()
gms = "com.google.android"


# ----------
# 登录弹窗-选择登录方式
# ----------
# 登录弹窗-选择登录方式-Tips
Source_LogInPopup_SelectLoginMode_Tips_ID = "tv_welcome"
LogInPopup_SelectLoginMode_Tips_ID = package + mapping_dict[Source_LogInPopup_SelectLoginMode_Tips_ID]

# 登录弹窗-选择登录方式-选择Phone方式
Source_LogInPopup_SelectLoginMode_SelectPhone_ID = "tv_login_phone"
LogInPopup_SelectLoginMode_SelectPhone_ID = package + mapping_dict[Source_LogInPopup_SelectLoginMode_SelectPhone_ID]

# 登录弹窗-选择登录方式-选择FB方式
# Source_LogInPopup_SelectLoginMode_SelectFacebook_ID = "tv_login_top"
# LogInPopup_SelectLoginMode_SelectFacebook_ID = package + \
#                                                mapping_dict[Source_LogInPopup_SelectLoginMode_SelectFacebook_ID]

# 登录弹窗-选择登录方式-选择More ways
Source_LogInPopup_SelectLoginMode_MoreWays_ID = "tv_more_ways"
LogInPopup_SelectLoginMode_MoreWays_ID = package + mapping_dict[Source_LogInPopup_SelectLoginMode_MoreWays_ID]

# 登录弹窗-选择登录方式-选择Email方式
Source_LogInPopup_SelectLoginMode_SelectEmail_ID = "tv_login_email"
LogInPopup_SelectLoginMode_SelectEmail_ID = package + mapping_dict[Source_LogInPopup_SelectLoginMode_SelectEmail_ID]

# 登录弹窗-选择登录方式-选择G+方式
# Source_LogInPopup_SelectLoginMode_SelectGoogle_ID = "img_login_google"
# LogInPopup_SelectLoginMode_SelectGoogle_ID = package + mapping_dict[Source_LogInPopup_SelectLoginMode_SelectGoogle_ID]

# ----------
# 登录弹窗-Email登录方式
# ----------
# 登录弹窗-Email登录方式-Tips文案(text=Use Email Address]
Source_LogInPopup_EmailLoginMode_Title_ID = "login_title"
LogInPopup_EmailLoginMode_Title_ID = package + mapping_dict[Source_LogInPopup_EmailLoginMode_Title_ID]

# 登录弹窗-Email登录方式-选择登录
Source_LogInPopup_EmailLoginMode_SelectLogIn_ID = "txt_login"
LogInPopup_EmailLoginMode_SelectLogIn_ID = package + mapping_dict[Source_LogInPopup_EmailLoginMode_SelectLogIn_ID]

# 登录弹窗-Email登录方式-选择注册
Source_LogInPopup_EmailLoginMode_SelectSignUp_ID = "txt_sign_up"
LogInPopup_EmailLoginMode_SelectSignUp_ID = package + mapping_dict[Source_LogInPopup_EmailLoginMode_SelectSignUp_ID]

# 登录弹窗-Email登录方式-选择取消
Source_LogInPopup_EmailLoginMode_SelectCancel_ID = "txt_login_cancel"
LogInPopup_EmailLoginMode_SelectCancel_ID = package + mapping_dict[Source_LogInPopup_EmailLoginMode_SelectCancel_ID]

# 登录弹窗-Email登录方式-关闭
Source_LogInPopup_EmailLoginMode_Close_ID = "txt_login_close"
LogInPopup_EmailLoginMode_Close_ID = package + mapping_dict[Source_LogInPopup_EmailLoginMode_Close_ID]

# ----------
# Email登录页
# ----------
# 邮箱登录页-输入框-通用IDS([0]Email_Input/[1]Password_Input]
Source_EmailLogInPage_InputBox_Common_IDS = "et_input"
EmailLogInPage_InputBox_Common_IDS = package + mapping_dict[Source_EmailLogInPage_InputBox_Common_IDS]

# 邮箱登录页-输入框-邮箱输入框
Source_EmailLogInPage_EmailInputBox_ID = "et_email"
EmailLogInPage_EmailInputBox_ID = package + mapping_dict[Source_EmailLogInPage_EmailInputBox_ID]

# 邮箱登录页-输入邮箱后下一步
Source_EmailLogInPage_EmailInputNext_ID = "btn_next"
EmailLogInPage_EmailInputNext_ID = package + mapping_dict[Source_EmailLogInPage_EmailInputNext_ID]



# 邮箱登录页-输入框-明文密码
Source_EmailLogInPage_InputBox_InputVisibility_ID = "img_input_visibility"
EmailLogInPage_InputBox_InputVisibility_ID = package + mapping_dict[Source_EmailLogInPage_InputBox_InputVisibility_ID]

# 邮箱登录页-登录-确认登录
Source_EmailLogInPage_LogIn_Confirm_ID = "btw_email_confirm"
EmailLogInPage_LogIn_Confirm_ID = package + mapping_dict[Source_EmailLogInPage_LogIn_Confirm_ID]

# 邮箱登录页-清空输入框-通用IDS
Source_EmailLogInPage_ClearInputBox_Common_IDS = "img_input_delete"
EmailLogInPage_ClearInputBox_Common_IDS = package + mapping_dict[Source_EmailLogInPage_ClearInputBox_Common_IDS]

# 邮箱登录页-错误提示-IDS
# 帐号错误：不能为空：Your email cannot be empty./邮箱未注册：This Email is not registered yet, please Sign Up now.
# 密码错误：不能为空：Your password cannot be empty./密码错误：Username or password is incorrect
Source_EmailLogInPage_errorPrompt_Common_IDS = "tv_warning"
EmailLogInPage_errorPrompt_Common_IDS = package + mapping_dict[Source_EmailLogInPage_errorPrompt_Common_IDS]

# 邮箱登录页-忘记密码-跳转链接
Source_EmailLogInPage_ForgotPassword_Link_ID = "tv_email_forget_password"
EmailLogInPage_ForgotPassword_Link_ID = package + mapping_dict[Source_EmailLogInPage_ForgotPassword_Link_ID]

# ------以下内容暂未维护------------------------------------------------------------------------------------------------
# ----------
# 2>Phone 登录
# ----------
# 预选手机号弹窗——Title(text=选择要登录的帐号以继续：]
Phone_PreselectionTitle_ID = gms + ".gms:id/credentials_hint_picker_title"

# 预选手机号——首个手机号
PhonePhone_PreselectionFirstNumber_ID = gms + ".gms:id/credential_primary_label"

# 预选手机号——以上都不是
PhonePhone_PreselectionCancel_ID = gms + ".gms:id/cancel"

# PhoneHome Tips (text=输入手机号/请输入发送到{number}的验证码/]
PhoneHome_Tips_ID = "com_accountkit_title"

# PhoneHome Describe（text=轻触下一步通过 Account Kit powered by Facebook 验证你的帐户。
# 即使没有 Facebook 帐户，你也可以使用 Account Kit。你可通过手机短信接收手机号验证码。
# 此过程可能产生短信和流量资费。详细了解 Facebook 如何使用你的信息。）
PhoneHome_Describe_ID = "com_accountkit_text"

# Phone 当前选择国家国旗（点击可拉起切换弹窗，text="🇨🇳"）
Phone_NowCountryCode_ID = "country_code"

# Phone 输入手机号
Phone_input_ID = "com_accountkit_phone_number"
# Phone_input_Class = "android.widget.EditText"

# Phone 下一步/继续
Phone_Next_ID = "com_accountkit_next_button"

# 验证码输入框——首个（1-6对应6个输入框）
Code_FirstInputBox_ID = "com_accountkit_confirmation_code_1"

# 未收到验证码
Not_Received_Code_ID = "com_accountkit_retry_button"

# 验证你的手机号{AreaCode}{PhoneNumber}
Verify_Your_Number_ID = "com_accountkit_accountkit_verify_number"

# 重发短信
Recapture_Code_ID = "com_accountkit_resend_button"

# ----------
# 3>G+ 登录
# ----------

# G+ google预选账号弹窗（text=“选择帐号”）
Google_PreselectionPopup_ID = gms + ".gms:id/main_title"

# G+ 添加账号
Google_AddAccountNumber_ID = gms + ".gms:id/add_account_chip_title"

# G+ 预选账号
Google_PreselectionAN_IDS = gms + ".gms:id/account_display_name"

# G+ 谷歌第三方登录页（text=“登录”）
Google_AddLogInPage_Title_ID = "headingText"

# G+ 谷歌第三方登录——输入电子邮件地址或电话号码
Google_AddLogInPage_InputAN_ID = "identifierId"

# G+ 添加账号“下一步”按钮
Google_ANNext_ID = "identifierNext"

# G+ 添加账号报错信息
Google_AddAN_ErrorText_Xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/" \
                               "android.widget.FrameLayout/android.widget.FrameLayout/android.widget." \
                               "FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view." \
                               "View[1]/android.view.View[3]/android.view.View/android.view.View[2]"

# G+ 谷歌第三方登录——显示账号（text=xinqiji871002@gmail.com）
Google_AddLogInPage_ShowAN_ID = "profileIdentifier"

# G+ 谷歌第三方登录——输入密码(class唯一]
Google_AddLogInPage_InputPWD_Class = "android.widget.EditText"

# G+ 输入密码下一步
Google_PWDNext_ID = "passwordNext"

# G+ 我同意
Google_ConsentNext_ID = "signinconsentNext"

# G+ google服务页的“下箭头”
Google_ServiceDownArrow_ID = gms + ".gms:id/suw_navbar_more"

# G+ google服务页的“接受”
Google_ServiceAccept_ID = gms + ".gms:id/suw_navbar_next"

# ----------
# 4>Facebook 登录——弹出弹窗（未安装FB）
# ----------

# Facebook 弹窗——h5_header 用于Find
FBPopup_Title_ID = "header"

# Facebook 弹窗——关闭弹窗(class唯一]
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
FBPage_Pre_LoginAnotherAccount_Text = "new UiSelector(].text(\"登录另一帐户\"]"

# Facebook 页面——输入账号
FBPage_inputAN_AID = "帐号"
# xpath = "//android.widget.EditText[@content-desc='帐号']"

# Facebook 页面——登录按钮(输入账号点一次，输入密码点一次]
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
QuickLogin_Btn_ID = package + mapping_dict[Source_QuickLogin_Btn_ID]

# 切换至普通登录
Source_CommonLogin_Btn_ID = "tv_switch_login"
CommonLogin_Btn_ID = package + mapping_dict[Source_CommonLogin_Btn_ID]

# Development 开发者模式
Source_Development_Btn_ID = "img_star_maker"
Development_Btn_ID = package + mapping_dict[Source_Development_Btn_ID]

# 快速登录头像
Source_QuickLogin_Image_ID = "img_latest_avatar"
QuickLogin_Image_ID = package + mapping_dict[Source_QuickLogin_Image_ID]

# 快速登录用户名
Source_QuickLogin_StageName_ID = "tv_latest_name"
QuickLogin_StageName_ID = package + mapping_dict[Source_QuickLogin_StageName_ID]
