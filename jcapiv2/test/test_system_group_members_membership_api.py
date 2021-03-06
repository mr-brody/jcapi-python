# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The next version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings. The most recent version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import jcapiv2
from jcapiv2.rest import ApiException
from jcapiv2.apis.system_group_members_membership_api import SystemGroupMembersMembershipApi


class TestSystemGroupMembersMembershipApi(unittest.TestCase):
    """ SystemGroupMembersMembershipApi unit test stubs """

    def setUp(self):
        self.api = jcapiv2.apis.system_group_members_membership_api.SystemGroupMembersMembershipApi()

    def tearDown(self):
        pass

    def test_graph_system_group_member_of(self):
        """
        Test case for graph_system_group_member_of

        List the System Group's parents
        """
        pass

    def test_graph_system_group_members_list(self):
        """
        Test case for graph_system_group_members_list

        List the members of a System Group
        """
        pass

    def test_graph_system_group_members_post(self):
        """
        Test case for graph_system_group_members_post

        Manage the members of a System Group
        """
        pass

    def test_graph_system_group_membership(self):
        """
        Test case for graph_system_group_membership

        List the System Group's membership
        """
        pass


if __name__ == '__main__':
    unittest.main()
