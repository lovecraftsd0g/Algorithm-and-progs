h = float(input("input height by cm:"))
i = int(h//2.54)
f=int(h//30.48)
h = round((h/100) * 88)

print("you are ",i,"inches")
print("you are also ",f," feet tall")
print("your recomended board length is ",h)