f=open("movie.txt","r")

movie_list=[]
movie_list=[line.rstrip("\n").split(",")for line in f ]

# for line in f:
#     movie=line.rstrip("\n").split(",")
#     movie_list.append(movie)
#     print(movie)

grpby_year=[movie for movie in movie_list if movie[1]=='2022']
print(len(grpby_year))

grpby_lang=[movie for movie in movie_list  if movie[-2]=="malayalam"]
print(len(grpby_lang))

movie_out={}

for movie in movie_list:
    year=movie[1]
    if year in movie_out:
        movie_out[year]+=1
    else:
        movie_out[year]=1
print(movie_out)

print(movie_out.items())
out=max(movie_out.items(),key=lambda it:it[1])
print(out)