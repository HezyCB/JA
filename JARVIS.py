import requests
import json
import random
 
#The main function that will grab a reply
def grab_reply(question):
	#Navigate to the Search Reddit Url
	r = requests.get('https://www.reddit.com/r/AskReddit/search.json?q=' + question + '&sort=relevance&t=all', headers = {'User-agent': 'Chrome'})
	
	answers = json.loads(r.text)	#Load the JSON file
	
	Children = answers["data"]["children"]
 
	ans_list= []
 
	for post in Children:
		if post["data"]["num_comments"] >= 5:	#Greater then 5 or equal  comments
			ans_list.append (post["data"]["url"])
			return "I am JARVIS, how can I assist you? "
	if len(ans_list) == 0:
		return "I do not know"
	
	#Pick A Random Post
	comment_url=ans_list[random.randint(0,len(ans_list)-1)] + '.json?sort=top'	#Grab Random Comment Url and Append .json to end
 
	#Navigate to the Comments
	r = requests.get(comment_url, headers = {'User-agent': 'Chrome'})
	reply= json.loads(r.text)
	
	Children = reply[1]['data']['children']
	
	
	reply_list= []
 
	for post in Children:
		reply_list.append(post["data"]["body"])	#Add Comments to the List
	
	if len(reply_list) == 0:
		return "I do not know"
		
	#Return a Random Comment
	return reply_list[random.randint(0,len(reply_list)-1)]
 
 
 
#Main Loop, Always ask for a question
while 1:
	q=raw_input("I am JARVIS, how ca I assist you? ")
	q=q.replace(" ", "+")	#Replace Spaces with + for URL encoding
	print(grab_reply(q))	#Grab and Print the Reply
