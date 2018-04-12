import pandas as pd
import pickle

sp_characters = ['@', '%', '+', "\\", '/', "'", '!', '#', '$', '^', '?', ':', '(', ')', '{', '}', '[', ']', '~', '-',
                 '_', '.', '"', ',','|']
spam_strings = {}
ham_strings = {}
special_character_dict = {0: '@', 1: '%', 2: '+', 3: "\\", 4: '/', 5: "'", 6: '!', 7: '#', 8: '$', 9: '^', 10: '?',
                          11: ':', 12: '(', 13: ')', 14: '{', 15: '}', 16: '[', 17: ']', 18: '~', 19: '-', 20: '_'}


def is_special_character_present(string):
    present_list = []
    for i in range(0, 21):
        if (special_character_dict[i] in string):
            present_list.append(1)
        else:
            present_list.append(0)

    return present_list


def put_in_dict(string):
    try:
        if (ham_strings[string] >= 0 and spam_strings[string] >= 0):
            return
    except:
        ham_strings[string] = 0
        spam_strings[string] = 0


def incr_in_ham_dict(string):
    ham_strings[string] += 1


def incr_in_spam_dict(string):
    spam_strings[string] += 1

def num_or_special_char_present(string):
    nums=['0','1','2','3','4','5','6','7','8','9']
    for i in string:
        if i in nums:
            return True
        if i in sp_characters:
            return True

def get_word(string):
    for j in range(0, 20):
        for i in sp_characters:
            string = string.strip(i)

    if(num_or_special_char_present(string)==True):
        return
    return string


def add_special_characters():
    for i in sp_characters:
        put_in_dict(i)


def main():
    add_special_characters()
    df = pd.read_csv('spam.csv', encoding='latin-1')

    tuple_count = 0
    ham_spam_list = []
    for row in df.itertuples():
        ham_spam_list.append(row.v1)
        tuple_count += 1
        if (tuple_count > 3900):  # total tuples for training!
            break

    tuple_count = 0
    count = 0
    for row in df.itertuples():
        if (tuple_count > 3900):
            break

        special_characters = is_special_character_present(row.v2)
        words_with_sp_chars = (row.v2).split(' ')

        for i in words_with_sp_chars:
            correct_word = get_word(i)
            if(correct_word==None):
                continue
            correct_word = correct_word.lower()

            put_in_dict(correct_word)
            if (ham_spam_list[count] == 'spam'):
                incr_in_spam_dict(correct_word)
            # print(correct_word,'in spam|',row.v1)
            else:
                incr_in_ham_dict(correct_word)
            # print(correct_word,'in ham|',row.v2)

        for i in range(0, 21):
            if (ham_spam_list[count] == 'spam' and special_characters[i] == 1):
                incr_in_spam_dict(special_character_dict[i])
            else:
                incr_in_ham_dict(special_character_dict[i])
        # print(row.v1)
        count += 1
        tuple_count += 1


main()

pickle_out_spam = open('spam_dict.pickle', 'wb')
pickle_out_ham = open('ham_dict.pickle', 'wb')
pickle.dump(spam_strings, pickle_out_spam)
pickle.dump(ham_strings, pickle_out_ham)

# print(spam_strings)
