
from bs4 import BeautifulSoup
from urllib import request

url="https://www.imdb.com/chart/top"
link=request.urlopen(url)
imdb=BeautifulSoup(link,"html.parser")
link.close()




for i in imdb.find_all("a"):
    print(i["href"])



"""for movie name"""
for i in imdb.find_all("td",{"class":"titleColumn"}):
    print(i.find_next("a").string)



"""for movie rating"""
for i in imdb.find_all("td",{"class":"ratingColumn imdbRating"}):
   print(i.find_next("strong").string)




"""for movie year"""
for i in imdb.find_all("td",{"class":"titleColumn"}):
    print(i.find_next("span").string)


"""for movie,year and rating"""
for i in imdb.find_all("td",{"class":"titleColumn"}):
    m=(i.find_next("a").string)
    y=(i.find_next("a").find_next("span").string)
    z=(i.find_next("a").find_next("span").find_next("strong").string)
    print("Movie name:",m)
    print("Movie Year:", y)
    print("Movie Rating:",z)
    print("\n"*3)


"""for all"""
for i in imdb.find_all("td",{"class":"titleColumn"}):
    print("Movie name:", i.find_next("a").string)
    print("Movie Year:", i.find_next("span").string)
    print("Movie Rating:", i.find_next("strong").string)
    print("\n"*3)






"""for director"""
for i in imdb.find_all("td",{"class":"titleColumn"}):
    print(i.find_next("a")["title"])
 

"""for all """
for i in imdb.find_all("td",{"class":"titleColumn"}):
    m=(i.find_next("a").string)
    y=(i.find_next("a").find_next("span").string)
    z=(i.find_next("a").find_next("span").find_next("strong").string)
    print("Movie name:",m)
    print("Movie Year:", y)
    print("Movie Rating:",z)
    print("Director:",i.find_next("a")["title"])
    print("\n"*3)

"""for next page"""
for i in imdb.find_all("td",{"class":"titleColumn"}):
    l=(i.find_next("a")["href"])
    ur2="https://www.imdb.com"+(l)
    
    link2=request.urlopen(ur2)
    
    imdb2=BeautifulSoup(link2,"html.parser")
    
    

    for j in imdb2.find_all("div",{"class":"inline canwrap"}):
        print(j.find_next("p").find_next("span").string)
print("/n"*5)
