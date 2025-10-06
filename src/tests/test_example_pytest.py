"""
Docstring
test_example_pytest.py
Show a demo for Pytest tests and fixtures
"""
import pytest
import logging

from utils.logger import get_logger

logger = get_logger(__name__)

class TestExamplePytest:
    """
    Test Example Pytest to show fixtures and tests
    """
    def setup_class(self):
        """
        Setup class to initialize environment and browser
        """
        logger.debug("Setup class")
        self.environment = pytest.env

    # fixture
    def setup_method(self):
        logger.debug("Setup")

    def test_one(self):
        """
        Test one shows the test name
        """
        logger.debug("test one")

    def test_two(self, first_entry):
        """
        Test two shows the test name and a parameter first entry
        @param first_entry: fixture first entry fixture return a string
        """
        logger.debug("test two: %s", first_entry)

    def test_three(self, order):
        logger.debug("test three: %s", order)

    # fixture
    def teardown_method(self):
        logger.debug("tearDown")

    def teardown_class(self):
        logger.debug("Teardown class")