from math import pi
from unittest import TestSuite
from unittest import main as unitTestMain

from codeallybasic.UnitTestBase import UnitTestBase

from pyfdl.Point import Point
from pyfdl.Vector import Vector


class TestVector(UnitTestBase):
    """
    Auto generated by the one and only:
        Gato Malo - Humberto A. Sanchez II
        Generated: 07 February 2024
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def testMultiplication(self):

        vector:    Vector = Vector(magnitude=5.0, direction=180.0)
        magVector: Vector = Vector(magnitude=2.0, direction=0)

        newVector: Vector = vector * magVector

        self.assertIsNotNone(newVector, 'Something should come back')

        self.assertEqual(10.0, newVector.magnitude, 'Multiply did not work')
        self.assertEqual(180.0, newVector.direction, 'direction should not change')

    def testToPointFlat(self):
        vector:    Vector = Vector(magnitude=5.0, direction=180.0)

        expectedPoint: Point = Point(x=5, y=0)
        actualPoint:   Point = vector.toPoint()

        self.assertEqual(expectedPoint, actualPoint, 'What the heck')

    def testAddition(self):

        vector:     Vector = Vector(magnitude=1.0, direction=180.0)
        plusVector: Vector = Vector(magnitude=2.0, direction=180.0)

        vectorPoint: Point = vector.toPoint()
        PI_180 = pi / 180.0
        self.logger.info(f'{PI_180=} {vectorPoint=}')

        newVector: Vector = vector + plusVector

        self.assertIsNotNone(newVector, 'Something should come back')

        # direction 1.0
        # magnitude 899.99
        self.assertAlmostEqual(180.0, newVector.direction,   places=2, msg='Direction incorrect')
        self.assertAlmostEqual(3.0, newVector.magnitude, places=2, msg='I guess not close enough')


def suite() -> TestSuite:
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestVector))

    return testSuite


if __name__ == '__main__':
    unitTestMain()
