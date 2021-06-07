from typing import Text
from bs4.element import PageElement
import requests
from bs4 import BeautifulSoup


def get_site(url):
    return requests.get(url).text


def parse_site(page):
    result = ''
    soup = BeautifulSoup(page, 'lxml')

    result += soup.find('h1').next

    text = (soup.find(id='arrticle').contents)
    trash = ['<div']
    for strin in text:
        strin = str(strin).replace('<p>','\n')
        strin = strin.replace('</p>','\n')
        if strin.find('<em>') > 0:
            strin = strin.replace('<em>', '')
            strin = strin.replace('</em>', '')
        if strin.find('<strong>') > 0:
            strin = strin.replace('<strong>', '')
            strin = strin.replace('</strong>', '')
        if strin.find('<br>') > 0 or strin.find('</br>') or strin.find('<br/>'):
            strin = strin.replace('<br>', '\n')
            strin = strin.replace('</br>', '\n')
            strin = strin.replace('<br/>', '\n')
        if strin.find('<div') == -1:
            result += strin
    return result

def parse_next(page):
    result = ''
    soup = BeautifulSoup(page, 'lxml')
    result = soup.find(id='next')['href']
    return str(result)


def parse_prev(page):
    result = ''
    soup = BeautifulSoup(page, 'lxml')
    result = soup.find(id='prev')['href']
    return str(result)




def main(url, option='text'):
    page = get_site(url)
    if 'https://ranobes.com/chapters/' in url and option == 'text':
        return parse_site(page)
    
    if 'https://ranobes.com/chapters/' in url and option == 'next':
        return parse_next(page)

    if 'https://ranobes.com/chapters/' in url and option == 'prev':
        return parse_prev(page)

#print(main('https://ranobes.com/chapters/you-called-on-the-wrong/244254-1.html', 'next'))