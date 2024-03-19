from typing import *


class Solution:
	def findArray(self, pref: List[int]) -> List[int]:
		prev = pref[0]
		for i in range(1, len(pref)):
			pref[i] ^= prev
			prev ^= pref[i]

		return pref

"""
xor(^)은 순서가 상관이 없다.
[5,2,0,3,1]
output[i] = prev ^ pref[i]       
    ?     =   5  ^    2  => 7 => pref[i] = 7
    prev ^= pref[i]    
         ^=  5 ^ 7 = 2 
--->next
output[i] = prev ^ pref[i]       
    ?     =  2   ^   0   => 2 => pref[i] = 2
    prev ^= pref[i]    
         ^=  2 ^ 2 = 0

# 기존의 pref[i]의 값을 변경하였기에 기존값을 다시 XOR하여 prev로 저장하는 방식.
"""