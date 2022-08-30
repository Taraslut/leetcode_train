from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rez = []
        for word in strs[::-1]:
            for group in rez:
                if group and len(group[0]) == len(word):
                    word_copy = word[:]
                    for letter in group[0]:
                        if word_copy.find(letter) == -1 or word_copy.count(letter) != group[0].count(letter):
                            break
                    else:
                        group.insert(1, word)
                        break
            else:
                rez.append([word])
        return rez


if __name__ == '__main__':
    s = Solution()

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    rez = s.groupAnagrams(strs)
    expect = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert rez == expect, f"{rez} != {expect} "

    strs = [""]
    rez = s.groupAnagrams(strs)
    assert rez == [[""]]

    strs = ["a"]
    rez = s.groupAnagrams(strs)
    assert rez == [["a"]]

    strs = ["ddddddddddg","dgggggggggg"]
    rez = s.groupAnagrams(strs)
    assert rez == [["dgggggggggg"],["ddddddddddg"]]
