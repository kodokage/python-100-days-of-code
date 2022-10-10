auction = {}

is_auction = True

while is_auction:
    bidder_name = input('Enter your name : ').lower()

    bid = int(input('Enter your bid : '))

    auction[bidder_name] = bid

    another_bid = input('Another Bid : ')
    if another_bid == 'no':
        is_auction = False

print(auction)