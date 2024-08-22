class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a_dist,b_dist=list(set(s)),list(set(t))
        a_dic_count,b_dic_count={},{}
        for i in a_dist:
            a_dic_count[i] = s.count(i)
        for j in b_dist:
            b_dic_count[j] = t.count(j)
        if a_dic_count == b_dic_count:
            return True
        else:
            return False
        """if set(s) != set(t):
            return False
        for i in s:
            if s.count(i) != t.count(i):
                return False
        return True
        """
