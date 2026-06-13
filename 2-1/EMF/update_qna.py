import re

with open("Plane wave qna.md", "r") as f:
    lines = f.readlines()

questions = []
for i, line in enumerate(lines):
    if line.startswith("### "):
        # Extract the core question by removing "### ", "Q.X ", "(a)", etc.
        core = re.sub(r'^###\s*(Q\.\d+\s*)?(\([a-ziv]+\)\s*)*', '', line).strip()
        if core and "up untill 2013" not in core:
            questions.append((i, core, line))

# Find duplicates
from collections import defaultdict
counts = defaultdict(list)
for i, core, line in questions:
    counts[core].append(i)

# Update lines
for core, indices in counts.items():
    if len(indices) > 1:
        for idx in indices:
            if "🔴" not in lines[idx]:
                lines[idx] = lines[idx].replace("### ", "### 🔴 ")

with open("Plane wave qna.md", "w") as f:
    f.writelines(lines)
print("Updated duplicated questions.")
