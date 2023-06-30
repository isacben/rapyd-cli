import sys

import clidir

def main() -> int:
    args = sys.argv
    clidir.run(args)
    
    return 0

if __name__ == "__main__":
    exit(main())
