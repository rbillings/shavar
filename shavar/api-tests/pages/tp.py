# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pypom import Page, Region
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TrackingProtectionPage(Page):

    _cat_locator = (By.CSS_SELECTOR, '#cat')
    _fox_locator = (By.CSS_SELECTOR, '#fox')

    @property
    def tracking_protection_off(self):
        return self.is_element_displayed(*self._cat_locator )

    @property
    def tracking_protection_on(self):
        return self.is_element_displayed(*self._fox_locator )
