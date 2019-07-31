# 1、find_elements_by_accessibility_id，以accessibility_id进行定位，
# 对Android而言，就是content-description属性(使用uiautomatorviewer 可以查看到)
#     self.driver.find_element_by_accessibility_id('XXX')
#     self.driver.find_elements_by_accessibility_id('XXX')
#
# 2、find_element_by_class_name, 根据class进行定位
#     self.driver.find_element_by_class_name("android.widget.EditText")  # 定位唯一元素
#     self.driver.find_elements_by_class_name("android.widget.EditText")[0]  # 找到所有android.widget.EditText并定位第一个
#
# 兼容性不高，易报错，根据text定位建议使用方法4
# 3、find_elemnt_by_name, 根据name进行定位，对于android来说，就是text属性
#     self.driver.find_element_by_name("XXX")
#
# 4、find_element_by_android_uiautomator, 使用uiautomator定位，后面参数更改即可
# - UiSelector().text,根据text属性进行定位
#     self.driver.find_element_by_android_uiautomator('new UiSelector().text("XXX")')
#
# - UISelector.textContains, 根据text属性模糊定位(text包含XXX)
#     self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("XXX")')
#
# - UISelector.textStartsWith, 根据text的前面几位是否与text一致来定位(text以XXX开头)
#     self.driver.find_element_by_android_uiautomator('new UiSelector().textStartsWith("XXX")')
#
# - UISelector.textMatches, 通过正则表达式和text来进行定位
#
# 5、UISelector.className, 通过class来进行定位，合理利用层级定位，例如找到所有的Edittext然后根据text定位
#     self.driver.find_element_by_android_uiautomator('new UiSelector()'
#                                                      '.className("android.widget.EditText")'
#                                                      '.textContains("XXX")')
#
# 6、UISelector.classNameMatches, 通过正则表达式和class来进行定位
#
# 7、UiSelector.description, 通过描述定位(参考4)
# - UiSelector.descriptionMatches, 通过描述模糊匹配
# - UiSelector.descriptionStartWith, 通过描述开头匹配
#
# 8、driver.find_element_by_id 与 UiSeletor.resourceId
# 都是通过resourceId来进行定位，这个属性只有在ApiLevel 18(Android 4.3 Jelly Bean  糖豆)以上才有
#     self.driver.find_element_by_id("XXX")
#     self.driver.find_element_by_android_uiautomator('new Uiseletor()'
#                                                              '.resourceId'
#                                                              '("XXX")')
