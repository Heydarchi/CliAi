# This is a test file for the AppSetting class
import unittest
import pytest
from modules.utility.AppSetting import AppSetting


class MyTestCase(unittest.TestCase):
    def test_init(self):
        app_setting = AppSetting()
        self.assertEqual(app_setting.openapi_key, None)

    def test_get_api_key_raises_exception(self):
        app_setting = AppSetting()
        with pytest.raises(ValueError, match="API key is not set"):
            app_setting.get_api_key()
