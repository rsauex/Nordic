#!/usr/bin/python3

import os
import sys
import xml.sax
import subprocess

def inkscape_render_rect(icon_file, rect, output_file):
    print("%s %s %s" % (icon_file, rect, output_file))

class ContentHandler(xml.sax.ContentHandler):
    ROOT = 0
    SVG = 1
    LAYER = 2
    OTHER = 3
    TEXT = 4

    def __init__(self, path, force=False, filter=None):
        self.stack = [self.ROOT]
        self.inside = [self.ROOT]
        self.path = path
        self.rects = []
        self.state = self.ROOT
        self.chars = ""
        self.force = force
        self.filter = filter

    def endDocument(self):
        pass

    def startElement(self, name, attrs):
        if self.inside[-1] == self.ROOT:
            if name == "svg":
                self.stack.append(self.SVG)
                self.inside.append(self.SVG)
                return
        elif self.inside[-1] == self.SVG:
            if (name == "g" and ('inkscape:groupmode' in attrs) and ('inkscape:label' in attrs)
               and attrs['inkscape:groupmode'] == 'layer' and attrs['inkscape:label'].startswith('Baseplate')):
                self.stack.append(self.LAYER)
                self.inside.append(self.LAYER)
                self.context = None
                self.icon_name = None
                self.rects = []
                return
        elif self.inside[-1] == self.LAYER:
            if name == "text" and ('inkscape:label' in attrs) and attrs['inkscape:label'] == 'context':
                self.stack.append(self.TEXT)
                self.inside.append(self.TEXT)
                self.text = 'context'
                self.chars = ""
                return
            elif name == "text" and ('inkscape:label' in attrs) and attrs['inkscape:label'] == 'icon-name':
                self.stack.append(self.TEXT)
                self.inside.append(self.TEXT)
                self.text = 'icon-name'
                self.chars = ""
                return
            elif name == "rect":
                self.rects.append(attrs)

        self.stack.append(self.OTHER)

    def endElement(self, name):
        stacked = self.stack.pop()
        if self.inside[-1] == stacked:
            self.inside.pop()

        if stacked == self.TEXT and self.text is not None:
            assert self.text in ['context', 'icon-name']
            if self.text == 'context':
                self.context = self.chars
            elif self.text == 'icon-name':
                self.icon_name = self.chars
            self.text = None
        elif stacked == self.LAYER:
            assert self.icon_name
            assert self.context

            if self.filter is not None and not self.icon_name in self.filter:
                return

            for rect in self.rects:
                width = rect['width']
                height = rect['height']
                id = rect['id']

                # inkscape_render_rect(self.path, id, os.path.join(self.context, self.icon_name))
                inkscape_render_rect(self.path, id, self.icon_name)

    def characters(self, chars):
        self.chars += chars.strip()

for f in sys.argv[1:]:
    if os.path.exists(os.path.join(f)):
        handler = ContentHandler(f, True)
        xml.sax.parse(open(f), handler)
    else:
        print ("Error: No such file", f)
        sys.exit(1)
