# Bounded context
Poker engine 

# Description
A mechanism that allows users to emulate a process of various poker games:
- Hold'em
- Omaha
- etc.

# Ubiquitous language
- `Deck` - an ordered set of unique cards
- `Card` - a playing card which can be identified by it's rank and suit (e.g. ace of spades, trey of diamonds)
- `Suit` - a card's suit (spades, hearts, diamonds, clubs)
- `Rank` - a card's rank (ace, king, ..., trey, deuce)


- `Round` - a single game episode
- `Street` - a certain stage of the game with ability to deal board or pocket cards, draw cards and players' action 
- `Table` - an ordered set of unique players
- `Board` - a set of community cards on the table (all cards are open)
- `Pocket` - a set of player's cards (can contain hole and open cards)
- `Hand` - a set of cards which represents a combination of certain power depending on the game type 
- `Player` - a game participant with certain amount of chips which can be identified by his nickname
- `Decision` - a player's decision in the certain moment of the game (fold, check, call, bet, raise)
- `Pot` - chips which players are gave to dealer
- `Dealer` - a person who controls the game
- `Event` - a certain event during the round
