#!/usr/bin/env python
import re
import sys

comment_re = re.compile(r'/\*.*\*/', re.DOTALL | re.MULTILINE)
space_re = re.compile(r'\s*({|;|:|})\s*', re.MULTILINE)
def compress(source_name):
    f = open(source_name, 'r')
    content = f.read()
    f.close()
    # Strip comments and unnecessary whitespace.
    content = space_re.sub('\\1', comment_re.sub('', content))
    # Remove semi-colon from the last declaration.
    content = content.replace(';}', '}')
    print content

if __name__ == '__main__':
    if not len(sys.argv) == 2:
        sys.stderr.write('Usage: %s <path to css file>\n' % sys.argv[0])
        sys.exit(1)
    compress(sys.argv[1])
