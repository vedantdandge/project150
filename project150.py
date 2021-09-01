from tkinter import *
import random

root=Tk()
root.title("Country Capitals")
root.geometry("500x500")

enter_country = Entry(root)
enter_country.place(relx = 0.5,rely = 0.2, anchor = CENTER)

enter_capitals = Entry(root)
enter_capitals.place(relx = 0.5,rely = 0.3, anchor = CENTER)

country_list = Label(root)
capital_list_label = Label(root)
country_list_label = Label(root)
city_list_label = Label(root)

list1 = []
list2 = []

def addcountry():
    country_name = enter_country.get()
    list1.append(country_name)
    country_list["text"] = "Country Name : "+str(list1)
    
def addcapital():
    capital_name = enter_capitals.get()
    list2.append(capital_name)
    capital_list_label["text"] = "Capital Name : "+str(list2)
    
def countrylist():
    length = len(list2)
    random_no = random.randint(0, length-2)
    display_country_list["text"] = "Country Name :" + str(country_list)

def capitallist():
    length = len(list2)
    random_no = random.randint(0, length-2)
    display_capital_list["text"] = "Capital Name :" +str(capital_list_label)
    
btn = Button(root, text="Display Country And City Names: ", command = addcountry)
btn.place(relx = 0.5,rely= 0.4, anchor = CENTER)

root.mainloop()