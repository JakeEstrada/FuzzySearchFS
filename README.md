# FuzzySearchFS

**FuzzySearchFS** is a Python tool for quickly finding folders in a huge directory tree using fuzzy search.

## Features

- Fuzzy matching using `fuzzywuzzy`
- Uses paths that you specify in the json folder
- Displays folder contents on match
- Optional: Open folder in Windows Explorer via WSL (`wslview`)

## Requirements

- Python 3.x
- [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy)
- (Recommended) `python-Levenshtein` for better performance
- WSL (for opening folders with `wslview`)

Install dependencies:

```bash
pip install fuzzywuzzy python-Levenshtein
```

## How to specify paths to search

{
  "base_paths": [
    "/mnt/c/Users/YourName/Some/Directory1",
    "/mnt/c/Users/YourName/Some/Directory2"
  ]
}
