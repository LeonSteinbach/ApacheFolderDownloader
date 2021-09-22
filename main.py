import os
import sys
import wget
import requests
from bs4 import BeautifulSoup


def download_folder(url, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)

    content = requests.get(url).text

    soup = BeautifulSoup(content, "html.parser")
    
    links = [link.text for link in soup.select("td > a")[1:]]
    for link in links:
        new_url = url + link
        new_dst = os.path.join(dst, link)

        print("\t" + new_url)

        if link.endswith("/"):
            download_folder(new_url, new_dst)
        else:
            wget.download(new_url, new_dst)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <url> <destination path>")
    
    url = sys.argv[1]
    dst = sys.argv[2]

    if not url.endswith("/"):
        print("Url is not a directory, did you forget to include a / at the end?")
        sys.exit(1)

    download_folder(url, dst)
