# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import jcapiv1
from jcapiv1.api.commands_api import CommandsApi  # noqa: E501
from jcapiv1.rest import ApiException


class TestCommandsApi(unittest.TestCase):
    """CommandsApi unit test stubs"""

    def setUp(self):
        self.api = jcapiv1.api.commands_api.CommandsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_command_file_get(self):
        """Test case for command_file_get

        Get a Command File  # noqa: E501
        """
        pass

    def test_commands_delete(self):
        """Test case for commands_delete

        Delete a Command  # noqa: E501
        """
        pass

    def test_commands_get(self):
        """Test case for commands_get

        List an individual Command  # noqa: E501
        """
        pass

    def test_commands_list(self):
        """Test case for commands_list

        List All Commands  # noqa: E501
        """
        pass

    def test_commands_post(self):
        """Test case for commands_post

        Create A Command  # noqa: E501
        """
        pass

    def test_commands_put(self):
        """Test case for commands_put

        Update a Command  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
