# for x in range(1,481):
#     sentence = "button_"+str(x)+".bind('<Button-1>', left)"
#     sentence2 = "button_"+str(x)+".bind('<Button-3>', right)"
#     print(sentence)
#     print(sentence2)

# button_1.bind('<Button-1>', left)
# button_1.bind('<Button-3>', right)

# import random
# #
#
# board = []
# for row in range(0, 20):
#     board.append([])
#     for column in range(0, 24):
#         board[row].append([])
#
# mineLocations = {}
# # Creates a dictionary of mine locations
# for counter in range(0, 20):
#     mineLocations.update({counter: []})
#
#
# def populateMines(row, column):
#     mineCounter = 99
#     while mineCounter != 0:
#         mineRow = random.randint(0, 19)
#         mineColumn = random.randint(0, 23)
#         if mineColumn not in mineLocations[mineRow]:
#             if mineRow==row:
#                 if mineColumn == column or mineColumn == column +1 or mineColumn == column -1:
#                     pass
#                 else:
#                     board[mineRow][mineColumn] = "Mine"
#                     mineLocations[mineRow].append(mineColumn)
#                     mineCounter -= 1
#             elif mineRow == row-1:
#                 if mineColumn == column or mineColumn == column +1 or mineColumn == column -1:
#                     pass
#                 else:
#                     board[mineRow][mineColumn] = "Mine"
#                     mineLocations[mineRow].append(mineColumn)
#                     mineCounter -= 1
#             elif mineRow == row+1:
#                 if mineColumn == column or mineColumn == column +1 or mineColumn == column -1:
#                     pass
#                 else:
#                     board[mineRow][mineColumn] = "Mine"
#                     mineLocations[mineRow].append(mineColumn)
#                     mineCounter -= 1
#             else:
#                 board[mineRow][mineColumn] = "Mine"
#                 mineLocations[mineRow].append(mineColumn)
#                 mineCounter -= 1
# # abc(z(test_3))
#
# populateMines(10,10)
# for x in board:
#     print(x)

def longestPalindrome(s: str) -> str:
    palindromes = []
    if s == s[::-1]:
        return s

    longest = ""
    for i in range(0, len(s)):
        for j in range(i + 1, len(s) + 1):
            word = s[i:j]
            if word == word[::-1]:
                if len(word) > len(longest):
                    longest = word

    return longest

a = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
print(longestPalindrome(a))