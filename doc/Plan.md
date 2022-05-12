# Plan
***3.20.2022***

## Phase 0:

### End goal:
**Casino Hold'em poker** a way to play Casino Hold'em Poker that allows you to view your cards against
the houses cards.  We want to make this program so that it could easily add features in the future.

### Interface:
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

## Phase 1:
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


## Phase 2:

### User interface class

### Menu Class
```python

```
### Menu Options Class

### Card Printing Class

### Random Number Sort Class

### Hand Class
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
countMatches() # returns the highest number of matches exist in the hand
countSets()    # returns the number of sets in a hand (a two pair would return 2)
checkFlush()      
checkStraight()
checkRoyal()
sortHand()

values = {1:'a',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'j',12:'q',13:'k',14:'a'}
```
```python
def __init__(self, cards):
    cards = cards
    state = { varCards = cards
    flush = False
    straight = False
    royal = False
    matches = 0
    sets = 0 }
    
def __len__(self):
    return len(self.cards)
```



```python
Def determineHand():
    # Royal flush     — flush, ordered, royal cards
    checkFlush()      
    checkStraight()
    checkRoyal()    
    if all thingsare true return the hand and hand type
    
    # Straight flush  — flush, ordered
    # Four of a kind  — matching values 
    # Full house      — matching values 
    # Flush           — flush
    # Straight        — ordered
    # Three of a kind — matching values
    # Two pair        — matching values
    # Pair            — matching values
    # High card       —
```

```python
def isFlush(self):
    suitsCount = {'clubs':0,'spades':0,'hearts':0,'diamonds':0}
    count the suits in the hand
    if there doesnt exits a count >= 5
        return False
    remove the non suited cards
    return True    
```

```python
def checkStraight(self):
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
        assign straightCards to self.state[varCards]
        assign true to isStraight on self
        
```

```python
def sortHand(self):
    sortingHand(self,0)

def sortingHand(self,  i, highCard):
    if i > len(self): return 
    if self[i].getVal() > highCard.getVal():
        newHighCard = self[i] 
        self[i] = highCard
        sortingHand(self, i+1, newHighCard)
```
### Money Class


man this is harder than I thought