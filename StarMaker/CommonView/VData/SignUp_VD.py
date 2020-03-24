# coding=utf-8
from StarMaker.Utils.GetDevicesInfo import DevicesInfo
from StarMaker.Utils.reSource import get_mapping_from_file

package = DevicesInfo().package()
mapping_dict = get_mapping_from_file()
gms = "com.google.android"


# ----------
# SignUp
# ----------
# SignUp页面-预选帐号-Tips
SignUpPage_Preselection_Tips_ID = gms + ".gms:id/credentials_hint_picker_title"

# SignUp页面-Tips-text(text="Enter your email address"]
Source_SignUpPage_Tips_Text_ID = "com_accountkit_title"
SignUpPage_Tips_Text_ID = package + mapping_dict[Source_SignUpPage_Tips_Text_ID]

# ----------
# EmailSignUp
# ----------
