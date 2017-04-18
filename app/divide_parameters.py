params = ["Taco", "Bell", "William", "Cannon"]
bubbles = []

def bridge(s1,s2):
    return s1 + " " + s2

def captureBubble(b):

    if len(b) > 1:
        limit = b[len(b)-1]
        start = b[0]
        string = params[b[0]]
        start += 1
        while start <= limit:
            string = bridge(string,params[start])
            start += 1
    else:
        string = params[b[0]]
    return (string)

# print (captureBubble([0]))
# print (captureBubble([0,1]))
# print (captureBubble([0,1,2]))

def captureLeft(b):
    lowest = b[0]
    if lowest == 0:
        return None
    string = params[b[0] - 1]
    lowest -= 1
    while lowest > 0:
        lowest -= 1
        string = bridge(params[lowest], string)
    return (string)

# print (captureLeft([0]))
# print (captureLeft([1,2]))
# print (captureLeft([2,3]))
# print (captureLeft([3]))

def captureRight(b):
    highest = b[len(b) - 1]
    if highest == len(params) - 1:
        return None
    string = params[highest + 1]
    highest += 1
    while highest < len(params) - 1:
        highest += 1
        string = bridge(string, params[highest])
    return (string)

# print (captureRight([0]))
# print (captureRight([1]))
# print (captureRight([2]))
# print (captureRight([3]))


def clean(old):
    new = []
    d = {}
    for e in old:
        if not e in d:
            d[e] = 1
            new.append(e)
    return new

def make_divisions():
    bigL = []
    for i in range (1,len(params)):
        bubbles.append([])
        for j in range(i):
            bubbles[i-1].append(j)

        count = 0
        while bubbles[i-1][len(bubbles[i-1]) - 1] < len(params): #trippy AF while right bubble component hasn't reached past end
            l = []

            if not captureLeft(bubbles[i-1]) == None:
               l.append(captureLeft(bubbles[i-1]))

            l.append(captureBubble(bubbles[i-1]))

            if not captureRight(bubbles[i-1]) == None:
                l.append(captureRight(bubbles[i-1]))

            print(l)
            bigL.append(tuple(l))

            bubbles[i-1] = [k + 1 for k in bubbles[i-1]]
            count += 1

    return clean(bigL)