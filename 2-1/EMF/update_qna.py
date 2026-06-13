import re

file_path = "/data/data/com.termux/files/home/storage/shared/Obsidian/GitVlt/Obsidian_uni/2-1/EMF/Static Electric Field qna.md"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Patterns or keywords for groups of repeated questions
groups = [
    # Conservative property
    ["conservative property", "independent of the path"],
    # Gauss's Law
    ["Gauss's Law", "Gauss' law", r"\\nabla \\cdot \\bar{D} = \\rho_v", r"\\nabla \\cdot \\mathbf{D} = \\rho_v"],
    # Boundary Conditions
    ["boundary conditions"],
    # Coulomb's Law
    ["Coulomb's law", "Coulomb's force law"],
    # Electric Field Intensity Definition
    ["Define Electric Field and Electric Field intensity", "Define electric field intensity"],
    # Absolute Potential
    ["absolute potential"],
    # Electric Dipole
    ["electric dipole", "dipole moment"],
    # Effect on Conductor
    ["effect of electric field on conductor", "effect of static electric field on a conducting material"],
    # Energy Stored
    ["energy stored in an electric field", "energy stored in an electrostatic field"]
]

def is_repeated(line):
    if not line.startswith("### Q"):
        return False
        
    # Check if it matches any group
    # A line matches a group if it contains any of the keywords in the group
    # Wait, we need to be careful not to match problems that just happen to use the word.
    # Let's do exact substring matching based on my manual review.
    return False

# Manual line numbers identified (1-indexed)
repeated_lines = [
    58, 302, 1415, # Group 1
    72, 920, 1344, 1836, 1864, 2044, # Group 2
    163, 1939, 2336, # Group 3
    880, 1650, # Group 4
    1256, 1675, # Group 5
    1059, 1897, # Group 6
    1122, 1140, 1486, 1755, # Group 7
    1284, 1982, # Group 8
    1521, 2251 # Group 9
]

for i in repeated_lines:
    idx = i - 1
    if lines[idx].startswith("### Q"):
        lines[idx] = lines[idx].replace("### Q", "### 🔴 Q", 1)

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"Updated {len(repeated_lines)} questions.")
