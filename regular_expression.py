import re  #Regular Expression Module

# patterns = ['term1','term2']
# text = 'This is a string with term1. not the other'
#
# for pattren in patterns:
#     print('I am searching for: '+pattren)
#
#     if re.search(pattren,text):
#         print("MATCH!")
#     else:
#         print("NO MATCH!")


# split_term = '@'
# email = 'user@gmail.com'
#
# print(re.split(split_term,email))


#print(re.findall('match','test phase match in match middle'))

#Multi Re findall

def multiRefind(pattren,phase):
    for pat in pattren:
        print("Searching for pattren: {}".format(pat))
        print(re.findall(pat,phase))
        print('\n')

test_phase = 'This is a string! But it has punctuation. How can we remove it?'
#test_pattren = ['sd*']
#test_pattren = ['sd{2,3}']
#test_pattren = ['[^!?]+']
test_pattren = ['[A-Z]+']

multiRefind(test_pattren,test_phase)
