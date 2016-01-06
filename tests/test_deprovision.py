# Copyright 2014 Microsoft Corporation
#
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
#
# Requires Python 2.4+ and Openssl 1.0+
#
# Implements parts of RFC 2131, 1541, 1497 and
# http://msdn.microsoft.com/en-us/library/cc227282%28PROT.10%29.aspx
# http://msdn.microsoft.com/en-us/library/cc227259%28PROT.13%29.aspx

import tests.env
from tests.tools import *
import unittest
import azurelinuxagent.distro.default.deprovision as deprovision_handler

def MockAction(param):
    #print param
    pass

def MockSetup(self, deluser):
    warnings = ["Print warning to console"]
    actions = [
        deprovision_handler.DeprovisionAction(MockAction, ['Take action'])
    ]
    return warnings, actions

class TestDeprovisionHandler(unittest.TestCase):
    def test_setup(self):
        handler = deprovision_handler.DeprovisionHandler(None)
        warnings, actions = handler.setup(False)
        self.assertNotEquals(None, warnings)
        self.assertNotEquals(0, len(warnings))
        self.assertNotEquals(None, actions)
        self.assertNotEquals(0, len(actions))
        self.assertEquals(deprovision_handler.DeprovisionAction, type(actions[0]))

    
    @mock(deprovision_handler.DeprovisionHandler, 'setup', MockSetup)
    def test_deprovision(self):
        handler = deprovision_handler.DeprovisionHandler(None)
        handler.deprovision(force=True)

if __name__ == '__main__':
    unittest.main()