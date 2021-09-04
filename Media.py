from pyfiglet import Figlet
import ast
import pytube
from pytube import YouTube
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

    def Add_Video(self):
        Add_id=int(input("Please type your id media :"))
        Add_name=input("Please type your name media :")
        Add_directore=input("Please type your director media :")
        Add_imbd=float(input("Please type your IMDB media :")) 
        Add_url=input("Please type your url media :")
        Add_duration=int(input("Please type your duration media :"))
        Add_casts=input("Please type your actor media :") 
        VIDEO=[]
        VIDEO["Add_id"]=int(Add_id)
        VIDEO["Add_name"]=Add_name
        VIDEO["Add_directore"]=Add_directore
        VIDEO["Add_imbd"]=float(Add_imbd)
        VIDEO["Add_url"]=Add_url
        VIDEO["Add_duration"]=int(Add_duration)
        VIDEO["Add_casts"]=Add_casts
        self.list.append(self.VIDEO_MEDIA)
        
    def Show_list(self):
        for i in range(len(self.VIDEO_MEDIA)):
            print(self.VIDEO_MEDIA[i]["id"], "\t" 
                ,self.VIDEO_MEDIA[i]["name"], "\t" 
                ,self.VIDEO_MEDIA[i]["director"], "\t" 
                ,self.VIDEO_MEDIA[i]["imdb"], "\t" 
                ,self.VIDEO_MEDIA[i]["url"], "\t" 
                ,self.VIDEO_MEDIA[i]["duration"], "\t" 
                ,self.VIDEO_MEDIA[i]["casts"], "\t")

    def Show_edit_menu(self):
        print("1.Do you want the media name to change?")
        print("2.Do you want the media director to change?")
        print("3.Do you want the media imdb to change?")
        print("4.Do you want the media url to change?")
        print("5.Do you want the media id to change?")
        print("6.Do you want the media id to change?")
        print("7.end of edit")
                     
    def Edit_Video(self):
        id = int(input("enter your id media for edit :"))
        for i in range (len(self.VIDEO_MEDIA)):
            if self.VIDEO_MEDIA[i]["id"] == id:
                while True:
                        A.Show_edit_menu()
                        select=int(input("select from edit menu:"))

                        if select == 1:
                            new_name =input("enter your new name :")
                            self.VIDEO_MEDIA[i]["name"]== new_name

                        elif select == 2:
                            new_director =input("enter your new price:")
                            self.VIDEO_MEDIA[i]["director"] == new_director

                        elif select == 3:
                            new_imdb =float(input("enter your new count :"))
                            self.VIDEO_MEDIA[i]["imdb"] == new_imdb

                        elif select == 4:
                            new_url =input("enter your new price:")
                            self.VIDEO_MEDIA[i]["url"] == new_url

                        elif select == 5:
                            new_duration =int(input("enter your new price:"))
                            self.VIDEO_MEDIA[i]["duration"] == new_duration

                        elif select == 6:
                            break
                        else:
                            print("The entered id is not defined")

    def Delete_Video(self):
        id= int(input("enter your id media for delete :"))
        
        for i in range(len(self.VIDEO_MEDIA)):
            if self.VIDEO_MEDIA [i]["id"]==id:
                self.VIDEO_MEDIA.pop(i)
                print("removede")
                break

    def Search_Video(self):
        user_keyword = input("Enter a name or media idea to search : ")

        for i in range(len(self.VIDEO_MEDIA)):
        
           if self.VIDEO_MEDIA[i]['name'] == user_keyword or str(self.VIDEO_MEDIA[i]["id"])== user_keyword:
            print(self.VIDEO_MEDIA[i]) 
           else:
               print("not foand !")

    def Download_Video(self):
        link='http://www.youtube.com/watch?v=lVFNRrL79w0'
        first_stream=pytube.YouTube(link).streams.first
        first_stream.download(output_path='./',filename="test.mp4")
        print(first_stream)
   
    def Save_and_exit(self):
        f=open("datas.txt","w")
        for i in range(len(self.VIDEO_MEDIA)):
            data=int(self.VIDEO_MEDIA[i]["id"])+","
            +self.VIDEO_MEDIA[i]["name"]+","
            +self.VIDEO_MEDIA[i]["director"]+","
            +float(self.VIDEO_MEDIA[i]["imdb"])+","
            +self.VIDEO_MEDIA[i]["url"]+","
            +int(self.VIDEO_MEDIA[i]["duration"])+","
            +self.VIDEO_MEDIA[i]["casts"]+"\n"
            f.write(data)
        f.close()
        exit()


    def Show_all(self):
        print("1.Add video media")
        print("2.Edit video media")
        print("3.Delete video media")
        print("4.Search Video media")
        print("5.Show all")
        print("6.Download Video media")
        print("7.Exit of app")

A=Media(3,"nagahanderakht","safiyazdanian",4.9,"url:http://namadownload.ir.domains.blog.ir/post/download-film-nagahan-derakht",91,"peimanmoadi")

A.Show_info()
f=Figlet(font="standard")
print(f.renderText("Manage video media"))
A.Show_all()
while True:
    select=int(input("Please enter the number : "))

    if select ==1:
        (A.Add_Video())
    elif select==2:
        (A.Edit_Video())
    elif select==3:
        (A.Delete_Video())
    elif select==4:
        (A.Search_Video())
    elif select==5:
        (A.Show_list())
    elif select==6:
        (A.Download_Video())  
    elif select==7:
        (A.Save_and_exit())
        