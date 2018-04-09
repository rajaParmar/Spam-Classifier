import pandas as pd



def main():
	df=pd.read_csv('spam.csv',encoding='latin-1')
	count=0
	spam_counter=0
	for row in df.itertuples():
		if(count>4000):
			break

		if(row.v1=='spam'):
			spam_counter+=1

		count+=1

	print("Prob Spam Overall: ",spam_counter/4000," Ham Overall: ",1-(spam_counter/4000))

main()
