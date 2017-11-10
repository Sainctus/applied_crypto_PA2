#!/usr/bin/env python


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", help="Key file", required=True)
    parser.add_argument("--i", help="Input file", required=True)
    parser.add_argument("--o", help="Output file", required=True)
    args = parser.parse_args()

    main(args.k, args.i, args.o)
