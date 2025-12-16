import hashlib
import itertools
import os

TARGET_HASH = "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7"

SUBSTITUTIONS = {
    'o': '0',
    'l': '1',
    'i': '1'
}

DICTIONARY_FILE_PATH = "10k-most-common.txt"

def read(word):
    options = []
    for char in word:
        choices = [char]

        if char.isalpha():
            choices.extend([char.lower(), char.upper()])
        
        if char.lower() in SUBSTITUTIONS:
            choices.append(SUBSTITUTIONS[char.lower()])
        
        options.append(list(set(choices)))

    candidates = []
    for combo in itertools.product(*options):
        candidates.append("".join(combo))
        
    return list(set(candidates))


def Hacking_sha1(target_hash, file_path):
    if not os.path.exists(file_path):
        print(f"\nError : Don't have file'{file_path}'")
        return None
    print(f"\ntarget hash : {target_hash}")

    try:
        with open(file_path) as f:
            word_list = f.read().splitlines()
    except Exception as e:
        print(f"Error read file : {e}")
        return None

    total_words = len(word_list)
    print(f"Load all words : {total_words} ")
    

    for i, word in enumerate(word_list):
        word = word.strip() 
        if not word:
            continue
            
        candidates = read(word)
        
        for candidate in candidates:
            try:
                sha1_hash = hashlib.sha1(candidate.encode('utf-8')).hexdigest()
            except UnicodeEncodeError:
                continue
            
            if sha1_hash == target_hash:
                print("="*50)
                print(f"target word : '{candidate}'")
                print(f"Hash vaule SHA1 word of matching : {sha1_hash}")
                print("="*50)
                return candidate
    
    print("[Error] Don't found word matches the hash value in target word.")
    return None

found_word = Hacking_sha1(TARGET_HASH, DICTIONARY_FILE_PATH)

if found_word:
    print(f"target word : '{found_word}'\n")