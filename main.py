import sys
import utils
import random

def select_chars(num):
    chars = []
    for i in range(len(num)-1,-1,-1):
        c = num[i]
        chars.append(utils.katapayadi_mapping[c])
    return chars

def permute_chars(chars):
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

def find_consonant_group_index(chars, cgi):
    """Find index excluding the maatras
     """
    index = si = ei = 0 
    for i in range(len(chars)):
        if list(filter(lambda x:x, [chars[i] in cl for cl in utils.vyanjanas])):
            index = index + 1
        if index == cgi:
            si = ei = i
            while ei + 1 < len(chars):
                if utils.is_vyanjana(chars[ei+1]):
                    break
                else:
                    ei += 1
            break
    return (si, ei)

def add_maathras(clist):
    """ Add maatras to each character in the list
    """
    ml = [clist[0]+m+clist[1:] for m in utils.maathras[:-2]]
    numc = utils.count_vyanjanas(clist)
    for i in range(2, numc+1):
        newl = []
        for c in ml:
            si, ei = find_consonant_group_index(c, i)
            if i != numc:
                newl.extend([c[:ei]+c[ei]+m+c[ei+1:] for m in utils.maathras[:-2]])
            else:
                newl.extend([c+m for m in utils.maathras])
        ml = newl
    return ml

def create_consonants_list():
    cl = []
    for c in utils.vyanjanas:
        cl.extend(c)
    return cl

def add_half_consonants(clist, utmost=1):
    """ Add half consonants with upper limit
    """
    inscount = 0
    numc = utils.count_vyanjanas(clist)
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

def print_usage():
    print('Usage')
    print('python main.py [--method=<brute>] [--mode=<single>] <number>')

def generate_bruteforce(num):
    print('Using bruteforce method to generate ...')
    chars = select_chars(num)
    permutechars = permute_chars(chars)
    kwords = []
    for c in permutechars:
        ml = add_maathras("".join(c))
        for m in ml:
            cwords = add_half_consonants(m)
            kwords.extend(cwords)
    return kwords

def parse_arguments(argv):
    cmdargs = dict(mode='single', method='brute',num='')
    options = ['mode','method']
    for usropt in argv:
        found = 0
        for i, opt in enumerate(options):
            if usropt.find(opt) != -1:
                cmdargs[opt] = usropt.split('=')[1]
                found = 1
                break
        if found:
            del options[i]
        else:
            try:
                _ = int(usropt)
            except Exception as e:
                print_usage()
                raise e
            cmdargs['num'] = usropt
    return cmdargs
    
def main(argv):
    cmdargs = parse_arguments(argv)
    if cmdargs['method'] == 'brute':
        num = cmdargs['num']
        kwords = generate_bruteforce(num)
        random.seed()
        i = random.randint(0,len(kwords))
        print(f"The Katapayadi string for {num} is: {kwords[i]}")          
    else:
        print('Unknown mode')
        print_usage()
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        cmdargs = input('Enter command line arguments: ')
        cmdargs = list(cmdargs.split())
    else:
        cmdargs = sys.argv[1:]
    if '=' in cmdargs or '--' in cmdargs:
        # Check whether unnecessary space is added
        print_usage()
    else:
        main(cmdargs)
