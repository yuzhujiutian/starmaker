# coding=utf-8
from StarMaker.Utils.GetDevicesInfo import DevicesInfo
from StarMaker.Utils.reSource import get_mapping_from_file

package = DevicesInfo().package()
mapping_dict = get_mapping_from_file()
gms = "com.google.android"


# ----------
# Development
# ----------
# Development-勾选框-通用ID
DevelopmentPage_CheckBox_IDS = "android.widget.CheckBox"

# Development-打点服务器弹窗-输入框
DevelopmentPage_DotTestServer_InputBox_ID = "android.widget.EditText"

# Development-打点服务器弹窗-确认按钮
DevelopmentPage_DotTestServer_ConfirmButton_ID = "android:id/button1"