import pickle
from frequency import sp_characters

spam_dict = pickle.load(open('spam_dict.pickle', 'rb'))
ham_dict = pickle.load(open('ham_dict.pickle', 'rb'))

spam_values = []
ham_values = []


def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list


def main():
    for i in spam_dict:
        spam_values.append(spam_dict[i])

    for i in ham_dict:
        ham_values.append(ham_dict[i])

    new_spam_values = remove_duplicates(spam_values)
    new_ham_values = remove_duplicates(ham_values)

    new_spam_values.sort(reverse=True)
    new_ham_values.sort(reverse=True)

    new_spam_dict = {}
    new_ham_dict = {}

    #print(new_spam_values, len(new_spam_values))
    # print(new_ham_values,len(new_ham_values))
    temp_k = 400

    k = temp_k
    for i in new_spam_values:
        for j in spam_dict:
            if (k <= 0):
                break
            if (spam_dict[j] == i):
                new_spam_dict[j] = i
                k -= 1
        if (k <= 0):
            break

    # print(new_spam_dict,len(new_spam_dict))
    #
    k = temp_k

    for i in new_ham_values:
        for j in ham_dict:
            if j in sp_characters:
                continue
            if (k <= 0):
                break
            if (ham_dict[j] == i):
                new_ham_dict[j] = i
                k -= 1
        if (k <= 0):
            break

    # print(new_ham_dict,len(new_ham_dict))

    pickle_out_top_k_spam_dict = open("top_400_spam_dict.pickle", 'wb')
    pickle_out_top_k_ham_dict = open("top_400_ham_dict.pickle", 'wb')

    pickle.dump(new_spam_dict, pickle_out_top_k_spam_dict)
    pickle.dump(new_ham_dict, pickle_out_top_k_ham_dict)


main()
