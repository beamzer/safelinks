#!/usr/bin/env python2
#
# 20191221 Ewald
# descramble Microsoft ATP Safe Links

import posixpath as path
import sys
import fileinput
import StringIO
from urlparse import urlparse, parse_qs, urlunparse

buf = StringIO.StringIO()
buf.write("\n")

if len(sys.argv) < 2:
    for url in fileinput.input():
        url.rstrip()
        buf.truncate(0)
        if url.lower().startswith("http"):
            target = parse_qs(urlparse(url).query)['url'][0]
#            print(target)
            p = urlparse(target)
#            print(p)
#            q = p._replace(path=path.join(path.dirname(path.dirname(p.path)), path.basename(p.path)))
#            print(q)
#            z = urlunparse(q)
            z = urlunparse(p)
#           buf.write("%s\n" % z)
            buf.write("%s" % z)
            print(buf.getvalue())

if len(sys.argv) > 2:
    print("Please only one Safe Link at a time, or switch to STDIN mode")
    sys.exit()

if len(sys.argv) == 2:
    url=sys.argv[1]
    if url.lower().startswith("http"):
        target = parse_qs(urlparse(url).query)['url'][0]
        p = urlparse(target)
        q = p._replace(path=path.join(path.dirname(path.dirname(p.path)), path.basename(p.path)))
        print urlunparse(q)
    else:
        print("descramble Microsoft ATP Safe Links")
        print("Usage:")
        print("./safelinks.py https://safelink-url")
        print("- or parse from file:")
        print("cat file-with-safelinks | ./safelinks.py")
        print("- or paste from commandline and end with ctrl-d")
        print("cat | ./safelinks.py")
