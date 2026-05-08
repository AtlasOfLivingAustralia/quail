# coding=utf-8
"""Dialog test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = "amanda.buyan@csiro.au"
__date__ = "2025-10-01"
__copyright__ = "Copyright 2025, Atlas of Living Australia"

import unittest

from alaQgisPlugin_dialog import AlaQgisPluginDialog
from qgis.PyQt.QtGui import QDialog, QDialogButtonBox
from qgis.testing import mocked, start_app, unittest
from utilities import get_qgis_app

start_app()


class AlaQgisPluginDialogTest(unittest.TestCase):
    """Test dialog works."""

    @classmethod
    def setUp(self):
        """Runs before each test."""
        self.iface = mocked.get_iface()

    @classmethod
    def tearDown(self):
        """Runs after each test."""
        self.iface = None

    def test_mint_doi(self):
        """Test whether or not you get True when you tick the DOI button"""
        checkBox = self.iface.createDoiCheckBox()  # really not sure about this
        checkBox.click()
        result = AlaQgisPluginDialog.mint_doi.result()
        self.assertEqual(result, True)


if __name__ == "__main__":
    suite = unittest.makeSuite(AlaQgisPluginDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
