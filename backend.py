import fb
import requests

GRAPH_API_ACCESS_TOKEN = "CAACEdEose0cBAAkAPnrtEChXdmLM6N5ZB5UefjU4FmfdLM0dhpdl1KOve6wjM5ZAg3wCosBJH3hyrxB8OOeinha6KLnZCc8Bzv8vy7FMc9ZBNmnahZCiZAh3TmnEG7ZCfBZBbIGwNHIXWnrtnN6ZAYTYteZBne6z32B1sSiMt6LPt4Su1MHHYilxTx9hICoIpaESaow9yPqpTH0yrimL1n9xHx"

def friendSearch(accessToken):
	url = "https://graph.facebook.com/v2.2/me/friends?access_token=" + accessToken
	resp = requests.get(url)
	print url
	print resp

	

	
	