import requests
from bs4 import BeautifulSoup

def get_minfo(chapterid):
    url="https://chapmanganato.com/manga-"+chapterid

    URL=(url)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    #print("Page:",page)
        #print("Soup:",soup)

    details=soup.find_all(class_="table-label")
    detailsvalue=soup.find_all(class_="table-value")
    image=soup.find(class_="info-image")
    main=soup.find_all(class_="chapter-name text-nowrap")
    updatedate=soup.find(class_="stre-value")

    desc=soup.find(class_="panel-story-info-description")

    a=[]

    d=[]

    chaptername=[]
    chapterlink=[]

    author=[]
    genres=[]

    name2={"title":"","author":[],"status":"","description":"","updated":"","genres":[],"alternative":[],"chapters":[]}

    mname=str(image).split('alt="')
    fname=mname[1].split('" class')

    mauthor=str(detailsvalue[1]).split('rel="nofollow">')
    for au in range(len(mauthor)):
        #print(au)
        try:
            fauthor=mauthor[au+1].split('</a>')
            author.append(fauthor[0])
        except:
            pass
    #print(mauthor)

    mstatus=str(detailsvalue[2]).split('<td class="table-value">')

    mdesc=str(desc).split("<h3>Description :</h3>")[1].split("</div>")[0]

    mupdated=str(updatedate).split('">')

    mgenres=str(detailsvalue[3]).split('genre-')
    #print(mgenres)

    for mg in range(len(mgenres)):
        try:
            fgenres=mgenres[mg+1].split('">')[1].split('</a>')
            genres.append(fgenres[0])
        except:
            pass

    malternatives=str(detailsvalue[0]).split('<h2>')
    falternatives=malternatives[1].split('</h2>')
    
    name2["title"]=(str(fname[0]))
    name2["author"]=author
    name2["genres"]=genres
    name2["updated"]=mupdated[1].split('</')[0]
    name2["status"]=mstatus[1].split('</td>')[0]
    name2["description"]=mdesc.replace("\n","")
    name2["alternative"]=falternatives[0].split(';')

    for titlei in main:
        a.append(titlei)
        #print(title)

    #for detaili in details:
       # d.append(detaili)

    for i in range(len(a)):
        mtitle=str(a[i]).split('title="')
        #print("Title0",mtitle)
        mangatitle=mtitle[1].split('">')
        chaptername.append(mangatitle[0])

        #print("--------------------------------------------------")

        mlink=str(mtitle[0]).split(chapterid+"/")
        #print("Link0",mlink)
        mangalink=mlink[1].split('" rel')
        chapterlink.append(mangalink[0])
        #print(mangalink[0])

        #name2[mangatitle[0]]=(mangalink[0])
        #finaljson=(json.dumps({"Chapters":(mangatitle[0],mangalink[0])}))

        
        name2["chapters"].append({mangalink[0]:mangatitle[0]})
    
    return name2

