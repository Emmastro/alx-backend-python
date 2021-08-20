#!/usr/bin/env python3
""" test file """
import unittest
from unittest.mock import patch
from parameterized import parameterized

from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):
    """ Class test nested map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """ returns correct output """
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """ raises correct exception """

        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)

        self.assertEqual(str(e.exception)[1:-1], wrong_output)


class TestGetJson(unittest.TestCase):
    """ Test with json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ test utils.get_json """
        mock_get.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ test with memoize """
    def test_memoize(self):
        """ Ttest assert_called_once
        """
        class TestClass:
            """ class """
            def a_method(self):
                """ method  """
                return 42

            @memoize
            def a_property(self):
                """ property """
                return self.a_method()
        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once