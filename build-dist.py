#!/usr/bin/env python3
"""Build site/ into a deployable dist/ with clean URLs.

Run:  python3 build-dist.py
Then: drag dist/ onto netlify.com/drop

Only the thirteen live pages ship. _shell.html is the shared navbar and
footer and is deliberately not a page. The DEV-ONLY preview hooks are
stripped on the way out.
"""
import os, re, shutil, sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist')

# source file -> url path ('' means site root)
PAGES = {
    'index.html':                      '',
    'accounts.html':                   'accounts',
    'accounts-ecn.html':               'accounts/ecn',
    'accounts-demo.html':              'accounts/demo',
    'accounts-precious-metals.html':   'accounts/precious-metals',
    'accounts-standard.html':          'accounts/standard',
    'why-a-book.html':                 'why-a-book',
    'legal-terms.html':                'legal/terms',
    'legal-risk-disclosure.html':      'legal/risk-disclosure',
    'legal-privacy.html':              'legal/privacy',
    'legal-cookies.html':              'legal/cookies',
    'legal-client-agreement.html':     'legal/client-agreement',
    'legal-pamm.html':                 'legal/pamm',
}
LINK = {src: ('/' + path if path else '/') for src, path in PAGES.items()}


def clean(html):
    # the preview hook must never reach a public URL
    html = re.sub(
        r'\n?<script>\s*/\* DEV-ONLY.*?</script>', '', html, flags=re.S)
    # pages now live in subfolders, so relative asset paths would break
    html = re.sub(r'(href|src|data)="assets/', r'\1="/assets/', html)
    html = html.replace('href="./assets/', 'href="/assets/')
    # same for the legal PDFs, which sit in docs/
    html = re.sub(r'(href|src|data)="docs/', r'\1="/docs/', html)
    html = html.replace('href="./docs/', 'href="/docs/')
    # point every internal link at its clean URL
    for src, url in LINK.items():
        html = html.replace('href="%s"' % src, 'href="%s"' % url)
        html = html.replace('href="%s#' % src, 'href="%s#' % url)
    return html


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    written = []
    for src, path in PAGES.items():
        s = open(os.path.join(SRC, src), encoding='utf-8', errors='replace').read()
        s = clean(s)
        target_dir = os.path.join(OUT, path) if path else OUT
        os.makedirs(target_dir, exist_ok=True)
        target = os.path.join(target_dir, 'index.html')
        open(target, 'w', encoding='utf-8').write(s)
        written.append((('/' + path if path else '/'), len(s) / 1024))

    # ship only the assets the live pages actually reference
    used = set()
    for src in PAGES:
        s = open(os.path.join(SRC, src), encoding='utf-8', errors='replace').read()
        used |= set(re.findall(r'assets/([A-Za-z0-9_.\-]+)', s))
    os.makedirs(os.path.join(OUT, 'assets'), exist_ok=True)
    total = 0
    for name in sorted(used):
        s = os.path.join(SRC, 'assets', name)
        if os.path.exists(s):
            shutil.copy2(s, os.path.join(OUT, 'assets', name))
            total += os.path.getsize(s)
        else:
            print('  ! missing asset:', name)

    # the signed PDFs the legal pages embed
    docs_src = os.path.join(SRC, 'docs')
    if os.path.isdir(docs_src):
        shutil.copytree(docs_src, os.path.join(OUT, 'docs'))
        print('docs: %d PDF(s)' % len(os.listdir(docs_src)))

    # netlify: keep trailing-slash URLs tidy and serve the old names too
    open(os.path.join(OUT, '_redirects'), 'w').write(
        '\n'.join('/%s  %s  301' % (src, url) for src, url in LINK.items()) + '\n')

    print('pages:')
    for url, kb in written:
        print('  %-26s %6.0f KB' % (url, kb))
    print('assets: %d files, %.1f MB' % (len(used), total / 1024 / 1024))
    print('output: %s' % OUT)


if __name__ == '__main__':
    main()
