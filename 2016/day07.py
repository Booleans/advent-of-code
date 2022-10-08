with open("inputs/day07.txt") as f:
    addresses = f.read().split("\n")


def is_TLS_supported(address):
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
