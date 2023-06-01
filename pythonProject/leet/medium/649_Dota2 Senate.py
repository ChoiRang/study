import collections


class Solution:
	def predictPartyVictory(self, senate: str) -> str:
		vote_r = collections.deque()
		vote_d = collections.deque()
		for i, s in enumerate(senate):
			if s == "R":
				vote_r.append(i)
			else:
				vote_d.append(i)

		N = len(senate)
		while vote_r and vote_d:
			r = vote_r.popleft()
			d = vote_d.popleft()
			if r < d:
				vote_r.append(r + N)
			else:
				vote_d.append(d + N)

		return "Radiant" if vote_r else "Dire"
