import sys
import random
import katapayadi as kpd
from stardict import StarDictReader

def print_usage():
    print("""
Usage
    print('python main.py [--method=<brute|dict>] [--mode=<single>] <number>')
method: brute - Permutation based
              dict  - Dictionary based
mode:  single - Outputs only one value
    """)

def generate_bruteforce(num):
    print('Using bruteforce method to generate ...')
    chars = kpd.select_chars(num)
    permutechars = kpd.permute_chars(chars)
    kwords = []
    for c in permutechars:
        ml = kpd.add_maathras("".join(c))
        for m in ml:
            cwords = kpd.add_half_consonants(m)
            kwords.extend(cwords)
    return kwords

def remove_maathras(word):
    nw = ''
    for i,c in enumerate(word):
        if not kpd.is_maathra(c):
            nw += c
    return nw

def remove_half_consonants(word):
    nw = ''
    for i,c in enumerate(word):
        if kpd.is_vyanjana(c):
            if (i+1) < len(word):
                if word[i+1] != '\u094D':
                    nw += c
            else:
                nw += c
        elif c != '\u094D':
            nw += c
    return nw

def convert_katapayadi_number(w):
    num = ''
    #print('length: ', len(w))
    for i in range(len(w)-1,-1,-1):
        ch = w[i]
        #print(ch)
        if ch in kpd.swaras:
            num += '0'
        else:
            for n, l in kpd.katapayadi_mapping.items():
                if ch in l:
                    num += n
                    break
    return num

def calculate_inverse_katapayadi(w):
    wm = remove_maathras(w)
    #print(wm)
    wm2 = remove_half_consonants(wm)
    #print(wm2)
    num = convert_katapayadi_number(wm2)
    return num

def generate_dict(num):
    print('Using dictionary based method to generate ...')
    words = StarDictReader('dict/apte-1890')._words
    nlist = {}
    for i in range(int(len(num)/2)):
        nlist[num[2*i:2*i+2]] = []
    for w in words:
        ik = calculate_inverse_katapayadi(w)
        if ik in nlist:
            nlist[ik].append(w)
    for n in nlist:
        print(n)
        print(nlist[n])
        

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
    num = cmdargs['num']
    if cmdargs['method'] == 'brute':
        kwords = generate_bruteforce(num)
        random.seed()
        i = random.randint(0,len(kwords))
        print(f"The Katapayadi string for {num} is: {kwords[i]}")
    elif cmdargs['method'] == 'dict':
        generate_dict(num)
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
