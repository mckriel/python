print('''
         d8b 888                   888                                   888    d8b                   
         Y8P 888                   888                                   888    Y8P                   
             888                   888                                   888                          
.d8888b  888 888  .d88b.  88888b.  888888      8888b.  888  888  .d8888b 888888 888  .d88b.  88888b.  
88K      888 888 d8P  Y8b 888 "88b 888            "88b 888  888 d88P"    888    888 d88""88b 888 "88b 
"Y8888b. 888 888 88888888 888  888 888        .d888888 888  888 888      888    888 888  888 888  888 
     X88 888 888 Y8b.     888  888 Y88b.      888  888 Y88b 888 Y88b.    Y88b.  888 Y88..88P 888  888 
 88888P' 888 888  "Y8888  888  888  "Y888     "Y888888  "Y88888  "Y8888P  "Y888 888  "Y88P"  888  888 
                                                                                                      
''')

bid_entry = {}
bidding_closed = False

def add_bid():
    bid_name = input('Please input your name: ')
    bid_price = int(input('Please input your bid price: '))
    bid_entry[bid_name] = bid_price

def highest_bid(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            bid_amount = highest_bid
            winner = bidder
    print(f'The winner of the auction is {winner} with an auction amount of {highest_bid} :)')


while not bidding_closed:
    add_bid()
    bid_complete = input('Are there any other people who would like to bid? (y/n) ')

    if bid_complete == 'n':
        break
        # bidding_closed == True

highest_bid(bid_entry)