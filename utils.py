maathras = [
    '',          '\u093E',
    '\u093F','\u0940',
    '\u0941','\u0942',
    '\u0943',
    '\u0944',
    '\u0947',
    '\u0948',
    '\u094B',
    '\u094C',
    '\u0902',
    '\u0903',]

vyanjanas = [
    ['\u0915','\u0916','\u0917','\u0918','\u0919'],
    ['\u091A','\u091B','\u091C','\u091D','\u091E'],
    ['\u091F','\u0920','\u0921','\u0922','\u0923'],
    ['\u0924','\u0925','\u0926','\u0927','\u0928'],
    ['\u092A','\u092B','\u092C','\u092D','\u092E'],
    ['\u092F','\u0930','\u0932','\u0935','\u0936','\u0937','\u0938','\u0939']
]

swaras = [
    '\u0905','\u0906',
    '\u0907','\u0908',
    '\u0909','\u090A',
    '\u090B',
    '\u090C',
    '\u090F',
    '\u0910',
    '\u0913',
    '\u0914'
]

katapayadi_mapping = {
    '1': [vyanjanas[0][0],  vyanjanas[2][0],  vyanjanas[4][0], vyanjanas[5][0]],
    '2': [vyanjanas[0][1],  vyanjanas[2][1],  vyanjanas[4][1], vyanjanas[5][1]],
    '3': [vyanjanas[0][2],  vyanjanas[2][2], vyanjanas[4][2], vyanjanas[5][2]],
    '4': [vyanjanas[0][3],  vyanjanas[2][3], vyanjanas[4][3], vyanjanas[5][3]],
    '5': [vyanjanas[0][4],  vyanjanas[2][4], vyanjanas[4][4], vyanjanas[5][4]],
    '6': [vyanjanas[1][0],  vyanjanas[3][0], vyanjanas[5][5]],
    '7': [vyanjanas[1][1],  vyanjanas[3][1], vyanjanas[5][6]],
    '8': [vyanjanas[1][2],  vyanjanas[3][2], vyanjanas[5][7]],
    '9': [vyanjanas[1][3],  vyanjanas[3][3]],
    '0': [vyanjanas[1][4],  vyanjanas[3][4]]
}

def count_vyanjanas(clist):
    """ Counts the number of vjanjanas
         excluding maathras and 
    """
    count = 0
    for i in range(len(clist)):
         if list(filter(lambda x:x, [clist[i] in cl for cl in vyanjanas])):
             count += 1
    return count

def is_vyanjana(c):
    """ Checks whether a character c is a consonant.
    """
    return  list(filter(lambda x:x, [c in cl for cl in vyanjanas])) == [True]

def is_maathra(c):
    """ Checks whether a character c is a maathra.
    """
    return c in maathras[1:]
