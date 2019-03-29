import spacy
import random
def mcq(txt,nlp,nlp1):
    PERSON=["Anamika","Anand","Sherlock","George","Kiran"]
    person_type = ["archaeologist", "farmer", "hunter", "hunter gatherer", "shopkeeper", "wholesaler",
                   "wandering herder"]
    animal = ["dog", "sheep", "goat", "cow", "pig", "deer"]
    tools = ["grinding stone", "flour", "pot", "utensil", "medal", "knife", "hand axe", "needles", "money"]
    years = ["12000", "4,500", "3,500", "1200", "3,200", "5,000"]
    place = ["west asia", "southeast asia", "mekong delta", "europe", "satpura", "vindhya", "central india",
             "bhimbetka", "andaman and nicobar islands"]
    state = ["madhya pradesh","rajasthan","maharashtra","bihar","kerala"]
    age = ["stone age", "metal age", "copper age", "bronze age", "paleolithic age", "mesolithic age", "neolithic age"]
    metal = ["copper", "bronze", "tin", "iron","zinc"]
    country = ["india", "egypt", "china", "turkey", "england", "germany", "united states"]
    work = ["hunt", "fish", "persistence hunt", "trade", " shipbuild"]
    names = ["marco polo", "christopher columbus", "vasco da gama", "ferdinand magellan","shivaji maharaj"]
    century = ["17th", "18th", "19th", "20th", "21st"]
    invention = ["car", "flight", "wheel", "locomotive", "electricity"]
    comm = ["printing press", "telephone", "telegraph", "typewriter", "radio", "television", "satellite", "internet",
            "mobile phone"]
    # Civics
    calledc = ["democracy", "directive", "constituency", "political party", "opposition"]
    rights = ["equality", "freedom", "education", "religion", "live"]
    systems = ["legislature", "executive", "judiciary", "constituency", "constitution"]
    posts = ["president", "governor", "prime minister", "chief minister", "mp", "mla"]
    courts = ["high court", "supreme court", "district court", "normal court", "tennis court"]
    sabha = ["parliament", "vidhan sabha", "rajya sabha", "legislative assembly", "lok sabha"]
    # Geography
    calledg = ["latitude", "longitude", "hemisphere", "meridian", "equator", "altitude"]
    direc = ["east", "west", "north", "south", "southeast"]
    direc2 = ["northeast", "northwest", "southeast", "southwest", "east"]
    ctr = ["jakarta", "new york", "africa", "india", 'USA']
    clm_type = ["hot", "humid", "pleasant", "cold", "temperate"]
    clm_2 = ["winter", "summer", "monsoon", "spring", "rainy"]
    global ques
    qu=[]
    ques = ""
    cnt = 1
    doc = nlp1(txt)
    dictn = [person_type, animal, tools, years, place, state, age, metal, country, work, names,
             century, invention, comm, calledc, rights, systems, posts, courts, sabha, calledg, direc,
             direc2, ctr, clm_type, clm_2]
    # print(text1)
    list99 = list(doc.sents)
    # print(list99)
    list98 = []
    # for j in range(len(list99)):
    # if list99[j].isupper():
    # print(list99)
    list98 = []
    ll = 1
    for j in range(len(list99)):
        if str(list99[j]).isupper():
            ll = 1
        else:
            list98.append(list99[j])

    for line9 in list98:
        txt1 = str(line9)
        nounsinsent = []
        tk = ""
        line09 = nlp1(txt1)
        for token in line9:
            # print(token.text,token.tag_,token.lemma_)
            if "NN" in str(token.tag_):
                nounsinsent.append(str(token.lemma_).lower())
                txt1 = txt1.replace(str(token.text), str(token.lemma_).lower())
                tk = tk + str(token.lemma_).lower() + " "
            else:
                if tk != "":
                    tk = tk[0:(len(tk) - 1)]
                if " " in tk:
                    nounsinsent.append(tk)
                tk = ""
                # print(nounsinsent)
        for nouns in nounsinsent:
            fl = 0
            for x in dictn:
                j = 0
                # print("x=",x)
                for y in x:
                    # print("y=",y)
                    if y == nouns:
                        fl = 1
                        break
                    j = j + 1
                if fl == 1:
                    z = x
                    break
            if fl == 1:
                # print(nouns)
                ans = txt1.replace(nouns, "________")
                m = len(z)
                # print(ans)
                ques = str(cnt) + "." + ans + "\n"
                cnt = cnt + 1
                # print(ques)
                number1 = random.randrange(0, 4)
                # print(number1)
                # print(notin,j)
                notin = [j]
                i = 0
                while i < 4:
                    number = random.randrange(0, m)
                    if number in notin:
                        # print(number)
                        i = i - 1
                    else:
                        if i == number1:
                            # print(i+1,".",nouns)
                            ques = ques + str(i + 1) + "." + str(nouns) + "\n"
                        else:
                            # print(i+1,".",z[number])
                            ques = ques + str(i + 1) + "." + str(z[number]) + "\n"
                            notin.append(number)
                    i = i + 1
                # print()
                #ques = ques + "\n"
                # print("Correct answer:",nouns)
                #ques = ques + "Correct answer: " + str(nouns) + "\n"
                # print()
                #ques = ques + "\n"
                # print()
                #ques = ques + "\n"
                qu.append(ques)
                break
        if len(nounsinsent)<3:
            zu=[]
            print("hahaha")
            txt1 = str(line9)
            for ent in line09.ents:
                print(ent.label_)
                if str(ent.label_) == 'PERSON':
                    ans = txt1.replace(str(ent), "________")
                    print(ans)
                    print("hahah")
                    zu.append(str(ent))
                    ques = str(cnt) + "." + ans + "\n"
                    cnt=cnt+1
                    m = len(PERSON)
                    io=0
                    while io<3:
                        numbr=random.randrange(0,m)
                        if PERSON[numbr] not in zu:
                            zu.append(PERSON[numbr])
                            io=io+1
                    numbr=random.randrange(0,4)
                    temp=zu[0]
                    zu[0]=zu[numbr]
                    zu[numbr]=temp
                    print(zu)
                    for x1 in range(0,4):
                        ques = ques + str(x1 + 1) + "." + zu[x1] + "\n"
                    qu.append(ques)
                    break





    return qu

    # print(ques)