def all_construct(target: str, word_bank: list,memo={}) -> list:
    if(target in memo):
        return memo[target]
    if target == '':
        return [[]]
    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = [el[:] for el in suffix_ways]
            [el.insert(0, word) for el in target_ways]
            result.extend(target_ways)
    memo[target]=result
    return memo[target]
print(all_construct("abcd",["a","abc","c","d"]))
print(all_construct("purple",["purp","ur","p","le","purpl"]))

