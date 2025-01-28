from collections import Counter 
class Solution:
    def makingAnagrams(self,s1, s2):
        h_map_set_1=dict(Counter(s1))
        h_map_set_2=dict(Counter(s2))
        count=0 
        for i in h_map_set_1:
            if i in h_map_set_2:
                if h_map_set_2[i]!=h_map_set_1[i]:
                    count=abs(h_map_set_1[i]-h_map_set_2[i])
            else:
                count+=h_map_set_1[i]
        for j in h_map_set_2:
            if j not in h_map_set_1:
                count+=h_map_set_2[j]
        return count