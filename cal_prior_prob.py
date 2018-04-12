import pickle
import pandas as pd

ham_strings = pickle.load(open('top_400_ham_dict.pickle', 'rb'))
spam_strings = pickle.load(open('top_400_spam_dict.pickle', 'rb'))
# total_vocabulary=pickle.load(open('total_vocabulary.pickle','rb'))


prior_prob_ham_strings = {}
prior_prob_spam_strings = {}

total_vocabulary={}

def create_total_vocabulary():
    for i in ham_strings:
        if i not in total_vocabulary:
            total_vocabulary[i]=ham_strings[i]

    for i in spam_strings:
        if i not in total_vocabulary:
            total_vocabulary[i]=spam_strings[i]



def main():
    spam_count = 519
    ham_count = 3381
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




create_total_vocabulary()
main()

print(prior_prob_ham_strings,len(prior_prob_ham_strings))
pickle_out_spam = open("pickle_out_prior_spam.pickle", 'wb')

pickle_out_ham = open("pickle_out_prior_ham.pickle", 'wb')

pickle_out_total_vocabulary=open('total_vocabulary.pickle','wb')

pickle.dump(prior_prob_spam_strings, pickle_out_spam)
pickle.dump(prior_prob_ham_strings, pickle_out_ham)

pickle.dump(total_vocabulary,pickle_out_total_vocabulary)

print(prior_prob_spam_strings,len(prior_prob_spam_strings))
