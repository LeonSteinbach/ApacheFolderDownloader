# ApacheFolderDownloader

The ApacheFolderDownloader is a Python script for downloading entire directories from Apache web servers. It uses the Beautiful Soup library to parse the HTML of the directory and the wget library to download files.

## Features

The ApacheFolderDownloader can:

* Download entire directories from Apache web servers
* Recursively download subdirectories

## Requirements

* Python 3.x
* Beautiful Soup 4
* wget
* requests

## Usage

This command will recursively download all data inside the folder hosted at ```<url>``` and store it inside the folder ```<destination path>```:

```python main.py <url> <destination path>```
