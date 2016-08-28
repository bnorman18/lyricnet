from lxml import html
import requests
import csv


def getSongLyrics(link, wr):
    page = requests.get(link)
    tree = html.fromstring(page.content)
    whole_song=tree.xpath('//div[@class="lyricbox"]/text()')
    print "This is song is length %d" % len(whole_song)
    for song_line in whole_song:
        wr.writerows([[song_line]])


def getAllArtistLyrics(artist):
    root = 'http://lyrics.wikia.com'
    artist = '/wiki/' + artist

    resultFile = open("songfile.csv",'wb')
    wr = csv.writer(resultFile, dialect='excel')
    page = requests.get(root+artist)
    tree = html.fromstring(page.content)

    for td in tree.xpath('//ol'):
        for song in td.getchildren():

            b = song.getchildren()[0]

            if (len(b.getchildren()) > 0):
                a = b.getchildren()[0]
                if (a != None):
                    href = a.get('href')
                    getSongLyrics(root + href, wr)


def main():
    artist = 'Whiskey_Myers'
    getAllArtistLyrics(artist)

main()
