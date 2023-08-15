import requests
from bs4 import BeautifulSoup

#searchterm=input(str("Enter:"))

def get_mdetails(searchterm):
    searchterm_modified=searchterm.replace(" ","_")

    url="https://manganato.com/search/story/"+searchterm_modified

    URL=(url)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    main=soup.find_all(class_="search-story-item")

    a=[]

    name=[]
    link=[]

    author=[]
    updated_on=[]

    name2={}

    for titlei in main:
        a.append(titlei)

    for i in range(len(a)):
        title0=str(a[i]).split('title="')

        title1=title0[1].split('">')
        name.append(title1[0])

        link0=str(title0[0]).split('href="')
        link1=link0[1].split('" rel')
        link.append(link1[0])

        if ("chapmanganato" in link1[0]):
            primary=link1[0].split("https://chapmanganato.com/manga-")
        elif("manganato" in link1[0]):
            primary=link1[0].split("https://manganato.com/manga-")

        try:
            author0=str(title0[5]).split('">')
            author.append(author0[0])
        except:
            author0=str(title0[4]).split('">')
            author.append(author0[0])

        try:
            updated_on0=str(title0[5]).split('Updated : ')
            updated_on1=updated_on0[1].split("</span>")
            updated_on.append(updated_on1[0])
        except:
            updated_on0=str(title0[4]).split('Updated : ')
            updated_on1=updated_on0[1].split("</span>")
            updated_on.append(updated_on1[0])

        name2[primary[1]]={"title":title1[0],"author":author0[0],"updated_on":updated_on1[0]}
    return name2

#print(get_mdetails("naruto"))
