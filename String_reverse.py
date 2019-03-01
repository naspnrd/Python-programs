#string Reversal using slicing trick

string = 'neerajChaudhary'
##
##for i in string[::-1]:
##    print(i)

#using reversal and str.join()

##for element in reversed(string):
##    print(element)

#using both

print("".join(reversed(string)))

#The “Classic” In-Place String Reversal Algorithm Ported to Python
def reverse_string3(string):
    ##"""Return a reversed copy of `string`"""
    chars = list(string)
    for i in range(len(string)):
        tmp = chars[i]
        chars[i] = chars[len(string) - i - 1]
        chars[len(string) - i - 1] = tmp
    return ''.join(chars)

