def decode(pairs: list):
    dictionary = {0: ""}
    next_idx = 1
    output = ""

    for item in pairs:
        entry = dictionary[item[0]] + item[1]
        output += entry
        
        dictionary[next_idx] = entry
        next_idx += 1

    return output