import requests
from bs4 import BeautifulSoup
import json


def parse_vocabulary_com_examples(word):
    num_of_examples = 4
    word = "debut"
    url = "https://corpus.vocabulary.com/api/1.0/examples.json?query=" + word + "&maxResults=" + str(num_of_examples)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    dictionary = json.loads(str(soup))

    for i in range(0, num_of_examples):
        print("------------------------------------------------------")
        print("name:", dictionary["result"]["sentences"][i]["volume"]["corpus"]["name"])
        print("sentence:", dictionary["result"]["sentences"][i]["sentence"])
        print("datePublished:", dictionary["result"]["sentences"][i]["volume"]["dateAdded"][:10])


parse_vocabulary_com_examples("debut")
