#main file to run that takes care of input and communicates with other files

#import from modules  within project
from Scrape.Ebay import Ebay
from Scrape.Utillities import Utilities
#import scraping packages
from bs4 import BeautifulSoup
import requests

class General:
    def __init__(self,store) -> None:
        self.store = store

    def startScrape(self,productIn,shipChecked,condChecked,sort_by):

        #print(f"libdub={shipChecked},{condChecked}")
        if self.store=="Ebay":
            link=f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={productIn}&_sacat=0"
            utils = Utilities()
            ebayObj = Ebay(self.store,productIn,utils.initDicts("h3","s-item__title"),utils.initDicts(htmlClass="s-item__link"),utils.initDicts("span","s-item__price"),utils.initDicts("span","SECONDARY_INFO"),utils.initDicts("span","s-item__shipping s-item__logisticsCost"))

        productLs,remove = ebayObj.getNames() #contains indexes of products from pdouct_ls that do not have proper/complete information
        #print(f"remove{remove}")
        productLinks = ebayObj.getLinks()
        utils.delProducts(remove,productLinks)
        productConditions = ebayObj.getConditions()
        productShip = ebayObj.getShipping()
        productPrice = ebayObj.getPrices()
        productImages = ebayObj.getImages()
            
        if self.store=="Ebay":   
            productList = utils.orgProdInfo(productLs,productPrice,productLinks,productConditions,productShip,productImages)
            if shipChecked or condChecked:
                productList = ebayObj.badShippingOrCondition(productList,shipChecked,condChecked)



            sellerFeedback=[]
            sellerRatings=[]

            #sellerFeedback,sellerRatings=ebayObj.getSpecificProdInfo(productLinks)
            if sort_by=="reviews":
                sellerFeedback=ebayObj.getSellerInfo(productList,"feedback")
            elif sort_by=="rating":
                sellerRatings=ebayObj.getSellerInfo(productList,"reviews")
                #print(f"BUGSY MOGES={sellerRatings}")
            
            productList = utils.addSellerStats(productList,sellerFeedback,sellerRatings)
            if sort_by=="priceLow":
                productList = ebayObj.sorter(productList,"priceLow","price")
            elif sort_by == "priceHigh":
                productList = ebayObj.sorter(productList,"priceHigh","price")
            elif sort_by=="reviews":
                productList = ebayObj.sorter(productList,"","seller-feedback")
            elif sort_by=="rating":
                productList = ebayObj.sorter(productList,"","seller-reviews")


        return productList
           # ebayObj.prodInfo = utils.orgProdInfo(productLs,productPrice,productLinks)

            #for key,value in ebayObj.prodInfo.items():
             #   print(f"{key}:{value}")

#gen=General("Ebay")
#gen.startScrape("shoe")



