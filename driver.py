from utils.encoder import encode
from utils.decoder import decode

def main():
    print("\n---- LZ78\\LZ2 -----\n")

    inputString = input("Enter input string to encode:\n>>> ")

    encodedList = encode(
        text=inputString
    )
    print("\nCompressed String:", encodedList)

    print()

    decodedString = decode(
        pairs=encodedList
    )
    print("Decompressed String:", decodedString)

    print()

main()