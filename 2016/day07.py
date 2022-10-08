with open("inputs/day07.txt") as f:
    addresses = f.read().split("\n")


def is_TLS_supported(address: str) -> bool:
    supports_TLS = False
    in_hypernet = False

    for i, char in enumerate(address[:-3]):
        if char == "[":
            in_hypernet = True
            continue
        elif char == "]":
            in_hypernet = False
            continue
        else:
            substring = address[i : i + 4]
            if substring == substring[::-1] and substring[0] != substring[1]:
                if in_hypernet:
                    return False
                else:
                    supports_TLS = True

    return supports_TLS


# Part 1 solution.
num_tls_supported_addresses = sum(is_TLS_supported(address) for address in addresses)

print(f"The number of addresses that support TLS is {num_tls_supported_addresses}.")


def valid_aba(substring: str) -> bool:
    return substring[0] == substring[2] and substring[0] != substring[1]


def convert_ABA_to_BAB(ABA: str) -> str:
    B = ABA[1]
    A = ABA[0]
    return f"{B}{A}{B}"


def supports_SSL(address: str) -> bool:
    supports_SSL = False
    in_hypernet = False
    ABAs = set()
    BABs = set()

    for i, char in enumerate(address[:-2]):
        if char == "[":
            in_hypernet = True
            continue
        elif char == "]":
            in_hypernet = False
            continue
        else:
            substring = address[i : i + 3]
            if valid_aba(substring):
                if in_hypernet:
                    BABs.add(substring)
                else:
                    ABAs.add(substring)

    for ABA in ABAs:
        BAB = convert_ABA_to_BAB(ABA)
        if BAB in BABs:
            return True
    return False


num_SSL_supported = sum(supports_SSL(address) for address in addresses)

# Part 2 solution.
print(f"The number of addresses that support SLL is {num_SSL_supported}.")
