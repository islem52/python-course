def anagrams(str1, str2):
    """Check if two strings are anagrams of each other."""
    return sorted(str1) == sorted(str2)

# Test
print(anagrams("tame", "meta"))  # True
print(anagrams("tame", "mate"))  # True
print(anagrams("tame", "team"))  # True
print(anagrams("tabby", "batty"))  # False
print(anagrams("python", "java"))  # False
