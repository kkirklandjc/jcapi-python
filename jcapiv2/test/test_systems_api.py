# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import jcapiv2
from jcapiv2.rest import ApiException
from jcapiv2.apis.systems_api import SystemsApi


class TestSystemsApi(unittest.TestCase):
    """ SystemsApi unit test stubs """

    def setUp(self):
        self.api = jcapiv2.apis.systems_api.SystemsApi()

    def tearDown(self):
        pass

    def test_graph_system_associations_list(self):
        """
        Test case for graph_system_associations_list

        List the associations of a System
        """
        pass

    def test_graph_system_associations_post(self):
        """
        Test case for graph_system_associations_post

        Manage associations of a System
        """
        pass

    def test_graph_system_member_of(self):
        """
        Test case for graph_system_member_of

        List the parent Groups of a System
        """
        pass

    def test_graph_system_traverse_command(self):
        """
        Test case for graph_system_traverse_command

        List the Commands bound to a System
        """
        pass

    def test_graph_system_traverse_policy(self):
        """
        Test case for graph_system_traverse_policy

        List the Policies bound to a System
        """
        pass

    def test_graph_system_traverse_user(self):
        """
        Test case for graph_system_traverse_user

        List the Users bound to a System
        """
        pass

    def test_graph_system_traverse_user_group(self):
        """
        Test case for graph_system_traverse_user_group

        List the User Groups bound to a System
        """
        pass

    def test_systems_get_fde_key(self):
        """
        Test case for systems_get_fde_key

        Get System FDE Key
        """
        pass


if __name__ == '__main__':
    unittest.main()
