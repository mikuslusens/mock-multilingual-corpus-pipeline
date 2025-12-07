@echo off
setlocal enabledelayedexpansion

for %%L in (lv en) do (
    if not exist extracted\%%L mkdir extracted\%%L
    if not exist cleaned\%%L mkdir cleaned\%%L
)

echo === Extracting LV ===
for %%f in (raw_html\lv\*.html) do (
    python extract_text.py "%%f" "extracted\lv\%%~nf.txt"
)

echo === Extracting EN ===
for %%f in (raw_html\en\*.html) do (
    python extract_text.py "%%f" "extracted\en\%%~nf.txt"
)

echo === Cleaning LV ===
for %%f in (extracted\lv\*.txt) do (
    python clean_text.py "%%f" "cleaned\lv\%%~nf.clean.txt"
)

echo === Cleaning EN ===
for %%f in (extracted\en\*.txt) do (
    python clean_text.py "%%f" "cleaned\en\%%~nf.clean.txt"
)

echo === Generating bilingual document pairs ===
python pairs_generator.py

echo === DONE ===
pause

