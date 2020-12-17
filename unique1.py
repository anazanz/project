def getuniquewords(str):
    list=str.split()
    res=[]
    for word in list:
          if word not in res:
              res.append(word)
    return res
text="python is good java is also good"
print(getuniquewords(text))





