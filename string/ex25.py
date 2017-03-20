def ceaser_encrypt(realtext,step):
    outtext=[]

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

    for eachletter in realtext:
        if eachletter in uppercase:
            index = uppercase.index(eachletter)
            cry_index = (index + step) % 26
            outtext.append(uppercase[cry_index])
        elif eachletter in lowercase:
            index = lowercase.index(eachletter)
            cry_index = (index + step) % 26
            outtext.append(lowercase[cry_index])
        else:
            outtext.append(eachletter)
    return outtext

realtext=" In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence."

code=ceaser_encrypt(realtext,5)
print ()
print ('' .join(code))
print ()