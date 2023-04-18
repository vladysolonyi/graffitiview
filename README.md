# graffitiview: Steetview graffiti collection
Theg main goal of this project was collecting a dataset of panoramas from Google Streetview and searching for graffiti pieces to preserve them in a generative archive.
This experiment was created during a machine learning CoCreate course at HGK FHNW by [@gu-ma](https://github.com/gu-ma)

## Description
- **[dl_pano.py 💾](/dl_pano.py)** <br>Fetches all panoramas from a given bounding box *(For example surrounding a town)* and downloads them. Additionally it writes a JSON file in the directory containing information about every single image.

- **[normalize_json.py 🧯](/normalize_json.py)** <br>Removes duplicates and non existing ones

- **[preprocess_dataset.py 🪚](/preprocess_dataset.py)** <br>Splits panorama in to two separate images by cutting it in the middle. Crops a bit from every side away to get rid of the unuseful regions.

- **[graffiti_detection.ipynb 🧿](/graffiti_detection.ipynb)** <br>Runs images from the dataset through a recognition model and creates a new JSON file, that contains all panoramas with graffiti and their positions in the frame.

- **[finalize.py 🏁](/finalize.py)** <br>Filters the dataset based on the exported JSON file from the Google Colab notebook.

## Installation

**Coming soon...**

## Credits

*I used a [model](https://github.com/abundis-rmn2/graffiti_detection_OD_TF) by **abundis-rmn2** for the actual graffiti detection.* *Also for the dataset creation, I used a beautiful [library](https://github.com/sk-zk/streetlevel) created by **sk-zk**, that allowed me to fetch panoramas in a given region without any access to the official API :P*
