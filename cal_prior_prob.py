import pickle
import pandas as pd

ham_strings = pickle.load(open('top_400_ham_dict.pickle', 'rb'))
spam_strings = pickle.load(open('top_400_spam_dict.pickle', 'rb'))
total_vocabulary=pickle.load(open('total_vocabulary.pickle','rb'))


prior_prob_ham_strings = {}
prior_prob_spam_strings = {}


def main():
    spam_count = 535
    ham_count = 3465
    epsilon=1/2

    for i in total_vocabulary:
        if i in spam_strings:
            prior_prob_spam_strings[i] = (spam_strings[i]+epsilon) / (spam_count + 2*epsilon)
        else:
            prior_prob_spam_strings[i]=(epsilon)/(spam_count+2*epsilon)

    for i in total_vocabulary:
        if i in ham_strings:
            prior_prob_ham_strings[i]=(ham_strings[i]+epsilon)/(ham_count+2*epsilon)
        else:
            prior_prob_ham_strings[i]=(epsilon)/(ham_count+2*epsilon)

    # print(prior_prob_ham_strings)




main()

print(prior_prob_ham_strings,len(prior_prob_ham_strings))
pickle_out_spam = open("pickle_out_prior_spam.pickle", 'wb')

pickle_out_ham = open("pickle_out_prior_ham.pickle", 'wb')

pickle.dump(prior_prob_spam_strings, pickle_out_spam)
pickle.dump(prior_prob_ham_strings, pickle_out_ham)

# print(prior_prob_ham_strings)
