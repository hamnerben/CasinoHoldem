# Plan
***3.20.2022***

# Phase 0:

## End goal:
**Casino Hold'em poker** a way to play Casino Hold'em Poker that allows you to view your cards against
the houses cards.  We want to make this program so that it could easily add features in the future.
## Interface:
```
Welcome to Casino Hold'em
  N - New game
  X - Exit 
>
```
```
Current Balance: $x.xx
Enter an ante amount [$1 - $x]:
>
```
```
                 _____________________
                |Royal Flush    |100:1|
                |Straight Flush |20:1 |
                |Four of a Kind |10:1 |
=======         |Full House     |3:1  |
 House          |Flush          |2:1  |
=======         |_______________|_____|
 _____   _____   _____   _____   _____
|A .  | |A .  | |A .  | |\ ~ /| |\ ~ /|
| /.\ | | /.\ | | /.\ | |}}:{{| |}}:{{|
|(_._)| |(_._)| |(_._)| |}}:{{| |}}:{{|
|  |  | |  |  | |  |  | |}}:{{| |}}:{{|
|____V| |____V| |____V| |/_~_\| |/_~_\|

====== 
 Hand          
======
 _____   _____ 
|A .  | |A .  |
| /.\ | | /.\ |
|(_._)| |(_._)|
|  |  | |  |  |
|____V| |____V|
___________________
ante: $x
    to call: ~$2x~
balance: $bal
Call $2? (y)es, (n)o, or (q)uit
>
```

# Phase 1:
* User Interface Class
* A Menu Class
* A Menu Options Class
* A card printing class
* Random Number Sort class
* Calculate Hands Class
  * will determine hand
  * will calculate winner
* Money class
  * store balance and ante info
  * algorithm for betting etc


# Phase 2:

## User interface module
0. `Welcome to Casino Hold'em`
   1. `N - New game`
   2. `X - Exit`
1. `Enter an ante amount [$1 - $x]:`
2. forever loop:
   1. `(c)all or (f)old`
   2. `(c)ontinue, new (a)nte, or (q)uit`
     
## Prompt Class
```python
def __init__(self, chCommands, prompt):
    self.chCommands = chCommands
    self.prompt = prompt
```

```python
def prompt(self):
    # keep looping
    # check if input is valid
    # if so return the command inputed
    # otherwise throw a message and keep looping
```

## Card Printing module
the main print cards function will accept a list of cards to print
and the method will print the cards side by side.

The method will need to add whitespace on each line that doesn't measure
up to be as long as the longest line.

```python
def printCards(ls):
    find the greatest card length
    for loop range the greatest length
        for loop each card and find the maxLineLength
        for loop each card and print the index line checking for out of bounds
```

## Card Class
```python
def __init__(self, value, suit):
    self.val = value
    self.suit = suit
    self.used = False
```
## Deck Class

* `card(n)`
* `shuffleDeck()`

```python
def __init__(self):
    cards = []
    for s in SUIT_LIST:
        for v in VAL_LIST:
            cards.append(Card(v, s))
```

I am just going to make a list of cards and use `random.shuffle(list)`

## Hand Class
```markdown
==========================================
~ PARSING THE REQUIREMENTS FOR THE HANDS ~
==========================================
Royal flush     — flush, ordered, royal cards
Straight flush  — flush, ordered
Four of a kind  — matching values 
Full house      — matching values 
Flush           — flush
Straight        — ordered
Three of a kind — matching values
Two pair        — matching values
Pair            — matching values
High card       —
```

```python
# Private methods:
countSets() 
checkFlush()      
checkStraight()
checkRoyal()
sortHand()
rstIndicators()

# getters
getHandName()
getCards()

values = {1:'a',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'j',12:'q',13:'k',14:'a'}
```
```python
def __init__(self, cards):
    __cards = cards  # shouldn't be changed
    tempCards = cards
    flush = False
    straight = False
    royal = False
    topSetSize = 0
    sets = 0
    handName = self.determineHand()
    
def __len__(self):
    return len(self.cards)
```



