from frequency import sp_characters
from frequency import is_special_character_present
from frequency import get_word

import pandas as pd
import pickle

p_spam_general = 0.13375
p_ham_general = 0.86625

prior_prob_spam = pickle.load(open('pickle_out_prior_spam.pickle','rb'))
prior_prob_ham = pickle.load(open('pickle_out_prior_ham.pickle','rb'))

def union(dict1,dict2):
    list_of_all_words=[]

    for i in dict1:
        if i not in list_of_all_words:
            list_of_all_words.append(i)
    for i in dict2:
        if i not in list_of_all_words:
            list_of_all_words.append(i)

    return list_of_all_words




def main():
    message_count_total = 0
    classified_correct = 0
    accuracy = 0
    df = pd.read_csv('spam.csv', encoding='latin-1')
    count = 0

    list_of_all_words=union(prior_prob_spam,prior_prob_ham)

    for row in df.itertuples():
        prob_message_giv_spam=1
        prob_message_giv_ham=1
        if (count <= 4000):
            count += 1
        else:
            raw_message = row.v2
            #special_characters = is_special_character_present(raw_message)
            words_with_special_char = raw_message.split(' ')
            correct_words_sentence=[]
            for i in words_with_special_char:
                correct_word=get_word(i)
                if(correct_word==None):
                    continue
                else:
                    correct_words_sentence.append(correct_word)

            feature_list={}

            for i in list_of_all_words:
                if i in correct_words_sentence:
                    feature_list[i]=1
                else:
                    feature_list[i]=0


            for i in feature_list:
                if feature_list[i]==1:
                    prob_message_giv_spam*=prior_prob_spam[i]
                else:
                    prob_message_giv_spam*=(1-prior_prob_spam[i])

            for i in feature_list:
                if feature_list[i]==1:
                    prob_message_giv_ham*=prior_prob_ham[i]
                else:
                    prob_message_giv_ham*=(1-prior_prob_ham[i])

            prob_spam_giv_message=(prob_message_giv_spam*p_spam_general)/((prob_message_giv_spam*p_spam_general)+(prob_message_giv_ham*p_ham_general))
            #print(prob_spam_giv_message,row.v1,row.v2)



            if prob_spam_giv_message >.75:#classify spam!
                if(row.v1=='spam'):
                    classified_correct+=1

            else:
                 if(row.v1=='ham'):
                    classified_correct+=1

            message_count_total+=1

    accuracy=classified_correct/message_count_total

    print(accuracy*100,"% Classified Correctly!!!" )

main()











