import hashlib
import itertools
import os
import time
import sys

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

def create_sha1_hash_table(file_path) :
    if not os.path.exists(file_path):
        print(f"Error : Don't have file '{file_path}'")
        return None
    try:
        with open(file_path) as f:
            word_list = f.read().splitlines()
    except Exception as e:
        print(f"An error occurred while reading the file.: {e}")
        return None

    total_words = len(word_list)
    print(f"\nLoad all words : {total_words}")

    rainbow_table = {}

    start_time = time.time()
    total_candidates = 0

    print("Create SHA1 Hash Table")
    for i, word in enumerate(word_list) :
        word = word.strip()
        if not word:
            continue
    
        candidates = read(word)
        total_candidates += len(candidates)

        for candidate in candidates:
            try:
                sha1_hash = hashlib.sha1(candidate.encode('utf-8')).hexdigest()
        
                rainbow_table[sha1_hash] = candidate
            except UnicodeEncodeError:
                continue

    end_time = time.time()
    creation_time = end_time - start_time

    return rainbow_table, creation_time, total_candidates

hash_table, creation_time, total_candidates = create_sha1_hash_table(DICTIONARY_FILE_PATH)

if hash_table is not None:
    table_size_count = len(hash_table)
    
    memory_size_bytes = sys.getsizeof(hash_table)
    
    print("="*50)
    print("Create SHA1 Hash Table finish")
    print("="*50)
    
    print("\n### Time Measurement ###")
    print(f"Time taken to create the table. : {creation_time:.2f} second\n")
    
    print("\n### Table Size Measurement ###")
    print(f"Number of items in the table : {table_size_count:,} ")
    print(f"The total words that can be created : {total_candidates:,} ")
    print(f"Memorey Object Size : {memory_size_bytes / (1024*1024):.2f} MB\n")
    