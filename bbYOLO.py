import Tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import Image
#----------------------------------------------------------------------
width = 800
height = 600
step = 50
class MainWindow():
   
    #----------------

    def __init__(self, main):
               #set the page properties 
        main.title("Reconhecimento de cone")
        self.dimen= '{}x{}'.format(width+180 ,height +100)
        main.geometry(self.dimen)
         

        # canvas for image
        self.canvas = tk.Canvas(main, width=width, height=height)
        self.canvas.grid(row=0, column=0,columnspan=3, rowspan=5)
        #self.x0 = self.canvas.create_line(0,0,0,0,fill="red", dash=(4,4))
        #self.y0 = self.canvas.create_line(0,0,0,0,fill="red", dash=(4,4))
        self.coord_mouse = (self.canvas.create_line(0,0,0,0,fill="red", dash=(4,4)),self.canvas.create_line(0,0,0,0,fill="red", dash=(4,4)))
        self.selected = self.canvas.create_rectangle(0,0,0,0)

        self.boxes = []
        self.list = []
        self.rIds=[]
        self.number=0
        self.fileTxt = ""
        self.Start = True
        self.First = True 
        self.stepx = 0
        self.stepy = 0
        self.image_width = 0
        self.image_height = 0
        # images
        self.im = Image.open("Cover.png")
        self.my_image = ImageTk.PhotoImage(self.im.resize((height,width)))
        self.my_image_id = 0
        # set first image on canvas
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor = "nw", image = self.my_image)

        # button to change image
        self.bBack = tk.Button(main, text="< Back", command=self.Back)
        self.bBack.grid(row=5, column=0)
        self.bSave = tk.Button(main, text="SAVE", command=self.Save)
        self.bSave.grid(row=5, column=1)
        self.bNext = tk.Button(main, text="Next >", command=self.Next)
        self.bNext.grid(row=5, column=2)
        self.bOpen = tk.Button(main, text= "Open", command=self.Open)
        self.bOpen.grid(row=6,column=0) 
        self.bClose = tk.Button(main, text= "Close", command=self.Close)
        self.bClose.grid(row=6,column=3) 


        self.sCurrent = tk.Label(main, text="<====Select one or more images")
        self.sCurrent.grid(row=6,column=1,columnspan=2)
        # Drawing Box
        self.sBox = tk.Label(main, text = "Pontos")
        self.sBox.grid(row=0, column=3)
        self.listbox = tk.Listbox(main)
        self.listbox.grid(row =1, column =3, rowspan = 4)
        # Drawing tool
        self.canvas.bind("<Motion>", self.Motion)
        self.canvas.bind("<Button-1>", self.Click)
        self.listbox.bind("<Double-Button-1>",self.CurSelet)
        main.bind("<Left>", self.Left)
        main.bind("<Right>", self.Right)
        main.bind("<Up>", self.Up)
        main.bind("<Escape>",self.Cancel)
        self.canvas.bind("<Escape>",self.Cancel)
        main.bind("<Down>", self.Down)
    #----------------
    def Close(self):
        root.destroy()
    def Cancel(self,x):
        self.First = True
    def CurSelet(self,x):
        self.stepx = 0
        self.stepy=0

        #print "----------------REMOVE----------"
        self.canvas.delete("all")
        self.path = self.files[self.my_image_id]
        self.im = Image.open(self.path)
        self.fileTxt = self.path.replace(".jpg",".txt")
        #print self.fileTxt
        #print ImageTk.PhotoImage(self.im).width()
        self.image = ImageTk.PhotoImage(self.im)
        self.canvas.create_image(0,0,anchor="nw",image = self.image)
        id = self.listbox.get(self.listbox.curselection())
        print "selected",id[0][0]
        #print type(int(id[0][0]))
        self.listbox.delete(int(id[0][0]))
        #print "lista antes de deletar", self.list
        del self.list[int(id[0][0])]
        print self.rIds
        del self.rIds[int(id[0][0])]
        print self.rIds
        #print "lista depois de deletar",self.list
        #print id
        END = len(self.list)
        self.listbox.delete(0,END)
        for l in self.list:
            a = ((int(l[0][0]),int(l[0][1])))
            b = ((int(l[1][0]),int(l[1][1])))
            #print self.list.index(l),"--------",l            
            textbox = "{} ---{},{}".format(self.list.index(l),a,b)
            #print "-----textbox ------",textbox
            self.listbox.insert(self.list.index(l),textbox)
            self.boxes.append(self.canvas.create_rectangle(l[0][0],l[0][1],l[1][0],l[1][1],width =1,outline="red"))
            self.rIds.append(self.canvas.create_text(min(l[0][0],l[1][0]),min(l[0][1],l[1][1]), anchor="nw",fill = "red"))
            self.canvas.itemconfig(self.rIds[len(self.rIds)-1], text=self.list.index(l))

    def Left(self,x):
        #print "Left",x
        self.stepx+=step
        #print "steps = ",self.stepx,",",self.stepy
        self.canvas.move("all",+step,0)
    def Right(self,x):
        #print "Right",x
        self.stepx-=step
        self.canvas.move("all",-step,0)

    def Up(self,x):

        #print "Left",x
        self.stepy+=step
        self.canvas.move("all",0,step)
    def Down(self,x):
        self.stepy -= step
        self.canvas.move("all",0,-step)

 
    def Load(self):
        #print " --------------------------Load--------------------------------"

        self.canvas.delete("all")
        self.path = self.files[self.my_image_id]
        self.im = Image.open(self.path)
        self.fileTxt = self.path.replace(".jpg",".txt")
        #print self.fileTxt
        self.image_width = ImageTk.PhotoImage(self.im).width()
        self.image_height=ImageTk.PhotoImage(self.im).height()
        self.my_image = ImageTk.PhotoImage(self.im)
        self.CurrentImage = self.canvas.create_image(0,0,anchor="nw",image = self.my_image)
        self.refresh()
    
    
    
    
    
    def refresh(self):
        self.stepx= 0
        self.stepy=0
        END = len(self.list)
        #print "LISTAAAA - ", self.list
        self.listbox.delete(0,END)
        with open(self.fileTxt) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        #print "antes do refresh", self.list
        #print content
        temp = []
        temp2= []
        for c in content:
            #print "c===== ",c
            coord = map(float, c.split(" "))
            #print "coord = ", coord
            a =((coord[1] - coord[4]/2)*self.image_width , (coord[2] - coord[3]/2)*self.image_height)
            b =((coord[1] + coord[4]/2)*self.image_width , (coord[2] + coord[3]/2)*self.image_height)
            temp.append((a,b))

            a = ((int(a[0]),int(a[1])))
            b = ((int(b[0]),int(b[1])))
            ind = len(temp)-1
            textbox = "{} ---{},{}".format(ind,a,b)
            #print "+++++texbox ====",textbox
            self.listbox.insert(ind,textbox)
            #print "a = ", a 
            #print "b = ",b
            #print "a0 =", a[0] ,"a1 =" ,a[1]
            self.boxes.append(self.canvas.create_rectangle(a[0],a[1],b[0],b[1],width =1,outline="red"))

            temp2.append(self.canvas.create_text(min(a[0],b[0]),min(a[1],b[1]), anchor="nw",fill = "red"))
            self.canvas.itemconfig(temp2[ind], text=ind)
        self.list = temp    
        self.rIds = temp2 
    
    def Next(self):
        #print "Next"
        if self.my_image_id < len(self.files) -1:
            self.my_image_id+=1
            self.Load()
        else:
            print "Fim da Lista"
    



    def Open (self):
        self.ftype = [('PNG Image','.jpg')]
        self.files = fd.askopenfilenames(parent=root, title = "Choose the Images", filetypes=self.ftype)
        #print self.files
        self.my_image_id = 0
        self.Load()
    



    def Back(self):
        #print "Back"
        if self.my_image_id > 0 :
            self.my_image_id -=1
            self.Load()
        else:
            print "Fim da Lista"




    def Click(self, event):
        x,y = event.x,event.y

        if ( x-self.stepx<0 or y-self.stepy<0 or x-self.stepx>self.image_width or y-self.stepy>self.image_height):
            print "fora"

        else: 
            if self.First==True:
                self.First = False
                self.UL = (x-self.stepx,y-self.stepy) 
                #print "first click -- ", self.UL
                #print "tipo do UL", type(self.UL)
            
            else:
                self.First=True
                self.BR = (x-self.stepx,y-self.stepy)
                #print "Second Click -- ", self.BR
                #print "tipo do BR", type(self.BR)
                new_rec =self.canvas.create_rectangle(self.UL[0],self.UL[1],self.BR[0],self.BR[1],width =1,outline="red")
                self.boxes.append(new_rec)
                self.canvas.move(new_rec,self.stepx,self.stepy)
                self.list.append((self.UL,self.BR))
                ind = len(self.list) -1
                #print "self.list ----",self.list[ind][0]
                element = "{} --{},{}".format(ind,self.list[ind][0],self.list[ind][1])
                self.listbox.insert(ind,element)
                #print "adicionado  ---", self.list[ind]
                self.rIds.append(self.canvas.create_text(min(self.UL[0],self.BR[0])+self.stepx,min(self.UL[1],self.BR[1])+self.stepy, anchor="nw",fill = "red"))
                self.canvas.itemconfig(self.rIds[len(self.rIds)-1], text=ind)
    
    
    def Save(self):
        #print self.list
        with open(self.fileTxt,"w") as myfile:
            for l in self.list:
                #print "l --->", l
                #print "tiplo l1",type(l[1])
                #print "tipol l",type(l)
                #print "l[1][0]==",l[1][0],type(l[1][0])
                #print type(l[0][0])
                cx = abs((float(l[0][0])+float(l[1][0]))/2)
                cy = abs((float(l[0][1])+float(l[1][1]))/2)
                width = abs(float(l[1][0]) - float(l[0][0]))
                height = abs(float(l[1][1]) - float(l[0][1]))
                #print "width salvo -", width
                #print "height salvo - ", height
                data = "0 {} {} {} {}".format(cx/self.image_width,cy/self.image_height,height/self.image_height, width/self.image_width)
                #print data
                myfile.write(data+"\n")





    def Motion(self, event):
    
        self.canvas.delete(self.selected) 
        self.canvas.delete(self.coord_mouse[0])               
        self.canvas.delete(self.coord_mouse[1])
        x,y= event.x,event.y
        if ( x-self.stepx<0 or y-self.stepy<0 or x-self.stepx>self.image_width or y-self.stepy>self.image_height):
            pass
            #print "Fora da imagem"
        else:
            self.coord_mouse = (self.canvas.create_line(0,y,width,y,fill="red", dash=(4,4)),self.canvas.create_line(x,0,x,height,fill="red", dash=(4,4)))
            if self.First == True:
                pass
            else:
                self.selected = self.canvas.create_rectangle(self.UL[0]+self.stepx,self.UL[1]+self.stepy,x,y)
            
        #self.x0 = self.canvas.create_line(0,y,width,y,fill="red", dash=(4,4))
        #self.y0 = self.canvas.create_line(x,0,x,height,fill="red", dash=(4,4))
                #print('{},{}'.format(x,y))
#----------------------------------------------------------------------
root = tk.Tk()
MainWindow(root)
root.mainloop()
