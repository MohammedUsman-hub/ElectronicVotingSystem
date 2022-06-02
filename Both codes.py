import tkinter
import tkinter as tk
import time as tm          # Importing time package to use (Usman)
import tkinter.messagebox  # Importing time package to use (Usman)
import tkinter.ttk as ttk




# LogIn Page
window = tkinter.Tk()                  # Creates a new window using Tkinter (Usman)
window.title("Login Page")             # Gives a title for the window  (Usman)
window.geometry('390x190')             # Creates the size of the window (Usman)
tkinter.Label(window, text = "If you do not have an account click on register", fg = 'Red').grid(row = 4, column = 0)
tkinter.Label(window, text = "Username").grid(row = 0, column = 0)    # The .Label allows user to type data into the available space (Usman)
tkinter.Entry(window).grid(row = 0, column = 1)                       # Places the lables in a certain posiiton within the window (Usman)
tkinter.Label(window, text = "Password").grid(row = 1, column = 0)
tkinter.Entry(window).grid(row = 1, column =1)
tkinter.Checkbutton(window, text = "Keep Me Logged In").grid(columnspan = 2) # This Creates a checkbutton to allow the user to choose an option to keep them logged in (Usman)
tkinter.Button = tkinter.Button # Creates a button for this window (Usman)
tkinter.Button(window, text = "Login").grid(row = 6)                        # Creates a button for this window (Usman)





# Register Page
def create_window():                # Creates a function (Usman)
    window = tkinter.Tk()
    window.title("Registration")
    window.geometry('350x150')
    tkinter.Label(window, text="Username").grid(row=0)
    tkinter.Entry(window).grid(row=0, column=1)
    tkinter.Label(window, text="Password").grid(row=1)
    tkinter.Entry(window).grid(row=1, column=1)
    tkinter.Button(window, text="Register", command = reg_comp).grid(row=6, column=1)
tkinter.Button(window, text = "Register", command = create_window).grid(row = 7)
tkinter.messagebox.showinfo('Welcome!', 'Click OK To Continue!') # A message box which welcomes the user (Usman)

def reg_comp():
    tkinter.messagebox.showinfo('Registration', 'Registration Is Complete!') # A message box which tells the user that the registration is successful (Usman)





# Deadline Time
def display_time():
    current_time = tm.strftime('%I:%M:%S:%p')  # A variable that is showing a digital time (Usman)
    clock_label['text'] = current_time         # Displays the digital time (Usman)
    clock_label.after(1000,display_time)       # The speed of the counting of time (Usman)

window = tkinter.Tk()                          # Creates a new window
window.title('Deadline Time')
window.geometry('250x190')
tkinter.Label(window, text = "Deadline Will Close At Midnight!", font = 'ariel 12', fg = 'Red').grid(row = 10) # Displays a message to the user, with where it will be placed on the user as well as the font colour (Usman)
clock_label = tk.Label(window, font = 'ariel 30')  # Displays the font and font size of the digital clock (Usman)
clock_label.grid(row = 0, column = 0) # Places the digital clock in a certain position in the window (Usman)
display_time()                        # Implements the code (Usman)





#def job_des():
window = tkinter.Tk()
window.title("GSU Job Description ")
window.geometry('300x200')
tkinter.Label(window, text = "Please click on the position you're interested in", fg = 'Green').grid(row = 0)
tkinter.Checkbutton(window, text = "GSU Officer").grid(row = 1, column = 0)
tkinter.Checkbutton(window, text = "President").grid(row = 2, column = 0)
tkinter.Checkbutton(window, text = "Faculty Officer").grid(row = 3, column = 0)
tkinter.Checkbutton(window, text = "Socail").grid(row = 4, column = 0)
tkinter.Button(window, text = "Apply").grid(row = 5)

#def apply_pos():
 #   tkinter.messagebox.showinfo('Position Role', 'You have been applied to this role')





# Text Files
def wordcount(filename, listwords):   # Creates a function (Usman)
    try:
        file = open(filename, 'r')    # Opens a file but allows an reading option (Usman)
        read = file.readlines()
        file.close()                  # closes the file (Usman)
        for word in listwords:
            lower = word.lower()
            count = 0                # Counts the values in the text script 0 = false 1 = True (Usman)
            for sentance in read:
                line = sentance.split()
                for each in line:
                    line2 = each.lower()
                    if lower == line2:
                        count += 1
            print(lower, ":", count)   # Makes the outcome look more neat and presentable (Usman)
    except FileExistsError:
        print("No Such File Exist")    # If there is no file that exists, then this message will be printed (Usman)
wordcount("StudentVoters.txt", ["as6445f", "anumsheikhpetersmith", "petersmith1annaparker", "annaparker1"]) # Stating what user ID should have access to login from the text files (Usman)


