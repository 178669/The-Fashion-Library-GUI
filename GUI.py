from tkinter import *
import tkinter as tk
"""
window = tk.Tk()

window.configure(bg="pink")
window.rowconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1) #weight allows for resizing
window.geometry("800x800")
"""
class startApp(tk.Tk):
    #startApp constructor
    def __init__(self, *args, **kwargs):

        #Tk constructor
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        #weight=1 allows for resizing
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #an array of frames will be used for traversing "pages"
        self.frames = {}

        #loop for frame/page initialization
        for F in (StartPage, ChoicePage, DonatePage, TokenPage, ShopPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    #displays current frame passed as input
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], minsize=0, weight=1)
        self.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], minsize=0, weight=1) #weight allows for resizing

        b_startimg = tk.PhotoImage(file='Images/b_pink.png')

        #b_start = tk.Button(self, text="Start a Trade", width=200, command=lambda:controller.show_frame(Page1))
        b_start = tk.Button(self, image=b_startimg, command=lambda: controller.show_frame(ChoicePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_start.photo = b_startimg
        b_start.grid(row=3, rowspan=1, column=3, columnspan=3, sticky="nsew")

        RENT_CLOTHES = tk.Label(self, text="TRADE CLOTHES", bg="white", fg="pink", font=('Ubuntu Condensed', 200))
        RENT_CLOTHES.grid(row=2, column=3, columnspan=3)

"""
        b_startimg = tk.PhotoImage(file='images/startbutton.png')
        img_label = tk.Label(image=b_startimg) 
"""




class ChoicePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(5, minsize=50, weight=0)
        self.columnconfigure(3, minsize=50, weight=0)  # weight allows for resizing

        b_donateimg = tk.PhotoImage(file='Images/b_donateo50.png')
        b_shopimg = tk.PhotoImage(file='Images/b_shop.png')
        b_tradeimg = tk.PhotoImage(file='Images/b_trade.png')

        img1 = tk.PhotoImage(file='Images/oneimg.png')
        img2 = tk.PhotoImage(file='Images/twoimg.png')
        img3 = tk.PhotoImage(file='Images/threeimg.png')

        imglab1 = Label(self, image=img1, borderwidth=0)
        imglab2 = Label(self, image=img2, borderwidth=0)
        imglab3 = Label(self, image=img3, borderwidth=0)

        imglab1.photo=img1
        imglab2.photo=img2
        imglab3.photo=img3

        imglab1.grid(row=1, column=0, pady=10)
        imglab2.grid(row=3, column=0, pady=10)
        imglab3.grid(row=5, column=0, pady=10)

        fill1=Label(self, height=1, highlightthickness=0, borderwidth=0, bg="white", text="SELECT AN OPTION", font=('Ubuntu Condensed', 80))
        fill1.grid(row=0, column=2, columnspan=3)

        fill2=LabelFrame(self, width=200, borderwidth=0, highlightthickness=0, bg="white")
        fill2.grid(row=0, column=1)
        #fill3=LabelFrame(self, width=50, borderwidth=0, highlightthickness=0, bg="white")
        #fill3.grid(row=0, column=2)

        b_donate = tk.Button(self, image=b_donateimg, command=lambda: controller.show_frame(DonatePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_donate.photo = b_donateimg
        b_donate.grid(row=1, column=1, columnspan=2)
        donatelabel = tk.Label(self,text= "Donate washed clothing items to the bin below. \nGain 1 Shop Credit per Item.", font=('Ubuntu Condensed', 40), justify="left", bg="white")
        donatelabel.grid(row=2,column=2, columnspan=2)

        b_shop = tk.Button(self, image=b_shopimg, command=lambda: controller.show_frame(ShopPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_shop.photo = b_shopimg
        b_shop.grid(row=3, column=1, columnspan=2)
        shoplabel = tk.Label(self, text= "Browse through our washed clothes and select one to rent. \nPick up your item at the Clothing Collection Window", font=('Ubuntu Condensed', 40), justify="left", bg="white", highlightthickness=0)
        shoplabel.grid(row=4,column=2, columnspan=4)

        b_trade = tk.Button(self, image=b_tradeimg, command=lambda: controller.show_frame(DonatePage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_trade.photo = b_tradeimg
        b_trade.grid(row=5, column=1, columnspan=2)
        tradelabel = tk.Label(self, text= "Once you are done wearing your item, redonate it and take another", font=('Ubuntu Condensed', 40), justify="left", bg="white")
        tradelabel.grid(row=6,column=2, columnspan=6)


        #


class DonatePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(6, weight=1)
        self.columnconfigure(0, weight=1)

        b_home = tk.Button(self, text="HOME", highlightthickness=0, command=lambda: controller.show_frame(StartPage))
        b_home.grid(row=0, column=0, sticky="ne")

        donatetitle = tk.Label(self, text="DONATE", font=('Ubuntu Condensed', 275), fg="pink", bg="white")
        donatetitle.grid(row=0, column=0)

        donatetext = tk.Label(self, text="Place Item In Donation Box Below", font=('Ubuntu Condensed',100), fg="red", bg="white")
        donatetext.grid(row=1,column=0)

        """
        fill1=LabelFrame(self, height=30)
        fill1.grid(row=5, column=0)
        """

        arrimg = tk.PhotoImage(file='Images/downarrow.png')
        arrlab = Label(self, image=arrimg, bg="white", borderwidth=0, highlightthickness=0)
        arrlab.photo = arrimg
        arrlab.grid(row=4, column=0)

        doneimg = tk.PhotoImage(file='Images/b_done.png')
        b_done = tk.Button(self, image=doneimg, command=lambda: controller.show_frame(TokenPage), borderwidth=0, bg="white", activebackground="white", highlightthickness=0)
        b_done.photo = doneimg
        b_done.grid(row=6, column=0)

class TokenPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=1)

        fill1=LabelFrame(self, height=100, borderwidth=0, highlightthickness=0, bg="white")
        fill1.grid(row=0, column=0)

        tokentitle = tk.Label(self, text="Please Tap Your ID", font=('Ubuntu Condensed', 150), fg="pink", bg="white")
        tokentitle.grid(row=2, column=0)

        tokentitlep2 = tk.Label(self, text="to Receive Your Token", font=('Ubuntu Condensed', 100), fg="pink", bg="white")
        tokentitlep2.grid(row=3,column=0)

        b_home = tk.Button(self, text="HOME", highlightthickness=0, command=lambda: controller.show_frame(StartPage))
        b_home.grid(row=0, column=0, sticky="ne")

class ShopPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")
        self.rowconfigure(5, weight=1)
        self.columnconfigure(3, weight=1)

        fill1=LabelFrame(self, height=10, borderwidth=0, highlightthickness=0, bg="white")
        fill1.grid(row=0, column=0)

        tokentitle = tk.Label(self, text="SHOP", font=('Ubuntu Condensed', 200), fg="pink", bg="white")
        tokentitle.grid(row=2, column=1)

        b_home = tk.Button(self, text="HOME", highlightthickness=0, command=lambda: controller.show_frame(StartPage))
        b_home.grid(row=0, column=3, sticky="ne")

        item1img = PhotoImage(file='ClothesImages/greyblousere.png')
        item1 = Label(self, image=item1img)
        item1.photo = item1img
        item1.grid(row=3,column=0)

        item2img = PhotoImage(file='ClothesImages/redtop.png')
        item2 = Label(self, image=item2img)
        item2.photo = item2img
        item2.grid(row=3,column=1)

        item3img = PhotoImage(file='ClothesImages/blackdress.png')
        item3 = Label(self, image=item3img)
        item3.photo = item3img
        item3.grid(row=3,column=2)

        fill2=LabelFrame(self, width=10, borderwidth=0, highlightthickness=0, bg="white")
        fill2.grid(row=0, column=0, columnspan=3)


"""
home_frame = Frame(window)
home_frame.grid(row=0, column=1)
home_frame.rowconfigure(0, minsize=50, weight=1)
"""

"""
lbl_value = tk.Label(master=window, text="Start a Trade")
lbl_value.grid(row=0, column=0, columnspan=3)

b_home = tk.Button(master=window, text="Back to Home", width=50)
b_home.grid(row=4, column=0, sticky="nsw")

b_start = tk.Button(master=window, text="Start a Trade", width=200)
b_start.grid(row=1, rowspan=2, column=1, columnspan=3, sticky="nsew")

btn_increase = tk.Button(master=window, text="Tokens", width=50)
btn_increase.grid(row=4, column=4, sticky="nse")
"""

app = startApp()
app.geometry("1920x1080")
app.mainloop()