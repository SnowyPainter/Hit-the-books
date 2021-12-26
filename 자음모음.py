class Consonant:
    def __init__(self, c, where, how, isringing):
        self.c = c
        self.where = where
        self.how = how
        self.isring = isringing
    def data(self):
        str = "안울림 소리"
        if(self.isring == True):
            str = "울림 소리"
        
        return {
            "자음" : self.c,
            "울림" : str,
            "장소" : self.where,
            "방식" : self.how
        }

cs = {'ㄱ':['연구개음','파열음'], 'ㄷ':['잇몸소리', '파열음'], 'ㅂ':['입술소리','파열음'],
     'ㅈ':['경구개음', '파찰음'], 'ㅇ':['연구개음', '비음'], 'ㅎ':['목청소리', '마찰음'], 
     'ㄴ':['잇몸소리', '비음'], 'ㄹ':['잇몸소리', '유음'], 'ㅁ':['입술소리', '비음'], 'ㅅ':['잇몸소리', '마찰음']}
rs = ['ㄴ', 'ㄹ', 'ㅁ', 'ㅇ']



consonants = []
for k, c in cs.items():
    t = k in rs
    a = Consonant(k, c[0], c[1], t) 
    consonants.append(a)

for c in consonants:
    print(c.data())