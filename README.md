# Prodigy Facial Images Labeling

## ⏩ Getting started

It is highly recommended to create a new virtual environment before starting. 

```bash
python -m venv .env
source .env/bin/activate
```

When you have a fresh environment, run the following commands from the root repo directory:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Prodigy Setup


There is also a `requirements-prodigy.txt` file, _not included in this repo_, for installing Prodigy. The file is only:

```txt
--extra-index-url https://XXXX-XXXX-XXXX-XXXX@download.prodi.gy/index 
prodigy>=1.11.0,<2.0.0
```

Where your product key is substituted for `XXXX-XXXX-XXXX-XXXX`. You can then use this to install prodigy, if you need to label data, with `pip install -r requirements-prodigy.txt`