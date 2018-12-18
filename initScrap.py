import requests
import bs4


def grabEmail(url):

    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    x = ''
    for i in soup.find_all('a', href=True):
        if i['href'].find('@') != -1:
            x = i['href']
    s = x.split('@')
    counter = 0
    for i in s[0]:
        if not i.isalpha():
            if not i.isdigit():
                s[0] = s[0][counter + 1:]

        counter += 1
    if len(s) != 1:
        x = s[0] + '@' + s[1]
    return x
