#!/usr/bin/env python
# encoding=utf-8

from __future__ import print_function, unicode_literals

from collections import namedtuple
from itertools import cycle

import jinja2
from PIL import Image

Point = namedtuple('Point', ['x', 'y'])
Pixel = namedtuple('Pixel', ['r', 'g', 'b'])
RenderItem = namedtuple('RenderItem', ['color', 'char'])
RenderGroup = list
HTMLImage = list

TEMPLATE = '''
<html>
<head>
    <meta charset="utf-8">
    <title>{{ title }}</title>
    <style type="text/css">
        body {
            margin: 0px; padding: 0px; line-height:100%; letter-spacing:0px; text-align: center;
            min-width: {{width}}px;
            width: auto !important;
            font-size: {{size}}px;
            background-color: #{{background}};
            font-family: {{font_family}};
        }
    </style>
</head>
<body>
<div>
{% for group in html_image %}
    {% for item in group %}<font color="#{{ item.color }}">{{ item.char }}</font>{% endfor %}
    <br>
{% endfor %}
</div>
</body>
</html>'''


_c = cycle(r'/-\|')


def _progress_callback(percent):
    if percent == 100:
        print('\rDone!               ')
    else:
        import sys, time
        lca = getattr(_progress_callback, '_last_call_at', 0)
        if time.time() - lca > 0.1:
            _progress_callback._last_call_at = time.time()
            sys.stdout.write('\r{} progress: {:.2f}%'.format(_c.next(), percent))
            sys.stdout.flush()


class Img2HTMLConverter(object):
    def __init__(self,
                 font_size=10,
                 char='䦗',
                 background='#000000',
                 title='img2html by xlzd',
                 font_family='monospace',
                 progress_callback=None):
        self.font_size = font_size
        self.background = background
        self.title = title
        self.font_family = font_family
        if isinstance(char, str):
            char = char.decode('utf-8')
        self.char = cycle(char)
        self._prg_cb = progress_callback or _progress_callback

    def convert(self, source):
        image = Image.open(source)

        width, height = image.size
        row_blocks = int(round(float(width) / self.font_size))
        col_blocks = int(round(float(height) / self.font_size))

        html_image = HTMLImage()
        progress = 0.0
        step = 1. / (col_blocks * row_blocks)

        for col in xrange(col_blocks):
            render_group = RenderGroup()
            for row in xrange(row_blocks):
                pixels = []
                for y in xrange(self.font_size):
                    for x in xrange(self.font_size):
                        point = Point(row * self.font_size + x, col * self.font_size + y)
                        if point.x >= width or point.y >= height:
                            continue
                        pixels.append(Pixel(*image.getpixel(point)[:3]))
                average = self.get_average(pixels=pixels)
                color = self.rgb2hex(average)
                render_item = RenderItem(color=color, char=self.char.next())
                render_group.append(render_item)

                progress += step
                self._prg_cb(progress * 100)

            html_image.append(render_group)

        self._prg_cb(100)
        return self.render(html_image)

    def render(self, html_image):
        template = jinja2.Template(TEMPLATE)
        return template.render(
            html_image=html_image,
            size=self.font_size,
            background=self.background,
            title=self.title,
            font_family=self.font_family,
            width=self.font_size * len(html_image[0]) * 2
        )

    @staticmethod
    def rgb2hex(pixel):
        return '{:02x}{:02x}{:02x}'.format(*pixel)

    @staticmethod
    def get_average(pixels):
        r, g, b = 0, 0, 0
        for pixel in pixels:
            r += pixel.r
            g += pixel.g
            b += pixel.b
        base = float(len(pixels))
        return Pixel(
            r=int(round(r / base)),
            g=int(round(g / base)),
            b=int(round(b / base)),
        )
