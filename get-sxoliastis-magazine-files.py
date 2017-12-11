import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

lista = []
listb = []


# ALL links - needs proccessing 
url="http://pandemos.panteion.gr/index.php?lang=el&op=record&type=&q=&page=0&pid=cid:212"

page1 = urllib.request.urlopen(url)
soup1 = BeautifulSoup(page1.read(), "html.parser")

# Get each page of 1st-level  
for link in soup1.find_all("a"):
    lista.append(link)

#### Only for checking - DELETE AFTER script WORKS OK
##num=0
##for i in lista:
##    print(i,num)
##    num  = num+1
    

# Proccess each page of 1st-level
posb=0
for i in range(18,105):

    listc = []
    listd = []
    file_index = 0
    end=0

# Get each 2nd level page - with link to pdf file
    listb.append("http://pandemos.panteion.gr/"+lista[i]['href'])
    url2=listb[posb]

##    print(url2)
    
    page2 = urllib.request.urlopen(url2)
    soup2 = BeautifulSoup(page2.read(), "html.parser")

# Get from each 2nd level page the link to pdf file
##    print("\n\nProcessing 2nd level pages ...\n\n")
    for link2 in soup2.find_all("a"):
           listc.append(link2['href'])
##           print(link2['href'])

##    print(listc[19])
       
    listd.append(listc[19])

    end= len(listd[0])
    file_index= listd[0].find("=", end-30, end)
      
    pdfname=listd[0][file_index+1:]
    url3="http://pandemos.panteion.gr/"+listd[0]

    print("Downloading with urllib : {:s} ".format(pdfname) )
    urllib.request.urlretrieve(url3, pdfname)

    posb=posb+1  # go to next page





