#Nakul Nayak
#OnlineScraper.py
#Description: GUI interface with backend web scraper that serves as an aid in finding good shopping deals on sites like Ebay, Amazon, etc.

#general scraper with methods applicable to all shopping platforms
class onlineScraper:
    def getNames(self):
        #print(soup.prettify())
        scrapedProducts = self.generalSoup.find_all(str(self.htmlTitle["tag"]),class_=str(self.htmlTitle["class"]))
        cleanProducts=[]
        remove=[]
        for i,name in enumerate(scrapedProducts):
            if len(name)!=0:
                cleanProducts.append(name.text)
            else:
                remove.append(i)

        #z=soup.find_all("li",class_="s-item s-item__sep-on-bottom")
        #print(links)
        #x=officers.find_all("h3",class_="s-item__title")
        #for off in officers:
        #print(len(officers))
        #for i,product in enumerate(scrapedProducts):
        #    print(f"{i} Product Name: {product.text}")
        return cleanProducts,remove

    def getLinks(self):
        #print(f"self.htmlLink={self.htmlLink}")
        jumbledLinks = self.generalSoup.find_all(class_=str(self.htmlLink["class"]))
        cleanLinks=[]
        for link in jumbledLinks:
            cleanLinks.append(link['href'])
        #for lin in cleanLinks:
            #print(lin)
    
        return cleanLinks

    def getPrices(self):
        scrapedPrices = self.generalSoup.find_all(str(self.htmlPrice["tag"]),class_=str(self.htmlPrice["class"]))
        cleanPrices = []
        for price in scrapedPrices:
            cleanPrices.append(price.text)
        #print(f"Clean prices={cleanPrices}")
        #for pr in cleanPrices:
            #print(f"Price: {pr}")
        return cleanPrices
    
    def getConditions(self):
        scrapedConditions = self.generalSoup.find_all(str(self.htmlCondition["tag"]),class_=str(self.htmlCondition["class"]))
        cleanConditions = []
        condIndices=[]
        for cond in scrapedConditions:
            cleanConditions.append(cond.text)
        return cleanConditions
    
    def getShipping(self):
        scrapedShipping = self.generalSoup.find_all(str(self.htmlShipping["tag"]),class_=str(self.htmlShipping["class"]))
        cleanShipping = []
        for ship in scrapedShipping:
            cleanShipping.append(ship.text)

        #print(f"cleanshipping={cleanShipping}")
        return cleanShipping

    def getImages(self):
        scrapedImages = []
        images = self.generalSoup.find_all("img")
        for img in images:
                if img.has_attr('src') and img.has_attr('class') and img['class'][0]=="s-item__image-img":
                    scrapedImages.append(img['src'])
       # print(f"scrapedImages={scrapedImages[0]}")
        return scrapedImages
    
    def customPriceRange(self,min,max):
        validProducts = {}
        for product in self.prodInfo:
            price = self.prodInfo[product][0]
            if min<=price<=max:
                validProducts[product] = self.prodInfo[product]

        return validProducts
    
        
    def sorter(self,productList,priceSortType,sortType):
        #print("hallo",productList[0]['price'])
        #print(f"awesome={float(productList[0]['price'][1:])}")
        cpList=list(productList)
        for prod in cpList:
            #print(f"prodPrice={prod['price']}")
            if "to" in prod['price']:
                try:
                    #print('asueleu')
                        #print(prod['price'])
                        index=prod['price'][1:].index('$')+2
                        #print(f"index={index}")
                        prod['cleanPrice']=float(prod['price'][index:].replace(",",""))
                        #print(f"lallu={prod['cleanPrice']}")
                except:
                    prod['price']="Price not found"
                    prod['cleanPrice']=0
            else:
                try:
                    prod['cleanPrice']=float(prod['price'][1:].replace(",",""))
                except:
                    prod['price']="Price not found"
                    prod['cleanPrice']=0

        
        if sortType=="price":
            highest = True

            if priceSortType=="priceLow":
                highest=False
            cpList = sorted(productList, key=lambda d: d['cleanPrice'],reverse=highest) 

        elif sortType=="seller-feedback":
            cpList = sorted(productList, key=lambda d: d['seller-feedback'],reverse=True) 
        
        elif sortType=="seller-reviews":
            cpList = sorted(productList, key=lambda d: d['seller-reviews'],reverse=True) 


        #cpList.pop('cleanPrice',None)
        return cpList
    
    
    def hasKeyword(self,word):
        validProducts = {}
        for product in self.prodInfo:
            if word in product:
                validProducts[product] = self.prodInfo[product]

        return validProducts

