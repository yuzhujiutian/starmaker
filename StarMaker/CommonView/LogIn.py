# coding=utf-8
# 维护版本：7.4.5 http://119.28.249.120:8080/job/Assemble/3/
# 维护日期：2019.6.13
# 维护人员：崔尧椋
# ----------
# 登录模块
# ----------
from StarMaker.CommonView.VData import LogIn_VD
from StarMaker.Utils.FindElement import find_element
from StarMaker.Utils.Tools import Tools


# 登录模块
class LogIn(object):
    def __init__(self):
        self.findID = find_element().ID
        self.findIDS = find_element().IDS
        self.findCla = find_element().Cla
        self.findClaS = find_element().ClaS
        self.findXpa = find_element().Xpa
        self.findAID = find_element().AID
        self.findAU = find_element().AU

    # ----------
    # 登录弹窗
    # ----------
    # 登录弹窗-选择登录方式-Tips(
    # ClickMeTab_text=Log in and check profile
    # Post_text=Log in and post covers
    # ClickMessage_text=Log in and check messages
    # ktv&live_text=Log in and enjoy all features
    # DetailsPage_like_text=Please log in to like it.
    # DetailsPage_comment_text=Please log in to comment.
    # DetailsPage_Share&Gift_text=Log in and enjoy all features
    def LogInPopup_SelectLoginMode_Tips(self):
        LogInPopup_SelectLoginMode_Tips_ID = self.findID(LogIn_VD.LogInPopup_SelectLoginMode_Tips_ID)
        return LogInPopup_SelectLoginMode_Tips_ID

    # 登录弹窗-选择登录方式-选择Phone方式
    def LogInPopup_SelectLoginMode_SelectPhone(self):
        LogInPopup_SelectLoginMode_SelectPhone_ID = self.findID(LogIn_VD.LogInPopup_SelectLoginMode_SelectPhone_ID)
        return LogInPopup_SelectLoginMode_SelectPhone_ID

    # 登录弹窗-选择登录方式-选择FB方式
    # def LogInPopup_SelectLoginMode_SelectFacebook(self):
    #     LogInPopup_SelectLoginMode_SelectFacebook_ID = self.findID(LogIn_VD.LogInPopup_SelectLoginMode_SelectFacebook_ID)
    #     return LogInPopup_SelectLoginMode_SelectFacebook_ID

    # 登录弹窗-选择登录方式-选择More ways
    def LogInPopup_SelectLoginMode_MoreWays(self):
        LogInPopup_SelectLoginMode_MoreWays_ID = self.findID(LogIn_VD.LogInPopup_SelectLoginMode_MoreWays_ID)
        return LogInPopup_SelectLoginMode_MoreWays_ID

    # 登录弹窗-选择登录方式-选择Email方式
    def LogInPopup_SelectLoginMode_SelectEmail(self):
        LogInPopup_SelectLoginMode_SelectEmail_ID = self.findID(LogIn_VD.LogInPopup_SelectLoginMode_SelectEmail_ID)
        return LogInPopup_SelectLoginMode_SelectEmail_ID

    # 登录弹窗-选择登录方式-选择G+方式
    # def LogInPopup_SelectLoginMode_SelectGoogle(self):
    #     LogInPopup_SelectLoginMode_SelectGoogle_ID = self.findID(LogIn_VD.LogInPopup_SelectLoginMode_SelectGoogle_ID)
    #     return LogInPopup_SelectLoginMode_SelectGoogle_ID

    # ----------
    # 登录弹窗-Email登录方式
    # ----------
    # 登录弹窗-Email登录方式-Tips文案(text=Use Email Address)
    def LogInPopup_EmailLoginMode_Title(self):
        LogInPopup_EmailLoginMode_Title_ID = self.findID(LogIn_VD.LogInPopup_EmailLoginMode_Title_ID)
        return LogInPopup_EmailLoginMode_Title_ID

    # 登录弹窗-Email登录方式-选择登录
    def LogInPopup_EmailLoginMode_SelectLogIn(self):
        LogInPopup_EmailLoginMode_SelectLogIn_ID = self.findID(LogIn_VD.LogInPopup_EmailLoginMode_SelectLogIn_ID)
        return LogInPopup_EmailLoginMode_SelectLogIn_ID

    # 登录弹窗-Email登录方式-选择注册
    def LogInPopup_EmailLoginMode_SelectSignUp(self):
        LogInPopup_EmailLoginMode_SelectSignUp_ID = self.findID(LogIn_VD.LogInPopup_EmailLoginMode_SelectSignUp_ID)
        return LogInPopup_EmailLoginMode_SelectSignUp_ID

    # 登录弹窗-Email登录方式-选择取消
    def LogInPopup_EmailLoginMode_SelectCancel(self):
        LogInPopup_EmailLoginMode_SelectCancel_ID = self.findID(LogIn_VD.LogInPopup_EmailLoginMode_SelectCancel_ID)
        return LogInPopup_EmailLoginMode_SelectCancel_ID

    # 登录弹窗-Email登录方式-选择关闭
    def LogInPopup_EmailLoginMode_SelectClose(self):
        LogInPopup_EmailLoginMode_SelectClose_ID = self.findID(LogIn_VD.LogInPopup_EmailLoginMode_Close_ID)
        return LogInPopup_EmailLoginMode_SelectClose_ID

    # ----------
    # Email登录页
    # ----------
    # 邮箱登录页-Title-Text文案
    def EmailLogInPage_Title_Text(self):
        EmailLogInPage_Title_Text_AU = self.findAU("new UiSelector().text(\"Log In\")")
        return EmailLogInPage_Title_Text_AU

    # 邮箱登录页-输入框-邮箱输入框([0]Email_Input)
    def EmailLogInPage_InputBox_EmailInput(self):
        EmailLogInPage_InputBox_EmailInput_IDS = self.findIDS(LogIn_VD.EmailLogInPage_InputBox_Common_IDS, 0)
        return EmailLogInPage_InputBox_EmailInput_IDS

    # 邮箱登录页-输入框-邮箱输入框
    def EmailLogInPage_EmailInputBox(self):
        EmailLogInPage_EmailInputBox_ID = self.findID(LogIn_VD.EmailLogInPage_EmailInputBox_ID)
        return EmailLogInPage_EmailInputBox_ID

    # 邮箱登录页-输入邮箱后下一步
    def EmailLogInPage_EmailInputNext(self):
        EmailLogInPage_EmailInputNext_ID = self.findID(LogIn_VD.EmailLogInPage_EmailInputNext_ID)
        return EmailLogInPage_EmailInputNext_ID

    # 邮箱登录页-输入框-明文密码
    def EmailLogInPage_InputBox_InputVisibility(self):
        EmailLogInPage_InputBox_InputVisibility_ID = self.findID(LogIn_VD.EmailLogInPage_InputBox_InputVisibility_ID)
        return EmailLogInPage_InputBox_InputVisibility_ID

    # 邮箱登录页-输入框-密码输入框([1]Password_Input)
    def EmailLogInPage_InputBox_PasswordInput(self):
        EmailLogInPage_InputBox_PasswordInput_IDS = self.findIDS(LogIn_VD.EmailLogInPage_InputBox_Common_IDS, 1)
        return EmailLogInPage_InputBox_PasswordInput_IDS

    # 邮箱登录页-登录-确认登录
    def EmailLogInPage_LogIn_Confirm(self):
        EmailLogInPage_LogIn_Confirm_ID = self.findID(LogIn_VD.EmailLogInPage_LogIn_Confirm_ID)
        return EmailLogInPage_LogIn_Confirm_ID

    # 邮箱登录页-清空输入框-清空帐号输入框
    def EmailLogInPage_ClearInputBox_ClearEmail(self):
        EmailLogInPage_ClearInputBox_Common_IDS = self.findIDS(LogIn_VD.EmailLogInPage_ClearInputBox_Common_IDS, 0)
        return EmailLogInPage_ClearInputBox_Common_IDS

    # 邮箱登录页-清空输入框-清空密码输入框
    def EmailLogInPage_ClearInputBox_ClearPWD(self):
        EmailLogInPage_ClearInputBox_Common_IDS = self.findIDS(LogIn_VD.EmailLogInPage_ClearInputBox_Common_IDS, 1)
        return EmailLogInPage_ClearInputBox_Common_IDS

    # 邮箱登录页-错误提示-帐号错误
    # 帐号错误：不能为空：Your email cannot be empty./邮箱未注册：This Email is not registered yet, please Sign Up now.
    def EmailLogInPage_errorPrompt_UsernameError(self):
        EmailLogInPage_errorPrompt_Common_IDS = self.findIDS(LogIn_VD.EmailLogInPage_errorPrompt_Common_IDS, 0)
        return EmailLogInPage_errorPrompt_Common_IDS

    # 邮箱登录页-错误提示-密码错误
    # 密码错误：不能为空：Your password cannot be empty./密码错误：Username or password is incorrect
    def EmailLogInPage_errorPrompt_PasswordError(self):
        EmailLogInPage_errorPrompt_Common_IDS = self.findIDS(LogIn_VD.EmailLogInPage_errorPrompt_Common_IDS, 1)
        return EmailLogInPage_errorPrompt_Common_IDS

    # 邮箱登录页-忘记密码-跳转链接
    def EmailLogInPage_ForgotPassword_Link(self):
        EmailLogInPage_ForgotPassword_Link_ID = self.findID(LogIn_VD.EmailLogInPage_ForgotPassword_Link_ID)
        return EmailLogInPage_ForgotPassword_Link_ID

