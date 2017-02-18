from lxml import html
import requests
from fnmatch import fnmatch

if __name__ == '__main__':
    '''
    page = requests.get('http://leagueoflegends.wikia.com/wiki/Item#List_of_Items')
    tree = html.fromstring(page.content)
    items = tree.xpath('//span[@class="item-icon tooltips-init-complete"]/a[starts-with(@href, "http://leagueoflegends.'
                       'wikia.com/wiki/")]/text()')
    print ('Items: ', items)
    '''

    #'''
    page = requests.get('http://leagueoflegends.wikia.com/wiki/Void_Staff')
    tree = html.fromstring(page.content)
    item = tree.xpath('//div[@class="pi-data-value pi-font"]//text()')

    #Get the passives for the item
    passive = item[:]
    keep = keep = []
    count = 0
    for i in range(len(passive)):
        keep.insert(i, i + 1)

    stat = 0
    for i in passive:
        if stat == 1:
            stat = 0
        elif fnmatch(i, '+*'):
            stat = 1
        elif fnmatch(i, '*›*'):
            pass
        else:
            for n in keep:
                if n > 0:
                    keep[count] = 0 - count - 1
                    break
        count += 1

    removed = 0
    for n in keep:
        if n > 0:
            del passive[n - 1 - removed]
            removed += 1

    current = 0
    for x in passive:
        if fnmatch(x, '*:'):

        current += 1
    print ('Passive: ', passive)

    #Get the base stats for the item
    '''
    stats = item[:]
    keep = []
    count = 0
    for i in range(len(stats)):
        keep.insert(i, i + 1)

    for i in stats:
        if fnmatch(i, '+*'):
            for n in keep:
                if n > 0:
                    keep[count] = 0 - count - 1
                    keep[count + 1] = 0 - count - 2
                    break
        count += 1

    for n in keep:
        if n > 0:
            while (1):
                try:
                    del stats[n - 1]
                except IndexError:
                    break
            break
    print ('Stats: ', stats)
    '''

    '''
    page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
    tree = html.fromstring(page.content)
    buyers = tree.xpath('//div[@title="buyer-name"]/text()')
    prices = tree.xpath('//span[@class="item-price"]/text()')
    print ('Buyers: ', buyers)
    print ('Prices: ', prices)
    '''