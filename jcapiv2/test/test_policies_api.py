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
from jcapiv2.apis.policies_api import PoliciesApi


class TestPoliciesApi(unittest.TestCase):
    """ PoliciesApi unit test stubs """

    def setUp(self):
        self.api = jcapiv2.apis.policies_api.PoliciesApi()

    def tearDown(self):
        pass

    def test_graph_policy_associations_list(self):
        """
        Test case for graph_policy_associations_list

        List the associations of a Policy
        """
        pass

    def test_graph_policy_associations_post(self):
        """
        Test case for graph_policy_associations_post

        Manage the associations of a Policy
        """
        pass

    def test_graph_policy_traverse_system(self):
        """
        Test case for graph_policy_traverse_system

        List the Systems bound to a Policy
        """
        pass

    def test_graph_policy_traverse_system_group(self):
        """
        Test case for graph_policy_traverse_system_group

        List the System Groups bound to a Policy
        """
        pass

    def test_policies_delete(self):
        """
        Test case for policies_delete

        Deletes a Policy
        """
        pass

    def test_policies_get(self):
        """
        Test case for policies_get

        Gets a specific Policy.
        """
        pass

    def test_policies_list(self):
        """
        Test case for policies_list

        Lists all the Policies
        """
        pass

    def test_policies_post(self):
        """
        Test case for policies_post

        Create a new Policy
        """
        pass

    def test_policies_put(self):
        """
        Test case for policies_put

        Update an existing Policy
        """
        pass

    def test_policyresults_get(self):
        """
        Test case for policyresults_get

        Get a specific Policy Result.
        """
        pass

    def test_policyresults_list(self):
        """
        Test case for policyresults_list

        Lists all the policy results for an organization.
        """
        pass

    def test_policyresults_list_0(self):
        """
        Test case for policyresults_list_0

        Lists all the policy results of a policy.
        """
        pass

    def test_policystatuses_list(self):
        """
        Test case for policystatuses_list

        Lists the latest policy results of a policy.
        """
        pass

    def test_policystatuses_list_0(self):
        """
        Test case for policystatuses_list_0

        List the policy statuses for a system
        """
        pass

    def test_policytemplates_get(self):
        """
        Test case for policytemplates_get

        Get a specific Policy Template
        """
        pass

    def test_policytemplates_list(self):
        """
        Test case for policytemplates_list

        Lists all of the Policy Templates
        """
        pass


if __name__ == '__main__':
    unittest.main()
