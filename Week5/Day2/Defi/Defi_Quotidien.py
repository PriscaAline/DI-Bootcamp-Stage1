
"""class Pagination():
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.__phrase = " ".join(items)
        self.totalPage =(len(self.__phrase)/pageSize)
        self.__choix =[]
        self.__compt=0
        if int(self.totalPage)==self.totalPage:
            self.totalPage=self.totalPage
        else:
            self.totalPage=int(self.totalPage)+1
    def firstPage(self):
        result=self.__phrase[0:self.pageSize]
        i=0
        while i<len(result):
            self.__choix.append(result[i])
            i+=1
        self.__compt=self.__compt
    def lastPage(self):
        number=(self.totalPage-1)*self.pageSize
        result=self.__phrase[number:]
        i=0
        while i<len(result):
            self.__choix.append(result[i])
            i+=1
        self.__compt=number
    def nextPage(self):
        a=self.__compt+self.pageSize
        result=self.__phrase[a:a+self.pageSize]
        i=0
        while i<len(result):
            self.__choix.append(result[i])
            i+=1
        self.__compt=a
    def prevPage(self):
        a=self.__compt-self.pageSize
        result=self.__phrase[a:self.__compt]
        i=0
        while i<len(result):
            self.__choix.append(result[i])
            i+=1
        self.__compt=a

    def goToPage(self,pageNum):
        if pageNum<=0 or pageNum==1:
            self.firstPage()
        elif pageNum>self.totalPage or pageNum==self.totalPage:
            self.lastPage()
        else:
            fin=(self.pageSize*pageNum)-1
            debut=fin-(self.pageSize-1)
            if (fin+1)>len(retour):
                result=self.__phrase[debut: ]
                i=0
                while i<len(result):
                    self.__choix.append(result[i])
                    i+=1
                self.__compt=debut
            else:
                result=self.__phrase[debut:(fin+1)]
                i=0
                while i<len(result):
                    self.__choix.append(result[i])
                    i+=1
                self.__compt=debut
    def getVisibleItems(self):
        if self.__choix==[] :
            print("Paging error!!")
        else:
            print(self.__choix)
            self.__choix.clear()
"""