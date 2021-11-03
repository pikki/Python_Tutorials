#
# sq = dict(
# )
#
# for i in range(1,11):
#     sq[i] = i**2
#
# #print(sq)
#
# print({i:i**2 for i in range(1,11)})

s = 'Himalaya'
print(s.count("a"))

dist_s = {}

# for i in range(len(s)):
#     dist_s[s[i]] = s.count(s[i])
# print(dist_s)

# for letter in s:
#     dist_s[letter] = s.count(letter)
# print(dist_s)


print({letter: s.count(letter) for letter in s})


