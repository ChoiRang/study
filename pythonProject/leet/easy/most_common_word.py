from typing import *
from collections import Counter
import re


class Solution:
	def most_common_word(self, paragraph: str, banned: List[str]) -> str:
		words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]

		return Counter(words).most_common(1)[0][0]
