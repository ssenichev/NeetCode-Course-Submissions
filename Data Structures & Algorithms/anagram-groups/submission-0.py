class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = sorted(strs)
        strset = set(["".join(sorted(s)) for s in strs])
        
        answ = []
        
        if strset == strs:
            return [[x] for x in strs]

        j = 0
        for u in strset:
            un = []
            for s in strs:
                if "".join(sorted(s)) == u:
                    un.append(s)
            answ.append(un)
        
        return answ
        

