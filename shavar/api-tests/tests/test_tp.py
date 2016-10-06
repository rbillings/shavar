# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import time

from pages.tp import TrackingProtectionPage


@pytest.mark.nondestructive
def test_tp_off(base_url, selenium):
    page = TrackingProtectionPage(selenium, base_url).open()
    assert page.tracking_protection_off
