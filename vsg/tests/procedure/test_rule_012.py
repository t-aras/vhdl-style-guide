
import os
import unittest

from vsg.rules import procedure
from vsg import vhdlFile
from vsg.tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_012_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_012_test_input.fixed.vhd'), lExpected)


class test_procedure_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_012(self):
        oRule = procedure.rule_012()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'procedure')
        self.assertEqual(oRule.identifier, '012')
        self.assertEqual(oRule.groups, ['structure', 'structure::optional'])

        lExpected = [10]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_012(self):
        oRule = procedure.rule_012()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
