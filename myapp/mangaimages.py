import requests
from bs4 import BeautifulSoup

def get_chapter_link(chapter_id,chapter_no):
    url="https://chapmanganato.com/manga-"+str(chapter_id)+"/"+str(chapter_no)

    URL=(url)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    details=soup.find_all(class_="table-label")
    detailsvalue=soup.find_all(class_="table-value")

    main=soup.find_all(class_="container-chapter-reader")

    ti=str(main).split('alt="')

    chapter_link={chapter_no:[]}

    for i in range(len(ti)):
        mtitle=str(ti[i]).split('alt="')
        #print("Title0",mtitle)
        try:
            mangatitle=mtitle[0].split('- MangaNato.com" src="')

            manga_chapter_image=mangatitle[1].split('" title=')
            #print(mangatitle)
            
        except:
            continue

        chapter_link[chapter_no].append({"alt":mangatitle[0],"img":manga_chapter_image[0]})

    return chapter_link

#print(get_chapter_link("pb992910","chapter-1"))
