#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO
)


def main() -> None:
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = 'World'
    logging.info(f'Hello {name}!')


if __name__ == '__main__':
    main()
