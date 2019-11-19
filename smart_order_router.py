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

print "** BITSTAMP ** our bankroll is: $%s" % bankroll_bitstamp.quantize(TWOPLACES)
print "** BITSTAMP ** total fees are: $%s" % fees_bitstamp.quantize(TWOPLACES)
bitstamp_takehome = bankroll_bitstamp - fees_bitstamp - Decimal(0.90)
print "** BITSTAMP ** take home is: $%s" % (bitstamp_takehome).quantize(TWOPLACES)

order = Decimal(sys.argv[1])
bankroll_kraken = 0
fees_kraken = 0
orderbook_kraken = k.query_public('Depth',{'pair':'XBTUSD'})
bids = orderbook_kraken['result']['XXBTZUSD']['bids']
length_bids_kraken = len(bids)
i = 0

while (i < length_bids_kraken):
	price_kraken = Decimal(orderbook_kraken['result']['XXBTZUSD']['bids'][i][0])
	volume_kraken = Decimal(orderbook_kraken['result']['XXBTZUSD']['bids'][i][1])
	#print "%s,%s" % (volume,price)
	if (order <= 0):
		break
	else:
		if (volume_kraken > order):
			remain = volume_kraken - order
			bankroll_kraken = bankroll_kraken + (price_kraken * order)
			fees_kraken = fees_kraken + (price_kraken * order * Decimal(0.005))
			#print 0
			break
		else:
			order = order - volume_kraken
			bankroll_kraken = bankroll_kraken + (price_kraken * volume_kraken)
			fees_kraken = fees_kraken + (price_kraken * volume_kraken * Decimal(0.005))
			#print order
	i = i + 1

print "** kraken ** our bankroll is: $%s" % bankroll_kraken.quantize(TWOPLACES)
print "** kraken ** total fees are: $%s" % fees_kraken.quantize(TWOPLACES)
kraken_takehome = bankroll_kraken - fees_kraken - Decimal(0.90)
print "** kraken ** take home is: $%s" % (kraken_takehome).quantize(TWOPLACES)

client = bitfinex.Client()
orderbook_bitfinex = client.order_book('btcusd')
order = Decimal(sys.argv[1])
bankroll_bitfinex = 0
fees_bitfinex = 0
bids = orderbook_bitfinex['bids']
length_bids_bitfinex = len(bids)

while (i < length_bids_bitfinex):
	price_bitfinex = Decimal(orderbook_bitfinex['bids'][i]['price'])
	volume_bitfinex = Decimal(orderbook_bitfinex['bids'][i]['amount'])
	#print "%s,%s" % (volume,price)
	if (order <= 0):
		break
	else:
		if (volume_bitfinex > order):
			remain = volume_bitfinex - order
			bankroll_bitfinex = bankroll_bitfinex + (price_bitfinex * order)
			fees_kraken = fees_bitfinex + (price_bitfinex * order * Decimal(0.005))
			#print 0
			break
		else:
			order = order - volume_bitfinex
			bankroll_bitfinex = bankroll_bitfinex + (price_bitfinex * volume_bitfinex)
			fees_bitfinex = fees_bitfinex + (price_bitfinex * volume_bitfinex * Decimal(0.005))
			#print order
	i = i + 1
