import os
import json

LV_DIR = "cleaned/lv"
EN_DIR = "cleaned/en"

output_file = "pairs.jsonl"

# Collect filenames without extensions
lv_files = {os.path.splitext(f)[0]: f for f in os.listdir(LV_DIR) if f.endswith(".txt")}
en_files = {os.path.splitext(f)[0]: f for f in os.listdir(EN_DIR) if f.endswith(".txt")}

pairs = []

for doc_id in lv_files:
    # Normalize doc_id: remove ".clean" suffix if present
    normalized_id = doc_id.replace(".clean", "")

    # EN file must match either the raw id or the clean variant
    for candidate in (normalized_id, normalized_id + ".clean"):
        if candidate in en_files:
            lv_path = os.path.join(LV_DIR, lv_files[doc_id]).replace("\\", "/")
            en_path = os.path.join(EN_DIR, en_files[candidate]).replace("\\", "/")

            pairs.append({
                "id": normalized_id,
                "lv": lv_path,
                "en": en_path
            })
            break

with open(output_file, "w", encoding="utf-8") as out:
    for pair in pairs:
        out.write(json.dumps(pair, ensure_ascii=False) + "\n")

print(f"Generated {len(pairs)} document pairs into {output_file}")