# ------以下内容暂未维护------------------------------------------------------------------------------------------------
    # ----------
    # 2>Phone 登录
    # ----------
    # LogTips 提示：输入手机号
    def PhoneHome_Tips(self):
        PhoneHome_Tips_ID = self.findID(LogIn_VD.PhoneHome_Tips_ID)
        return PhoneHome_Tips_ID

    # PhoneHome 描述信息
    def PhoneHome_Describe(self):
        PhoneHome_Describe_ID = self.findID(LogIn_VD.PhoneHome_Describe_ID)
        return PhoneHome_Describe_ID

    # Phone 当前选择国家（text="🇨🇳"）
    def Phone_NowCountryCode(self):
        Phone_NowCountryCode_ID = self.findID(LogIn_VD.Phone_NowCountryCode_ID)
        return Phone_NowCountryCode_ID

    # Phone 选择任意国家区号（"text = "{Country_name} + " " + ({Area_code})""）
    def Phone_SwitchCountryCode_GB(self):
        # 滑动停止后，每页13个，by_id（0-12）
        Phone_SwitchCountryCode_DIY = self.findIDS("a_q", 1)
        return Phone_SwitchCountryCode_DIY

    # 查找切换国家区号页面
    def Phone_SwitchCountryCode_CN(self):
        # 滑动停止后，每页26条，对应13个国家的国旗+区号（🇨🇳，中国 (+86)），by_class_name（0-25）
        Phone_SwitchCountryCode_CN = self.findClaS("android.widget.TextView", -1)
        return Phone_SwitchCountryCode_CN

    # Phone 输入手机号
    def Phone_input(self):
        Phone_input_ID = self.findID(LogIn_VD.Phone_input_ID)
        return Phone_input_ID

    # Phone 下一步
    def Phone_Next(self):
        Phone_Next_ID = self.findID(LogIn_VD.Phone_Next_ID)
        return Phone_Next_ID

    # 验证码输入框——首个
    def Code_FirstInputBox(self):
        Code_FirstInputBox_ID = self.findID(LogIn_VD.Code_FirstInputBox_ID)
        return Code_FirstInputBox_ID

    # code
    def Code(self):
        Code = self.findClaS("android.widget.TextView", 6)
        return Code

    # 未收到验证码按钮
    def Not_Received_Code(self):
        NotReceivedCode_Btn_ID = self.findID(LogIn_VD.Not_Received_Code_ID)
        return NotReceivedCode_Btn_ID

    # 验证你的手机号{AreaCode}{PhoneNumber}
    def Verify_Your_Number(self):
        VerifyYourNumber_ID = self.findID(LogIn_VD.Verify_Your_Number_ID)
        return VerifyYourNumber_ID

    # 重发短信
    def Recapture_Code(self):
        Recapture_Code_ID = self.findID(LogIn_VD.Recapture_Code_ID)
        return Recapture_Code_ID

    # ----------
    # 3>G+ 登录
    # ----------

    # 登录方式验证——Google 登录
    def LogInModeCase_Google(self):
        if self.findID(LogIn_VD.LogInWindow_Google_Btn_ID):
            return True
        else:
            return False

    # G+ 查找预选账号弹窗，如果存在返回True
    def FindGoogle_PreselectionPopup(self):
        if self.findID(LogIn_VD.Google_PreselectionPopup_ID):
            return True
        else:
            return False

    # G+ 添加账号
    def Google_AddAccountNumber(self):
        Google_AddAccountNumber_ID = self.findID(LogIn_VD.Google_AddAccountNumber_ID)
        return Google_AddAccountNumber_ID

    # G+ 第一个预选账号
    def Google_FirstAN(self):
        Google_FirstAN_Xpath = self.findXpa(LogIn_VD.Google_PreselectionAN_IDS)[0]
        return Google_FirstAN_Xpath

    # G+ 第二个预选账号
    def Google_SecondAN(self):
        Google_SecondAN_Xpath = self.findXpa(LogIn_VD.Google_PreselectionAN_IDS)[1]
        return Google_SecondAN_Xpath

    # G+ 第三个预选账号
    def Google_ThirdAN(self):
        Google_ThirdAN_Xpath = self.findXpa(LogIn_VD.Google_PreselectionAN_IDS)[2]
        return Google_ThirdAN_Xpath

    # G+ 特定预选帐号
    def Google_GivenAN(self):
        Google_GivenAN_Text = self.findAU("new UiSelector().text(\"刘誉\")")
        return Google_GivenAN_Text

    # G+ 谷歌第三方登录页（text=登录(输入账号)/欢迎(输入密码)）
    def Google_AddLogInPage_Title(self):
        Google_AddLogInPage_Title_ID = self.findID(LogIn_VD.Google_AddLogInPage_Title_ID)
        return Google_AddLogInPage_Title_ID

    # G+ 输入电子邮箱地址或电话号码
    def Google_AddLogInPage_InputAN(self):
        Google_AddLogInPage_InputAN_ID = self.findID(LogIn_VD.Google_AddLogInPage_InputAN_ID)
        return Google_AddLogInPage_InputAN_ID

    # G+ 添加账号下一步
    def Google_ANNext(self):
        Google_ANNext_ID = self.findID(LogIn_VD.Google_ANNext_ID)
        return Google_ANNext_ID

    # G+ 添加账号报错信息
    def Google_AddAN_ErrorText(self):
        Google_AddAN_ErrorText_Xpath = self.findXpa(LogIn_VD.Google_AddAN_ErrorText_Xpath)
        return Google_AddAN_ErrorText_Xpath

    # G+ 谷歌第三方登录——显示账号（text=xinqiji871002@gmail.com）
    def Google_AddLogInPage_ShowAN(self):
        Google_AddLogInPage_ShowAN_ID = self.findID(LogIn_VD.Google_AddLogInPage_ShowAN_ID)
        return Google_AddLogInPage_ShowAN_ID

    # G+ 谷歌第三方登录——输入密码(class唯一)
    def Google_AddLogInPage_InputPWD(self):
        Google_AddLogInPage_InputPWD_Class = self.findCla(LogIn_VD.Google_AddLogInPage_InputPWD_Class)
        return Google_AddLogInPage_InputPWD_Class

    # G+ 输入密码下一步
    def Google_PWDNext(self):
        Google_PWDNext_ID = self.findID(LogIn_VD.Google_PWDNext_ID)
        return Google_PWDNext_ID

    # G+ 我同意
    def Google_ConsentNext(self):
        Google_ConsentNext_ID = self.findID(LogIn_VD.Google_ConsentNext_ID)
        return Google_ConsentNext_ID

    # G+ google服务页“下箭头”
    def Google_ServiceDownArrow(self):
        Google_ServiceDownArrow_ID = self.findID(LogIn_VD.Google_ServiceDownArrow_ID)
        return Google_ServiceDownArrow_ID

    # G+ google服务页“接受”
    def Google_ServiceAccept(self):
        Google_ServiceAccept_ID = self.findID(LogIn_VD.Google_ServiceAccept_ID)
        return Google_ServiceAccept_ID

    # ----------
    # 4>Facebook 登录——弹出弹窗（未安装FB）
    # ----------

    # Facebook 弹窗——h5_header 用于Find
    def FBPopup_TitleFind(self):
        if self.findID(LogIn_VD.FBPopup_Title_ID):
            return True
        else:
            return False

    # Facebook 弹窗——关闭弹窗(class唯一)
    def FBPopup_Close(self):
        FBPopup_Close_Class = self.findCla(LogIn_VD.FBPopup_Close_Class)
        return FBPopup_Close_Class

    # Facebook 弹窗——输入账号
    def FBPopup_Email(self):
        FBPopup_Email_ID = self.findID(LogIn_VD.FBPopup_Email_ID)
        return FBPopup_Email_ID

    # Facebook 弹窗——输入密码
    def FBPopup_Password(self):
        FBPopup_Password_ID = self.findID(LogIn_VD.FBPopup_Password_ID)
        return FBPopup_Password_ID

    # Facebook 弹窗——登录
    def FBPopup_LogIn(self):
        FBPopup_LogIn_ID = self.findID(LogIn_VD.FBPopup_LogIn_ID)
        return FBPopup_LogIn_ID

    # Facebook 弹窗——继续
    def FBPopup_Continue(self):
        FBPopup_Continue_ID = self.findID(LogIn_VD.FBPopup_Continue_ID)
        return FBPopup_Continue_ID

    # Facebook 弹窗——继续
    @staticmethod
    def FBPopup_Continue_R():
        x1 = LogIn_VD.FBPopup_Continue_R[0]
        y1 = LogIn_VD.FBPopup_Continue_R[1]
        t = LogIn_VD.FBPopup_Continue_R[2]
        if Tools.Screen().AccurateClicks_Percentage(x1, y1, t):
            return True
        else:
            return False

    # ----------
    # 5>Facebook 登录——跳转页面（已安装FB）
    # ----------

    # Facebook 页面——预选账号title（text=轻触头像登录）用于Find
    def FBPage_Preselection_TitleFind(self):
        if self.findID(LogIn_VD.FBPage_Preselection_Title_Class):
            return True
        else:
            return False

    # Facebook 页面——预选账号判定是否存在
    def FBPage_Pre_FindLoginAnotherAccount(self):
        if self.findAU(LogIn_VD.FBPage_Pre_LoginAnotherAccount_Text):
            return True
        else:
            return False

    # Facebook 页面——预选账号-登录另一账户
    def FBPage_Pre_LoginAnotherAccount(self):
        FBPage_Pre_LoginAnotherAccount_Text = self.findAU(
            LogIn_VD.FBPage_Pre_LoginAnotherAccount_Text)
        return FBPage_Pre_LoginAnotherAccount_Text

    # Facebook 页面——输入账号
    def FBPage_inputAN(self):
        FBPage_inputAN_AID = self.findAID(LogIn_VD.FBPage_inputAN_AID)
        return FBPage_inputAN_AID

    # Facebook 页面——登录按钮(输入账号点一次，输入密码点一次)
    def FBPage_LogIn(self):
        FBPage_LogIn_AID = self.findAID(LogIn_VD.FBPage_LogIn_AID)
        return FBPage_LogIn_AID

    # Facebook 页面——输入密码
    def FBPage_inputPWD(self):
        FBPage_inputPWD_AID = self.findAID(LogIn_VD.FBPage_inputPWD_AID)
        return FBPage_inputPWD_AID

    # ----------
    # 6>快捷登录
    # ----------

    # 切换至快捷登录
    def QuickLogin_Btn(self):
        QuickLogin_Btn_ID = self.findID(LogIn_VD.QuickLogin_Btn_ID)
        return QuickLogin_Btn_ID

    # Development 开发者模式
    def Development_Btn(self):
        Development_Btn_ID = self.findID(LogIn_VD.QuickLogin_Btn_ID)
        return Development_Btn_ID

    # 查找 切换至普通登录 按钮
    def FindCommonLogin_Btn(self):
        if self.findID(LogIn_VD.CommonLogin_Btn_ID):
            return True
        else:
            return False

    # 切换至普通登录
    def CommonLogin_Btn(self):
        CommonLogin_Btn_ID = self.findID(LogIn_VD.QuickLogin_Btn_ID)
        return CommonLogin_Btn_ID

    # 快速登录头像
    def QuickLogin_Image(self):
        QuickLogin_Image_ID = self.findID(LogIn_VD.QuickLogin_Image_ID)
        return QuickLogin_Image_ID

    # 快速登录用户名
    def QuickLogin_StageName(self):
        QuickLogin_StageName_ID = self.findID(LogIn_VD.QuickLogin_StageName_ID)
        return QuickLogin_StageName_ID
