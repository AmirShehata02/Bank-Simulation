from tkinter import *
from PIL import Image,ImageTk
import random as r


bank=Tk()

input_user=Toplevel()
input_user.title("Settings")
come_line=Scale(input_user,from_=1,to=10,orient=HORIZONTAL,length=180,digits=4,label="Average of clients per 10 seconds",resolution=0.01)
come_line.pack()

go_line=Scale(input_user,from_=1,to=10,orient=HORIZONTAL,length=300,digits=4,label="Average of leave per 10 seconds",resolution=0.01)
go_line.pack()




screenwidth=bank.winfo_screenwidth()
screenheight=bank.winfo_screenheight()
bank.title("Bank")
bank.config(background="brown")
bank.geometry("504x504+"+str(int((screenwidth-504)/2))+"+"+str(int((screenheight-504)/2)))

background=ImageTk.PhotoImage(Image.open("E:\\mod_sim_project\\data\\m&s.png").resize((504,504)))
client_image=['']*7
variable_storage=['']*7
variable_storage2=['']*7
random_list=[]

for i in range(7):
    client_image[i]=ImageTk.PhotoImage(Image.open(f"E:\\mod_sim_project\\data\\Vector Smart Object-{i}.png").resize((54,54)))
    random_list.append(i)
random_list2=random_list.copy()
r.shuffle(random_list)
r.shuffle(random_list2)

can=Canvas(bank,width=504,height=504)
can.create_image(0,0,image=background,anchor=NW)


long=0
front=0
rear=-1
long2=0
front2=0
rear2=-1
bol=True
def remv(event):
    global long,long2,front,front2,rear,rear2,bol,tl
    turn=r.choice([1,2])
    if ((turn==2 and long2==0 )or turn==1) and long>0:

        if front>(rear):
            for j in range(front,7):
                i=random_list[j]
                can.delete(variable_storage[i])
            for j in range(0,rear+1):
                i=random_list[j]
                can.delete(variable_storage[i])
        else:
            for j in range(front,rear+1):
                i=random_list[j]
                can.delete(variable_storage[i])
        long-=1
        front+=1
        front%=7
        if front>(rear):
            for j,l in zip(range(front,7),range(long)):
                i=random_list[j]
                variable_storage[i]=can.create_image(202,122+l*50,image=client_image[i])
            for j,l in zip(range(0,rear+1),range(long)):
                i=random_list[j]
                variable_storage[i]=can.create_image(202,122+((7-front)+l)*50,image=client_image[i])
        else:
            for j,l in zip(range(front,rear+1),range(long)):
                i=random_list[j]
                variable_storage[i]=can.create_image(202,122+l*50,image=client_image[i])
        

    elif ((turn==1 and long==0 )or turn==2) and long2>0:
        
        if front2>(rear2):
            for j in range(front2,7):
                i=random_list2[j]
                can.delete(variable_storage2[i])
            for j in range(0,rear2+1):
                i=random_list2[j]
                can.delete(variable_storage2[i])
        else:
            for j in range(front2,rear2+1):
                i=random_list2[j]
                can.delete(variable_storage2[i])
        long2-=1
        front2+=1
        front2%=7
        if front2>(rear2):
            for j,l in zip(range(front2,7),range(long2)):
                i=random_list2[j]
                variable_storage2[i]=can.create_image(280,122+l*50,image=client_image[i])
            for j,l in zip(range(0,rear2+1),range(long2)):
                i=random_list2[j]
                variable_storage2[i]=can.create_image(280,122+((7-front2)+l)*50,image=client_image[i])
        else:
            for j,l in zip(range(front2,rear2+1),range(long2)):
                i=random_list2[j]
                variable_storage2[i]=can.create_image(280,122+l*50,image=client_image[i])
        
    else:
        print("empty Failed")
        bol=False
    if bol:
        tl=10000/go_line.get()
        bank.after(r.randint(int(tl-tl*0.25),int(tl+tl*0.25)),lambda:remv(None))

def addv(event):
    global long,long2,rear,rear2,bol
    turn=r.choice([1,2])
    if ((turn==2 and long2==7 )or turn==1) and long<7:

        rear+=1
        rear%=7
        i=random_list[rear]
        variable_storage[i]=can.create_image(202,122+long*50,image=client_image[i])
        long+=1
       

    elif ((turn==1 and long==7 )or turn==2) and long2<7:

        rear2+=1
        rear2%=7
        i=random_list2[rear2]
        variable_storage2[i]=can.create_image(280,122+long2*50,image=client_image[i])
        long2+=1
     
    

    else:
        print("alot Failed")
        bol=False
    
    
        
    if  bol: 
        tc=10000/come_line.get()
        bank.after(r.randint(int(tc-tc*0.25),int(tc+tc*0.25)),lambda:addv(None)) 


addv(None)

tl=10000/go_line.get()
bank.after(r.randint(int(tl-tl*0.25),int(tl+tl*0.25)),lambda:remv(None))

bank.bind("<a>",addv)
bank.bind("<r>",remv)




can.pack(expand=True)
bank.mainloop()