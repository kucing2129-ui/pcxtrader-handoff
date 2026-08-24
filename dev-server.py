#!/usr/bin/env python3
"""Static dev server for site/ that never lets the browser cache.

python -m http.server sends Last-Modified but no Cache-Control, so browsers
cache assets heuristically and happily serve a stale .webp long after the file
on disk has changed. That has repeatedly made a finished change look like it
never happened. This server sends no-store on everything instead.

    python3 dev-server.py [port] [--directory DIR]
"""
import argparse
import functools
import http.server
import os
import socketserver


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, fmt, *args):  # quieter: only non-200s
        if args and str(args[1]).startswith(('4', '5')):
            super().log_message(fmt, *args)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser()
    ap.add_argument('port', nargs='?', type=int, default=8734)
    ap.add_argument('--directory', default=os.path.join(here, 'site'))
    a = ap.parse_args()

    handler = functools.partial(NoCacheHandler, directory=a.directory)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(('', a.port), handler) as httpd:
        print('serving %s on http://localhost:%d (no-store)' % (a.directory, a.port))
        httpd.serve_forever()


if __name__ == '__main__':
    main()
