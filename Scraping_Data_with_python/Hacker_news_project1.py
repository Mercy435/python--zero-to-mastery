import requests  # helps download the html file
from bs4 import BeautifulSoup  # allows us to use the html and access data
import pprint  # pettyprint an inbuilt module to make print neat

response = requests.get('https://news.ycombinator.com/news')  # to get the info in the site
#print(response) # gives response[200]
# print(response.text) # this give u all the html files in the site
# beautifulsoup helps us parse, converting files from strings to objects that can be manipulated
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)
# print(soup.body)  #gives only the body of the files
# print(soup.body.contents)  # gives the contents in a list
# print(soup.findAll('div'))
# print(soup.findAll('a')) #gives all the links in the page
# print(soup.title) # gives the title of the site
# print(soup.a) # gives the first a tag
# print(soup.find('a')) # gives the first a tag
# print(soup.find(id='score_26923322')) #gives u the class score and id and points
# select helps grab data from soup
# print(soup.select('a')) # selects all the a tabs
# print(soup.select('.score')) # prints the class score, all of the scores, . is for class
# print(soup.select('#score_26922448')) # #is for id

# grab all of the link and title with 100 and above votes
# print(soup.select('.storylink')[0]) # to show the first link
links = soup.select('.storylink')
print(links)

# votes = soup.select('.score') # some links dont have votes, hence it gives an error when looped over,
# so we use subtext
subtext = soup.select('.subtext')


# print(votes[0])
# print(votes[0].get('id'))

def sort_stories_by_votes(hnlist):  # to sort the list
    return sorted(hnlist, key=lambda key: key['vote'], reverse=True)  # since its a dict in a list


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()  # gives the title of the links
        href = links[index].get('href', None)  # href is the id for links on the site, none is default
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            # hn.append(title) to append title
            # hn.append(href) to append href
            if points > 99:
                hn.append(
                    {'title': title, 'link': href, 'vote': points})  # to combine title and ink together use a dict
    #return hn
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))

# note that link is longer than point, cos some links don't have points
# all links have subtext so use it as ur basis
