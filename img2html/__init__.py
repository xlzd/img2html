#!/usr/bin/env python
# encoding=utf-8

from __future__ import print_function, unicode_literals

import argparse
import codecs

from img2html.converter import Img2HTMLConverter


def main():
    parser = argparse.ArgumentParser(description='img2html : Convert image to HTML')
    parser.add_argument('-b', '--background', default='000000', metavar='#RRGGBB',
                        help='background color (#RRGGBB format)')
    parser.add_argument('-s', '--size', default=10, type=int, metavar='(4~30)',
                        help='font size (int)')
    parser.add_argument('-c', '--char', default='爱', metavar='CHAR',
                        help='characters')
    parser.add_argument('-t', '--title', default='img2html by xlzd', metavar='TITLE',
                        help='html title')
    parser.add_argument('-f', '--font', default='monospace', metavar='FONT',
                        help='html font')
    parser.add_argument('-i', '--in', metavar='IN', help='image to convert', required=True)
    parser.add_argument('-o', '--out', default=None, metavar='OUT',
                        help='output file')

    args, text = parser.parse_known_args()

    converter = Img2HTMLConverter(
        font_size=args.size,
        char=args.char,
        background=args.background,
        title=args.title,
        font_family=args.font,
    )
    html = converter.convert(getattr(args, 'in'))

    if args.out:
        with codecs.open(args.out, 'wb', encoding='utf-8') as fp:
            fp.write(html)
    else:
        print(html)
