from bitstampy import api
import krakenex
import bitfinex
import sys
from decimal import Decimal

TWOPLACES = Decimal(10) ** -2
k = krakenex.API()
orderbook_bitstamp = api.order_book()
length_bitstamp = len(orderbook_bitstamp['bids'])
i = 0

order = Decimal(sys.argv[1])
bankroll_bitstamp = 0
fees_bitstamp = 0


while (i < length_bitstamp):
	price_bitstamp = Decimal(orderbook_bitstamp['bids'][i]['price'])
	volume_bitstamp = Decimal(orderbook_bitstamp['bids'][i]['amount'])
	#print "%s,%s" % (volume,price)
	if (order <= 0):
		break
	else:
		if (volume_bitstamp > order):
			remain = volume_bitstamp - order
			bankroll_bitstamp = bankroll_bitstamp + (price_bitstamp * order)
			fees_bitstamp = fees_bitstamp + (price_bitstamp * order * Decimal(0.005))
			#print 0
			break
		else:
			order = order - volume_bitstamp
			bankroll_bitstamp = bankroll_bitstamp + (price_bitstamp * volume_bitstamp)
			fees_bitstamp = fees_bitstamp + (price_bitstamp * volume_bitstamp * Decimal(0.005))
			#print order
	i = i + 1
