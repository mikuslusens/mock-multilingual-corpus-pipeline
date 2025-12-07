# **Mock Multilingual Corpus Pipeline**

This project showcases the essential skills involved in building multilingual text corpora for NLP applications such as:

* machine translation
* chatbot training
* language model fine-tuning
* text analytics and preprocessing

It implements a miniature pipeline that:

1. Ingests HTML documents in Latvian and English
2. Extracts main text content using XPath
3. Cleans and normalizes text (Unicode normalization, whitespace cleanup, noise reduction)
4. Removes boilerplate (navigation items, copyright, cookie policy, etc.)
5. Organizes data into corpus structure
6. Produces a document-level parallel corpus (`pairs.jsonl`)

This repo demonstrates practical ability in Python, HTML parsing, text cleaning, regex, XPath, and automation - common requirements for data gathering roles in NLP and machine translation.

---

## **Project Structure**

```
mock-multilingual-corpus-pipeline/
│
├── raw_html/            # raw source HTML files
│   ├── lv/              # Latvian input documents
│   └── en/              # English input documents
│
├── extracted/           # text extracted from HTML
│   ├── lv/
│   └── en/
│
├── cleaned/             # cleaned, normalized text files
│   ├── lv/
│   └── en/
│
├── meta/                # optional metadata per document
│
├── extract_text.py      # HTML -> text extractor using XPath
├── clean_text.py        # text cleaning + boilerplate removal
├── pairs_generator.py   # builds bilingual document pairs file
├── run_pipeline.bat     # batch script to run full pipeline
└── pairs.jsonl          # final list of LV–EN document pairs
```

---

## **Pipeline Overview**

### 1. Raw Data Acquisition

HTML files have been manually downloaded into `raw_html/` for demonstration purposes. They can be replaced with any number of HTML files in the supported languages.

---

### 2. Text Extraction (`extract_text.py`)

Extracts readable content from HTML using:

* lxml for DOM parsing
* XPath to target likely article containers (`<article>`, `<main>`, etc.)
* fallback to full `<body>` if needed
* removal of `<script>` and `<style>` elements
* extraction of titles and metadata

---

### 3. Cleaning & Normalization (`clean_text.py`)

Applies several preprocessing steps:

* Unicode normalization (NFC)
* whitespace cleanup
* removal of short noisy lines
* regex-based boilerplate filtering
* removal of control characters
* paragraph alignment

---

### 4. Document-Level Pairing (`pairs_generator.py`)

Documents with matching IDs across languages are paired into a structured JSONL file:

```json
{"id": "{document_id}", "lv": "cleaned/lv/{document_id}.clean.txt", "en": "cleaned/en/{document_id}.clean.txt"}
```

---

### 5. Automation (`run_pipeline.bat`)

The batch script automates the full workflow:

1. Extract text for each language
2. Clean all extracted files
3. Generate bilingual document pairs

---

## **Output Example**

After running the pipeline, cleaned files appear in:

```
cleaned/lv/{document_id}.clean.txt
cleaned/en/{document_id}.clean.txt
```

And the bilingual pair is listed in `pairs.jsonl`:

```json
{"id": "{document_id}", "lv": "cleaned/lv/{document_id}.clean.txt", "en": "cleaned/en/{document_id}.clean.txt"}
```

---

## **How to Run**

1. Place your HTML files into `raw_html/lv/` and `raw_html/en/`.
2. Run:

```
run_pipeline.bat
```

3. Inspect results in `cleaned/` and `pairs.jsonl`.

---

## **Notes**

* This is a simplified demonstration project intended to show practical familiarity with corpus creation workflows.
* Real production pipelines involve larger scale, more varied formats (PDF, XML), site-specific extraction rules, and alignment models - but the principles demonstrated here are foundational to that work.
