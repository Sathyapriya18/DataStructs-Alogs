from collections import Counter


def groupAnagrams(strs):
    dict = {}

    # traverse list of strings
    for strVal in strs:


        key = ''.join(sorted(strVal))


        if key in dict.keys():
            dict[key].append(strVal)
        else:
            dict[key] = []
            dict[key].append(strVal)


    output = ""
    new_lsit = []

    for v in dict.values():
        new_lsit.append(v)


    print(new_lsit)





groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
