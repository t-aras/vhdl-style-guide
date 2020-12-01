

from vsg.vhdlFile.extract import utils

from vsg.vhdlFile.extract.get_line_succeeding_line import get_line_succeeding_line


def get_line_below_line_ending_with_token(lTokens, lAllTokens, oTokenMap):

    lReturn = []
    
    lTokenIndexes = utils.get_indexes_of_token_list(lTokens, oTokenMap)
    lIndexes = []
    for iIndex in lTokenIndexes:
        if utils.is_token_at_end_of_line(iIndex, oTokenMap):
            lIndexes.append(iIndex)

    lLine = utils.get_line_numbers_of_indexes_in_list(lIndexes, oTokenMap) 
    for iLine in lLine:
        oToi = get_line_succeeding_line(iLine, lAllTokens, 1, oTokenMap)
        if oToi is not None:
            lReturn.append(oToi)

    return lReturn
#
#
#from vsg import parser
#
#from vsg.vhdlFile import utils
#from vsg.vhdlFile import vhdlFile
#
#
#def get_line_below_line_ending_with_token(lTokens, lAllTokens):
#    lReturn = []
#    iLine = 1
#    lTemp = []
#    bTokenFound = False
#    bCrFound = False
#    for iIndex in range(0, len(lAllTokens)):
#
#        if not bTokenFound:
#            for oToken in lTokens:
#                if isinstance(lAllTokens[iIndex], oToken):
#                    if utils.are_next_consecutive_token_types([parser.carriage_return], iIndex + 1, lAllTokens):
#                        bTokenFound = True
#                        break
#                    if utils.are_next_consecutive_token_types([parser.whitespace, parser.carriage_return], iIndex + 1, lAllTokens):
#                        bTokenFound = True
#                        break
#                    if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment, parser.carriage_return], iIndex + 1, lAllTokens):
#                        bTokenFound = True
#                        break
#                    if utils.are_next_consecutive_token_types([parser.comment, parser.carriage_return], iIndex + 1, lAllTokens):
#                        bTokenFound = True
#                        break
#
#
#        if bCrFound:
#            lTemp.append(lAllTokens[iIndex])
#
#        if isinstance(lAllTokens[iIndex], parser.carriage_return):
#            if bCrFound:
#                lTemp.pop()
#                lReturn.append(vhdlFile.Tokens(iStart, iLine, lTemp))
#                lTemp = []
#                bCrFound = False
#                bTokenFound = False
#            elif bTokenFound:
#                bCrFound = True
#                iStart = iIndex + 1
#
#            iLine +=1
#
#    return lReturn
