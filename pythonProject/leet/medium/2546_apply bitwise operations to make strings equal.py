class Solution:
	def makeStringsEqual(self, s: str, target: str) -> bool:
		return ('1' in s) == ('1' in target)


"""
1H, no Counter()
---
You are given two 0-indexed binary strings s and target of the same length n. You can do the following operation
on s any number of times:

Choose two different indices i and j where 0 <= i, j < n. Simultaneously, replace s[i] with (s[i] OR s[j]) and s[j]
with (s[i] XOR s[j]). For example, if s = "0110", you can choose i = 0 and j = 2, then simultaneously replace s[0]
with (s[0] OR s[2] = 0 OR 1 = 1), and s[2] with (s[0] XOR s[2] = 0 XOR 1 = 1), so we will have s = "1110". Return
true if you can make the string s equal to target, or false otherwise.
-----
print(0 or 0) = 0
print(1 or 1) = 1
print(0 or 1) = 1
print(1 or 0) = 1

xor == ^
print(0 ^ 0) = 0
print(1 ^ 1) = 0
print(0 ^ 1) = 1
print(1 ^ 0) = 1
---
replace s[i] = (s[i] OR s[j]), s[j] = (s[i] XOR s[j])
s[i], s[j] => s[i], s[j]
0, 0 => 0, 0
1, 1 => 1, 0
0, 1 => 1, 1
1, 0 => 1, 1
---
i, j 둘중 하나가 1 을 가지고 있을때 1, 0을 만들 수 있다. -> 1이 없으면 조건을 아예 맞출 수 없다.
1이 1개 이상 존재할때 0으로 전부 치환이 불가능하다.
"""