'''
Copyright (C) 2017-2019  Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from cryptofeed.backends.mongo import TradeMongo, BookDeltaMongo, BookMongo
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Coinbase

from cryptofeed.defines import TRADES, L2_BOOK, BOOK_DELTA


def main():
    """
    Because periods cannot be in keys in documents in mongo, the bids and asks dictionaries
    are converted to BSON. They will need to be decoded after being read
    """
    f = FeedHandler()
    f.add_feed(Coinbase(max_depth=10, channels=[L2_BOOK],
                        pairs=['BTC-USD'],
                        callbacks={TRADES: TradeMongo('coinbase', collection='trades'),
                                   L2_BOOK: BookMongo('coinbase', collection='l2_book'),
                                   BOOK_DELTA: BookDeltaMongo('coinbase', collection='l2_book')}))

    f.run()


if __name__ == '__main__':
    main()
