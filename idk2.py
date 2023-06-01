def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    sIndex = 0
    pIndex = 0
    star = ""
    currentString = ""
    length = max(len(s), len(p))

    secondP = ""

    sIndex = 0
    pIndex = 0
    star = ""
    currentString = ""
    length = len(s)

    for stuff in range(len(p)):
        if stuff+1<len(p):
            if p[stuff+1] == "*":
                if p[stuff] not in s:
                    continue
                star = p[stuff]
                continue
        if star not in s:
            continue
        if p[stuff]!="*":
            secondP+=p[stuff]

    while pIndex < len(p):
        if pIndex == len(p):
            break
        if p[pIndex] == ".":
            currentString += s[sIndex]
            if pIndex + 1 < len(p):
                if p[pIndex + 1] == "*":
                    star = "."
                sIndex += 1
                pIndex += 1
                length -= 1
                continue
        if pIndex + 1 < len(p):
            if p[pIndex + 1] == "*":
                star = p[pIndex]
                pIndex += 1

        if sIndex < len(s):
            if s[sIndex] == star or star == ".":
                currentString += s[sIndex]
                length -= 1

                sIndex += 1
                if pIndex + 1 < len(p):
                    if p[pIndex + 1] == star:
                        pIndex+=1
                elif p[pIndex]!="*":
                    currentString+=s[sIndex]
                    pIndex+=1
                continue
            if s[sIndex] == p[pIndex]:
                currentString += s[sIndex]
                pIndex += 1
                sIndex += 1
                length -= 1
                continue

        if p[pIndex] != "*":
            if p[pIndex] != ".":
                currentString += p[pIndex]
        pIndex += 1

    if p[-1] != s[-1] and p[-1] != "*" and p[-1] != ".":
        return False

    if s == currentString:
        return True
    else:
        return False

s = "abc"
p = "d*a*.b*.c*"
if isMatch(s, p) == True:
    print("Example 0 is correct")


s = "aa"
p = "a"
if isMatch(s, p) == False:
    print("Example 1 is correct")

s = "aa"
p = "a*"
if isMatch(s, p) == True:
    print("Example 2 is correct")


s = "ab"
p = ".*"
if isMatch(s, p) == True:
    print("Example 3 is correct")

s = "mississippi"
p = "mis*is*p*."
if isMatch(s, p) == False:
    print("Example 4 is correct")

s = "aab"
p = "c*a*b"
if isMatch(s, p) == True:
    print("Example 5 is correct")

s = "ab"
p = ".*c"
if isMatch(s, p) == False:
    print("Example 6 is correct")

s = "aaa"
p = "aaaa"
if isMatch(s, p) == False:
    print("Example 7 is correct")


s = "mississippi"
p = "mis*is*ip*."
if isMatch(s, p) == True:
    print("Example 8 is correct")


s = "aaa"
p = "a*a"
if isMatch(s, p) == True:
    print("Example 9 is correct")

s = "aaa"
p = "ab*a*c*a"
if isMatch(s, p) == True:
    print("Example 10 is correct")




















