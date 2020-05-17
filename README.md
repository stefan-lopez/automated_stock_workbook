# Stock Visualizer Workbook


## Project File Overview

- [`stock_archivist.py`](stock_archivist.py) script for downloading .
- [`gmailer.py`](gmailer.py) helper module for emailing functionality.
- [`config.yaml`](config.yaml) config file for definining which stocks to download and providing necessary authentication.
- [`stock_archive_template.xlsx`](stock_archive_template.xlsx) template Excel workbook used to generate final stock workbook.

## Requirements

You’ll need the following:

- [Python 3.7.0](https://www.python.org/downloads/release/python-368/) (other Python 3 versions may work as well)
- Python's PIP package installer
- Microsoft Excel

## Getting Started

The commands below are for Windows and my Python alias is "python" but yours may be "python3", "py -3", etc.

Make sure you have the virtualenv package in your global Python environment.

```
python -m pip install virtualenv
```

Move this project to its own folder and setup a virtual environment inside of it.

```
python -m venv env
```

Activate your virtual environment.

```
env/Scripts/activate
```

Install the project's dependencies into your virtual environment.

```
pip install -r requirements.txt
```
