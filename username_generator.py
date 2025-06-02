import random

leet_map = {
    'a': ['a', '4'], 'b': ['b', '8'], 'e': ['e', '3'],
    'g': ['g', '6'], 'i': ['i', '1'], 'o': ['o', '0'],
    's': ['s', '5'], 't': ['t', '7'], 'z': ['z', '2']
}

keywords = [
    "crypto", "chain", "block", "web", "x", "genz", "top", "hash",
    "bot", "link", "vibe", "tech", "ai", "ravi", "code", "data",
    "pay", "mint", "dapp", "gas", "wallet", "defi", "xrpl", "sol", "eth"
]

def leetify(word):
    return ''.join(random.choice(leet_map.get(c, [c])) for c in word)

def generate_usernames(n=100):
    usernames = set()
    while len(usernames) < n:
        word1 = random.choice(keywords)
        word2 = random.choice(keywords)
        if word1 != word2:
            name = leetify(word1 + word2)
            if len(name) <= 15:
                usernames.add(name.lower())
    return list(usernames)
