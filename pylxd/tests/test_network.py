# Copyright (c) 2016 Canonical Ltd
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from pylxd import network
from pylxd.tests import testing


class TestNetwork(testing.PyLXDTestCase):
    """Tests for pylxd.network.Network."""

    def test_all(self):
        """A list of all networks are returned."""
        networks = network.Network.all(self.client)

        self.assertEqual(1, len(networks))

    def test_get(self):
        """Return a container."""
        name = 'lo'

        an_network = network.Network.get(self.client, name)

        self.assertEqual(name, an_network.name)

    def test_partial(self):
        """A partial network is synced."""
        an_network = network.Network(self.client, name='lo')

        self.assertEqual('loopback', an_network.type)
