from lxml import html
import requests


def getSongLyrics(link):
    page = requests.get(link)
    tree = html.fromstring(page.content)
    print tree.xpath('//div[@class="lyricbox"]/text()')

def getAllArtistLyrics(artist):
    root = 'http://lyrics.wikia.com'
    artist = '/wiki/' + artist


    page = requests.get(root+artist)
    tree = html.fromstring(page.content)

    for td in tree.xpath('//ol'):
        for song in td.getchildren():

            b = song.getchildren()[0]

            if (len(b.getchildren()) > 0):
                a = b.getchildren()[0]
                if (a != None):
                    href = a.get('href')
                    getSongLyrics(root + href)


def main():
    artist = 'Steely_Dn'
    getAllArtistLyrics(artist)

main()
