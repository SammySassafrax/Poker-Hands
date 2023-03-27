#!/home/pi/software/bin/python3

import cgi, cgitb
import subprocess

def findCategory(cards) :
    chosen = ""
    if isHighCard(cards):
        chosen = "High Card"
    elif isOnePair(cards):
        chosen = "One Pair"
    elif isTwoPair(cards):
        chosen = "Two Pair"
    elif isThreeOfAKind(cards):
        chosen = "Three Of A Kind"
    elif isStraight(cards):
        chosen = "Straight"
    elif isFlush(cards):
        chosen = "Flush"
    elif isFullHouse(cards):
        chosen = "Full House"
    elif isFourOfAKind(cards):
        chosen = "Four Of A Kind"
    elif isStraightFlush(cards):
        chosen = "Straight Flush"
    return chosen

def isHighCard(cards) :
    if not (isOnePair(cards) or isTwoPair(cards) or isThreeOfAKind(cards) or isStraight(cards) or isFlush(cards) or isFullHouse(cards) or isFourOfAKind(cards) or isStraightFlush(cards)):
        return True

def isOnePair(cards) :
    x = 0
    rank = [i[0] for i in cards]
    rankTypes = set(rank)

    for i in rankTypes:
        if rank.count(i) == 3:
            x = 1

    pairs = [i for i in rankTypes if rank.count(i) == 2]

    if len(pairs) != 1 or x == 1:
        return False

    return True

def isTwoPair(cards) :
    rank = [i[0] for i in cards]
    rankTypes = set(rank)

    pairs = [i for i in rankTypes if rank.count(i) == 2]

    if len(pairs) != 2:
        return False

    return True

def isThreeOfAKind(cards) :
    rank = [i[0] for i in cards]
    rankTypes = set(rank)

    if len(rankTypes) != 3:
        return False
    for i in rankTypes:
        if rank.count(i) == 3:
            return True

    return False

def isStraight(cards) :
    dict = []
    rank = [i[0] for i in cards]

    if isStraightFlush(cards) == True:
        return False

    for i in range (5):
        if rank[i] == "t":
            temp = 10
            dict.append(temp)
        elif rank [i] == "j":
            temp = 11
            dict.append(temp)
        elif rank [i] == "q":
            temp = 12
            dict.append(temp)
        elif rank [i] == "k":
            temp = 13
            dict.append(temp)
        elif rank [i] == "a":
            temp = 14
            dict.append(temp)
        elif isinstance(rank[i], str):
            temp = int(rank[i])
            dict.append(temp)
        else:
            dict.append(rank[i])

    ordered = sorted(dict, reverse = True)

    if ordered[0] == 14 and ordered[1] == 5:
        for i in range (3):
            if ordered[i+1] - ordered[i+2] != 1:
                return False
    else:
        for i in range (4):
            if ordered[i] - ordered[i+1] != 1:
                return False

    return True

def isFlush(cards) :
    rank = [i[1] for i in cards]

    if isStraightFlush(cards) == True:
        return False

    if len(set(rank)) != 1:
        return False

    return True

def isFullHouse(cards) :
    rank = [i[0] for i in cards]
    rankTypes = set(rank)

    pairs = [i for i in rankTypes if rank.count(i) == 2]

    for i in rankTypes:
        if rank.count(i) == 3:
            x = 1

    if len(pairs) == 1 and x == 1:
        return True

    return False

def isFourOfAKind(cards) :
    rank = [i[0] for i in cards]
    rankTypes = set(rank)

    if len(rankTypes) != 2:
        return False
    for i in rankTypes:
        if rank.count(i) == 4:
            return True

    return False

def isStraightFlush(cards) :
    dict = []
    rank = [i[0] for i in cards]
    rankOther = [i[1] for i in cards]

    if len(set(rankOther)) != 1:
        return False

    for i in range (5):
        if rank[i] == "t":
            temp = 10
            dict.append(temp)
        elif rank [i] == "j":
            temp = 11
            dict.append(temp)
        elif rank [i] == "q":
            temp = 12
            dict.append(temp)
        elif rank [i] == "k":
            temp = 13
            dict.append(temp)
        elif rank [i] == "a":
            temp = 14
            dict.append(temp)
        elif isinstance(rank[i], str):
            temp = int(rank[i])
            dict.append(temp)
        else:
            dict.append(rank[i])

    ordered = sorted(dict, reverse = True)

    if ordered[0] == 14 and ordered[1] == 5:
        for i in range (3):
            if ordered[i+1] - ordered[i+2] != 1:
                return False
    else:
        for i in range (4):
            if ordered[i] - ordered[i+1] != 1:
                return False
    return True

def piInfo():
    print(subprocess.check_output("date", shell=True, text=True) + "<br/>")
    print(subprocess.check_output("ps ax | grep nginx", shell=True, text=True) + "<br/>")
    print(subprocess.check_output("uname -a", shell=True, text=True) + "<br/>")
    print(subprocess.check_output("cat /sys/class/net/eth0/address", shell=True, text=True) + "<br/>")
    print(subprocess.check_output("cat /proc/cpuinfo | tail -5", shell=True, text=True) + "<br/>")
    print(subprocess.check_output("ifconfig | grep netmask", shell=True, text=True) + "<br/>")

def main():
    cgitb.enable( )

    form = cgi.FieldStorage( )
    cards = form.getvalue('cards')
    numOfCards = len(cards)

    print("Content-type: text/html\n\n")

    print("<html>")
    print("<head>")
    print("<title>Python Hand Analyzer</title>\n")
    print("</head>")
    print("<body>")
    if numOfCards != 5:
        print("You need 5 cards, you have ")
        print(numOfCards)
    else:
        for i in range (5):
            temp = cards[i]+".png"
            print("<img src= cards/+temp>")
        print("<br/>")
        print(sorted(cards))
        print("<br/>")
        print("Your poker hand is a " + findCategory(cards))
        print("<br/>")
        print("<br/>")
        print("<br/>")
        piInfo()

    print("</body>")
    print("</html>")


if __name__ == "__main__" :
   main( )
