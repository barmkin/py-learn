favorite_language = ' python '
print(f"'{favorite_language}'")
print(f"'{favorite_language.rstrip()}'")
print(f"'{favorite_language.lstrip()}'")
print(f"'{favorite_language.strip()}'")

# Remove prefixes and suffixes
url = "https://github.com/barmkin/py-learn"
print(url.removeprefix("https://").removesuffix("/py-learn"))
