#!/usr/bin/env python3

# Version: 0.1
# Last Modified: Sep 3rd, 2019 
# Author: Kushagra Sharma
# Email: kushagra.sharma@buffercode.in
# Copyright: Open source

from twitter_image import save_twitter_data
from get_data import get_sources


def test():
    all_sources = get_sources()
    if all_sources:
        for sources in all_sources:
            for source in sources:
                if "twitter" in sources[source]:
                    save_twitter_data(sources[source])


if __name__ == "__main__":
    test()
