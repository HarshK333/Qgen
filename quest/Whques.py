import spacy
import random
def wh(txt,nlp,nlp1):
    ques=""
    qu=[]
    doc1=nlp(txt)
    doc3= doc1._.coref_resolved
    txt = str(doc3)
    doc=nlp(txt)
    list1 = list(doc.sents)
    c = -1
    k = 1
    for x in list1:
        ans=""
        line = str(x)
        # print(line)
        line09 = nlp1(line)
        line0=str(x)
        cnt = 0
        cnta = 0
        cntb = 0
        cntc = 0
        cntd = 0
        c = c + 1
        if ":" in line:
            l = line.split(':')
            m = nlp(l[0])
            for token in m:
                if (token.tag_ == "VBP"):
                    b = str(token.text)
                    n = str(m).split(b)
                    ques = "Q)" + "What " + b + " " + n[0].lower() + n[1] + '?'
                    q = nlp(ques)
                    for t in q:
                        if str(t.tag_) == "NN":
                            b = 1
                            break
                    if b == 1:
                        # print(str(k)+") "+ques)
                        ans = ans + "Q)" + ques + '\n'
                        k = k + 1
                        break
        elif "when" in line:
            l = line.split('when')
            line1 = nlp1(str(l[0]))
            print(str(l[0]))
            h = ""
            for token in line1:
                # print(token.text,token.dep_)
                if "aux" in str(token.dep_):
                    h = h + token.text
                    break
            if h != "":
                m = str(line1).split(h)
                ques = 'When' + ' ' + h + ' ' + m[0].lower() + m[1] + '?'
            else:
                ques = 'When' + ' ' + str(line1) + '?'
            # print(str(k)+") "+ques)
            ans = ans + "Q)"+ ques + '\n'
            k = k + 1
        elif "because" in line.lower():
            l = line.lower().split('because')
            line1 = nlp1(str(l[0]))
            h = ""
            if str(l[0]) == " ":
                l1 = line.split(',')
                m = nlp1(str(l1[1]))
                for token in m:
                    if str(token.tag_) == "DT":
                        n = str(m).split(str(token.text))
                        n[1] = n[1].replace(n[1][-1], '?')
                        ques = "Which" + "" + n[1].lower()
                        # print(str(k)+") "+ques)
                        ans = ans + "Q)"+ ques + '\n'
                        k = k + 1
            else:
                for token in line1:
                    # print(token.text,token.dep_,token.tag_)
                    if "aux" in str(token.dep_):
                        h = h + token.text
                        break
                    if h != "":
                        m = str(line1).split(h)
                        ques = 'Why' + ' ' + h + ' ' + m[0].lower() + m[1] + '?'
                    else:
                        ques = 'Why' + ' ' + str(line1).lower() + '?'
                    q = nlp(ques)
                    for t in q:
                        if str(t.tag_) == "NN":
                            b = 1
                            break
                    if b == 1:
                        # print(str(k)+") "+ques)
                        ans = ans + "Q)" + ques + '\n'
                        k = k + 1
                    break
        elif "called" in line:
            b = 0
            l = line.split('called')
            m = nlp(l[0])
            for token in m:
                ques = 'What' + " " + str(m[-1:]) + " " + str(m[:-1]).lower() + " called ?"
                q = nlp(ques)
                for t in q:
                    if str(t.tag_) == "NN":
                        b = 1
                        break
                if b == 1:
                    # print(str(k)+") "+ques)+'\n'
                    ans = ans + "Q)" + ques + '\n'
                    k = k + 1
                break
        elif "As a result" in line:
            l = line.split('As a result,')
            m = nlp(l[1])
            h = ""
            for token in m:
                # print(token.text,token.dep_,token.tag_)
                if "aux" in str(token.dep_):
                    h = h + token.text
                    break
            if h != "":
                n = str(m).split(h)
                p = n[1]
                ques = 'Why' + ' ' + h + ' ' + n[0].lower() + p[:-1] + '?'
                # print(str(k)+") "+ques)
                ans = ans + "Q)"+ ques + '\n'
            else:
                for token in m:
                    if (token.tag_ == "VBP"):
                        a = "do"
                    elif (token.tag_ == "VBD"):
                        a = "did"
                    elif (token.tag_ == "VBZ"):
                        a = "does"
            n = str(m)
            for token in m:
                if (token.tag_ == "VBD" or token.tag_ == "VBP" or token.tag_ == "VBZ"):
                    n = re.sub(str(token.text), str(token.lemma_), n)
            ques = 'Why' + ' ' + a + ' ' + n.lower() + '?'
            # print(str(k)+") "+ques)
            ans = ans + "Q)"+ ques + '\n'
            k = k + 1
            break
        elif "for example" in line.lower() or "for instance" in line.lower():
            if "for example" in line.lower():
                b = "for example"
            else:
                b = "for instance"
            l = line.lower().split(b)
            if not l[0]:
                ques = 'Give an example:' + ' ' + str(list1[c - 1]).lower()
            else:
                if "-" in str(l[0]).lower():
                    l = str(l[0]).lower().split('-')
                    ques = 'Give an example:' + ' ' + str(l[1]).lower()
                else:
                    ques = 'Give an example:' + ' ' + str(l[0]).lower()
                if ques[-1] == ",":
                    ques = ques.replace(ques[-1], '.')
            # print(str(k)+") "+ques)
            ans = ans + "Q)" + ques + '\n'
            k = k + 1
        elif "since" in line:
            z = 0
            l = line.split('since')
            line1 = nlp1(str(l[0]))
            line3 = nlp1(str(l[1]))
            for ent in line3.ents:
                if str(ent.label_) == 'TIME' or str(ent.label_) == 'DATE':
                    z = 1
                    break
            for token in line3:
                if str(token.lemma_) == 'start' or str(token.lemma_) == 'end' or str(
                        token.lemma_) == 'begin':
                    z = 1
                    break
            h = ""
            for token in line1:
                # print(token.text,token.dep_)
                if "aux" in str(token.dep_):
                    h = h + token.text
                    break
            if z == 0:
                if h != "":
                    m = str(line1).split(h)
                    ques = 'Why' + ' ' + h + ' ' + m[0].lower() + m[1] + '?'
                else:
                    line2 = str(line1)
                    line2 = line2.replace(line2[-1], " ")
                    ques = 'Why' + ' ' + line2.lower() + '?'
            else:
                if h != "":
                    m = str(line1).split(h)
                    ques = 'Since when' + ' ' + h + ' ' + m[0].lower() + m[1] + '?'
                else:
                    ques = 'Since when' + ' ' + str(line1) + '?'
            # print(str(k)+") "+ques)
            ans = ans + "Q)"+ ques + '\n'
            k = k + 1
        elif "hence" in line.lower() or "thus" in line.lower() or "therefore" in line.lower():
            if "hence" in line.lower():
                l = (line.lower()).split('hence')
            elif "thus" in line.lower():
                l = (line.lower()).split('thus')
            elif "therefore" in line.lower():
                l = (line.lower()).split('therefore')
            ques = 'Explain why' + ' ' + str(l[1]) + '?'
            # print(str(k)+") "+ques)
            ans = ans + "Q)"+ ques + '\n'
            k = k + 1
        elif "although" in line or "though" in line or "however" in line:
            if "although" in line:
                l = line.split('although')
            elif "though" in line:
                l = line.split('though')
            else:
                l = line.split('however')
            line100 = nlp1(line)
            for token in line100:
                # print(token.text,token.dep_,token.tag_)
                line1 = nlp1(str(l[1]))
                line2 = nlp1(str(l[0]))
            h = ""
            for token in line1:
                # print(token.text,token.dep_,token.tag_)
                if "aux" in str(token.dep_):
                    h = h + token.text
                    break
            if h != "":
                m = str(line1).split(h)
                p = m[1]
                ques = h.capitalize() + ' ' + m[0].lower() + p[:-1] + '?'
                # print(str(k)+") "+ques)
                ans = ans + "Q)" + ques + '\n'
                k = k + 1
                h1 = h + '\'t'
                ques = h1.capitalize() + ' ' + m[0].lower() + p[:-1] + '?'
                # print(str(k)+") "+ques)
                ans = ans + "Q)" + ques + '\n'
                k = k + 1
            # print(str(k)+") "+ques)
            ans = ans + "Q)" + ques + '\n'
            k = k + 1
            break
        elif "-" in line:
            l = line.split('-')
            m = nlp(l[0])
            if str((l[1][:1]).isupper()) == "True":
                for token in m:
                    if str(token.tag_) == "-RRB-":
                        h = token.text
                        l[0] = str(m).split(h)
                        m = l[0][1]
                    ques = "Write in detail about " + str(m).lower() + "?"
                # print(str(k)+") "+ques)
                ans = ans + "Q)" + ques + '\n'
                k = k + 1
        elif str(line.isupper()) == "True" and "SUMMARY" not in line:
            b = 0
            ques = "Write short note on " + line.lower()
            ques = nlp(ques)
            for token in ques:
                if (str(token.tag_) == "-RRB-"):
                    b = 1
                    break
            if b == 0:
                # print(str(k)+") "+str(ques))
                ans = ans + "Q)" + str(ques) + '\n'
                k = k + 1
        if ans!="":
            qu.append(ans)
    if len(qu)<1:
        qu1=wh1(txt,nlp,nlp1)
        for x in qu1:
            qu.append(x)
    return qu

