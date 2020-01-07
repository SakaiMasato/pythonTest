#!/usr/bin/env python
# -*- coding: utf-8 -*-

' download cartoon '

__author__ = 'Bob'

import requests, os, logging, bs4, threading

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')


def download(start, end):
    for i in range(start, end):
        url = 'http://xkcd.com/%s' % i
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'lxml')
        images = soup.select('#comic img')
        if len(images) == 0:
            print('...can not find any image...')
        else:
            imageUrl = 'http:' + images[0].get('src')
            logging.info('...Downloading image %s...' % imageUrl)
            image = requests.get(imageUrl)
            res.raise_for_status()
            imageLocalFile = open(os.path.join('xkcdComics', os.path.basename(imageUrl)), 'wb')
            for chunk in image.iter_content(100000):
                imageLocalFile.write(chunk)
            imageLocalFile.close()

    logging.info('... All done...')


def main():
    os.makedirs('xkcdComics', exist_ok=True)  # exist_ok = False, if folder has existed, throw Error.
    start = 100
    end = 110
    threadpools = []
    for i in range(start, end, 5):
        thread = threading.Thread(target=download, args=(i, i + 4))
        threadpools.append(thread)
        thread.start()
    for t in threadpools:
        t.join()
    print('Done!')


if __name__ == '__main__':
    main()
