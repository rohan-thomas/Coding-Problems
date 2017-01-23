class Rohan(object):
    def isAnagram(self,s, t):
            maps = {}
            mapt = {}
            for c in s:
                maps[c] = maps.get(c,0)+1
            for c in t:
                mapt[c] = mapt.get(c,0)+1
            if maps == mapt:
                print("true")
            else:
                print("false")
            return maps == mapt

        
rohan1 = "rohanthomas"
rohan2 = "thomnahoras"

test = Rohan()
test.isAnagram(rohan1,rohan2)