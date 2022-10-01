from dataclasses import dataclass, field


@dataclass
class Passphrase:
    raw: list[str]
    words: list[str] = field(init=False)
    no_repeated_words: bool = field(init=False)
    no_anagrams: bool = field(init=False)

    def __post_init__(self):
        self.words = self.raw.split()
        self.no_repeated_words = len(self.words) == len(set(self.words))
        sorted_letters = ["".join(sorted(word)) for word in self.words]
        self.no_anagrams = len(sorted_letters) == len(set(sorted_letters))


with open("inputs/day04.txt") as f:
    passphrases = [Passphrase(row) for row in f.read().split("\n")]

num_valid_phrases = sum(passphrase.no_repeated_words for passphrase in passphrases)

# Part 1 solution.
print(f"The number of passphrases with no repeated words is {num_valid_phrases}.")

num_valid_phrases = sum(
    passphrase.no_repeated_words and passphrase.no_anagrams
    for passphrase in passphrases
)

# Part 2 solution.
print(
    f"The number of passphrases with no repeated words and no anagrams is {num_valid_phrases}."
)
