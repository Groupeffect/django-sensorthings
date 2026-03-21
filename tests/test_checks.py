# from __future__ import annotations

# import re

# import pytest
# from django.core.checks import CheckMessage, Error
# from django.core.management import base, call_command
# from django.test import SimpleTestCase
# from django.test.utils import override_settings

# from sensorthings.checks import check_settings


# class ChecksTests(SimpleTestCase):
#     def check_error_codes(self, expected: list[str]) -> list[CheckMessage]:
#         errors = check_settings()
#         assert len(errors) == len(expected)
#         assert all(isinstance(e, Error) for e in errors)
#         assert [e.id for e in errors] == expected
#         return errors

#     def test_defaults_pass(self):
#         self.check_error_codes([])

#     def test_defaults_pass_check(self):
#         call_command("check")


#     @override_settings(SENSORTHING_API_PREFIX=object)
#     def test_api_prefix_obj(self):
#         self.check_error_codes(["sensorthings.E001"])

#     @override_settings(SENSORTHING_API_PREFIX=[object])
#     def test_api_prefix_list(self):
#         self.check_error_codes(["sensorthings.E001"])

#     @override_settings(SENSORTHING_API_PREFIX=1111)
#     def test_api_prefix_int(self):
#         self.check_error_codes(["sensorthings.E001"])

#     @override_settings(SENSORTHING_API_PREFIX=11.11)
#     def test_api_prefix_float(self):
#         self.check_error_codes(["sensorthings.E001"])

#     @override_settings(SENSORTHING_API_PREFIX="accept")
#     def test_api_prefix_string(self):
#         """success"""
#         self.check_error_codes(["sensorthings.E001"])
