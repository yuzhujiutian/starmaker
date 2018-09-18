#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum
from collections import namedtuple


class UIComponents:

    # named tuple to hold two xPath values for each platform
    Component = namedtuple('Component', ['iOS', 'Android'])

    LABEL = Component(iOS='//XCUIElementTypeStaticText[{}]', Android='//android.widget.TextView[{}]')
    BUTTON = Component(iOS='//XCUIElementTypeButton[{}]', Android='//android.widget.Button[{}]')
    TEXTFIELD = Component(iOS='//XCUIElementTypeTextField[{}]', Android='//android.widget.EditText[{}]')
    PWDFIELD = Component(iOS='//XCUIElementTypeSecureTextField[{}]', Android='//android.widget.EditText[{}]')
    LIST = Component(iOS='//XCUIElementTypeTable/*[{}]', Android='//android.widget.ListView/*[{}]')
    SWITCH = Component(iOS='//XCUIElementTypeSwitch[{}]', Android='TBD')
    SLIDER = Component(iOS='//XCUIElementTypeSlider[{}]', Android='TBD')
    ALERT = Component(iOS='//XCUIElementTypeAlert', Android='(//android.widget.LinearLayout | //android.widget.FrameLayout)[contains(@resource-id, \'id/parentPanel\')]')
    # For app compat v7 alert dialog
    # //android.widget.FrameLayout[contains(@resource-id, 'id/action_bar_root')]
    # For native alert dialog
    # //android.widget.LinearLayout[contains(@resource-id, 'id/parentPanel')]