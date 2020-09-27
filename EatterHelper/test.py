import re
from collections import Counter
import _io
from typing import *


# with open("/Users/chengyinliu/D/USC/2020_Spring/dso-560-nlp-and-text-analytics/HW/Week1/Data/good_amazon_toy_reviews.txt") as file:
#     print(type(file))


def occasion_appears_time(male_recipients: List[str], reviews: List[str]) -> int:
    counter = 0
    regex = r"\b(" + '|'.join(male_recipients) + r")\b"
    print(f"Searching male using {regex}")
    for review in reviews:
        if re.search(regex, review):
            counter += 1
    return counter





