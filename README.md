# Pokémon 3D API — Assets

This repository serves as the high-performance asset engine for the Pokémon 3D API. It features an automated Stateless Asset Pipeline that downloads, optimizes, and serves 3D Pokémon models with zero manual intervention.

## 🚀 The Automated Pipeline

You don't need to optimize models manually. When you add an entry to the data source, the GitHub Action:

1. **Downloads** the raw `.glb` from Sketchfab.
2. **Optimizes** geometry using **Draco** compression.
3. **Resizes** textures to 1024x1024.
4. **Compresses** textures into **WebP** for lightning-fast web loading.
5. **Prunes** repository history every 5 commits to keep the repo size tiny.

## 🛠️ How to Contribute

To add new models, you only need to modify `scripts/model_map.json`.
**Step-by-Step:**

1. **Fork** and **clone** the repository.

   ```bash
   git clone --filter=blob:none --sparse https://github.com/Pokemon-3D-api/assets.git
   ```

   ```bash
   cd assets
   ```

   ```bash
   git sparse-checkout set scripts .github
   ```

2. Open `scripts/model_map.json`.
3. Add your new Pokémon object (see the format below).
4. **Commit and Push**. The GitHub Action will handle the rest.

## 📄 JSON Data Structure

The pipeline uses a specific JSON format to determine how to save and process your files. You only need to provide one entry per model.
Format Breakdown:

- `id`: (Required) The National Dex number.
- `category`: (Required) The folder where the optimized file will live (e.g., `regular`, `shiny`, `alolan`).
- `url`: (Required) The direct Sketchfab model URL.
- `suffix`: (Optional) Use this for Gender differences (e.g., `-M`, `-F`). Results in `668-M.glb`.
- `custom_name`: (Optional) Overwrites everything. Use this for forms or special names. Results in `rotom-wash.glb`.

## Example `model_map.json` entry:

```json
[
  {
    "id": 1000,
    "category": "regular",
    "url": "https://sketchfab.com/3d-models/gholdengo-450f19056379446cb57716b726c39929"
  },
  {
    "id": 668,
    "category": "regular",
    "suffix": "-M",
    "url": "https://sketchfab.com/3d-models/pyroar-male-64d85834863c45668612187b545f49ce"
  },
  {
    "id": 668,
    "category": "regular",
    "suffix": "-F",
    "url": "https://sketchfab.com/3d-models/pyroar-female-54d85834863c45668612187b545f49cf"
  },
  {
    "id": 479,
    "category": "multi",
    "custom_name": "rotom-wash",
    "url": "https://sketchfab.com/3d-models/rotom-wash-56d85834863c45668612187b545f49ca"
  },
  {
    "id": 25,
    "category": "special",
    "custom_name": "pikachu-ash-hat",
    "url": "https://sketchfab.com/3d-models/pikachu-hat-86d85834863c45668612187b545f49cb"
  }
]
```

> Note: If you use `custom_name`, the `id` and `suffix` are ignored for the filename, but the `id` is still used by the internal script to track the Pokémon.

## Pokémon Categories and Counts

This app supports various Pokémon forms and categories. Below is a breakdown of the available Pokémon models and their counts:

<!-- STATS_TABLE_START -->

| **Category** | **Available** | **Total** | **Description** |
| ------------------------ | ------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Regular Forms** | 971 | 1028 | Standard Pokémon forms from Generations 1 to 9 including male & female. |
| **Shiny Forms** | 150 | 1028 | Alternate color variants of all standard Pokémon. |
| **Gigantamax** | 10 | 32 | Special forms of select Pokémon with unique appearances in _Sword and Shield_. |
| **Mega Evolutions** | 56 | 49 | Includes both single Mega forms and X/Y variants. |
| **MegaShiny Evolutions** | 15 | 49 | Includes both single Mega forms and X/Y variants. |
| **Hisuian Forms** | 17 | 17 | Regional variants from _Pokémon Legends: Arceus_. |
| **Alolan Forms** | 12 | 18 | Regional variants introduced in _Pokémon Sun and Moon_. |
| **Shiny Alolan Forms** | 0 | 16 | Alternate color variants of the regional forms of Pokémon originally discovered in the Alola region |
| **Galarian Forms** | 11 | 20 | Regional variants from _Pokémon Sword and Shield_. |
| **Primal Forms** | 2 | 2 | Primal Groudon and Primal Kyogre. |
| **Unique Forms** | 4 | 4 | Ash's Greninja, Armoured Mewtwo, Eternamax Eternatus, Ultra Necrozma |
| **Shadow Forms** | 3 | 131 | Dark, corrupted versions of Pokémon often seen in Pokémon Colosseum and XD: Gale of Darkness. |
| **Fusion Forms** | 6 | 6 | Kyurem (black/white), Necrozma (Dusk Mane/Dawn Wings), Calyrex (Ice Rider/Shadow Rider) |
| **Origin Forms** | 3 | 3 | Origin Forms represent the true or primal state of certain legendary Pokémon, showcasing their full power and unique design. i.e Giratina, and Dialga/Palkia. |
| **Multi Forms** | 32 | 200 | Non-standard, non-shiny forms of a single Pokémon (e.g., Unown B-Z, Deoxys Attack/Defense/Speed, all Rotom/Alcremie forms, Zygarde 10%/Complete). |
| **Special Variants** | 17 | — | ZA, X/Y, SZA, and other experimental variants. |

<!-- STATS_TABLE_END -->

## 🔍 Previewing Models

To check if a model has animations before adding it to the JSON:

1. Use the **[3D Preview](https://marketplace.visualstudio.com/items?itemName=mohitkumartoshniwal.3d-preview)** extension in VS Code.
2. If animations exist, they will appear in the "Animations" dropdown within the viewer.

## ⚖️ License & Credits

- **Models**: All 3D assets are property of **Nintendo/Creatures Inc./GAME FREAK inc**.
- **Optimization**: Powered by `gltf-transform`.
- **Architecture**: Built with ❤️ by the [**Pokémon 3D API Organization**](https://github.com/Pokemon-3D-api).
