# coding=utf-8
# ----------
# 登录模块
# ----------
from Utils import Tools
from Utils.FindElement import find_element
from CommonView.VData import LogIn_VD


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
    # 登录弹窗-选择登录方式-Tips(Profile_text=Please log in before checking your profile./Post_text=Please log in to make a post./
    # Notification_text=Please log in before checking the latest news./ktv&live_text=Enjoy all features after log in./
    # Share_text=Please log in to repost it./Like_text=Please log in to like it.)
    def LogInPopup_SelectLoginMode_Tips(self):
        LogInPopup_SelectLoginMode_Tips_ID = self.findID(LogIn_VD.LogInPopup_SelectLoginMode_Tips_ID)
        return LogInPopup_SelectLoginMode_Tips_ID

    # 登录弹窗-选择登录方式-选择FB方式
    def LogInPopup_SelectLoginMode_SelectFacebook(self):
        LogInPopup_SelectLoginMode_SelectFacebook_ID = self.findID(LogIn_VD.LogInPopup_SelectLoginMode_SelectFacebook_ID)
        return LogInPopup_SelectLoginMode_SelectFacebook_ID

    # 登录弹窗-选择登录方式-选择Email方式
    def LogInPopup_SelectLoginMode_SelectEmail(self):
        LogInPopup_SelectLoginMode_SelectEmail_ID = self.findID(LogIn_VD.LogInPopup_SelectLoginMode_SelectEmail_ID)
        return LogInPopup_SelectLoginMode_SelectEmail_ID

    # 登录弹窗-选择登录方式-选择Phone方式
    def LogInPopup_SelectLoginMode_SelectPhone(self):
        LogInPopup_SelectLoginMode_SelectPhone_ID = self.findID(LogIn_VD.LogInPopup_SelectLoginMode_SelectPhone_ID)
        return LogInPopup_SelectLoginMode_SelectPhone_ID

    # 登录弹窗-选择登录方式-选择G+方式
    def LogInPopup_SelectLoginMode_SelectGoogle(self):
        LogInPopup_SelectLoginMode_SelectGoogle_ID = self.findID(LogIn_VD.LogInPopup_SelectLoginMode_SelectGoogle_ID)
        return LogInPopup_SelectLoginMode_SelectGoogle_ID

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
        LogInPopup_EmailLoginMode_SelectClose_ID = self.findID(LogIn_VD.EmailWindow_Close_Btn_ID)
        return LogInPopup_EmailLoginMode_SelectClose_ID

    # ----------
    # 登录弹窗-FB登录方式
    # ----------
    # 登录弹窗-FB登录方式-登录点击按钮
    def LogInPopup_FBLoginMode_LogInClickBtn(self):
        LogInPopup_FBLoginMode_LogInClickBtn_AID = self.findAID(LogIn_VD.LogInPopup_FBLoginMode_LogInClickBtn_AID)
        return LogInPopup_FBLoginMode_LogInClickBtn_AID

    # ----------
    # Email登录页
    # ----------
    # 邮箱登录页-Title-Text文案
    def EmailLogInPage_Title_Text(self):
        EmailLogInPage_Title_Text_AU = self.findAU("new UiSelector().text(\"Log In\")")
        return EmailLogInPage_Title_Text_AU

    # 邮箱登录页-输入框-邮箱输入框([0]Email_Input)
    def EmailLogInPage_InputBox_EmailInput(self):
        EmailLogInPage_InputBox_EmailInput_ClaS = self.findClaS(LogIn_VD.EmailLogInPage_InputBox_CommonClaS, 0)
        return EmailLogInPage_InputBox_EmailInput_ClaS

    # 邮箱登录页-输入框-明文密码
    def EmailLogInPage_InputBox_InputVisibility(self):
        EmailLogInPage_InputBox_InputVisibility_ID = self.findID(LogIn_VD.EmailLogInPage_InputBox_InputVisibility_ID)
        return EmailLogInPage_InputBox_InputVisibility_ID

    # 邮箱登录页-输入框-密码输入框([1]Password_Input)
    def EmailLogInPage_InputBox_PasswordInput(self):
        EmailLogInPage_InputBox_PasswordInput_ClaS = self.findClaS(LogIn_VD.EmailLogInPage_InputBox_CommonClaS, 1)
        return EmailLogInPage_InputBox_PasswordInput_ClaS

    # 邮箱登录页-登录-确认登录
    def EmailLogInPage_LogIn_Confirm(self):
        EmailLogInPage_LogIn_Confirm_ID = self.findID(LogIn_VD.EmailLogInPage_LogIn_Confirm_ID)
        return EmailLogInPage_LogIn_Confirm_ID





    # ----------------------------------------------------------------------------------------------------------------------








    # ----------
    # 1>Email 登录
    # ----------
    # 【登录注册】弹窗上点击Email方式
    def LogInWindow_Email_Btn(self):
        LogInWindow_Email_Btn_ID = self.findID(LogIn_VD.LogInWindow_Email_Btn_ID)
        return LogInWindow_Email_Btn_ID

    # 【登录注册】弹窗上点击Phone方式
    def LogInWindow_Phone_Btn(self):
        LogInWindow_Phone_Btn_ID = self.findID(LogIn_VD.LogInWindow_Phone_Btn_ID)
        return LogInWindow_Phone_Btn_ID

    # 【登录注册】弹窗上点击G+方式
    def LogInWindow_Google_Btn(self):
        LogInWindow_Google_Btn_ID = self.findID(LogIn_VD.LogInWindow_Google_Btn_ID)
        return LogInWindow_Google_Btn_ID

    # Email 弹窗 —— 登录
    def EmailWindow_LogIn_Btn(self):
        EmailWindow_LogIn_Btn_ID = self.findID(LogIn_VD.EmailWindow_LogIn_Btn_ID)
        return EmailWindow_LogIn_Btn_ID

    # Email 弹窗 —— 注册
    def EmailWindow_SignUp_Btn(self):
        EmailWindow_SignUp_Btn_ID = self.findID(LogIn_VD.EmailWindow_SignUp_Btn_ID)
        return EmailWindow_SignUp_Btn_ID

    # Email 账号输入框
    def Email_Username_Box(self):
        Email_Username_Box_Class = self.findClaS(LogIn_VD.Email_Username_Box_Class, 0)
        return Email_Username_Box_Class

    # Email 清空账号输入框
    def Email_Clear_EmailBox_Btn(self):
        Email_Clear_EmailBox_Btn_Xpath = self.findID(LogIn_VD.Email_Clear_EmailBox_Btn_ID)
        return Email_Clear_EmailBox_Btn_Xpath

    # Email 登录——清空
    # 1.当输入账号、密码其中一项时，使用Email_Clear_UsernameBox_Btn/Email_Clear_PWDBox_Btn
    # 2.当输入账号且输入密码时，使用Email_Clear_Class[]，清空账号[1]/清空密码[2]
    def Email_Clear_Class_UsernameBox(self):
        Email_Clear_Class = self.findClaS(LogIn_VD.Email_Clear_Class, 1)
        return Email_Clear_Class

    def Email_Clear_Class_Pwd(self):
        Email_Clear_Class = self.findClaS(LogIn_VD.Email_Clear_Class, 2)
        return Email_Clear_Class

    # Email 账号错误
    def Email_Username_Error(self):
        Email_Username_Error_ID = self.findID(LogIn_VD.Email_Username_Error_ID)
        return Email_Username_Error_ID

    # Email 账号未注册——Sign Up（ACP）
    @staticmethod
    def Email_Username_SignUpNow_ACP():
        x1 = LogIn_VD.Email_Username_SignUpNow_ACP[0]
        y1 = LogIn_VD.Email_Username_SignUpNow_ACP[1]
        t = LogIn_VD.Email_Username_SignUpNow_ACP[2]
        if Tools.Screen().AccurateClicks_Percentage(x1, y1, t):
            return True
        else:
            return False

    # Email 密码输入框
    def Email_Password_Box(self):
        Email_Password_Box_Class = self.findClaS(LogIn_VD.Email_Password_Box_Class, 1)
        return Email_Password_Box_Class

    # Email 清空密码输入框
    def Email_Clear_PWDBox_Btn(self):
        Email_Clear_PWDBox_Btn_Xpath = self.findID(LogIn_VD.Email_Clear_PWDBox_Btn_ID)
        return Email_Clear_PWDBox_Btn_Xpath

    # Email 密码错误
    def Email_Password_Error(self):
        Email_Password_Error_ID = self.findID(LogIn_VD.Email_Password_Error_ID)
        return Email_Password_Error_ID

    # Email 显示密码
    def Email_ShowPassword_Btn(self):
        Email_ShowPassword_Btn_ID = self.findID(LogIn_VD.Email_ShowPassword_Btn_ID)
        return Email_ShowPassword_Btn_ID

    # Email 确认登录（提交账号密码验证）
    def LogIn_Confirm_Btn(self):
        LogIn_Confirm_Btn_ID = self.findID(LogIn_VD.LogIn_Confirm_Btn_ID)
        return LogIn_Confirm_Btn_ID

    # Email 忘记密码（link）
    def Email_ForgotPassword_Link(self):
        Email_ForgotPassword_Link_ID = self.findID(LogIn_VD.Email_ForgotPassword_Link_ID)
        return Email_ForgotPassword_Link_ID

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
        Phone_SwitchCountryCode_DIY = self.findIDS("com.starmakerinteractive.starmaker:id/a_q", 1)
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
