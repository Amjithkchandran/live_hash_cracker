import hashlib


def check_hash_type(hash_value):
    hash_types = {
        32: "MD5",
        40: "SHA-1",
        56: ["SHA-224", "SHA3-224"],
        64: ["SHA-256", "SHA3-256", "BLAKE2s"],
        96: ["SHA-384", "SHA3-384"],
        128: ["SHA-512", "SHA3-512", "BLAKE2b"],
    }
    return hash_types.get(len(hash_value), "Unknown Hash Type")


def hash_word(word, hash_type):
    if hash_type == "MD5":
        return hashlib.md5(word.encode()).hexdigest()
    elif hash_type == "SHA-1":
        return hashlib.sha1(word.encode()).hexdigest()
    elif hash_type == "SHA-224":
        return hashlib.sha224(word.encode()).hexdigest()
    elif hash_type == "SHA-256":
        return hashlib.sha256(word.encode()).hexdigest()
    elif hash_type == "SHA-384":
        return hashlib.sha384(word.encode()).hexdigest()
    elif hash_type == "SHA-512":
        return hashlib.sha512(word.encode()).hexdigest()
    elif hash_type == "SHA3-224":
        return hashlib.sha3_224(word.encode()).hexdigest()
    elif hash_type == "SHA3-256":
        return hashlib.sha3_256(word.encode()).hexdigest()
    elif hash_type == "SHA3-384":
        return hashlib.sha3_384(word.encode()).hexdigest()
    elif hash_type == "SHA3-512":
        return hashlib.sha3_512(word.encode()).hexdigest()
    elif hash_type == "BLAKE2s":
        return hashlib.blake2s(word.encode()).hexdigest()
    elif hash_type == "BLAKE2b":
        return hashlib.blake2b(word.encode()).hexdigest()


def crack_hash(hash_value, hash_type, wordlist=None, words=None):
    if words:
        for word in words:
            if hash_word(word, hash_type) == hash_value:
                return word
    elif wordlist:
        with open(wordlist, "r") as file:
            for word in file:
                word = word.strip()
                if hash_word(word, hash_type) == hash_value:
                    return word
    return None


def main():
    hash_value = input("Enter the hash value: ")

    hash_type_list = check_hash_type(hash_value)

    if isinstance(hash_type_list, list):
        formatted_list = ", ".join(hash_type_list)
        print(f"Detected Hash Type(s): {formatted_list}")
    else:
        print(f"Detected Hash Type: {hash_type_list}")

    if hash_type_list != "Unknown Hash Type":
        print("\nChoose an option:")
        print("1. Enter words to check manually")
        print("2. Use a wordlist to crack the hash")
        option = input("Enter your choice (1 or 2): ")

        if option == "1":
            words = input("Enter words to check (comma-separated): ").split(",")
            words = [word.strip() for word in words]
            for hash_type in (
                hash_type_list if isinstance(hash_type_list, list) else [hash_type_list]
            ):
                print(f"\nChecking with {hash_type}...")
                password = crack_hash(hash_value, hash_type, words=words)
                if password:
                    print(f"Password found: {password} using {hash_type}")
                    break
            else:
                print("No match found.")

        elif option == "2":
            wordlist = input("Enter the path to your wordlist: ")
            for hash_type in (
                hash_type_list if isinstance(hash_type_list, list) else [hash_type_list]
            ):
                print(f"\nAttempting to crack using {hash_type}...")
                password = crack_hash(hash_value, hash_type, wordlist=wordlist)
                if password:
                    print(f"Password found: {password} using {hash_type}")
                    break
            else:
                print("Password not found in wordlist.")
        else:
            print("Invalid option selected.")
    else:
        print("Unsupported or Unknown Hash Type")


if __name__ == "__main__":
    main()
