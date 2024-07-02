#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import argparse

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.DEBUG
)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='hello-cli',
        usage='%(prog)s [options] [NAME]',
        description='This program prints "Hello [NAME]".',
        epilog='epilog'
    )

    parser.add_argument('name', default='World', help="name of whom to greet", type=str)
    parser.add_argument('-v', '--verbose', action='store_true', help='enable verbose output')
    parser.add_argument('-d', '--debug', action='store_true', help='enable debug output')

    args = parser.parse_args()
    hello_message = f'Hello {args.name}!'

    if args.debug:
        logging.debug(args)
    if args.verbose:
        logging.info(hello_message)
    else:
        print(hello_message)


if __name__ == '__main__':
    main()
