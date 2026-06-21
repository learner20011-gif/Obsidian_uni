

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



### 1. Unpacking (Extracting Values)
*   **Basic:** Variables on the left must match items on the right.
    ```python
    x, y, z = [1, 2, 3]
    ```
*   **Swapping:** No temporary variable needed.
    ```python
    a, b = b, a
    ```
*   **Throwaway Variable (`_`):** Used for values you don't need.
    ```python
    x, _, z = (10, 20, 30) # 20 is ignored
    ```
*   **Extended (`*` catch-all):** Gathers remaining items into a list.
    ```python
    first, *middle, last = [1, 2, 3, 4, 5] 
    # first=1, middle=[2, 3, 4], last=5
    ```
*   **Nested:** Mirror the structure to unpack inside iterables.
    ```python
    name, (x, y) = ("Alice", [10, 20])
    ```
*   **Merging:** Combine iterables easily.
    ```python
    merged_list = [*list1, *list2]
    merged_dict = {**dict1, **dict2}
    ```
*   **Function Arguments:** `*` unpacks lists into args, `**` unpacks dicts into kwargs.
    ```python
    func(*[arg1, arg2])
    func(**{"kwarg1": val1, "kwarg2": val2})
    ```

---

### 2. Built-in Manipulation Functions
*(Note: These return memory-efficient iterators, not lists. Wrap in `list()` if you need a physical list).*

*   **`enumerate(iterable, start=0)`:** Yields `(index, value)`.
    ```python
    for i, val in enumerate(["a", "b"]): # 0: "a", 1: "b"
    ```
*   **`zip(*iterables)`:** Pairs items up. Stops at the **shortest** iterable.
    ```python
    for a, b in zip([1, 2], ["x", "y"]): # (1, "x"), (2, "y")
    ```
*   **Unzipping:** Use `zip` combined with `*`.
    ```python
    nums, letters = zip(*[(1, 'a'), (2, 'b')])
    ```
*   **`sorted(iterable, key=None)`:** Returns a **new** sorted list.
*   **`reversed(iterable)`:** Iterates backwards.
*   **`map(func, iterable)`:** Applies a function to all items.
*   **`filter(func, iterable)`:** Keeps items where `func` returns True.
    *   *Pro-tip: List comprehensions (`[x**2 for x in nums if x > 0]`) are often preferred over map/filter.*

---

### 3. `itertools` Module (Advanced)
`import itertools`

*   **`chain(*iterables)`:** Links multiple iterables together end-to-end without creating a new list.
    ```python
    list(itertools.chain([1, 2], [3, 4])) # [1, 2, 3, 4]
    ```
*   **`zip_longest(*iterables, fillvalue=None)`:** Like `zip()`, but stops at the **longest** iterable.
    ```python
    list(itertools.zip_longest([1, 2, 3], ['a'], fillvalue='x')) 
    # [(1, 'a'), (2, 'x'), (3, 'x')]
    ```
*   **`permutations(iterable, r)`:** All possible orderings (Order matters: AB ≠ BA).
*   **`combinations(iterable, r)`:** All unique groups (Order doesn't matter: AB = BA).