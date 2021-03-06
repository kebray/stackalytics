# Copyright (c) 2013 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import copy
import mock
import testtools

from stackalytics.processor import normalizer
from tests.unit import test_data


class TestDefaultDataProcessor(testtools.TestCase):
    def setUp(self):
        super(TestDefaultDataProcessor, self).setUp()

        self.get_users = mock.Mock(return_value=[
            test_data.USERS,
        ])

        normalized_data = copy.deepcopy(test_data.DEFAULT_DATA)
        normalizer.normalize_default_data(normalized_data)

    def tearDown(self):
        super(TestDefaultDataProcessor, self).tearDown()

    def test_normalizer(self):
        data = copy.deepcopy(test_data.DEFAULT_DATA)

        normalizer.normalize_default_data(data)

        self.assertIn('releases', data['repos'][0])
        self.assertEqual([], data['repos'][0]['releases'],
                         message='Empty list of releases expected')
        self.assertEqual(0, data['users'][0]['companies'][-1]['end_date'],
                         message='The last company end date should be 0')
        self.assertIn('user_id', data['users'][0])
        self.assertEqual(test_data.USERS[0]['launchpad_id'],
                         data['users'][0]['user_id'],
                         message='User id should be set')
