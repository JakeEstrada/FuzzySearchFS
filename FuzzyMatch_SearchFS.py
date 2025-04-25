import os
import json
import subprocess
from fuzzywuzzy import process

# Load base paths from JSON
with open("paths.json", "r") as f:
    config = json.load(f)

base_paths = config.get("base_paths", [])
if not base_paths:
    print("No paths found in paths.json.")
    exit()

# Prompt user
name_input = input("Search for customer folder name: ").lower()

# Collect all folder names with full paths
all_folders = []
for base in base_paths:
    try:
        for entry in os.listdir(base):
            full_path = os.path.join(base, entry)
            if os.path.isdir(full_path):
                all_folders.append((entry, full_path))
    except FileNotFoundError:
        continue

# Extract folder names for matching
folder_names = [name for name, _ in all_folders]

# Fuzzy match
match, score = process.extractOne(name_input, folder_names)

if score < 50:
    print(f"'{name_input}' not found (best match score: {score}).")
    exit()

match_path = next(path for name, path in all_folders if name == match)

print(f"\nFound match: {match} (score: {score})\nLocation: {match_path}")

# List folder contents
print("\nContents:")
for item in os.listdir(match_path):
    print(" -", item)

# Prompt to open
choice = input("\nOpen in Windows Explorer? (Y/n): ").strip().lower()
if choice != "n":
    subprocess.run(["wslview", match_path])