def wh1(txt,nlp,nlp1):
    ques=""
    qu=[]
    doc = nlp(txt)
    list1 = list(doc.sents)
    c = -1
    k = 1
    for x in list1:
        ans=""
        line = str(x)
        # print(line)
        line09 = nlp1(line)
        line0=str(x)
        cnt = 0
        cnta = 0
        cntb = 0
        cntc = 0
        cntd = 0
        c = c + 1
        for ent in line09.ents:
            if str(ent.label_) == "PERSON":
                cnt = cnt + 1
                line0e = line0.replace(str(ent), "?Who", 1)
                l0 = line0e.split("?Who")
                # print(line0)
                break
            if str(ent.label_) == "TIME" or str(ent.label_) == "DATE":
                cnta = cnta + 1
                z = " "
                uz = ""
                uz1 = ""
                for token in line09:
                    if "V" in str(token.tag_):
                        uz = str(token.text)
                        uz1 = str(token.lemma_)
                        break
                for token in line09:
                    # print(token)
                    if str(token.text) in str(ent):
                        # print(z)
                        break
                    elif str(token.tag_) == "IN":
                        z = z + " " + str(token.text)
                        # print(z)
                    else:
                        z = ""
                line0a = line0.replace(str(ent), "?When did", 1)
                line0a = line0a.replace(uz, uz1, 1)
                if z != "":
                    # print(z+" ?When did")
                    line0a = line0a.replace(z + " ?When did", " ?When did", 1)
                    # print(line0a)
                l0a = line0a.split("?When did")
                break
            elif str(ent.label_) == "MONEY" or str(ent.label_) == "QUANTITY":
                cntb = cntb + 1
                line0b = line0.replace(str(ent), "?How much did ", 1)
                l0b = line0b.split("?How much did")
                break
            elif str(ent.label_) == "PERCENT":
                cntc = cntc + 1
                line0c = line0.replace(str(ent), "?How much percentage did ", 1)
                l0c = line0c.split("?How much percentage did")
                break
            elif str(ent.label_) != "ORDINAL" or str(ent.label_) != "CARDINAL":
                cntd = cntd + 1
                line0d = line0.replace(str(ent), "?Which ", 1)
                l0d = line0d.split("?Which")
                break
        if cnt > 0:
            print(l0)
            l0[0] = l0[0].replace(",", "")
            l0[1] = l0[1].replace(".", "")
            ques = "Who" + l0[1] + " " + l0[0] + "?"
            # print(ques)
            ans = ans + "Q)"+ str(ques) + '\n'
            ans=ans.replace(".","")
            ans=ans.replace("\r"," ")
            ans = ans.replace("   ", " ")
            ans = ans.replace("\n", " ")
            ans = ans.replace("\r\n", " ")
            ans = ans.replace("  ", " ")
        if cnta > 0:
            l0a[0] = l0a[0].replace(",", "")
            l0a[1] = l0a[1].replace(".", "")
            ques = "When did" + l0a[1] + " " + l0a[0] + "?"
            # print(ques)
            ans = ans + "Q)" + str(ques) + '\n'
            ans=ans.replace(".","")
            ans=ans.replace("\r"," ")
            ans = ans.replace("   ", " ")
            ans = ans.replace("\n", " ")
            ans = ans.replace("\r\n", " ")
            ans = ans.replace("  ", " ")
        if cntb > 0:
            l0b[0] = l0b[0].replace(",", "")
            l0b[1] = l0b[1].replace(".", "")
            ques = "How much did" + l0b[0] + " " + l0b[1] + "?"
            # print(ques)
            ans = ans + "Q)" + str(ques) + '\n'
            ans=ans.replace(".","")
            ans=ans.replace("\r"," ")
            ans = ans.replace("   ", " ")
            ans = ans.replace("\n", " ")
            ans = ans.replace("\r\n", " ")
            ans = ans.replace("  ", " ")
        if cntc > 0:
            l0c[0] = l0c[0].replace(",", "")
            l0c[1] = l0c[1].replace(".", "")
            ques = "How much percentage did" + l0c[0] + " " + l0c[1] + "?"
            # print(ques)
            ans = ans + "Q)"+ str(ques) + '\n'
            ans=ans.replace(".","")
            ans=ans.replace("\r"," ")
            ans = ans.replace("\n", " ")
            ans = ans.replace("   ", " ")
            ans = ans.replace("\r\n", " ")
            ans = ans.replace("  ", " ")
        if cntd > 0:
            # print(l0d)
            l0d[0] = l0d[0].replace(",", "")
            l0d[1] = l0d[1].replace(".", "")
            ques = "Which place" + " " + l0d[0] + " " + l0d[1] + "?"
            # print(ques)
            ans = ans + str(k) + "Q)" + str(ques) + '\n'
            ans=ans.replace(".","")
            ans=ans.replace("\r"," ")
            ans = ans.replace("\n", " ")
            ans = ans.replace("\r\n", " ")
            ans = ans.replace("   ", " ")
            ans = ans.replace("  ", " ")
        if ans != "":
            qu.append(ans)
    return qu