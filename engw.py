e = {
    "I want to decorate my room with flowers" : "나는 내 방을 꽃으로 장식하고싶다",
    "Let me have the check please" : "계산서를 확인하겠습니다",
    "He is always complaining" : "그는 언제나 불평한다",
    "New yorkers built their city on a grand scale" : "뉴욕 사람들은 그들의 도시를 웅장하게 지었다.",
    "We are sorry for the inconvenience" : "불편함에 죄송함을 표합니다",
    "It soon became popular thanks to its innovative design" : "이것의 혁신적인 디자인 덕분에 곧 유명해졌다",
    "He has been working as a manager at this restaurant" : "이 식당에서 그는 관리자로 일해왔다",
    "She was put in charge of the matter" : "그녀는 이 문제의 책임을 맡게되었다",
    "The new restaurant put up a bright and colorful sign" : "새 식당은 밝고 화려한 사인을 내걸었다",
    "Do you have a reason for being so late?" : "늦은 이유가 있나요?",
    "I'm not satisfied with the steak" : "스테이크에 만족하지 않습니다",
    "It is hard to cook five servings of food all at once" : "한번에 5인분을 요리하는 것은 어렵다.",
    "I usually eat two slices of bread every morning" : "나는 주로 두 조각의 빵을 매일 먹는다",
    "You will take charge of the company" : "당신은 회사를 책임지게 될 것 입니다",
    "To stop fire, We need to get the oil out of the tank" : "불을 막기 위해서 탱크의 기름을 빼내야 합니다",
    "This place is open throughout the year" : "이곳은 연중무휴입니다.",
    "Unfortunately, I have no money with me" : "안타깝게도, 저에게는 돈이 없습니다."
}

i = 0
while True:
    for ex, t in e.items():
        correct = ex
        print(t)
        if(correct.upper() == input().upper()):
            i+=1
            print("passed {}".format(i))
        else:
            print(correct)
            