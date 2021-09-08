class Actor():
    def list_actor():
        actor=[]
        while True:
            name=input("please type the actor name : ")
            actor.append(name)
            if int(input("Do you want to continue?   0-1"))==0:
                break
        return actor    
