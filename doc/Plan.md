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

### Calculate Hands Class
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
isFlush()      
isStraight()
isRoyal()
sortHand()

Def determineHand():
If (isRoyal, isFlush, isStraight) return "royal flush"



elif (isflush, isStraight) return "straight flush"
elif(countMatches == 4) return "four of a kind"
elif(countMatches == 2 and countMatches == 3) return "full house"
elif(isFlush) return "flush"
elif(isStraight) return "straight"
elif(countMatches == 3) return "three of a kind"
elif(countSets == 2 and countMatches == 2) return "two pair"
elif(countMatches == 2) return "pair"
else return "high card"
```

```python
def isFlush(hand):
    suitsCount = {'clubs':0,'spades':0,'hearts':0,'diamonds':0}
    count the suits in the hand
    if there doesnt exits a count >= 5
        return (False,-1)
    store the suited cards in a list
    sort the cards using sortHand()
    return (True, sortedHand)
```
### Money Class


man this is harder than I thought