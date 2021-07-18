maathras = [
    '',      '\u093E',
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


def select_chars(num):
    """ Returns a list of list of characters for each digit in the
         number as per Katapayadi.
    """
    chars = []
    for i in range(len(num)-1,-1,-1):
        c = num[i]
        chars.append(katapayadi_mapping[c])
    return chars

def permute_chars(chars):
    """ Creates permutations
    """
    if len(chars) < 2:
        return []
    lchars = [(1,1)] * len(chars)
    # Calculate 
    for i,l in enumerate(chars):
        for z,j in enumerate(lchars):
            if z < i:
                lchars[z] = (lchars[z][0], lchars[z][1]*len(l))
            elif z > i:
                lchars[z] = (lchars[z][0]*len(l), lchars[z][1])
            else:
                pass
    permchars = []
    for i,l in enumerate(lchars):
        pchars = []
        for _ in range(l[0]):
            for c in chars[i]:
                pchars.extend([c]*l[1])
        permchars.append(pchars)
    return [z for z in zip(*permchars)]

def add_maathras(clist):
    """ Add maatras to each character in the list
    """
    ml = [clist[0]+m+clist[1:] for m in maathras[:-2]]
    numc = count_vyanjanas(clist)
    for i in range(2, numc+1):
        newl = []
        for c in ml:
            si, ei = find_consonant_group_index(c, i)
            if i != numc:
                newl.extend([c[:ei]+c[ei]+m+c[ei+1:] for m in maathras[:-2]])
            else:
                newl.extend([c+m for m in maathras])
        ml = newl
    return ml

def find_consonant_group_index(chars, cgi):
    """Find index excluding the maatras
     """
    index = si = ei = 0 
    for i in range(len(chars)):
        if list(filter(lambda x:x, [chars[i] in cl for cl in vyanjanas])):
            index = index + 1
        if index == cgi:
            si = ei = i
            while ei + 1 < len(chars):
                if is_vyanjana(chars[ei+1]):
                    break
                else:
                    ei += 1
            break
    return (si, ei)

def create_consonants_list():
    cl = []
    for c in vyanjanas:
        cl.extend(c)
    return cl

def add_half_consonants(clist, utmost=1):
    """ Add half consonants with upper limit
    """
    inscount = 0
    numc = count_vyanjanas(clist)
    cl = [clist]
    newl = []
    for i in range(numc, 0,-1):
        for c in cl:
            si, ei = find_consonant_group_index(c, i)
            newl.extend([c[:si]+co+'\u094D'+c[si:] for co in create_consonants_list()])
        inscount += 1
        if inscount < utmost:
            cl = cl + newl
            newl = []
    return cl + newl

