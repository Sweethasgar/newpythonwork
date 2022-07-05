f=open("abc.txt","w")
# for line in f:
#     print(line)

# lines=list(f)
# print(lines)

# out=[line.rstrip("\n")for line in f]
# print(out)

lst=["javascript","php","c++"]
for lang in lst:
    lang+="\n"
    f.write(lang)