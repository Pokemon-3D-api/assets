import os
import sys

BASE_PATH = "models/opt"

CATEGORY_MAP = {
    "regular":   ("Regular Forms",        1028, "Standard Pokémon forms from Generations 1 to 9 including male & female."),
    "shiny":     ("Shiny Forms",           1028, "Alternate color variants of all standard Pokémon."),
    "gmax":      ("Gigantamax",              32, "Special forms of select Pokémon with unique appearances in _Sword and Shield_."),
    "mega":      ("Mega Evolutions",         49, "Includes both single Mega forms and X/Y variants."),
    "megaShiny": ("MegaShiny Evolutions",    49, "Includes both single Mega forms and X/Y variants."),
    "hisuian":   ("Hisuian Forms",           17, "Regional variants from _Pokémon Legends: Arceus_."),
    "alolan":    ("Alolan Forms",            18, "Regional variants introduced in _Pokémon Sun and Moon_."),
    "shinyAlolan": ("Shiny Alolan Forms",    16, "Alternate color variants of the regional forms of Pokémon originally discovered in the Alola region"),
    "galar":     ("Galarian Forms",          20, "Regional variants from _Pokémon Sword and Shield_."),
    "primal":    ("Primal Forms",             2, "Primal Groudon and Primal Kyogre."),
    "unique":    ("Unique Forms",             4, "Ash's Greninja, Armoured Mewtwo, Eternamax Eternatus, Ultra Necrozma"),
    "shadow":    ("Shadow Forms",           131, "Dark, corrupted versions of Pokémon often seen in Pokémon Colosseum and XD: Gale of Darkness."),
    "fusion":    ("Fusion Forms",             6, "Kyurem (black/white), Necrozma (Dusk Mane/Dawn Wings), Calyrex (Ice Rider/Shadow Rider)"),
    "origin":    ("Origin Forms",             3, "Origin Forms represent the true or primal state of certain legendary Pokémon, showcasing their full power and unique design. i.e Giratina, and Dialga/Palkia."),
}

MULTI_FOLDERS    = ["multiform", "multiShinyForm", "multi"]
SPECIAL_FOLDERS  = ["za", "sza", "sx", "sy", "x", "y"]


def count_files(folder: str) -> int:
    """Count unique Pokémon models in a given subfolder of BASE_PATH."""
    path = os.path.join(BASE_PATH, folder)
    if not os.path.exists(path):
        return 0
    files = [f for f in os.listdir(path) if f.endswith(".glb")]
    unique: set[str] = set()
    for f in files:
        name = f[:-4]  # strip .glb
        base = name.split("-")[0]
        unique.add(base if base.isdigit() else name)
    return len(unique)


def count_multiple_folders(folders: list[str]) -> int:
    return sum(count_files(f) for f in folders)


def build_table() -> str:
    header = (
        "| **Category** | **Available** | **Total** | **Description** |\n"
        "| ------------------------ | ------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |"
    )
    rows = []
    for folder, (label, total, desc) in CATEGORY_MAP.items():
        available = count_files(folder)
        rows.append(f"| **{label}** | {available} | {total} | {desc} |")

    multi_total = count_multiple_folders(MULTI_FOLDERS)
    rows.append(
        f"| **Multi Forms** | {multi_total} | 200 | "
        "Non-standard, non-shiny forms of a single Pokémon "
        "(e.g., Unown B-Z, Deoxys Attack/Defense/Speed, all Rotom/Alcremie forms, Zygarde 10%/Complete). |"
    )

    special_total = count_multiple_folders(SPECIAL_FOLDERS)
    if special_total > 0:
        rows.append(
            f"| **Special Variants** | {special_total} | — | "
            "ZA, X/Y, SZA, and other experimental variants. |"
        )

    return header + "\n" + "\n".join(rows)


def update_readme() -> bool:
    """
    Re-writes the stats table in README.md between the sentinel comments.
    Returns True if the file was actually changed, False if it was already up to date.
    """
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("❌ README.md not found!")
        sys.exit(1)

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!-- STATS_TABLE_START -->"
    end_marker   = "<!-- STATS_TABLE_END -->"

    if start_marker not in content or end_marker not in content:
        print(f"❌ Markers not found. Ensure README has {start_marker} and {end_marker}")
        sys.exit(1)

    start_index = content.index(start_marker) + len(start_marker)
    end_index   = content.index(end_marker)

    new_table   = build_table()
    new_content = (
        content[:start_index]
        + "\n\n" + new_table + "\n\n"
        + content[end_index:]
    )

    if new_content == content:
        print("✅ Stats unchanged — README not modified.")
        return False

    with open(readme_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_content)

    print("✅ README stats updated successfully.")
    return True


if __name__ == "__main__":
    changed = update_readme()
    sys.exit(0 if changed else 2)