import string

# from itertools import cycle

all_alpha = list(string.ascii_lowercase)
print(all_alpha)


def crypto(s, shift):
    slist = list(s)
    for i in range(len(slist)):
        if slist[i] in all_alpha:
            updated_i = all_alpha.index(slist[i]) + shift
            slist[i] = all_alpha[updated_i % 26]
    return ''.join(slist)


#print(crypto('cat is 8', -1))

en_de =1
while(en_de) :
    en_de = input("\nDo you wish to encode or decode? \n 1 to encode \n 2 to decode \n 0 to exit : ")
    if en_de.isnumeric():
        #encode
        if(int(en_de) == 1):
            en_input = input("\nEnter the string:")
            en_shift = int(input("\nEnter the shift:"))
            print(crypto(en_input, en_shift))
        #decode
        elif (int(en_de) ==2):
            de_input = input("\nEnter the string:")
            de_shift = int(input("\nEnter the shift:"))
            print(crypto(de_input, -de_shift))
        elif (int(en_de) == 0):
            break
    else :
        #print(en_de)
        print("option invalid")

