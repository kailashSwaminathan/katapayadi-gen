import sys

def print_usage():
    print()
    
def main(argv):
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
    else:
        main(sys.argv)
