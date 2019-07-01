#!/usr/bin/python3
import tweepy
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from  nltk.stem import WordNetLemmatizer
from  nltk.corpus   import  stopwords
from textblob import TextBlob
from tkinter import *
import cv2

consumer_key=""
consumer_secret=""
access_key=""
access_secret=""



def print_output(filename):
	root.destroy()
	img=cv2.imread(filename,1)
	cv2.imshow('Polarity',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()	


def get_tweets(keyword):
	#authenticating twitter with consumer key and consumer  secret
	auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
	#setting access token
	auth.set_access_token(access_key,access_secret)
	#connecting bssetting access tokenpi
	api=tweepy.API(auth)
	#number_of_tweets=50
	tweets=api.search(q=keyword,count=10,lang='en')
	tmp=[]
	polarity=[]

	tweets_for_csv=[tweet.text for tweet in tweets]
	for j in tweets_for_csv:
		tmp.append(j)
	#print("Extracted tweets:",tmp)
	#print("####################################")
	for j in tweets:
		analize=TextBlob(j.text)
		check=analize.sentiment
		#print(check)
		polarity.append(analize.sentiment[0])


#working on matplotlib
	for i in range(1,len(polarity)+1):
		if(polarity[i-1]>0):
			plt.bar(i,polarity[i-1],color='b')
		else:
			plt.bar(i,polarity[i-1],color='g')
	plt.xlabel("Number of tweets")
	plt.ylabel("Opinion of the tweet")
	filename= keyword + '_polarity.png'
	plt.savefig(filename, bbox_inches='tight')
	plt.close()	
	print_output(filename)
	

def click():
	keyword=str(topic.get())
	#print(keyword)
	get_tweets(keyword)     #calling the function which actually does sentiment analysis
	
#tkinter module doing the work
if __name__=='__main__':
	root=Tk()
	root.title("Sentimental Analysis")
	root.configure(background="black")
	root.geometry('500x500')
	'''canvas = Canvas(root, width=500, height=500)
	canvas.pack()'''
	l2= Label (root, text="Enter keyword to perform Sentimental Analysis on", bg="black", fg="white", font="none 12 bold").pack()
	topic = StringVar()	
	textentry= Entry(root,textvariable=topic, width=20, bg="white").pack() 
	

#creating submit button

	Button(root, text="SUBMIT", width=6, command=click) .pack()

	root.mainloop()

