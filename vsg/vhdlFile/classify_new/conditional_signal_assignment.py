
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import conditional_waveform_assignment
from vsg.vhdlFile.classify_new import conditional_force_assignment

'''
    conditional_signal_assignment ::=
        conditional_waveform_assignment
      | conditional_force_assignment
'''

def detect(iToken, lObjects):

    if utils.is_next_token('when', iToken, lObjects):
        return False
    if utils.find_in_range('<=', iToken, ';', lObjects):
        if utils.find_in_range('when', iToken, ';', lObjects):
            return True
        return False
    return False


def classify(iToken, lObjects):

    iCurrent = conditional_force_assignment.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent    

    iCurrent = conditional_waveform_assignment.detect(iToken, lObjects)

    return iCurrent
