# coding=utf-8
from Utils import Tools
from Utils.GetDevicesInfo import DevicesInfo
package = DevicesInfo().package()
FS = Tools.Tools().FindSource
gms = "com.google.android"


# ----------
# SignUp
# ----------
# SignUp页面-预选帐号-Tips
SignUpPage_Preselection_Tips_ID = gms + ".gms:id/credentials_hint_picker_title"

# SignUp页面-Tips-text(text="Enter your email address")
Source_SignUpPage_Tips_Text_ID = "com_accountkit_title"
SignUpPage_Tips_Text_ID = package + FS(Source_SignUpPage_Tips_Text_ID)

# ----------
# EmailSignUp
# ----------
