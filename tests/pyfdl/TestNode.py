from typing import Any
from typing import cast
from unittest import TestSuite
from unittest import main as unitTestMain

from copy import deepcopy

from codeallybasic.UnitTestBase import UnitTestBase

from pyfdl.Point import Point
from tests.pyfdl.FakeNode import FakeNode


def toObjectId(anObject: Any) -> str:
    return hex(id(anObject))


class TestNode(UnitTestBase):
    """
    Auto generated by the one and only:
        Gato Malo - Humberto A. Sanchez II
        Generated: 10 February 2024
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testDeepCopy(self):

        parentNode: FakeNode = FakeNode(location=Point(x=100, y=100), fakeId=100)

        childNode1: FakeNode = FakeNode(location=Point(x=200, y=200), fakeId=200)
        childNode2: FakeNode = FakeNode(location=Point(x=300, y=300), fakeId=300)
        childNode3: FakeNode = FakeNode(location=Point(x=400, y=400), fakeId=400)

        parentNode.addChild(childNode1)
        parentNode.addChild(childNode2)
        parentNode.addChild(childNode3)

        doppleGanger: FakeNode = deepcopy(parentNode)

        parentNodeId:   str = toObjectId(parentNode)
        doppleGangerId: str = toObjectId(doppleGanger)

        self.assertNotEqual(parentNodeId, doppleGangerId, 'Should not be the same Node')

        parentLocationId:       str = toObjectId(parentNode.location)
        doppleGangerLocationId: str = toObjectId(doppleGanger.location)

        self.assertNotEqual(parentLocationId, doppleGangerLocationId, 'Should not be the same location')

        self.logger.info('parentNode connections:')
        for child in parentNode.connections:
            fakeNode: FakeNode = cast(FakeNode, child)
            childId: str = toObjectId(fakeNode)
            self.logger.info(f'{fakeNode._id} {childId}')

        self.logger.info('doppleGanger connections:')
        for child in doppleGanger.connections:
            fakeNode = cast(FakeNode, child)
            childId = toObjectId(fakeNode)
            self.logger.info(f'{fakeNode._id} {childId}')


def suite() -> TestSuite:
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestNode))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
