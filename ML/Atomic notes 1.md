

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



### A. Sampling Theory & Frequency
Converting continuous real-world signals into discrete digital numbers.

*   **Sampling Rate/Frequency:** The number of measurements ("snapshots") taken per second. Measured in Hertz (Hz).
*   **Nyquist-Shannon Theorem (Golden Rule):** To perfectly capture a signal, you must sample at least **twice as fast** as the highest frequency present in the signal.
    *   *Formula:* $f_{sampling} \ge 2 \times f_{highest\_signal}$
*   **Aliasing:** The error that occurs when you sample too slowly (breaking the Nyquist rule). High frequencies "ghost" or masquerade as lower frequencies (like car wheels spinning backward on video).

---

### B. Signal Windowing & Epoching
Chopping long signals into usable pieces for mathematical analysis.

*   **Epoching (Slicing):** Cutting a continuous signal into specific, event-aligned time chunks (e.g., extracting exactly 2 seconds of brainwave data every time a light flashes).
*   **Spectral Leakage (The Problem):** Abruptly slicing a signal creates hard edges. When doing frequency analysis (FFT), the math interprets these sharp cuts as fake high-frequency noise.
*   **Windowing (The Fix):** Applying a mathematical curve to an epoch to smoothly fade the edges in and out to zero. 
    *   *Examples:* Hamming or Hanning windows. They eliminate the sharp edges and fix the spectral leakage.

---

### C. Channel Concatenation / Data Fusion
Handling and combining data from multiple sensors.

*   **Channel Concatenation:** Stitching data from multiple *identical* sensors (like 4 mics or 64 EEG electrodes) into a single mathematical matrix (Channels × Time). Allows algorithms to analyze spatial relationships.
*   **Data Fusion:** Combining data from *different types* of sensors (e.g., Video + Audio + Accelerometer).
    *   **Early Fusion (Data-level):** Resampling and syncing raw data to the exact same timeline, then combining them into one matrix.
    *   **Feature Fusion (Mid-level):** Processing signals separately to extract "features" (e.g., audio pitch, video brightness), then combining only those features.
    *   **Late Fusion (Decision-level):** Separate algorithms make their own predictions ("Audio says dog", "Video says dog"), and a master system combines the decisions.
*   **Biggest Challenge:** **Synchronization.** Data must be perfectly time-aligned for fusion to work.

### A. European Data Format (EDF) Architecture
The universal file standard for medical time-series data (EEG, ECG, Sleep Studies).

*   **Structure:** Divided into two strict sections: the Text Header and the Digital Data.
*   **The Header (Metadata - ASCII text):**
    *   *Global Header:* Patient info, start time, date, total number of data records.
    *   *Signal Header:* Setup info for *each individual channel* (sensor label, physical units like $\mu V$, digital/physical min & max values, and sampling rate).
*   **Data Records (The Signals):**
    *   Data is stored in **Interleaved** chunks (usually 1-second blocks).
    *   *Format:* `[1s of Ch1] [1s of Ch2]` $\rightarrow$ `[Next 1s of Ch1] [Next 1s of Ch2]`
    *   *Why?* Memory efficiency. Allows software to load specific time blocks without loading the massive 8-hour file into RAM.
*   **EDF+:** A 2003 upgrade that added a dedicated channel for time-stamped **Annotations** (text markers like "Sleep Stage N2" or "Apnea Event").

---

### B. R&K to AASM Sleep Staging Standards
The rules for categorizing human sleep. Sleep is scored in **30-second epochs** using brainwaves (EEG), eye movement (EOG), and muscle tone (EMG).

*   **R&K Standard (1968 – 2007):**
    *   Created for the ink-and-paper era.
    *   **6 Stages:** Wake, Stage 1, Stage 2, **Stage 3** (deep sleep), **Stage 4** (very deep sleep), REM.
