Here are concise notes summarizing everything we covered about Python file system and path operations.

## **Python File System & Path Operations**

### **1. `pathlib` (The Modern Standard)**

Object-oriented and handles cross-platform differences (Windows vs. Mac/Linux) automatically. This is the recommended approach for new code.

- **Import:** `from pathlib import Path`
    
- **Get Current Directory:** `Path.cwd()`
    
- **Join Paths:** Use the forward slash `/` (e.g., `Path.cwd() / "folder" / "file.txt"`)
    
- **Check Existence:** `path_obj.exists()`, `path_obj.is_file()`, `path_obj.is_dir()`
    
- **Create Directory:** `path_obj.mkdir(parents=True, exist_ok=True)` _(Creates parent folders if missing; prevents errors if it already exists)_
    
- **List Items:** `path_obj.iterdir()`
    
- **Search for Files:** `path_obj.glob("*.txt")`
    
- **Quick Read/Write:** `path_obj.read_text()`, `path_obj.write_text("data")`
    

### **2. `os` & `os.path` (The Traditional Approach)**

Older, string-based approach. Very common in legacy codebases.

- **Import:** `import os`
    
- **Get Current Directory:** `os.getcwd()`
    
- **Join Paths:** `os.path.join("folder", "file.txt")` _(Required to handle slashes correctly across operating systems)_
    
- **Check Existence:** `os.path.exists(path_string)`
    
- **Create Directory:** `os.makedirs("new_folder", exist_ok=True)`
    
- **List Items:** `os.listdir(path_string)`
    

### **3. Searching and Sorting (`glob`)**

Used to find lists of files that match a specific pattern (like finding all `.csv` or `.txt` files).

- **Module vs. Function:** * `import glob` requires writing `glob.glob('*.txt')` (calling the function inside the module).
    
    - `from glob import glob` allows writing `glob('*.txt')`.
        
- **The Sorting Rule:** `glob` does **not** return files in alphabetical order. You must wrap it in Python's built-in `sorted()` function to process files chronologically/alphabetically.
    
- **Standard Syntax Example:** `ordered_files = sorted(glob.glob(os.path.join(folder, '*.txt')))`