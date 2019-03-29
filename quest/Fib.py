def fib(txt,nlp):
    ques=""
    qu=[]
    doc = nlp(txt)
    list1 = list(doc.sents)
    ans = ""
    c = -1
    k = 1
    for x in list1:
        line = str(x)
        line09 = nlp(line)
        c = c + 1
        ans=""
        if "means" in line:
            l = line.split('means')
            m = nlp(l[1])
            for token in m:
                ques = "______ means" + str(m)
                # print(str(k)+") "+ques)
                ans = ans+ str(k) + ") " + ques + '\n'
                k = k + 1
                break
        elif "called" in line:
            b = 0
            l = line.split("called")
            m = nlp(l[0])
            for token in m:
                ques = str(m) + " called______."
                ques = nlp(ques)
            for token in ques:
                if str(token.tag_) == 'NN' or str(token.tag_) == 'JJ':
                    b = 1
                    break
            if b == 1:
                # print(str(k)+") "+str(ques))
                ans = ans + str(k) + ") " + str(ques) + '\n'
                k = k + 1
        else:
            for e in line09.ents:
                if str(e.label_) == 'LAW':
                    line = line.replace(e.text, "________")
                    # print(str(k)+") "+line)
                    for token in nlp(line):
                        if str(token.text) == "this" or str(token.text) == "these" or str(
                                token.text) == "that":
                            line = str(list1[c - 1]) + line
                    # print(str(k)+") "+line)
                    ans = ans + str(k) + ") " + line + '\n'
                    k = k + 1
                    break
                elif str(e.label_) == 'DATE':
                    line = line.replace(e.text, "________")
                    # print(str(k)+") "+line)
                    for token in nlp(line):
                        if str(token.text).lower() == "this" or str(token.text).lower() == "these" or str(
                                token.text).lower() == "that":
                            line = str(list1[c - 1]) + line
                    # print(str(k)+") "+line)
                    ans = ans + str(k) + ") " + line + '\n'
                    k = k + 1
                    break
                elif str(e.label_) == 'PERSON':
                    line = line.replace(e.text, "________")
                    # print(str(k)+") "+line)
                    for token in nlp(line):
                        if str(token.text).lower() == "this" or str(token.text).lower() == "these" or str(
                                token.text).lower() == "that":
                            line = str(list1[c - 1]) + line
                    # print(str(k)+") "+line)
                    ans = ans + str(k) + ") " + line + '\n'
                    k = k + 1
                    break
                else:
                    line = line.replace(e.text, "________")
                    # print(str(k)+") "+line)
                    for token in nlp(line):
                        if str(token.text).lower() == "this" or str(token.text).lower() == "these" or str(
                                token.text).lower() == "that":
                            line = str(list1[c - 1]) + line
                    # print(str(k)+") "+line)
                    ans = ans + str(k) + ") " + line + '\n'
                    k = k + 1
                    break
        if ans!="":
            qu.append(ans)
    # print(ans)
    return qu