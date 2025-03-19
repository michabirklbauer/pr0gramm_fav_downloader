#!/usr/bin/env python3

# 2025 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com


def test1():
    from download import download_item, download_collection  # noqa: F401
    from download import __version

    assert type(__version) is str
