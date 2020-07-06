import requests
from bs4 import BeautifulSoup

page1 = requests.get('https://www.vocabulary.com/dictionary/abet')
page2 = requests.get('https://www.thesaurus.com/browse/cite?s=t')
page3 = requests.get('https://dictionary.cambridge.org/dictionary/english/abet')
page4 = requests.get('https://www.merriam-webster.com/dictionary/abet')

soup1 = BeautifulSoup(page1.content, 'html.parser')
soup2 = BeautifulSoup(page2.content, 'html.parser')
soup3 = BeautifulSoup(page3.content, 'html.parser')
soup4 = BeautifulSoup(page4.content, 'html.parser')

# print(soup.find_all('a'))
# synonyms = soup.findAll('a', {'class': 'css-18rr30y etbu2a31'})
# synonyms = soup.find_all("a", class_='css-18rr30y etbu2a31')
# synonyms1 = soup.find_all(class_='definition')
# synonyms4 = soup.find_all(class_='sentence')
# synonyms5 = soup.find_all(class_ = 'css-1lc0dpe et6tpn80')
# print(synonyms[0])
# print(synonyms4)
# print(synonyms[0])
# print(synonyms1[0].get_text())

synonyms2 = soup1.find_all(class_='short')
synonyms3 = soup1.find_all(class_='long')
print("Short Description of ABET: ", synonyms2[0].get_text(), "\n", )
print("Brief Description of ABET: ", synonyms3[0].get_text(), "\n", )

syn = soup2.find_all('a', class_='css-18rr30y etbu2a31')
find_syn = [syns.get_text() for syns in syn]
# print(syn[0].get_text())
print("Most relevant Synonyms of ABET: ", find_syn, "\n", )

print("Examples Of ABET: ")

# exmp1 = soup3.find_all(class_='eg deg')
# print(exmp1[0].get_text())
#
examp4 = soup4.find_all(class_='mw_t_sp')
print(examp4[0].get_text())
#
# examp3 = soup1.find_all(class_='sentence')
# print(examp3[0].get_text())

# examp2 = soup4.findAll(True, {'class': ['mw_t_sp', 'ex-sent first-child t no-aq sents']})
# print(examp2[1].get_text())
