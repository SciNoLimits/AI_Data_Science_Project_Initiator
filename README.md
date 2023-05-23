# AI / Data Science Project Initiator

This Python script creates a predefined directory structure for a AI / Data Science project. 
It sets up directories and files based on a dictionary representation of the desired structure.



## Directory Structure


```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- Make this project pip installable with `pip install -e`
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```
<br>

## Getting Started

### Prerequisites

Make sure you have the following requirements met:

- Python 3.x installed
- `colorama` module installed (`pip install colorama`)


### Usage

1. Clone the repository or download the script [initiate.py](initiate.py) to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script by executing the following command:

    ```shell
    python initiate.py
    ```

4. When prompted, enter the name of your project. This will be used as the root directory name.

    ```shell
    Your Project Name >>> my_project
    ```

5. The script will create the project directory structure based on the predefined dictionary. You will see the progress of file and directory creation in the terminal.

    <center><img src="images/project_initiator.png" width="50%"></center>

6. After the structure is created, you will be prompted to open the project in VS Code.

    - If you choose "YES" (or "Y"), the script will open the project directory in VS Code if it is installed in the system.
    - If you choose "NO" (or "N"), the script will exit.


    <center><img src="images/open_in_vscode.png" width="80%"></center>

7. You can now start working on your project within the created directory structure.


## Customizing the Directory Structure

The directory structure is defined in the `dir_struct` dictionary in the script. You can modify this dictionary to match your desired project structure.

Each key in the dictionary represents a directory or file. Directories are prefixed with `"d-"` and files are prefixed with `"f-"`. The nested structure is represented using nested dictionaries.

For example, the following entry in the dictionary:

<!-- For more customization, ```dir_struct``` dict can be modified as required in [initiate.py](initiate.py) file.



*Note: The ```dir_struct``` has naming conventions in order to seprate directories and files.*

- The Keys or Value starting with ```d-``` represents a directory.
- The Keys or Value starting with ```f-``` represents a files. -->

```python
    "d-src": {
    "f-__init__.py": {},
    "d-data": {"f-make_dataset.py": {}},
    "d-features": {"f-build_features.py": {}},
    "d-models": {"f-predict_model.py": {}, "f-train_model.py": {}},
    "d-visualization": {"f-visualize.py": {}},
},
```

will create the following structure:

```markdown
- src
    - __init__.py
    - data
        - make_dataset.py
    - features
        - build_features.py
```

<!-- ## Creating a Project

Clone this repo or download it, if required modify the directory structure in [initiate.py](initiate.py) file as suggested above.

```shell
python initiate.py
```
Provide your project name

```shell
Your Project Name >>> my_project
```
If VS Code is installed and you would like to open your project in it then type Y for yes or N for no.

```
Would you like to open your project in VS code YES/NO >>> Y
```

<center><img src="images/project_initiator.png" width="50%"></center>
<br><br>
<center><img src="images/open_in_vscode.png" width="80%"></center>

<br><br> -->

<div style='text-align: right;'>
    <sub>The directory structure used in this repo was inspired from 
    <a href="https://drivendata.github.io/cookiecutter-data-science/"> Cookiecutter Data Science</a>. However it can be modified as desired.</sup>
</div>

