from copy import deepcopy

def most_common_word(filename):
    file = open(filename, 'r')
    n = 0
    words = []
    all_words = []
    
    # init words list
    for line in file:
        for word in line.split():
            all_words.append(word)
            if word not in words:
                words.append(word)

    # searching for the most common word
    for i in range(len(words)):
        for j in range(len(all_words)):
            tmp_n = 0
            if words[i] == all_words[j]:
                tmp_n += 1
        if tmp_n > n:
            n = deepcopy(tmp_n)
            common = words[i]
    print(common, n)

if __name__ == "__main__":
    most_common_word("data/i_promessi_sposi.txt")
