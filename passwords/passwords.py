# Armira Nance
# passwords.py


import hashlib

words = [line.strip().lower() for line in open('words.txt')]
hashed_passwords_file = [line.strip() for line in open('hashed_passwords.txt')]
hash_words = {}
hashed_passwords = {}
cracked_passwords = {}

def hashWord(word):
    sha256_hash = hashlib.sha256()
    word_bytes = bytes(word, 'utf-8')
    sha256_hash.update(word_bytes)
    return sha256_hash.hexdigest()

def hashWords(words):
    hash_count = 0
    for w in words:
        hash_count += 1
        hashed = hashWord(w)
        hash_words[w] = hashed
    return hash_count

def parseHashedPasswords(hashed_passwords_file):
    for x in hashed_passwords_file:
        colon_index = x.index(':')
        hashed_passwords[x[:colon_index]] = x[colon_index + 1:]

def findAndAssign(hashed_passwords, words):
    pass_count = 0
    for y in hashed_passwords.items():
        if y[1] in list(hash_words.values()):
            find_original_word = [k for k, v in hash_words.items() if v == y[1]][0]
            cracked_passwords[y[0]] = find_original_word
            pass_count += 1
    return pass_count

def writeCrackedPasswordsToFile(cracked_passwords):
    with open('cracked1.txt', 'w') as file:
        for key, value in cracked_passwords.items():
            file.write(f"{key}: {value}\n")

def main():

    '''
    Part 1: Unsalted Passwords
    '''
    hash_count = hashWords(words)
    parseHashedPasswords(hashed_passwords_file)
    pass_count = findAndAssign(hashed_passwords, words)
    print("Hash Count: ", hash_count, '\n')
    print("Passwords Cracked: ", pass_count, '\n')
    writeCrackedPasswordsToFile(cracked_passwords)


main()
