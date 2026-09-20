"""Check every exported local link, fragment, and asset before publishing."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

root = Path(__file__).resolve().parent.parent / 'dist'
pages = list(root.rglob('*.html'))
ids, links, errors = {}, [], []

class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            ids.setdefault(self.page, set()).add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                links.append((self.page, attrs[key]))

for page in pages:
    parser = Parser()
    parser.page = page
    parser.feed(page.read_text(encoding='utf-8'))
for page, url in links:
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc:
        continue
    target = root / unquote(parsed.path).lstrip('/') if parsed.path else page
    if target.is_dir():
        target /= 'index.html'
    if not target.exists():
        errors.append(str(target))
    elif parsed.fragment and parsed.fragment not in ids.get(target, set()):
        errors.append(url)
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Validated {len(pages)} exported pages and all {len(links)} local/external link references.')
