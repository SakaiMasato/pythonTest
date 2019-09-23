#!/usr/bin/env python
# -*- coding: utf-8 -*-

' download cartoon '

__author__ = 'Bob'

import requests, os, logging, bs4

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')


def download():
    url = 'http://xkcd.com'
    os.makedirs('xkcdComics', exist_ok=True)  # exist_ok = False, if folder has existed, throw Error.
    while not url.endswith('#'):
        logging.info('...Downloading %s...' % url)
        res = requests.get(url)
        try:
            res.raise_for_status()
        except Exception as e:
            logging.error('there is something error: %s' % e)

        soup = bs4.BeautifulSoup(res.text, 'lxml')
        images = soup.select('#comic img')
        if len(images) == 0:
            logging.info('...can not find any image...')
        else:
            imageUrl = 'http:' + images[0].get('src')
            logging.info('...Downloading image %s...' % imageUrl)
            image = requests.get(imageUrl)
            try:
                res.raise_for_status()
            except Exception as e:
                logging.error('there is something error: %s' % e)

            imageLocalFile = open(os.path.join('xkcdComics', os.path.basename(imageUrl)), 'wb')
            for chunk in image.iter_content(100000):
                imageLocalFile.write(chunk)
            imageLocalFile.close()
            prevLink = soup.select('a[rel="prev"]')
            url = 'http://xkcd.com' + prevLink[0].get('href')
    logging.info('... All done...')


if __name__ == '__main__':
    download()
