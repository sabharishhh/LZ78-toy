def encode(text: str):
    next_idx = 1
    dictionary = {}
    current_phrase = ""
    output = list()

    for ch in text:
        candidate_phrase = current_phrase + ch
        #print(f"{current_phrase} + {ch} -> {candidate_phrase}")

        if candidate_phrase in dictionary:
            current_phrase = candidate_phrase
            #print("seen before:", candidate_phrase)
        else:
            if current_phrase == "":
                    idx = 0
            else:
                idx = dictionary[current_phrase]
            output.append((idx, ch))

            dictionary[candidate_phrase] = next_idx
            next_idx += 1
            current_phrase = ""
            #print("new phrase:", candidate_phrase)


    if (current_phrase != ""):
        index = dictionary[current_phrase]
        output.append((index, ''))

    return output
