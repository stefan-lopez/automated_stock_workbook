# Stock Visualizer Workbook


## Project File Overview

- [`stock_archivist.py`](stock_archivist.py) script for downloading historical data for the specified stocks.
- [`gmailer.py`](gmailer.py) helper module for emailing functionality.
- [`config.yaml`](config.yaml) config file for defining which stocks to download and providing necessary authentication.
- [`stock_archive_template.xlsx`](stock_archive_template.xlsx) template Excel workbook used to generate final stock workbook.

## Requirements

You’ll need the following:

- [Python 3.7.0](https://www.python.org/downloads/release/python-368/) (other Python 3 versions may work as well)
- Python's PIP package installer
- Microsoft Excel
- An API key from alphavantage.co, you can get one for free here: https://www.alphavantage.co/support/#api-key

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

Sign up for API access here and note the key they provide you upon successful sign up.

```
https://www.alphavantage.co/support/#api-key
```

Fill out the config.yaml file with your api key as well as the ticker symbols you wish to get daily data for. If you wish to send out an automatic email containing your workbook, fill out those fields as well.

If you elect to send emails you may run into authentication issues. Follow this link for info on how to enable your gmail account to send automated emails.

```
https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
```

Run the stock archivist script to create your own stock visualizer workbook.

```
python stock_archivist.py
```

WARNING: If you emailed the workbook out and attempt to open it directly from your browser, you may run into a corrupt file error. This is due to the Protected View on Office products and is expected behavior. You can either go to your downloads folder and open the workbook from there, or disable the Protected View on your version of Excel. Follow this link for more details:

```
https://www.easeus.com/resource/the-file-is-corrupted-and-cannot-be-opened.html
```

