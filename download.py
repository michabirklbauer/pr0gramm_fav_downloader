import json
from requests import get
import urllib.request as ur

base_url = "https://img.pr0gramm.com/"
user = ""
collection = f"https://pr0gramm.com/api/items/get?flags=31&user={user}&collection=favoriten&self=false"
cookies = {"me":
          """""",
          "pp":
          """"""}
item_count = 10909 # get from https://pr0gramm.com/api/profile/info?name={user}

def download():
    error_urls = list()
    seen_ids = set()
    first_pack = get(collection, cookies = cookies)
    first_pack_items = json.loads(first_pack.text)["items"]
    for item in first_pack_items:
        id = int(item["id"])
        item_url = str(item["image"]).strip()
        if item["fullsize"] is not None and str(item["fullsize"]).strip() != "":
            item_url = str(item["fullsize"]).strip()
        item_name = f"{id}_{item_url.split('/')[-1]}"
        try:
            current_url = base_url + item_url
            _ = ur.urlretrieve(current_url, item_name)
        except Exception as e:
            error_urls.append(current_url)
            current_url = base_url + str(item["image"]).strip()
            _ = ur.urlretrieve(current_url, item_name)
        seen_ids.add(id)
    print(f"Downloaded {len(seen_ids)} posts.")
    current_ids = set()
    current_max = 0
    finished = False
    while not finished:
        pack = get(collection + f"&newer={current_max}", cookies = cookies)
        pack_items = json.loads(pack.text)["items"]
        for item in pack_items:
            id = int(item["id"])
            if id in seen_ids:
                finished = True
                break
            item_url = str(item["image"]).strip()
            if item["fullsize"] is not None and str(item["fullsize"]).strip() != "":
                item_url = str(item["fullsize"]).strip()
            item_name = f"{id}_{item_url.split('/')[-1]}"
            try:
                current_url = base_url + item_url
                _ = ur.urlretrieve(current_url, item_name)
            except Exception as e:
                error_urls.append(current_url)
                current_url = base_url + str(item["image"]).strip()
                _ = ur.urlretrieve(current_url, item_name)
            seen_ids.add(id)
            current_ids.add(id)
        current_max = max(current_ids)
        current_ids = set()
        print(f"Downloaded {len(seen_ids)} posts.")
    print(f"Downloaded {len(seen_ids)} posts of {item_count}. Download finished!")
    print("The following URLs could not be fetched:")
    print("\n".join(error_urls))

if __name__ == "__main__":
    download()
