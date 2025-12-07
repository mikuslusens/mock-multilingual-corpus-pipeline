# extract_text.py
import sys
from lxml import html

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
    data = f.read()

doc = html.fromstring(data)

# Remove unneeded elements
nodes_to_remove = doc.xpath("//script | //style")

for node in nodes_to_remove:
    node.getparent().remove(node)

# 1. Extract Title
title = ""

# Try common <title> tag
t = doc.xpath("//title/text()")
if t:
    title = t[0].strip()

# Try <h1>
if not title:
    h1 = doc.xpath("//h1//text()")
    if h1:
        title = " ".join([x.strip() for x in h1 if x.strip()])

# 2. Extract Main Content
# Try common article containers used on many sites
XPATH_CANDIDATES = [
    "//article//p",
    "//div[@id='content']//p",
    "//div[@id='main-content']//p",
    "//div[contains(@class,'article')]//p",
    "//div[contains(@class,'post')]//p",
    "//main//p",
]

body_text = ""

for xp in XPATH_CANDIDATES:
    nodes = doc.xpath(xp)
    if nodes:
        # Extract text
        body_text = "\n".join(node.text_content() for node in nodes)
        break

# If no match found -> fallback to entire body
if not body_text:
    body_nodes = doc.xpath("//body//p")
    if body_nodes:
        body_text = "\n".join(node.text_content() for node in body_nodes)

# 4. Save Output
with open(output_file, "w", encoding="utf-8") as f:
    if title:
        f.write(title + "\n\n")
    f.write(body_text)

print(f"Extracted: {input_file} -> {output_file}")
