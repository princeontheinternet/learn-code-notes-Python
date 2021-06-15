# Understanding Hash function and how dictionary uses a hash tables
# Dictionary uses hash functions and all the values are indexed.
# Bcz of hash functions retrieving a value for a key is fast (using get() method)

data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]


# Part 1
def simple_hash(s: str) -> int:
    """A ridiculously simple hashing function"""
    basic_hash = ord(s[0])
    return basic_hash % 10


# Part 3
# Writing our own get function
def get(k: str) -> str:
    """Return the value for a key, or None if the key doesn't exist"""
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


# Part 2
keys = [""] * 10
values = keys.copy()

# PArt 1
for key, value in data:
    h = simple_hash(key)  # using our function
    # h = hash(key)           # using built-in hash function
    print(key, h)

    # Part 2
    keys[h] = key
    values[h] = value

print(keys)
print(values)

# Part 3
print()
value = get("banana")
print(value)