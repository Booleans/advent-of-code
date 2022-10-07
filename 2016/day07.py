import re

ABBA_match = re.compile(r"^.*(\w)(\w)\2\1.*$")
ABBA_match_in_hypernet = re.compile(r"\[\w*(\w)(\w)\2\1\w*\]")

with open("inputs/day07.txt") as f:
    addresses = f.read().split("\n")

supports_TLS = [
    (
        (ABBA_match.match(address) != None)
        and (ABBA_match_in_hypernet.search(address) == None)
    )
    for address in addresses
]

print(sum(supports_TLS))
