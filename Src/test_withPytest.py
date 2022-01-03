import pytest
from Src.BaseClass import BaseClass

class TestExample1(BaseClass):
    def test_1(self):
        log = self.getLogger()
        log.info('Testing info in test case')
