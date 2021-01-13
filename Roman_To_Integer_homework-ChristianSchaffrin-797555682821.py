#Convert Roman numbers to integer values
class romantointeger(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        a = 0
        b = 0
        while a<len(s):
            if a+1<len(s) and s[a:a+2] in roman:
                b+=roman[s[a:a+2]]
                a+=2
            else:
                #print(a)
                b+=roman[s[a]]
                a+=1
        return b

object = romantointeger()
print(object.romanToInt("MMMMCMXCIX"))
print(object.romanToInt("MMMCDXXI"))
print(object.romanToInt("MMCCCXII"))
print(object.romanToInt("CMXLIX"))
print(object.romanToInt("XII"))