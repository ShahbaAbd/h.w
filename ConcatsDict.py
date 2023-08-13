Contact={"Shahba":123,"Afraa":456,"Maraw":789}
#add
def add():
    addname=input("add name:")
    addnum=input("add number:")
    Contact[addname]=addnum

#-----------------------------------------------------

#update
def update():
    old=input("Enter old name:")
    new=input("Enter new name:")
    int(new)
    Contact.update({old:new})
#-----------------------------------------------------

#Delete
def remove():
    removename=input("Enter the name you want remove:")
    Contact.pop(removename)
#---------------------------------------------------------------------

#View
def view():
    print(Contact)
#---------------------------------------------------------------------

listoption=["1-add","2-updat","3-delete","4-view"]
print(f"{listoption[0]}\n{listoption[1]}\n{listoption[2]}\n{listoption[3]}")
#---------------------------------------------------------------------

canedit=0
#ifcondation
while   canedit<=3:
    canedit+=1
    useroption=input("enter number the option or the option:")

    if  "add"== useroption or "1" == useroption:
        add()
        print (Contact)
    else:
        print("")
    if  "updat" == useroption or "2" == useroption :
        update()
        print(Contact)
    elif "delete" == useroption or "3" == useroption:
        remove()   
        print(Contact)
    elif "view" == useroption or "4" == useroption:
        view()
        print(Contact)
    
 
    else:
        print(f" error {useroption} out option")
