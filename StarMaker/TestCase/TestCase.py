# coding=utf-8
# import time
# from CommonView.Home import Home
# from Utils.GetAppiumDeriver import GetAppiumDeriver
# from Utils.Tools import Page_Element_Verification


# def test():
#     a = GetAppiumDeriver().driver
#     time.sleep(5)
#     Home().HomeTab_Profile().click()
#     A = "com.starmakerinteractive.starmaker:id/tv_new_entrance_profile"
#     T = Page_Element_Verification().PEV_IDS(A)
#     T1 = ["DRAFTS", "SONGS", "HISTORY", "CHECK IN", "NOBLE", "BADGE", "RECHARGE", "TOOLS"]
#     if T == T1:
#         print("OK")
#     else:
#         print(T)
#         print("No")
#     # B = dr.find_elements_by_id("com.starmakerinteractive.starmaker:id/tv_tab_title")
#     # print(B)
#     time.sleep(5)
#     a.quit()
#
# 1.获取size，返回的是字典，如：{'width': 84, 'height': 84}
# .size
# 2.获取location，返回的是字典，如：{'y': 38, 'x': 192}
# .location





# ["DRAFTS", "SONGS", "HISTORY", "CHECK IN", "NOBLE", "BADGE", "RECHARGE", "TOOLS"]  # LOTTERY,INCOME,LIVE LVL,GUILD
#
# ["PROFILE", "MOMENTS", "POSTS", "COLLABS"]  # SHARES