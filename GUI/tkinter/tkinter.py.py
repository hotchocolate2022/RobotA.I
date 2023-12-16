#RESPONSIVE LAYOUT
#part 1 : Creating thee first group of widgets
#Part 2_Creating the Rest of the widgets
#Part 3_Retrieving the data from the checkbutton
#Part 4_Validation and error popups


import tkinter
from tkinter import ttk 
##TTK stands for Themed tkinter

from tkinter import messagebox


def enter_data():  #Function for the the button is clicked go ahead and execute the function enter data.
    # User info

    accepted = accept_var.get()

    if accepted == "Accepted":

        firstname = first_name_entry.get()#Retrieving the data from the input Widgets
        lastname = last_name_entry.get()# get function is to get the contects of this entry

        if firstname and lastname:

                title = title_combobox.get()
                age = age_spinbox.get()
                nationality = nationality_combobox.get()

                #Course info
                registration_status = reg_status_var.get()
                numcourses = numcourses_spinbox.get()
                numsemesters = numsemesters_spinbox.get()
    


                print("First name: ", firstname, "Last name: ", lastname) 
                print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
                print("# Courses: ", numcourses, "# Semseters ", numsemesters)
                print("Registration status", registration_status)
                print("----------------------------------------------------------------------")
        else:
                tkinter.messagebox.showwarning(title= "Error", message="First name and last name are required" )
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms" ) #For warning Pop up


#Part 3_Retrieving the data from the checkbutton
"""registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", 
                                       variable=reg_status_var, onvalue="Registered" , offvalue="Not Registered" )"""

#Assigned a default value of this check button





window = tkinter.Tk() #this is the root window all details are inside hier like a box (Parent window)
window.title("Data Entry Form")


#Placing all widgets

#geometry manager for placing on the screen
#layout manager 
#stack list Frames they are part of grid
frame = tkinter.Frame(window)
frame.pack()


#Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information") #This is a label Frame is not a Frame! First parameter is frame and second is text
user_info_frame.grid(row= 0, column=0, padx=20, pady=10) #pad x and y give to label Frame space from window
#anytime you use .grid you need to say row then specify a number and column then specify a number again.
#zero means row zero and column zero and not row 1 or column 1 like value of index sarting from zero.


#This is a Frame with border and Title this will able to group different widgets in interface
first_name_label = tkinter.Label(user_info_frame, text="First_Name")#Creating widgets inside of this label Frame (First Step). Second step is going to packing, placing it or grid
first_name_label.grid(row= 0, column=0)#This grid is inside of Label Frame
last_name_label = tkinter.Label(user_info_frame, text= "Last_Name")
last_name_label.grid(row= 0, column=1)


first_name_entry = tkinter.Entry(user_info_frame) #Entry is a textbox where user write as a input
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)




title_label = tkinter.Label(user_info_frame, text="Title")

#Combobox we need to import ttk beacuse comboboxitself doesnot exist t kinter
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "MS.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2) #In user information Label the seocnd grid is values of Combobox



#Spinbox
age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_ =18, to=110) #We give ounter with values for age from 18 to 110
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

#Combobox for users nationality
nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Germany", "Afrika", "Asia", "North-Amerika", "South-Amerika", "Europe"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

#Changing the padding for all of the Widgets

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


#Part 2_Creating the Rest of the widgets



#Saving Course Info

courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)#Sticky use it within the grid parameter within the grid function
#Padding is much better to like more formal data form

registered_label = tkinter.Label(courses_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")# This StrningVar will always contain the value of my check button
# Status Variable. This actually store the information of our check button

registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", 
                                       variable=reg_status_var, onvalue="Registered" , offvalue="Not Registered" )
# Onvalue is what the value of this check button will be when its actually checked this gonna be registered.


registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity') #spinbox is infinity numbers
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity') #spinbox is infinity numbers
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)


for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)



#Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Text & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)


accept_var = tkinter.StringVar(value="Not accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                                  variable=accept_var, onvalue= "Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)


# Button 
button = tkinter.Button(frame, text= "Enter data", command= enter_data) # This command mean wenn the button is clicked go ahead and execute the function enter data. 
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)




#Retrieving the data from the input Widgets


window.mainloop() # this must be always hier