*   **AASM Standard (2007 – Present):**
    *   The modern digital standard.
    *   **5 Stages:** W (Wake), N1, N2, **N3 (Slow Wave/Deep Sleep)**, R (REM).
    *   Includes strict, modern rules for scoring sleep apnea and micro-arousals.
*   **Key Data Science Takeaway (The Transition):**
    *   The AASM merged R&K Stages 3 and 4 because the clinical difference was negligible. 
    *   *Crucial:* If you are training machine learning models on older R&K datasets, you must programmatically **combine labels 3 and 4 into a single N3 label** to match modern standards.
Here are your concise, high-yield cheat-sheet notes for all the topics covered.

---

### 1. Z-Score Normalization (Standardization)
*   **What it is:** Scales data so the **Mean ($\mu$) = 0** and **Standard Deviation ($\sigma$) = 1**. 
*   **Why we need it:** Prevents features with large raw numbers (e.g., Salary) from overpowering features with small numbers (e.g., Age).
*   **Formula:** $z = \frac{x - \mu}{\sigma}$ (Translates raw data into "how many standard deviations it is from the average").
*   **When to use:** Distance-based models (KNN, SVM), Gradient Descent models (Neural Networks, Linear/Logistic Regression), and PCA.
*   **When NOT to use:** Tree-based models (Decision Trees, Random Forest, XGBoost) don't need scaled data.
*   **⚠️ The Golden Rule:** Always `fit` (calculate mean/std) on the **Training Data ONLY** to prevent data leakage. Then `transform` both Train and Test data.

### 2. Variance & Standard Deviation
*   **What they are:** Mathematical measures of how "spread out" or unpredictable your data is.
*   **Variance ($\sigma^2$):** The average *squared* distance of each point from the mean. Mathematically useful, but confusing for humans because the units are squared (e.g., "squared dollars").
*   **Standard Deviation ($\sigma$):** The square root of variance. Returns the spread back to normal units. Tells you the "typical" deviation from the average.
*   **The Empirical Rule (68-95-99.7 Rule):** In a normal (bell-curve) distribution:
    *   ~68% of data falls within $\pm 1\sigma$
    *   ~95% of data falls within $\pm 2\sigma$
    *   ~99.7% of data falls within $\pm 3\sigma$ (Anything beyond 3 is an extreme outlier).

### 3. Numerical Stability Constants (Epsilon $\epsilon$)
*   **What it is:** A purposefully microscopic number (e.g., $10^{-7}$ or $0.0000001$).
*   **Why we need it:** Computers will crash (`NaN` or `Inf` errors) if they try to divide by zero or take the logarithm of zero. 
*   **How it's used:** We add $\epsilon$ to denominators or logs to ensure they never hit exactly zero, saving the program without altering the actual math results.
*   **Examples:** $z = \frac{x - \mu}{\sigma + \epsilon}$ (Standardization) or $loss = \log(probability + \epsilon)$ (Neural Net Loss).

### 4. Tensor Reshaping & Dimensionality Expansion
*   **Tensors:** Simply containers for numbers (1D = Vector, 2D = Matrix, 3D = Stacked Matrices like images).
*   **Reshaping:** Rearranging the structure of a Tensor. 
    *   *Rule:* The total number of items must remain identical (e.g., `(4, 3)` = 12 items. Can reshape to `(2, 6)` or `(12,)`).
    *   *The `-1` Trick:* If you use `-1` as a dimension in Python, the computer will automatically calculate that dimension for you (e.g., `.reshape(2, -1)`).
*   **Dimensionality Expansion:** Adding an empty "dummy" dimension without adding new data (e.g., turning shape `(5,)` into `(5, 1)`).
*   **Why expand?:** ML frameworks are highly rigid. 
    *   Scikit-Learn strictly requires 2D arrays: `(samples, features)`.
    *   Neural Networks strictly require batch dimensions for images: `(batch_size, channels, height, width)`. Expanding allows a single item to pass through the model.