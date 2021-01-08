# iPython Notebooks

## Setup
After you clone the repository, `cd` into the `random-password` directory and run these:

```bash
python -m venv .venv
source ./.venv/bin/activate
pip install --upgrade pip poetry
poetry install
```

## Running the notebooks
```bash
jupyter-notebook --no-browser
```

That command will output a `locahost` URL that you can open in your browser.

For example:

    http://localhost:8888/?token=45cbed8528108d0c6066a252693bf03123b6630850d8c630
