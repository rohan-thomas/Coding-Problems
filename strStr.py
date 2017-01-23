class Rohan(object):
    def strStr(self, haystack, needle):

        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                print(i)
                return i
        print("No needle in the haystack!")
        return -1

        
haystack1 = "Arrow"
needle1 = "row"

test = Rohan()
test.strStr(haystack1,needle1)