class Rohan(object):
    def lengthOfLongestSubstring(self,s):

        start = 0
        maxlength = 0
        used = {}
        
        for curr_pos, char in enumerate(s):
            
            if char in used and start <= used[char]:
                start = used[char]+1
            else:
                maxlength = max(maxlength, curr_pos - start+1)
            
            used[char] = curr_pos
        print(maxlength)
        return maxlength

##Testing the code      
rohan1 = "hgbjghkjhkjlh"

test = Rohan()
test.lengthOfLongestSubstring(rohan1)  