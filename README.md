# pr0gramm Favoriten Runterlader

A simple python script to download images and videos from the "Favoriten"
collection of your [pr0gramm.com](https://pr0gramm.com/) user profile.
Uses the [pr0gramm API](https://github.com/pr0gramm-com/api-docs).

## Usage

- Install [python](https://www.python.org/).
- Install package `requests`: `pip install requests`.
- Set the following parameters inside `download.py`:
  ```python
  # pr0gramm username
  USER = ""
  # [optional] collection item count, get from https://pr0gramm.com/api/profile/info?name={USER}
  ITEM_COUNT = 0
  # login cookies for pr0gramm
  COOKIES = {"me": """cookie_value""", "pp": """cookie_value"""}
  ```
- Run the script with `python download.py`.

## Support pr0gramm

Consider supporting pr0gramm by buying [pr0mium](https://pr0gramm.com/pr0mium). 😉

## Contact

- [micha.birklbauer@gmail.com](mailto:micha.birklbauer@gmail.com)