```python
def determineHand(self):
"""determines and returns the hand name"""
    # Royal flush     — flush, ordered, royal cards
    self.sort()
    checkFlush()      
    checkStraight()
    checkRoyal()    
    if all thingsare true return the hand and hand type
    
    # Straight flush  — flush, ordered
    # Four of a kind  — matching values 
    rstIndicators()
    countSets()
    if topSetSize >= 4 return the hand and hand type
    # Full house      — matching values 
    if topSetSize 
    # Flush           — flush
    # Straight        — ordered
    # Three of a kind — matching values
    # Two pair        — matching values
    # Pair            — matching values
    # High card       —
```

```python
def checkFlush(self,cards):
  """if exists >= 5 suited cards
  stores True on hand for flush
  and puts suited cards in tempCards"""
    suitsCount = {'clubs':0,'spades':0,'hearts':0,'diamonds':0}
    count the suits in the hand
    if there doesnt exits a count >= 5
        set flush to False
    remove the non suited cards
    set flush to True    
```

```python
def checkStraight(self,cards):
  """if straight of >=5 cards exists
  stores them in tempCards
  sets straight to True"""
    cnt = 0
    straight = False
    straightCards = []
    two&Ace = False
    for while loop fowrads
        add current card to 
        if 'a' then check for '2'
        if ordred >= 5 straight is True
        if next card is adjacent increment cnt and check for 2
        elif not straight: reset cnt and reset cardsList and reset two&Ace
        else: exit loop # the next card is not in sequence but >= 5 cnt
    if straight: 
        assign straightCards to self.state[tempCards]
        assign true to isStraight on self
        
```

```python
def checkRoyal(self,cards):
  '''sets cardsVal in self to only royal cards
  sets royal to true'''
    royalCards = []
    royalCnt = {'a':0,'k':0,'q':0,'j':0,'10':0}
    for card in hand:
        check for royal and add it to cnt
    if there is at least 1 of each royal card
        set royal to true and update tempCards
```
sometimes will want to use to check `__cards` sometimes will want
to use on `tempCards` for that reason a hand is passed in.


```python
def countSets(self):
  '''counts the sets and set size in the hand
  stores set count in hand dict
  stores highest match number in hand
  stores the cards ordered from highest set size in tempCards'''
    valCnts = {all the vals = 0}
    sets = 0
    cards = []
    for card in hand:
        increment valCnt for the cards val
      
    for card in hand:
        if valCnt for val >= 3 store that card mark as used
    for card in hand:
        if valCnt > 1 and not used: store that card and mark as used
    for card in hand:
        store the rest of the unmarked cards after the others
    topCnt = 0
    for valCnt in valCnts:
        get highest val
        count the sets
    store topCnt
    store sets
    store cards in tempCards
    unmark the cards in hand
```
**What Happens with bad input?**
* This method only works if the hand is passed in ordered.

The above `countSets()` method will store any sets first in `tempCards` and
the remaining cards after.  The previous `flush()` and `straight()` methods
will automatically store at least 5 cards so I initailly didn't think to store
the extra cards. **TODO: implement that, I don't want to redesign it right now**

```python
def sortHand(self):
  """Sorts the cards in the hand
  'a' is set as highest"""
    sortingHand(self,0)

def sortingHand(self,  i, highCard):
    if i > len(self): return 
    if self[i].getVal() > highCard.getVal():
        newHighCard = self[i] 
        self[i] = highCard
        sortingHand(self, i+1, newHighCard)
```
## Balance Class

* `getBal()`
* `getAnte()`
* `setAnte()`
* `payAnte()`
* `won(handName)`
* `lost()`

```python
def __init__(self, ante):
    self.ante = ante
    self.balance = BALANCE
```

```python
def won(self, handName):
    """determines amount earned based on winning hand,
    adds said amount to object's balance"""
    # lookup the ratio based on the handName
    # multiply it to the ante
    # add the amount to the object's balance
```