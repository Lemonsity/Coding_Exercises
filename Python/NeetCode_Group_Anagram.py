def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = dict()
    for s in strs:
        occurs = dict()
        for char in s:
            occurs[char] = 1 + occurs.get(char, 0)
        occurs_list = sorted(list(occurs.items()))
        occurs_ser = str(occurs_list)

        if occurs_ser in result:
            result[occurs_ser].append(s)
        else:
            result[occurs_ser] = [s]

    return list(result.values())
