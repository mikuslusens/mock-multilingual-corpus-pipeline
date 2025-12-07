# clean_text.py
import sys
import re
import unicodedata

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Split into lines, clean each line, then re-join
lines = text.splitlines()
clean_lines = []

for line in lines:
    line = unicodedata.normalize("NFC", line)
    line = re.sub(r"\s+", " ", line).strip()
    if line:
        clean_lines.append(line)

text = "\n".join(clean_lines)

# Trim leading/trailing spaces
text = text.strip()

def remove_control_chars(s: str) -> str:
    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C" or ch in "\n\r\t")

text = remove_control_chars(text)

# Remove lines that are shorter than 5 words
text = "\n".join(
    line for line in text.splitlines()
    if len(line.split()) >= 5
)

def remove_boilerplate(text):
    patterns = [
        r"cookie(s)? (policy|preferences|settings).*",
        r"sīkdatņu (politika|uzstādījumi).*"
        r"©.*",
        r"all rights reserved.*",
        r"visas tiesības aizsargātas.*",
        r"terms of( use| service).*",
        r"lietošanas noteikumi.*",
        r"privacy policy.*",
        r"privātuma politika.*",
        r"contact us.*",
        r"sazinieties ar mums.*",
        r"izvēlne.*",
    ]

    cleaned_lines = []
    for line in text.splitlines():
        stripped = line.strip().lower()

        remove = False
        for p in patterns:
            if re.match(p, stripped):
                remove = True
                break

        if not remove:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)

text = remove_boilerplate(text)

# Save output
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Cleaned: {input_file} -> {output_file}")
