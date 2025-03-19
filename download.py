#!/usr/bin/env python3

# 2025 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

import json
from requests import get
import urllib.request as ur

from typing import Any
from typing import Dict
from typing import List

# pr0gramm username
USER = ""
# collection item count, get from https://pr0gramm.com/api/profile/info?name={USER}
ITEM_COUNT = 0
# login cookies for pr0gramm
COOKIES = {"me": """cookie_value""", "pp": """cookie_value"""}
BASE_URL = "https://img.pr0gramm.com/"
COLLECTION = f"https://pr0gramm.com/api/items/get?flags=31&user={USER}&collection=favoriten&self=false"


def download_item(item: Dict[Any, Any], error_urls: List[str]) -> None:
    id = int(item["id"])
    item_url = str(item["image"]).strip()
    if item["fullsize"] is not None and str(item["fullsize"]).strip() != "":
        item_url = str(item["fullsize"]).strip()
    item_name = f"{id}_{item_url.split('/')[-1]}"
    current_url = BASE_URL + item_url
    try:
        _ = ur.urlretrieve(current_url, item_name)
    except Exception:
        error_urls.append(current_url)
        current_url = BASE_URL + str(item["image"]).strip()
        _ = ur.urlretrieve(current_url, item_name)
    return


def download_collection() -> None:
    error_urls = list()
    seen_ids = set()
    first_pack = get(COLLECTION, cookies=COOKIES)
    first_pack_items = json.loads(first_pack.text)["items"]
    # get first batch
    for item in first_pack_items:
        id = int(item["id"])
        download_item(item, error_urls)
        seen_ids.add(id)
    # log completion of first batch
    print(f"Downloaded {len(seen_ids)} posts.")
    current_ids = set()
    current_max = 0
    finished = False
    # the API only returns a limited number of items, so we need
    # to repeatedly call the API to fetch all items
    # iterate over all batches, starting with the oldest
    while not finished:
        pack = get(COLLECTION + f"&newer={current_max}", cookies=COOKIES)
        pack_items = json.loads(pack.text)["items"]
        if len(pack_items) == 0:
            break
        for item in pack_items:
            id = int(item["id"])
            if id in seen_ids:
                finished = True
                break
            download_item(item, error_urls)
            seen_ids.add(id)
            current_ids.add(id)
        current_max = max(current_ids)
        current_ids = set()
        print(f"Downloaded {len(seen_ids)} posts.")
    # finish
    print(f"Downloaded {len(seen_ids)} posts of {ITEM_COUNT}. Download finished!")
    print("The following URLs could not be fetched:")
    print("\n".join(error_urls))
    return


if __name__ == "__main__":
    download_collection()
