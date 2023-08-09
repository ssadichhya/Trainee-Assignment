from collections import defaultdict

anagram_dict = defaultdict(list)
def anagram(input):   
    for word in input:
        sorted_word ="".join(sorted(word))  #sorted creates a list of letters in a word so we have to join to form a word
        anagram_dict[sorted_word].append(word)
        result=list(anagram_dict.values())
    return result
input_array = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagram(input_array))

