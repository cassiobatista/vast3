#!/usr/bin/env python3
#
# VAST Challenge 2019: Disaster at St. Himark!
# https://vast-challenge.github.io/2019/index.html
#
# Federal University of Pará (UFPA)
#
# author: june 2019
# cassio batista - cassio.batista.13@gmail.com
# edwin jueda - 
# erick campos - 

from xml.dom import minidom
import config

class SVGNode:
    def __init__(self, root, tag):
        super(SVGNode, self).__init__()
        self.root     = root
        self.tag      = tag
        self.level    = config.SVG_NODE_HIERARCHY.index(self.tag)
        self.metadata = {}
        self.children = []

        if self.root.hasAttributes():
            self.metadata = dict(self.root.attributes.items())

        if 'style' in self.metadata:
            self.metadata['style'] = dict(tuple(pair.split(':')) \
                    for pair in self.metadata['style'].split(';'))

        if self.root.hasChildNodes():
            for tag in config.SVG_NODE_HIERARCHY[self.level+1:]:
                for child in self.root.getElementsByTagName(tag):
                    self.children.append(SVGNode(child, tag))

    def to_string(self):
        string = '<' + self.tag + '\n'
        for key, value in self.metadata.items():
            if key == 'style':
                string += '%s="' % key
                for k, v in value.items():
                    string += '%s:%s;' % (k,v)
                string += '"\n'
                continue
            string += '%s="%s"\n' % (key, value)
        string += '>' + '\n'
        for child in self.children:
            string += child.to_string()
        string += '</' + self.tag + '>\n'
        return string

if __name__=='__main__':
    doc  = minidom.parse(config.SVGTEST)
    tag  = config.SVG_NODE_HIERARCHY[0]
    root = doc.getElementsByTagName(tag)[0]
    svg  = SVGNode(root, tag)
    print(svg.to_string())
