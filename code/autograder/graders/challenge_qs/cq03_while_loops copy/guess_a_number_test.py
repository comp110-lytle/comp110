"""Tests for CQ03 - num_instances function."""

__author__ = "Alyssa Lytle <abyrnes1@cs.unc.edu>"
__author__ = "Viktorya Hunanyan <vhunany@unc.edu>"

import pytest
from pytest import mark
from graders.helpers import reimport_module, assert_parameter_list, assert_return_type

MODULE = "CQs.cq03_while_loops"
module = None

@mark.weight(0)
def test_author():
    """__author__ str variable is correct PID format."""
    module = reimport_module(MODULE)
    assert hasattr(module, '__author__'), "__author__ variable is missing."
    assert isinstance(module.__author__, str), "__author__ should be a string."

@mark.weight(1)
def test_num_instances_params():
    """num_instances should take two parameters: phrase and search_char."""
    module = reimport_module(MODULE)
    # Check the parameter list of the num_instances function
    assert_parameter_list(module.num_instances, ['phrase', 'search_char'])  # WHY IS THIS NOT WORKINGGG????? 


@mark.weight(1)
def test_num_instances_return_type():
    """num_instances should return an integer."""
    module = reimport_module(MODULE)
    # Call num_instances with a sample input and check the return type
    result = module.num_instances('HelloHello', 'e')
    assert_return_type(result, int)  # WHY IS THIS NOT WORKINGGG????? 

@mark.weight(2)
def test_num_instances_basic_cases():
    """num_instances returns correct count for basic test cases."""
    module = reimport_module(MODULE)
    
    # Test case 1
    assert module.num_instances('HelloHeLloHEllo', 'e') == 2, "Failed on test case 1"
    
    # Test case 2
    assert module.num_instances('HelloHelloHello', 'e') == 3, "Failed on test case 2"
    
    # Test case 3
    assert module.num_instances('Happy Tuesday!', 'y') == 2, "Failed on test case 3"
    
    # Test case 4
    assert module.num_instances('Happy Tuesday!', 'z') == 0, "Failed on test case 4"
    
    # Additional Test Cases

    # Test case 5: Single character match
    assert module.num_instances('a', 'a') == 1, "Failed on single character test case (5)"
    
    # Test case 6: Single character no match
    assert module.num_instances('a', 'b') == 0, "Failed on single character no match test case (6)"
    
    # Test case 7: Multiple occurrences of search character at the start and end
    assert module.num_instances('abcabcabc', 'a') == 3, "Failed on multiple occurrences test case (7)"
    
    # Test case 8: Multiple occurrences of search character scattered
    assert module.num_instances('This is an example sentence.', 'e') == 5, "Failed on scattered occurrences test case (8)"
    
    # Test case 9: Empty string should return 0
    assert module.num_instances('', 'a') == 0, "Failed on empty string test case (9)"
    
    # Test case 10: String with no occurrences of search_char
    assert module.num_instances('abcdefg', 'x') == 0, "Failed on no occurrence in string test case (10)"
    
    # Test case 11: Search character is a space
    assert module.num_instances('Count the spaces in this sentence.', ' ') == 5, "Failed on space character test case (11)"
    
    # Test case 12: Search character is a number
    assert module.num_instances('123123123', '2') == 3, "Failed on numeric character test case (12)"
    
    # Test case 13: Special characters in the string
    assert module.num_instances('Testing special characters! @#$', '!') == 1, "Failed on special character test case (13)"
    
    # Test case 14: Repeated characters, case-sensitive
    assert module.num_instances('ABABababABAB', 'A') == 4, "Failed on case-sensitive test case (14)"
    
    # Test case 15: String contains newline characters
    assert module.num_instances('Line1\nLine2\nLine3', '\n') == 2, "Failed on newline character test case (15)"

@mark.weight(1)
def test_num_instances_case_sensitive():
    """num_instances should be case-sensitive."""
    module = reimport_module(MODULE)
    
    # Test case with different case letters
    assert module.num_instances('AaAaAa', 'a') == 3, "Failed case-sensitivity test for lowercase 'a'"
    assert module.num_instances('AaAaAa', 'A') == 3, "Failed case-sensitivity test for uppercase 'A'"

@mark.weight(1)
def test_num_instances_empty_string():
    """num_instances should return 0 if the phrase is an empty string."""
    module = reimport_module(MODULE)
    
    # Test with an empty phrase
    assert module.num_instances('', 'a') == 0, "Failed on empty string case"

@mark.weight(1)
def test_num_instances_no_occurrence():
    """num_instances should return 0 if the search_char does not occur in the phrase."""
    module = reimport_module(MODULE)
    
    # Test with no occurrence of the search character
    assert module.num_instances('This is a test', 'z') == 0, "Failed when search_char is not in phrase"

@mark.weight(1)
def test_num_instances_special_characters():
    """num_instances should handle special characters and spaces."""
    module = reimport_module(MODULE)

    # Test with special characters
    assert module.num_instances('Hello@World!', '@') == 1, "Failed special character test (@)"
    assert module.num_instances('Look! There is a cat!', '!') == 2, "Failed special character test (!)"

@mark.weight(1)
def test_num_instances_numeric_characters():
    """num_instances should handle numeric characters."""
    module = reimport_module(MODULE)

    # Test with numeric characters
    assert module.num_instances('123123123', '1') == 3, "Failed numeric character test (1)"
    assert module.num_instances('9876543210', '0') == 1, "Failed numeric character test (0)"
    
@mark.weight(1)
def test_num_instances_repeated_search_char():
    """num_instances should handle cases where the search_char repeats consecutively."""
    module = reimport_module(MODULE)

    # Test case with repeated consecutive characters
    assert module.num_instances('aaaaaaa', 'a') == 7, "Failed consecutive repeated characters test"
    assert module.num_instances('bbbbbbbbb', 'b') == 9, "Failed consecutive repeated characters test"

@mark.weight(1)
def test_num_instances_large_input():
    """num_instances should efficiently handle large input strings."""
    module = reimport_module(MODULE)
    
    # Test with large input string
    large_phrase = 'a' * 1000000  # 1 million 'a's
    assert module.num_instances(large_phrase, 'a') == 1000000, "Failed large input test"

    large_phrase_mixed = 'a' * 500000 + 'b' * 500000  # 500k 'a's and 500k 'b's
    assert module.num_instances(large_phrase_mixed, 'b') == 500000, "Failed large input mixed test"

