import sys
import random
import katapayadi as kpd

def print_usage():
    print('Usage')
    print('python main.py [--method=<brute>] [--mode=<single>] <number>')
    print("""method: brute - Permutation based
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
