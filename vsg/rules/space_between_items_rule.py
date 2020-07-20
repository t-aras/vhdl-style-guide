
from vsg import rule
from vsg import parser
from vsg import utils


class space_between_items_rule(rule.rule):
    '''
    Checks for and fixes none or multiple spaces after a word.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    sObjectType : string
       The object to check the space after.

    Attributes
    ----------

    self.phase : integer = 2
       Sets the phase the rule will run in.

    self.solution : string = None
       Instructions on how to fix the violation.
    '''

    def __init__(self, name, identifier, left, right, word):
        rule.rule.__init__(self, name=name, identifier=identifier)
        self.phase = 2
        self.solution = None
        self.spaces = 1
        self.configuration.append('spaces')
        self.sWord = word
        self.left = left
        self.right = right

    def analyze(self, oFile):
        lContexts = oFile.get_context_declarations()
        for dContext in lContexts:
            for iLine, oLine in enumerate(dContext['lines']):
                lObjects = oLine.get_objects()
                lAnalysis = []
                bLeftFound = False
                for iObject, oObject in enumerate(lObjects):
                    if isinstance(oObject, self.left):
                        bLeftFound = True
                    if bLeftFound:
                        lAnalysis.append(oObject)
                    if isinstance(oObject, self.right):
                        if len(lAnalysis) == 3:
                            if isinstance(lAnalysis[1], parser.whitespace):
                                if lAnalysis[1].get_value() != ' ' * self.spaces:
                                    self.add_violation(utils.create_violation_dict(dContext['metadata']['iStartLineNumber'] + iLine))

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = utils.get_violating_line(oFile, dViolation)
            lObjects = oLine.get_objects()
            for iObject, oObject in enumerate(lObjects):
                if isinstance(oObject, self.left):
                    lObjects[iObject + 1].set_value(' ' * self.spaces)
                    oLine.update_objects(lObjects)
                    break

    def _get_solution(self, iLineNumber):
        return 'Ensure there are only ' + str(self.spaces) + ' space(s) after the ' + self.sWord