# Anum Sheikh: opening GSUCandidates file for reading
f = open("GSUCandidates.txt", "r")
line = f.readlines()

#Anum Sheikh: Defining one class in order for all windows and their respective "Next!" buttons to work and link
class President:
    # Anum Sheikh: defining a function for president


    def __init__(self):
        # Anum Sheikh: making a window using tkinter
        self.window = tkinter.Tk()

        # Anum Sheikh: declaring specific president buttons as integers in order to use them to count total votes
        self.presbtn1 = tkinter.IntVar()
        self.presbtn2 = tkinter.IntVar()
        self.presbtn3 = tkinter.IntVar()
        self.presbtn4 = tkinter.IntVar()

        # Anum Sheikh: declaring and making individual buttons for president voting page, for each row and column
        # Buttons1
        self.presrad1 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.presbtn1).grid(column=1, row=0)
        self.presrad2 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.presbtn1).grid(column=2, row=0)
        self.presrad3 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.presbtn1).grid(column=3, row=0)
        self.presrad4 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.presbtn1).grid(column=4, row=0)

        # Buttons2
        self.presrad5 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.presbtn2).grid(column=1, row=1)
        self.presrad6 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.presbtn2).grid(column=2, row=1)
        self.presrad7 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.presbtn2).grid(column=3, row=1)
        self.presrad8 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.presbtn2).grid(column=4, row=1)

        # Buttons3
        self.presrad9 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.presbtn3).grid(column=1, row=2)
        self.presrad10 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.presbtn3).grid(column=2, row=2)
        self.presrad11 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.presbtn3).grid(column=3, row=2)
        self.presrad12 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.presbtn3).grid(column=4, row=2)

        # Buttons4
        self.presrad13 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.presbtn4).grid(column=1, row=3)
        self.presrad14 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.presbtn4).grid(column=2, row=3)
        self.presrad15 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.presbtn4).grid(column=3, row=3)
        self.presrad16 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.presbtn4).grid(column=4, row=3)

        # Anum Sheikh: making the pop-up window and getting the specific candidates from GSUCandidates.txt file
        self.window.title("President Candidates")
        self.window.geometry('400x250')
        self.President = line[0], line[1], line[2], line[3]

        # Anum Sheikh: loop to print each candidate on the window running for president
        j = 0
        for i in self.President:
            self.label = tkinter.Label(self.window, text=i).grid(row=j, column=0)
            j = j + 1

        # Anum Sheikh: making buttons which will save user's votes (Save! button) and will take them to next voting page (Next! button)
        self.Button = tkinter.Button
        self.saveButton = self.Button(self.window, text="Save!", command=self.presidentvote).grid()
        self.nextButton = self.Button(self.window, text="Next!", command=self.officer).grid()

        # Anum Sheikh: implementing the window
        self.window.mainloop()

    # Anum Sheikh: defining a function for getting the president votes of user
    def presidentvote(self):
        # Anum Sheikh: opening votes text file, get() method gets answer pressed by user and appends it to text file with their candidate preference.
        g = open("Votes.txt", "a")
        g.write(" User's President Votes are:" + "\n")
        self.pres1 = self.presbtn1.get()
        g.write("Alan Smith got:" + str(self.pres1) + "\n")
        self.pres2 = self.presbtn2.get()
        g.write("Jon Adams got:" + str(self.pres2) + "\n")
        self.pres3 = self.presbtn3.get()
        g.write("Lizzy Jones got:" + str(self.pres3) + "\n")
        self.pres4 = self.presbtn4.get()
        g.write("Zia Ahmed got:" + str(self.pres4) + "\n")
        # Anum Sheikh: closes text file
        g.close()

    # Anum Sheikh: defining a function for officer
    def officer(self):
        # Anum Sheikh: making a window using tkinter
        self.window = tkinter.Tk()
        self.window.title("Officer Candidates")
        self.window.geometry('450x250')
        # Anum Sheikh: getting the specific candidates from GSUCandidates.txt file
        self.officercan = line[4], line[5], line[6], line[7]

        # Anum Sheikh: declaring specific officer buttons as integers in order to use them to count total votes
        self.offbtn1 = tkinter.IntVar()
        self.offbtn2 = tkinter.IntVar()
        self.offbtn3 = tkinter.IntVar()
        self.offbtn4 = tkinter.IntVar()

        # Anum Sheikh: declaring and making individual buttons for officer voting page, for each row and column
        # Buttons1
        self.offrad1 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.offbtn1).grid(column=2, row=0)
        self.offrad2 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.offbtn1).grid(column=3, row=0)
        self.offrad3 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.offbtn1).grid(column=4, row=0)
        self.offrad4 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.offbtn1).grid(column=5, row=0)

        # Buttons2
        self.offrad5 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.offbtn2).grid(column=2, row=1)
        self.offrad6 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.offbtn2).grid(column=3, row=1)
        self.offrad7 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.offbtn2).grid(column=4, row=1)
        self.offrad8 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.offbtn2).grid(column=5, row=1)

        # Buttons3
        self.offrad9 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.offbtn3).grid(column=2, row=2)
        self.offrad10 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.offbtn3).grid(column=3, row=2)
        self.offrad11 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.offbtn3).grid(column=4, row=2)
        self.offrad12 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.offbtn3).grid(column=5, row=2)

        # Buttons4
        self.offrad13 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.offbtn4).grid(column=2, row=3)
        self.offrad14 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.offbtn4).grid(column=3, row=3)
        self.offrad15 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.offbtn4).grid(column=4, row=3)
        self.offrad16 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.offbtn4).grid(column=5, row=3)

        # Anum Sheikh: loop to print each candidate on the window running for officer
        j = 0
        for i in self.officercan:
            self.label = tkinter.Label(self.window, text=i).grid(row=j, column=0)
            j = j + 1

        # Anum Sheikh: making buttons which will save user's votes (Save! button) and will take them to next voting page (Next! button)
        self.Button = tkinter.Button
        self.saveButton = self.Button(self.window, text="Save!", command=self.officervote).grid()
        self.nextButton = self.Button(self.window, text="Next!", command=self.lasfaculty).grid()
        # Anum Sheikh: implementing the window
        self.window.mainloop()

    # Anum Sheikh: defining a function for getting the officer votes of user
    def officervote(self):
        # Anum Sheikh: opening votes text file, get() method gets answer pressed by user and appends it to text file with their candidate preference.
        g = open("Votes.txt", "a")
        g.write("User's Officer Votes are:" + "\n")
        self.officer1 = self.offbtn1.get()
        g.write("Penelope Dominguez got:" + str(self.officer1) + "\n")
        self.officer2 = self.offbtn2.get()
        g.write("Hamza Hooper got:" + str(self.officer2) + "\n")
        self.officer3 = self.offbtn3.get()
        g.write("Virginia Pike got:" + str(self.officer3) + "\n")
        self.officer4 = self.offbtn4.get()
        g.write("Kirsty Lugo got:" + str(self.officer4) + "\n")
        # Anum Sheikh: closes text file
        g.close()

    # Anum Sheikh: defining a function for lasfaculty
    def lasfaculty(self):
        # Anum Sheikh: making a window using tkinter
        self.window = tkinter.Tk()
        self.window.title("Liberal Arts and Sciences Faculty Candidates")
        self.window.geometry('600x400')

        # Anum Sheikh: declaring specific lasfaculty buttons as integers in order to use them to count total votes
        self.lasbtn1 = tkinter.IntVar()
        self.lasbtn2 = tkinter.IntVar()
        self.lasbtn3 = tkinter.IntVar()
        self.lasbtn4 = tkinter.IntVar()
        self.lasbtn5 = tkinter.IntVar()
        self.lasbtn6 = tkinter.IntVar()

        # Anum Sheikh: declaring and making individual buttons for lasfaculty voting page, for each row and column
        # Buttons1
        self.lasrad1 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.lasbtn1).grid(column=1,
                                                                                                         row=0)
        self.lasrad2 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.lasbtn1).grid(column=2,
                                                                                                          row=0)
        self.lasrad3 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.lasbtn1).grid(column=3,
                                                                                                         row=0)
        self.lasrad4 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.lasbtn1).grid(column=4,
                                                                                                          row=0)
        self.lasrad5 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.lasbtn1).grid(column=5,
                                                                                                         row=0)
        self.lasrad6 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.lasbtn1).grid(column=6,
                                                                                                         row=0)

        # Buttons2
        self.lasrad7 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.lasbtn2).grid(column=1,
                                                                                                         row=1)
        self.lasrad8 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.lasbtn2).grid(column=2,
                                                                                                          row=1)
        self.lasrad9 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.lasbtn2).grid(column=3,
                                                                                                         row=1)
        self.lasrad10 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.lasbtn2).grid(column=4,
                                                                                                           row=1)
        self.lasrad11 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.lasbtn2).grid(column=5,
                                                                                                          row=1)
        self.lasrad12 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.lasbtn2).grid(column=6,
                                                                                                          row=1)

        # Buttons3
        self.lasrad13 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.lasbtn3).grid(column=1,
                                                                                                          row=2)
        self.lasrad14 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.lasbtn3).grid(column=2,
                                                                                                           row=2)
        self.lasrad15 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.lasbtn3).grid(column=3,
                                                                                                          row=2)
        self.lasrad16 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.lasbtn3).grid(column=4,
                                                                                                           row=2)
        self.lasrad17 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.lasbtn3).grid(column=5,
                                                                                                          row=2)
        self.lasrad18 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.lasbtn3).grid(column=6,
                                                                                                          row=2)

        # Buttons4
        self.lasrad19 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.lasbtn4).grid(column=1,
                                                                                                          row=3)
        self.lasrad20 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.lasbtn4).grid(column=2,
                                                                                                           row=3)
        self.lasrad21 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.lasbtn4).grid(column=3,
                                                                                                          row=3)
        self.lasrad22 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.lasbtn4).grid(column=4,
                                                                                                           row=3)
        self.lasrad23 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.lasbtn4).grid(column=5,
                                                                                                          row=3)
        self.lasrad24 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.lasbtn4).grid(column=6,
                                                                                                          row=3)
        # Buttons5
        self.lasrad25 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.lasbtn5).grid(column=1,
                                                                                                          row=4)
        self.lasrad26 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.lasbtn5).grid(column=2,
                                                                                                           row=4)
        self.lasrad27 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.lasbtn5).grid(column=3,
                                                                                                          row=4)
        self.lasrad28 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.lasbtn5).grid(column=4,
                                                                                                           row=4)
        self.lasrad29 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.lasbtn5).grid(column=5,
                                                                                                          row=4)
        self.lasrad30 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.lasbtn5).grid(column=6,
                                                                                                          row=4)

        # Buttons6
        self.lasrad31 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.lasbtn6).grid(column=1,
                                                                                                          row=5)
        self.lasrad32 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.lasbtn6).grid(column=2,
                                                                                                           row=5)
        self.lasrad33 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.lasbtn6).grid(column=3,
                                                                                                          row=5)
        self.lasrad34 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.lasbtn6).grid(column=4,
                                                                                                           row=5)
        self.lasrad35 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.lasbtn6).grid(column=5,
                                                                                                          row=5)
        self.lasrad36 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.lasbtn6).grid(column=6,
                                                                                                          row=5)

        # Anum Sheikh: getting the specific candidates from GSUCandidates.txt file
        self.LAS = line[8], line[9], line[10], line[11], line[12], line[13]
        # Anum Sheikh: loop to print each candidate on the window running for president
        j = 0
        for i in self.LAS:
            self.label = tkinter.Label(self.window, text=i).grid(row=j, column=0)
            j = j + 1

        # Anum Sheikh: making buttons which will save user's votes (Save! button) and will take them to next voting page (Next! button)
        self.Button = tkinter.Button
        self.saveButton = self.Button(self.window, text="Save!", command=self.lasfacultyvote).grid()
        self.nextButton = self.Button(self.window, text="Next!", command=self.business).grid()
        # Anum Sheikh: implementing the window
        self.window.mainloop()

    # Anum Sheikh: defining a function for getting the lasfaculty votes of user
    def lasfacultyvote(self):
        # Anum Sheikh: opening votes text file, get() method gets answer pressed by user and appends it to text file with their candidate preference.
        g = open("Votes.txt", "a")
        g.write("User's Liberal Arts and Sciences Votes are:" + "\n")
        self.las1 = self.lasbtn1.get()
        g.write("Brianna Noel got:" + str(self.las1) + "\n")
        self.las2 = self.lasbtn2.get()
        g.write("Brandon Briggs got:" + str(self.las2) + "\n")
        self.las3 = self.lasbtn3.get()
        g.write("Solomon Cross got:" + str(self.las3) + "\n")
        self.las4 = self.lasbtn4.get()
        g.write("Ruby Clay got:" + str(self.las4) + "\n")
        self.las5 = self.lasbtn5.get()
        g.write("Matteo West got:" + str(self.las5) + "\n")
        self.las6 = self.lasbtn6.get()
        g.write("Zayn Gray got:" + str(self.las6) + "\n")
        # Anum Sheikh: closes text file
        g.close()

    # Anum Sheikh: defining a function for business faculty
    def business(self):
        # Anum Sheikh: making a window using tkinter
        self.window = tkinter.Tk()
        self.window.title("Business Faculty Candidates")
        self.window.geometry('600x300')

        # Anum Sheikh: declaring specific business buttons as integers in order to use them to count total votes
        self.bussbtn1 = tkinter.IntVar()
        self.bussbtn2 = tkinter.IntVar()
        self.bussbtn3 = tkinter.IntVar()
        self.bussbtn4 = tkinter.IntVar()
        self.bussbtn5 = tkinter.IntVar()
        self.bussbtn6 = tkinter.IntVar()

        # Anum Sheikh: declaring and making individual buttons for business voting page, for each row and column
        # Buttons1
        self.business1 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.bussbtn1).grid(column=1,
                                                                                                       row=0)
        self.business2 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.bussbtn1).grid(column=2,
                                                                                                        row=0)
        self.business3 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.bussbtn1).grid(column=3,
                                                                                                       row=0)
        self.business4 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.bussbtn1).grid(column=4,
                                                                                                        row=0)
        self.business5 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.bussbtn1).grid(column=5,
                                                                                                       row=0)
        self.business6 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.bussbtn1).grid(column=6,
                                                                                                       row=0)

        # buttons2
        self.business7 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.bussbtn2).grid(column=1,
                                                                                                       row=1)
        self.business8 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.bussbtn2).grid(column=2,
                                                                                                        row=1)
        self.business9 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.bussbtn2).grid(column=3,
                                                                                                       row=1)
        self.business10 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.bussbtn2).grid(column=4,
                                                                                                         row=1)
        self.business11 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.bussbtn2).grid(column=5,
                                                                                                        row=1)
        self.business12 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.bussbtn2).grid(column=6,
                                                                                                        row=1)

        # Buttons3
        self.business13 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.bussbtn3).grid(column=1,
                                                                                                        row=2)
        self.business14 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.bussbtn3).grid(column=2,
                                                                                                         row=2)
        self.business15 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.bussbtn3).grid(column=3,
                                                                                                        row=2)
        self.business16 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.bussbtn3).grid(column=4,
                                                                                                         row=2)
        self.business17 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.bussbtn3).grid(column=5,
                                                                                                        row=2)
        self.business18 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.bussbtn3).grid(column=6,
                                                                                                        row=2)

        # Buttons4
        self.business19 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.bussbtn4).grid(column=1,
                                                                                                        row=3)
        self.business20 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.bussbtn4).grid(column=2,
                                                                                                         row=3)
        self.business21 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.bussbtn4).grid(column=3,
                                                                                                        row=3)
        self.business22 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.bussbtn4).grid(column=4,
                                                                                                         row=3)
        self.business23 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.bussbtn4).grid(column=5,
                                                                                                        row=3)
        self.business24 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.bussbtn4).grid(column=6,
                                                                                                        row=3)
        # Buttons5
        self.business25 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.bussbtn5).grid(column=1,
                                                                                                        row=4)
        self.business26 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.bussbtn5).grid(column=2,
                                                                                                         row=4)
        self.business27 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.bussbtn5).grid(column=3,
                                                                                                        row=4)
        self.business28 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.bussbtn5).grid(column=4,
                                                                                                         row=4)
        self.business29 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.bussbtn5).grid(column=5,
                                                                                                        row=4)
        self.business30 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.bussbtn5).grid(column=6,
                                                                                                        row=4)

        # Buttons6
        self.business31 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.bussbtn6).grid(column=1,
                                                                                                        row=5)
        self.business32 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.bussbtn6).grid(column=2,
                                                                                                         row=5)
        self.business33 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.bussbtn6).grid(column=3,
                                                                                                        row=5)
        self.business34 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.bussbtn6).grid(column=4,
                                                                                                         row=5)
        self.business35 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.bussbtn6).grid(column=5,
                                                                                                        row=5)
        self.business36 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.bussbtn6).grid(column=6,
                                                                                                        row=5)

        # Anum Sheikh: getting the specific candidates from GSUCandidates.txt file
        self.Business = line[14], line[15], line[16], line[17], line[18], line[19]
        # Anum Sheikh: loop to print each candidate on the window running for business
        j = 0
        for i in self.Business:
            self.label = tkinter.Label(self.window, text=i).grid(row=j, column=0)
            j = j + 1

        # Anum Sheikh: making buttons which will save user's votes (Save! button) and will take them to next voting page (Next! button)
        self.Button = tkinter.Button
        self.saveButton = self.Button(self.window, text="Save!", command=self.businessvote).grid()
        self.nextButton = self.Button(self.window, text="Next!", command=self.edandhealth).grid()
        # Anum Sheikh: implementing the window
        self.window.mainloop()

    # Anum Sheikh: defining a function for getting the business votes of user
    def businessvote(self):
        # Anum Sheikh: opening votes text file, get() method gets answer pressed by user and appends it to text file with their candidate preference.
        g = open("Votes.txt", "a")
        g.write("User's Business Votes are:" + "\n")
        self.busvote1 = self.bussbtn1.get()
        g.write("Jasmine Edwards got:" + str(self.busvote1) + "\n")
        self.busvote2 = self.bussbtn2.get()
        g.write("Finn Cameron got:" + str(self.busvote2) + "\n")
        self.busvote3 = self.bussbtn3.get()
        g.write("Alyssia Read got:" + str(self.busvote3) + "\n")
        self.busvote4 = self.bussbtn4.get()
        g.write("Hailey Shields got:" + str(self.busvote4) + "\n")
        self.busvote5 = self.bussbtn5.get()
        g.write("Josh Christian got:" + str(self.busvote5) + "\n")
        self.busvote6 = self.bussbtn6.get()
        g.write("Jordyn Boyer got:" + str(self.busvote6) + "\n")
        # Anum Sheikh: closes text file
        g.close()

    # Anum Sheikh: defining a function for edandhealth faculty
    def edandhealth(self):
        # Anum Sheikh: making a window using tkinter
        self.window = tkinter.Tk()
        self.window.title("Education and Health Faculty Candidates")
        self.window.geometry('700x400')

        # Anum Sheikh: declaring specific edandhealth buttons as integers in order to use them to count total votes
        self.EandHbtn1 = tkinter.IntVar()
        self.EandHbtn2 = tkinter.IntVar()
        self.EandHbtn3 = tkinter.IntVar()
        self.EandHbtn4 = tkinter.IntVar()
        self.EandHbtn5 = tkinter.IntVar()
        self.EandHbtn6 = tkinter.IntVar()
        self.EandHbtn7 = tkinter.IntVar()

        # Anum Sheikh: declaring and making individual buttons for edandhealth voting page, for each row and column
        # Buttons1
        self.EandH1 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.EandHbtn1).grid(column=1,
                                                                                                         row=0)
        self.EandH2 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.EandHbtn1).grid(column=2,
                                                                                                          row=0)
        self.EandH3 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.EandHbtn1).grid(column=3,
                                                                                                         row=0)
        self.EandH4 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.EandHbtn1).grid(column=4,
                                                                                                          row=0)
        self.EandH5 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.EandHbtn1).grid(column=5,
                                                                                                         row=0)
        self.EandH6 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.EandHbtn1).grid(column=6,
                                                                                                         row=0)
        self.EandH7 = ttk.Radiobutton(self.window, text='seventh', value=7, variable=self.EandHbtn1).grid(column=7,
                                                                                                        row=0)
        # Buttons2
        self.EandH8 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.EandHbtn2).grid(column=1,
                                                                                                         row=1)
        self.EandH9 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.EandHbtn2).grid(column=2,
                                                                                                          row=1)
        self.EandH10 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.EandHbtn2).grid(column=3,
                                                                                                         row=1)
        self.EandH11 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.EandHbtn2).grid(column=4,
                                                                                                           row=1)
        self.EandH12 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.EandHbtn2).grid(column=5,
                                                                                                          row=1)
        self.EandH13 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.EandHbtn2).grid(column=6,
                                                                                                          row=1)
        self.EandH14 = ttk.Radiobutton(self.window, text='seventh', value=7, variable=self.EandHbtn2).grid(column=7,
                                                                                                          row=1)

        # Buttons3
        self.EandH15 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.EandHbtn3).grid(column=1,
                                                                                                          row=2)
        self.EandH16 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.EandHbtn3).grid(column=2,
                                                                                                           row=2)
        self.EandH17= ttk.Radiobutton(self.window, text='third', value=3, variable=self.EandHbtn3).grid(column=3,
                                                                                                          row=2)
        self.EandH18 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.EandHbtn3).grid(column=4,
                                                                                                           row=2)
        self.EandH19 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.EandHbtn3).grid(column=5,
                                                                                                          row=2)
        self.EandH20 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.EandHbtn3).grid(column=6,
                                                                                                          row=2)
        self.EandH21 = ttk.Radiobutton(self.window, text='seventh', value=7, variable=self.EandHbtn3).grid(column=7,
                                                                                                          row=2)

        # Buttons4
        self.EandH22 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.EandHbtn4).grid(column=1,
                                                                                                          row=3)
        self.EandH23 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.EandHbtn4).grid(column=2,
                                                                                                           row=3)
        self.EandH24 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.EandHbtn4).grid(column=3,
                                                                                                          row=3)
        self.EandH25 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.EandHbtn4).grid(column=4,
                                                                                                           row=3)
        self.EandH26 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.EandHbtn4).grid(column=5,
                                                                                                          row=3)
        self.EandH27 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.EandHbtn4).grid(column=6,
                                                                                                          row=3)
        self.EandH28 = ttk.Radiobutton(self.window, text='seventh', value=7, variable=self.EandHbtn4).grid(column=7,
                                                                                                          row=3)
        # Buttons5
        self.EandH29 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.EandHbtn5).grid(column=1,
                                                                                                          row=4)
        self.EandH30 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.EandHbtn5).grid(column=2,
                                                                                                           row=4)
        self.EandH31 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.EandHbtn5).grid(column=3,
                                                                                                          row=4)
        self.EandH32 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.EandHbtn5).grid(column=4,
                                                                                                           row=4)
        self.EandH33 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.EandHbtn5).grid(column=5,
                                                                                                          row=4)
        self.EandH34 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.EandHbtn5).grid(column=6,
                                                                                                          row=4)
        self.EandH35 = ttk.Radiobutton(self.window, text='seventh', value=7, variable=self.EandHbtn5).grid(column=7,
                                                                                                          row=4)

        # Buttons6
        self.EandH36 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.EandHbtn6).grid(column=1,
                                                                                                          row=5)
        self.EandH37 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.EandHbtn6).grid(column=2,
                                                                                                           row=5)
        self.EandH38 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.EandHbtn6).grid(column=3,
                                                                                                          row=5)
        self.EandH39 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.EandHbtn6).grid(column=4,
                                                                                                           row=5)
        self.EandH40 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.EandHbtn6).grid(column=5,
                                                                                                          row=5)
        self.EandH41 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.EandHbtn6).grid(column=6,
                                                                                                          row=5)
        self.EandH42 = ttk.Radiobutton(self.window, text='seventh', value=7, variable=self.EandHbtn6).grid(column=7,
                                                                                                          row=5)

        # Button 7
        self.EandH43 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.EandHbtn7).grid(column=1,
                                                                                                          row=6)
        self.EandH44 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.EandHbtn7).grid(column=2,
                                                                                                           row=6)
        self.EandH45 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.EandHbtn7).grid(column=3,
                                                                                                          row=6)
        self.EandH46 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.EandHbtn7).grid(column=4,
                                                                                                           row=6)
        self.EandH47 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.EandHbtn7).grid(column=5,
                                                                                                          row=6)
        self.EandH48 = ttk.Radiobutton(self.window, text='sixth', value=6, variable=self.EandHbtn7).grid(column=6,
                                                                                                          row=6)
        self.EandH49 = ttk.Radiobutton(self.window, text='seventh', value=7, variable=self.EandHbtn7).grid(column=7,
                                                                                                          row=6)

        # Anum Sheikh: getting the specific candidates from GSUCandidates.txt file
        self.EdAndHealth = line[20], line[21], line[22], line[23], line[24], line[25], line[26]
        # Anum Sheikh: loop to print each candidate on the window running for ed and health
        j = 0
        for i in self.EdAndHealth:
            self.label = tkinter.Label(self.window, text=i).grid(row=j, column=0)
            j = j + 1

        # Anum Sheikh: making buttons which will save user's votes (Save! button) and will take them to next voting page (Next! button)
        self.Button = tkinter.Button
        self.saveButton = self.Button(self.window, text="Save!", command=self.edandhealthvote).grid()
        self.nextButton = self.Button(self.window, text="Next!", command=self.engsci).grid()
        # Anum Sheikh: implementing the window
        self.window.mainloop()

    # Anum Sheikh: defining a function for getting the edandhealth votes of user
    def edandhealthvote(self):
        # Anum Sheikh: opening votes text file, get() method gets answer pressed by user and appends it to text file with their candidate preference.
        g = open("Votes.txt", "a")
        g.write("User's Ed and Health Votes are:" + "\n")
        self.eah1 = self.EandHbtn1.get()
        g.write("Manuel Hobbs got:" + str(self.eah1) + "\n")
        self.eah2 = self.EandHbtn2.get()
        g.write("Grayson Best got:" + str(self.eah2) + "\n")
        self.eah3 = self.EandHbtn3.get()
        g.write("Waseem Parson got:" + str(self.eah3) + "\n")
        self.eah4 = self.EandHbtn4.get()
        g.write("Madeline Sparrow got:" + str(self.eah4) + "\n")
        self.eah5 = self.EandHbtn5.get()
        g.write("Casey Reese got:" + str(self.eah5) + "\n")
        self.eah6 = self.EandHbtn6.get()
        g.write("Mike Warner got:" + str(self.eah6) + "\n")
        self.eah7 = self.EandHbtn7.get()
        g.write("Jaden Chang got:" + str(self.eah7) + "\n")
        # Anum Sheikh: closes text file
        g.close()

    # Anum Sheikh: defining a function for engsci
    def engsci(self):
        # Anum Sheikh: making a window using tkinter
        self.window = tkinter.Tk()
        self.window.title("Engineering and Science Faculty Candidates")
        self.window.geometry('600x300')

        # Anum Sheikh: declaring specific engsci buttons as integers in order to use them to count total votes
        self.engscibtn1 = tkinter.IntVar()
        self.engscibtn2 = tkinter.IntVar()
        self.engscibtn3 = tkinter.IntVar()
        self.engscibtn4 = tkinter.IntVar()
        self.engscibtn5 = tkinter.IntVar()

        # Anum Sheikh: declaring and making individual buttons for engsci voting page, for each row and column
        # Buttons1
        self.engsci1 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.engscibtn1).grid(column=1,
                                                                                                       row=0)
        self.engsci2 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.engscibtn1).grid(column=2,
                                                                                                        row=0)
        self.engsci3 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.engscibtn1).grid(column=3,
                                                                                                       row=0)
        self.engsci4 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.engscibtn1).grid(column=4,
                                                                                                        row=0)
        self.engsci5 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.engscibtn1).grid(column=5,
                                                                                                       row=0)

        # Buttons2
        self.engsci6 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.engscibtn2).grid(column=1,
                                                                                                       row=1)
        self.engsci7 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.engscibtn2).grid(column=2,
                                                                                                        row=1)
        self.engsci8 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.engscibtn2).grid(column=3,
                                                                                                       row=1)
        self.engsci9 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.engscibtn2).grid(column=4,
                                                                                                         row=1)
        self.engsci10 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.engscibtn2).grid(column=5,
                                                                                                        row=1)


        # Buttons3
        self.engsci11 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.engscibtn3).grid(column=1,
                                                                                                        row=2)
        self.engsci12 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.engscibtn3).grid(column=2,
                                                                                                         row=2)
        self.engsci13 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.engscibtn3).grid(column=3,
                                                                                                        row=2)
        self.engsci14 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.engscibtn3).grid(column=4,
                                                                                                         row=2)
        self.engsci15 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.engscibtn3).grid(column=5,
                                                                                                        row=2)


        # Buttons4
        self.engsci16 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.engscibtn4).grid(column=1,
                                                                                                        row=3)
        self.engsci17 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.engscibtn4).grid(column=2,
                                                                                                         row=3)
        self.engsci18 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.engscibtn4).grid(column=3,
                                                                                                        row=3)
        self.engsci19 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.engscibtn4).grid(column=4,
                                                                                                         row=3)
        self.engsci20 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.engscibtn4).grid(column=5,
                                                                                                        row=3)


        # Buttons5
        self.engsci21 = ttk.Radiobutton(self.window, text='first', value=1, variable=self.engscibtn5).grid(column=1,
                                                                                                        row=4)
        self.engsci22 = ttk.Radiobutton(self.window, text='second', value=2, variable=self.engscibtn5).grid(column=2,
                                                                                                         row=4)
        self.engsci23 = ttk.Radiobutton(self.window, text='third', value=3, variable=self.engscibtn5).grid(column=3,
                                                                                                        row=4)
        self.engsci24 = ttk.Radiobutton(self.window, text='fourth', value=4, variable=self.engscibtn5).grid(column=4,
                                                                                                         row=4)
        self.engsci25 = ttk.Radiobutton(self.window, text='fifth', value=5, variable=self.engscibtn5).grid(column=5,
                                                                                                        row=4)

        # Anum Sheikh: getting the specific candidates from GSUCandidates.txt file
        self.EngAndScience = line[27], line[28], line[29], line[30], line[31]
        # Anum Sheikh: loop to print each candidate on the window running for engsci
        j = 0
        for i in self.EngAndScience:
            self.label = tkinter.Label(self.window, text=i).grid(row=j, column=0)
            j = j + 1

        # Anum Sheikh: making buttons which will save user's votes (Save! button) and will take them to next voting page (Next! button)
        self.Button = tkinter.Button
        self.saveButton = self.Button(self.window, text="Save!", command=self.engscivote).grid()
        self.nextButton = self.Button(self.window, text="Logout!", command=exit).grid()
        # Anum Sheikh: implementing the window
        self.window.mainloop()

    # Anum Sheikh: defining a function for getting the engsci votes of user
    def engscivote(self):
        # Anum Sheikh: opening votes text file, get() method gets answer pressed by user and appends it to text file with their candidate preference.
        g = open("Votes.txt", "a")
        g.write("User's Engineering and Science Votes are:" + "\n")
        self.engscivote1 = self.engscibtn1.get()
        g.write("Manuel Hobbs got:" + str(self.engscivote1) + "\n")
        self.engscivote2 = self.engscibtn2.get()
        g.write("Grayson Best got:" + str(self.engscivote2) + "\n")
        self.engscivote3 = self.engscibtn3.get()
        g.write("Waseem Parson got:" + str(self.engscivote3) + "\n")
        self.engscivote4 = self.engscibtn4.get()
        g.write("Madeline Sparrow got:" + str(self.engscivote4) + "\n")
        self.engscivote5 = self.engscibtn5.get()
        g.write("Casey Reese got:" + str(self.engscivote5) + "\n")
        # Anum Sheikh: closes text file
        g.close()

def displayvotes(self):
    self.window = tkinter.Tk()
    self.window.title("USER'S VOTING RECEIPT")
    self.window.geometry('600x300')

    result = open("Votes.txt", "r")
    resultline = result.readlines()

    for i in resultline:
        self.tkinter.Label(self.window, text=i).grid()

    result.close()

    self.window.mainloop()

def userresults():
    window = tkinter.Tk()
    window.title("USER'S VOTING RECEIPT")

    result = open("Votes.txt", "r")
    resultline = result.readlines()

    for i in resultline:
        tkinter.Label(window, text=i).pack()

    window.mainloop()
    result.close()


#Anum Sheikh: calling and print the whole class to run
presClass = President()
print(presClass)

# Anum Sheikh: closing the candidates file
f.close()

window.mainloop()           # Implements the code (Usman)

