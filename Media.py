

class Media:
    def __init__(self,ID,NA,DI,IM,UR,DU,CA):
        self.id=ID
        self.name=NA
        self.director=DI
        self.imdb=IM
        self.url=UR
        self.duration=DU
        self.casts=CA

    VIDEO_MEDIA=[]

    def Show_info(self):
        print("Loding...")
        self.list=[]
        for i in range(len(self.list)):
            medi=list[i].split(",")
            self.VIDEO_MEDIA["id"]=int(medi[0])
            self.VIDEO_MEDIA["name"]=medi[1]
            self.VIDEO_MEDIA["director"]=medi[2]
            self.VIDEO_MEDIA["IMDB"]=float(medi[3])
            self.VIDEO_MEDIA["url"]=medi[4]
            self.VIDEO_MEDIA["duration"]=int(medi[5])
            self.VIDEO_MEDIA["casts"]=medi[6]
            self.list.append(self.VIDEO_MEDIA)
        print("Wellcome")

        