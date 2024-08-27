class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ls=[]
        dic={}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        for i in range(k):
            ls.append(list(sorted_dict.keys())[i])
        return ls