import os
import re

DOCS_DIR = "docs"
OUTPUT_FILE = os.path.abspath("index.html")

# YYYYMMDD(8桁連続数字）パターン)
date_pattern = re.compile(r"\d{8}")

files = []

for root, _, filenames in os.walk(DOCS_DIR):
    for name in filenames:

        # YYYYMMDDを含むファイルを除外
        if date_pattern.search(name):
            continue

        path = os.path.join(root, name)
        rel = os.path.relpath(path, ".")
        files.append(rel)

files.sort()

# テンプレート
html_top = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>ファイルダウンロード</title>
    <style>
        .btn {
            display: inline-block;
            padding: 8px 14px;
            background: #0366d6;
            color: white;
            text-decoration: none;
            border-radius: 8px;
        }
        .btn:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

<h1>ファイルダウンロード</h1>

<div>
<a href="https://hanihatena35-prog.github.io/portal-site/" class="btn" target="_blank">ポータルに戻る</a>
</div>

<ul>
"""

html_bottom = """

</body>
</html>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_top)

    for file in files:
        f.write(f'<li><a href="{file}">{file}</a></li>\n')
    f.write(html_bottom)

print("index.html generated at root")
print("OUTPUT:", os.path.abspath(OUTPUT_FILE))
