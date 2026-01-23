# Pokémon 3D API — Assets
## Contributing

We welcome contributions from the community! You can help by:

1. **Adding new 3D models** of Pokémon.
2. **Improving the user interface** and styling.
3. **Fixing bugs** and optimizing the app for better performance.
4. **Enhancing the code** with new features (like sorting Pokémon, filtering by type, etc.).
5. **Improving the documentation** for easier understanding and navigation.

### Steps to Contribute:
1. **Fork the Repository**: Fork the repo to your GitHub account.
2. **Clone your Fork**: Clone your fork to your local machine.
    ```bash
    git clone https://github.com/Pokemon3D-API/assets.git
    ```
3. **Create a Branch**: Create a new branch for your feature or bug fix.
    ```bash
    git checkout -b add-new-pokemon-model
    ```
4. **Make Your Changes**: Add new Pokémon models in the models and within the folder according to pokemon form and implement any necessary changes.
5. **Commit Your Changes**: Commit your changes with a meaningful message.
    ```bash
    git commit -m "Added new Pokémon model named 'Pikachu'"
    ```
6. **Push to Your Fork**: Push your changes to your fork on GitHub.
    ```bash
    git push origin add-new-pokemon-model
    ```
7. **Create a Pull Request**: Create a pull request to the main repository, describing your changes.


## How to Add More Models

To add new Pokémon models to the app, follow these steps:

1.  **Find or Create a 3D Model:** Locate or create Pokémon 3D models in `.glb` format.
2.  **Update the Data Source:** Add a new Pokémon object to your data source (e.g., `MergedOpt.json`) or database, following the JSON Response Structure outlined above.
3.  **Host the Model:** Ensure the model is hosted and accessible via a URL.


## Optimizing 3D Models

To ensure optimal performance, particularly for web-based applications, it's crucial to optimize 3D models. This involves reducing file sizes and improving rendering efficiency.

**Recommended Optimization Settings:**

For the best balance of visual quality and performance, we recommend optimizing your `.glb` models with the following settings:

* **Resolution:** Resize models to a maximum size of 1024x1024 pixels. This resolution provides good detail while keeping file sizes manageable.
* **Geometry Compression:** Use Draco compression to reduce the size of the model's geometry without significantly impacting visual quality.
* **Texture Compression:** Convert textures to WebP format, which offers excellent compression ratios and supports transparency.

For more detailed information on using gltf-transform, refer to the official documentation: [gltf-transform](https://gltf-transform.dev/cli).

### CLI Command for Optimization

1.  Install `gltf-transform` globally:

    ```bash
    npm i -g @gltf-transform/cli
    ```

2.  Install `gltf-transform` as a dev dependency (optional):

    ```bash
    npm i @gltf-transform/cli --save-dev
    ```

3.  Use the following `gltf-transform` command to resize and optimize your `.glb` models:

    ```bash
    gltf-transform resize models/glb/regular/1.glb models/opt/regular/1.glb --width 1024 --height 1024 && gltf-transform optimize models/opt/regular/1.glb models/opt/regular/1.glb --compress draco --texture-compress webp
    ```

## Pokémon Categories and Counts
This app supports various Pokémon forms and categories. Below is a breakdown of the available Pokémon models and their counts:

| **Category**             | **Available** | **Total** | **Description**                                                                                                                                                |
| ------------------------ | ------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Regular Forms**        | 965           | 1028      | Standard Pokémon forms from Generations 1 to 9 including male & female.                                                                                        |
| **Shiny Forms**          | 141           | 1028      | Alternate color variants of all standard Pokémon.                                                                                                              |
| **Gigantamax**           | 10            | 32        | Special forms of select Pokémon with unique appearances in *Sword and Shield*.                                                                                 |
| **Mega Evolutions**      | 49            | 49        | Includes both single Mega forms and X/Y variants.                                                                                                              |
| **MegaShiny Evolutions** | 7             | 49        | Includes both single Mega forms and X/Y variants.                                                                                                              |
| **Hisuian Forms**        | 17            | 17        | Regional variants from *Pokémon Legends: Arceus*.                                                                                                              |
| **Alolan Forms**         | 12            | 18        | Regional variants introduced in *Pokémon Sun and Moon*.                                                                                                        |
| **Shiny Alolan Forms**   | 0             | 16        | Alternate color variants of the regional forms of Pokémon originally discovered in the Alola region                                                            |
| **Galarian Forms**       | 11            | 20        | Regional variants from *Pokémon Sword and Shield*.                                                                                                             |
| **Primal Forms**         | 2             | 2         | Primal Groudon and Primal Kyogre.                                                                                                                              |
| **Unique Forms**         | 4             | 4         | Ash's Greninja, Armoured Mewtwo, Eternamax Eternatus, Ultra Necrozma                                                                                           |
| **Shadow Forms**         | 3             | 131       | Dark, corrupted versions of Pokémon often seen in Pokémon Colosseum and XD: Gale of Darkness.                                                                  |
| **Fusion Forms**         | 6             | 6         | Kyurem (black/white), Necrozma (Dusk Mane/Dawn Wings), Calyrex (Ice Rider/Shadow Rider)                                                                        |
| **Origin Forms**         | 3             | 3         | Origin Forms represent the true or primal state of certain legendary Pokémon, showcasing their full power and unique design. i.e  Giratina, and Dialga/Palkia. |
| **Multi Forms**          | 24            | 200       | Non-standard, non-shiny forms of a single Pokémon (e.g., Unown B-Z, Deoxys Attack/Defense/Speed, all Rotom/Alcremie forms, Zygarde 10%/Complete).              |
---

## Check Model Animations
To verify whether a model contains animations or to inspect its structure, you can use the **[3D Preview](https://marketplace.visualstudio.com/items?itemName=mohitkumartoshniwal.3d-preview)** extension in Visual Studio Code. This extension allows you to preview 3D models directly in the editor, making it easier to inspect and test your models.
1. Upload your `.glb` or `.gltf` file to Visual Studio Code, or open it using Visual Studio Code.  
2. If the extension is set as the default, you can easily open the 3D model from the sidebar or by right-clicking the file and selecting **3D Preview**.  
3. If the model contains animations, they will appear in a dropdown menu; otherwise, no animations will be shown.