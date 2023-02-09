"""


               **EIRION SLADE TASK MANAGEMENT SYSTEM**

This programme is a task management function. It has the following functionality:

    1) Allows an admin to add new users to a file user.txt
    2) Allows users to add tasks in a file tasks.txt which can be:
        i) Assigned to a user
        ii) Assigned a due date
        iii) Marked as complete or incomplete
    3) Allows users to view all tasks
    4) Allows users to view and edit their assigned tasks
    5) Allows users to generate reports
    6) Allows an admin to display these reports as statistics."""


#=========================================1)   importing libraries     ===============================================================================


import datetime
import os.path



#==========================================2)   Define Functions     ================================================================================


#=====reg_user======== YOU NEED TO FINISH EDITING THIS SECTION 27/01/2023
    #This function allows the admin to register a new username and password and add them to the file usere.txt

def reg_user (): 
    #Check user is the admin and continue if so
    if username.lower() == "admin":
        #Generate a list of the lines in the file user.txt
        with open ("user.txt","r+") as f:
            text = f.read()
            text = text.split("\n")
            
            #ask for username and confirm in a first nested while loop that the username is not already 
            #registered, and once this condition is met, move on to confirm the username and ensure this 
            #matches
            while True:
            
                while True:
                    user1 = input("You have selected to register a new user. Please enter the username of the new user or type 'e' to exit:\n").lower()
                    
                    if user1 == "e":
                        return
                    existing_user = False
                    #for each line, split by ", " and compare first element (existing username), with the user1,
                    #the username the user is trying to register. break and display an error message and return to top
                    for element in text:
                        current_user = element.split(", ")[0]
                        if  current_user.lower() == user1.lower():
                            existing_user = True 
                            breakpoint                
                    if existing_user == True:
                        print ("I am sorry but this username is already in use")
                        continue
                          
                        #request repeat username
                    user2 = input("Please confirm the username or enter 'e' to exit:\n")
                    #check they match and if they do continue. Else return to the top of user loop
                    if user2 == "e":
                        return
                    
                    if user1.lower() != user2.lower():
                        print("I am sorry these do not match. Please try again")
                        continue

                    else:
                        print("Usernames match!")
                        
                        #ask for password and confirm
                    while True:
                        password1 = input(f"Please enter desired password for {user1} or enter 'e' to exit:\n")
                        if password1 == "e":
                            return
                        password2 = input(f"Please confirm password for {user1} or enter 'e' to exit:\n")
                        if password1 == "e":
                            return
                            #if match continue else return to the top of password loop
                        if password1 != password2:
                            print("Passwords do not match. Try again\n")
                            continue
                        else:
                            print("passwords match!")
                            # if passwords match, continue add username and password to the file: user.txt
                            print(f"\n\nA new user has been added:\nusername: {user1}\npassword: {password1}\n")
                            f.write(f"\n{user1}, {password1}")
                            return
    #if user is not the admin display an error message and go back to the menu
    else:
        print("\nI am sorry but on the admin can add new users. Please contact your admin.\n")
        return

#=====add_task======
    #This function allows the user to add a new task to the file tasks.txt 

def add_task():

    while True:

            #request username and check that user is registered.
        user = input("\nYou have requested to add a new task. Please enter the username of the person to whom\n\
the task is assigned or type 'e' to exit:\n").lower()
        if user =='e':
            return

        with open ("user.txt","r") as f:
            text = f.read().lower()
            found = text.find(f"{user}, ")

            if found != -1:
                break

            else:
                print ("Sorry that user is not registered. Please try again.\n")

    #request title, description, due date and assigned date verifying that the due date is after 
    #the current date, using datetime and strftime

    title = input("Please enter the title of the task:\n")

    description = input ("Please enter a description of the task:\n")

    while True:
    
        due_date = input("Please enter the due date of the task in the format yyyy-mm-dd:\n")
        #carry out some checks on the format of the date
        try:
            if due_date[-3] != "-" or due_date[-6] != "-" or len(due_date) != 10 or len(str(due_date.replace("-",""))) != 8:
                print("An error has occurred")
                continue
        except:
            print("An error has occurred")
            continue
        
        #If it passes, convert todays date and the due date to numbers and compare them, with more error checks
        try:
            date_test = datetime.date(int(due_date[0:4]),int(due_date[5:7]),int(due_date[8:]))
            due_date_num = int(due_date.replace("-",""))
            assigned_date = datetime.date.today().strftime('%Y-%m-%d')
            assigned_date_num =  int(assigned_date.replace ("-",""))
        except:
            print ("\nAn error occurred.\n")
            continue
        
    
        
        #pass an error message if the due date is the same day (unfair) or before the assigned date
        if (assigned_date_num) >= (due_date_num):
            print ("Due date must be after assigned date. Please try again")
        #if the due date is after the assigned date, break the loop
        else:
            break

    #display output to confirm to the user that they have added a new task

    print(f"""Congratulations. You have successfully added a new task as shown below

                    User:                    {user}
                    Task title:              {title}
                    Task description:        {description}
                    Date assigned:           {assigned_date}
                    Date due:                {due_date}       
                    Completed:               "No"  
                    """)
    #write output to tasks.txt in a format readable by this programme.

    with open("tasks.txt","a+") as f:
                f.write (f"\n{user}, {title}, {description}, {assigned_date}, {due_date}, No")

#=====view_all=====
    #This function allows the user to view all the tasks in the file tasks.txt

def view_all():

    #opening message
    print ("""
------------------VIEW ALL TASKS-------------------
    
Please view tasks below""")

    #Now display each task in order (each corresponds to a line in tasks.txt)
    with open("tasks.txt","r+") as f:

        for line in f:
            task_list = line.split (", ")

            #reformat the dates in the required format and assign to variables
            due_date = datetime.date(int(task_list[4][0:4]),int(task_list[4][5:7]),int(task_list[4][8:]))
            due_date = due_date.strftime("%d %b %Y")

            assigned_date = datetime.date(int(task_list[3][0:4]),int(task_list[3][5:7]),int(task_list[3][8:]))
            assigned_date = assigned_date.strftime("%d %b %Y")

            task_list[5] = (task_list[5]).rstrip("\n")

            #print outputs in an easily readable format
            print(
f"""___________________________________________________

Task:                   {task_list[1]}
Assigned to:            {task_list[0]}
Date assigned:          {assigned_date}
Due date:               {due_date}
Task Complete?          {task_list[5]}
Task Description:
{task_list[2]}
___________________________________________________""")

    print("\n\n")

#====view_mine====
    #This function allows user to view their tasks and edit them

def view_mine():
    # This function first displays the tasks belonging to the logged-in user. It then gives them the option
    # of selecting a task, and for that task, the user can then choose to edit 1)the user assigned to the task, 
    # 2) the due date of the task, 3) whether the task is complete or incomplete.

    print (f"""

----------------------VIEW MY TASKS----------------------
    
Please view all tasks assigned to {username} below:
""")

    ###############Section 1 - display tasks and ask user which task they would like to edit################

    #-------opening tasks.txt, printing out the tasks in a readable format and producing
    # task_list_list, a list of lists relating to each task, which can be easily edited and re-written back to the file
    while True:
        with open("tasks.txt","r+") as f:
            
            #initialise some variables and lists
            tasknumber = 0
            tasknumberall = 0
            task_list_list = []
            task_list_list_all = []

            for line in f:

                task_list = line.split (", ")
                #only display tasks for the logged in user
                if task_list[0] == username:
                    #append a task-number to each task (of all the tasks)
                    task_list.append(str(tasknumberall))
                    #increment the task number(of just the user's tasks)
                    tasknumber +=1
                    #increment
                    tasknumberall +=1
                    #add this task to a list of all the tasks
                    task_list_list_all.append(task_list)
                    #add this task to a list of the user's tasks
                    task_list_list.append(task_list)
                    #reformat dates to the desired format
                    due_date = datetime.date(int(task_list[4][0:4]),int(task_list[4][5:7]),int(task_list[4][8:]))
                    due_date = due_date.strftime("%d %b %Y")
                    assigned_date = datetime.date(int(task_list[3][0:4]),int(task_list[3][5:7]),int(task_list[3][8:]))
                    assigned_date = assigned_date.strftime("%d %b %Y")
                
                    task_list[5] = (task_list[5]).rstrip("\n")
                    #print output in an easily readable format
                    
                    print(
    f"""_________________________________________________________

    Task Number             {tasknumber}
    Task:                   {task_list[1]}
    Assigned to:            {task_list[0]}
    Date assigned:          {assigned_date}
    Due date:               {due_date}
    Task Complete?          {task_list[5]}
    Task Description:
    {task_list[2]}
_________________________________________________________
    """)
                #if the task in the line does not belong to the logged-in user, update only task_list_list_all with the task
                else:
                    task_list.append(str(tasknumberall))
                    task_list_list_all.append(task_list)
                    task_list[5] = (task_list[5]).rstrip("\n")
                    tasknumberall +=1


        #Now if it turns out the logged-in user has no tasks assigned to them then say this and break the loop
        if tasknumber ==0:
            print("You have no tasks.\n")
            break

        #otherwise, give the user an option to edit a task and which task they would like to edit
        else:
        
            decision = input("""Would you like to edit a task or return to the main menu?
            
edit - enter 'edit'
return - enter 'return'

""")

            #return to main menu
            if decision.lower() == "return":
                break
            #continue to edit a task
            elif decision.lower() == "edit":

                while True:
                    # First find the task they want to edit
                    task_to_edit = input(f"\nPlease enter the number of the task you would like to edit from 1 to {tasknumber} or type 'e' to return:\n\n")
                    #make sure they have entered a number or return with error message
                    if task_to_edit =='e':
                        print("Please see your tasks displayed below")
                        break
                    try:
                        task_to_edit_float = float(task_to_edit)-1
                        task_to_edit_int = int(task_to_edit)-1
                    except ValueError:
                        print ("Error: Please try again")

                    #if number is entered, this is an integer and fits the number of tasks, continue
                    else:
                        if task_to_edit_float%1 == 0 and task_to_edit_float - tasknumber <= -1:
                            
                            #save the index within the task_list_list_all to allow editing of the whole list later
                            task_to_edit_all = task_list_list[task_to_edit_int][6]
                            #Confirm with the user the task that they have selected
                            while True:
                                print (f"""
                            
You have chosen to edit task {int(task_to_edit_int)+1}:

______________________________________________________________

Task:                   {task_list_list[task_to_edit_int][1]}
Assigned to:            {task_list_list[task_to_edit_int][0]}
Date assigned:          {task_list_list[task_to_edit_int][3]}
Due date:               {task_list_list[task_to_edit_int][4]}
Task Complete?          {task_list_list[task_to_edit_int][5]}
Task Description:
{task_list_list[task_to_edit_int][2]}
______________________________________________________________
""")

                                # set variable comp so if completed we return to the menu "Please enter the number of task..."
                                # and if not completed and the other tasks are performed, return back to the menu: would you like to edit a task...""
                                comp = 0
                                #if the task is marked as complete, display message and set comp to 1 to return to the early menu
                                if task_list_list[task_to_edit_int][5] == "Yes":
                                    print ("This task is now complete and cannot be edited.")
                                    comp = 1

                                #if the task is incomplete, give the user a list of the possible editing options and based on that per  
                                else:
                                    edit_section = input(f"""Please select from the following options:
1 - edit username of person task assigned to 
2 - edit the due date of the task
3 - mark the task as complete
4 - exit

""")


                            ###################Section 2: Task editing functions#############################

                            #-----------task edit 1) username--------------------

                            #edit  the username of the person the task is assigned to
                                    if edit_section == '1':

                                    #generate a list of the usernames and ask user which one they want to change to
                                        while True:
                                            with open("user.txt", "r+") as g:
                                                userlist = []
                                                counter = 0
                                                for line in g:
                                                    counter +=1
                                                    user = line.split(", ")[0]
                                                    userlist.append(f"{counter}: {user}")
                                                userlisttype = "\n".join(userlist)
                                            new_user = input(f"""The task is currently assigned to: {task_list_list[task_to_edit_int][0]}.

Please enter the number next to the user you would like to change to:

{userlisttype}\n\n""")   

                                                #extract username from this entry, giving error message if not possible
                                            try:
                                                user_to_change_to = userlist[int(new_user)-1].split(" ")[1]
                                            except:
                                                print ("\nIncorrect entry.\n")
                                                continue
                                                #If all okay, edit the entry in task_list_list and re-write the task document


                                            else:
                                                #define variable taskuser for message later
                                                taskuser = task_list_list[task_to_edit_int][0]   
                                                #change element in task_list_list_all
                                                task_list_list_all[int(task_to_edit_all)][0] = user_to_change_to

                                                #convert task_list_list into a block of text in appropriate format
                                                text_list = []
                                                counter = 0
                                                for element in task_list_list_all:
                                                    text_list.append ((", ").join(task_list_list_all[counter][:6]))
                                                    counter+=1
                                                text = "\n".join(text_list)

                                                #write this block of text back to tasks.txt
                                                with open("tasks.txt", "w+") as h:
                                                    h.write(text)
                                                print(f"""
                                                
The user for task {task_to_edit_int+1} has successfully been changed from:
{taskuser}
to
{user_to_change_to}

Your updated tasks are displayed below:

""")
                                                    
                                                
                                                break   
                                        
                                            
                                                  
                                                        
                                    #-------------Task edit 2) due date-------------------------     
                                      
                                    elif edit_section == '2':
                                        while True:
                                                #request input from user
                                                new_date = input(f"""The current due date of the task is {task_list_list[task_to_edit_int][4]}

Please enter the new date in the format yyyy-mm-dd:
""")
                                

                                                #check the date is in the right format and will be convertible by datetime
                                                try:
                                                    new_date_num = int(new_date.replace("-",""))
                                                    test_date = datetime.date(int(new_date[0:4]),int(new_date[5:7]),int(new_date[8:]))
                                                    
                                                #display and error message and return to the top if incorrect
                                                except:
                                                    
                                                    print("\nError: Please enter the date in the format yyyy-mm-dd\n")
                                                    continue

                                                #otherwise check the format of the date with another check
                                                else:
                                                    if new_date[-3] != "-" or new_date[-6] != "-" or len(new_date) != 10 or len(str(new_date_num)) != 8:
                                                        print("\nError: Please enter the date in the format yyyy-mm-dd\n")
                                                        continue
                                                    
                                                    #otherwise convert the assigned date into a number
                                                    assigned_date_num = int(task_list_list[task_to_edit_int][3].replace("-",""))
                                                    
                                                    #now check the new due date is after the assigned date and give an error if it is
                                                    if (assigned_date_num) >= (new_date_num):
                                                        print ("Due date must be after assigned date. Please try again.\n")
                                                        continue
                                                    #otherwise continue to update the due date
                                                    else:
                                                        #store original due date for output
                                                        original_due_date_num = int(task_list_list_all[int(task_to_edit_all)][4].replace("-",""))
                                                        #change element in task_list_list_all
                                                        task_list_list_all[int(task_to_edit_all)][4] = new_date

                                                        #convert task_list_list into a block of text in appropriate format
                                                        text_list = []
                                                        counter = 0
                                                        for element in task_list_list_all:
                                                            text_list.append ((", ").join(task_list_list_all[counter][0:6]))
                                                            counter+=1
                                                        text = "\n".join(text_list)

                                                        #write this block of text back to tasks.txt
                                                        with open("tasks.txt", "w+") as h:
                                                            h.write(text)
                                                        
                                                        #print a message to explain to the user that the date has been successfully changed and break the loop
                                                        print (f"""
        The due date of task {task_to_edit_int+1} has been successfully changed from:
        {str(original_due_date_num)[6:8]}-{str(original_due_date_num)[4:6]}-{str(original_due_date_num)[0:4]}
        to 
        {str(new_date_num)[6:8]}-{str(new_date_num)[4:6]}-{str(new_date_num)[0:4]}

Your updated tasks are displayed below:

""")
                                                    break  
                                        break


                                    #-------------Task edit 3) Mark the task complete

                                    elif edit_section == '3':

                                        #Confirm with user that they would like to mark the task as complete
                                        while True:
                                            new_complete = input(f"""Are you sure you would like to mark task {task_to_edit_int+1} as complete?
1 - Yes (mark as complete)
2 - No  (keep as incomplete)

""")
                                            if new_complete == "1":
                                                status = "Yes"
                                                break
                                            elif new_complete == "2":
                                                status = "No"
                                                break
                                            else:
                                                print ("Error: Please enter either 1 or 2")
                                                
                                        #Change element in task_list_list_all
                                        task_list_list_all[int(task_to_edit_all)][5] = status

                                        #Now convert task_list_list_all into a block of text to be written back into tasks.txt
                                        text_list = []
                                        counter = 0
                                        for element in task_list_list_all:
                                            text_list.append ((", ").join(task_list_list_all[counter][0:6]))
                                            counter+=1
                                        text = "\n".join(text_list)

                                        #write this block of text back to tasks.txt
                                        with open("tasks.txt", "w+") as h:
                                            h.write(text)
                                        #print a message to confirm to the user that the completion status has been updated
                                        print (f"""
The completion status of task {task_to_edit_int+1} is now:

{status}

Your updated tasks are listed below:

""")
                                        break

                                    #Exit
                                    elif edit_section == '4':
                                        print("You have chosen to exit. Your tasks are displayed below")
                                        
                                    #if entry not in list of choices then return to top of loop
                                    else:
                                        print("\nI am sorry. Your selection was invalid.\n")
                                        continue
                                
                                break
                            #if the task has been completed then break the loop and exit
                            if comp == 0:
                                break
                        
                        #error message if incorrect task number entry
                        else:
                            print(f"Error: Please try again")
            #error message if incorrect entry at edit/return command   
            else:
                print("\nI am sorry you have entered an invalid option. Please try again\n.")

#====generate_reports====
#This function reads files and generates new files task_overview and user_overview, which the admin can call to the terminal using the display
#statistics function


def generate_reports():

    #generate a list of users with initialised stats [username, total number of tasks assigned, total number of complete tasks, total number of incomplete tasks, total number of overdue tasks]
    with open("user.txt","r+") as g:
        user_list_list = []
        for line in g:
            #generate list for each user of the following form [username, total number of tasks assigned, total number of complete tasks, total number of incomplete tasks, total number of overdue tasks]
            user_list_list.append([line.split(", ")[0],0,0,0,0,])

    ##################     File 1: user_overview    ################

    #open tasks.txt and extract data into a task_list_list. Perform operations to generate the appropriate data for task_overview and user_overview
    with open("tasks.txt","r+") as f:

        #initiate task_list_list and initiate some variables                
        task_list_list = []
        complete_num = 0
        incomplete_num = 0
        num_incomplete_and_overdue = 0
        today = datetime.datetime.now()
        today = today.strftime("%Y%m%d") 

        #for each line in tasks.txt, cycle through the list of users and update user_list_list when the task is assigned to that user
        for line in f:
            for user_list in user_list_list:
                #if the user task is assigned to the user in user_list:
                if user_list[0] == line.split(", ")[0]:

                    #split the line into task_list
                    task_list = line.split (", ")            

                    #add this list to task_list_list
                    task_list_list.append(task_list)

                    #clean the \n's
                    task_list[5] = (task_list[5]).rstrip("\n")

                    #if the task is completed, increment
                    if task_list [5] == "Yes":
                        complete_num += 1
                    #else increment the incomplete tasks and incomplete and overdue tasks as appropriate
                    else:
                        incomplete_num += 1
                        duedate_num = task_list[4].replace("-","")
                        if duedate_num <today:
                            num_incomplete_and_overdue +=1

                    #Now focussing on the user_list values:  [username, total number of tasks assigned, total number of complete tasks, total number of incomplete tasks, total number of overdue tasks]      

                    #increment the total number of tasks assigned to this user
                    user_list[1]+=1
                    #increment the complete tasks for this user as appropriate
                    if task_list[5] == "Yes":
                        user_list[2] += 1
                    #increment the incomplete and overdue incomplete tasks for this user
                    else:
                        user_list[3] += 1
                        #increment the number of incomplete overdue tasks as appropriate
                        if duedate_num <today:
                            user_list[4]+=1
        

        #Extract the total number of tasks:
        task_total = len(task_list_list)
        
        #user_list_list is now updated with the relevant statistics for each user

        
    #Now we are going to print these statistics in a readable format in user_overview
    with open("user_overview.txt","w+") as u:

        #Print an initial message containing the total number of registered users, which is the length of user_list_list
        u.write(f"""You have requested a user report. Please see below:

______________________________________________________________________

Total number of registered users:                {len(user_list_list)}

""")
        #now initialise a counter and cycle through the users, displaying their stats
        counter = 0
        for user_list in user_list_list:
            counter +=1

            #if user has no tasks assigned, display this (to avoid division by zero)
            if user_list[1]==0:
                u.write(f"""
______________________________________________________________________                
User {counter}:                                             {user_list[0]}

Total number of assigned tasks:                     0
                
                """)



            #else display the appropriate outputs by extracting data from user_list_list and performing operations
            else:
                u.write(f"""
______________________________________________________________________
User {counter}:                                             {user_list[0]}

Total number of assigned tasks:                     {user_list[1]}
Percentage of tasks assigned to user:               {user_list[1]/task_total*100:.1f}%
Percentage of assigned tasks completed:             {user_list[2]/user_list[1]*100:.1f}%
Percentage of assigned tasks not yet completed:     {user_list[3]/user_list[1]*100:.1f}%
Percentage of assigned tasks not yet completed
and overdue:                                        {user_list[4]/user_list[1]*100:.1f}%
______________________________________________________________________

                """)
                
            
############################    File 2) task_overview     ###########################
        #in the special case that there are not tasks, write this to task_overview.txt in a message
        if task_total == 0:
            with open("task_overview.txt","w+") as t:
                t.write("There are no tasks registered")

        #Otherwise, derive values from the data extracted above
        else:
            #derive percentages from existing variables
            perc_incomplete = incomplete_num/task_total * 100
            perc_overdue = num_incomplete_and_overdue/task_total * 100

            #Generate a task report and write this to task_overview.txt
            task_overview_text = (f"""
            
You have selected to generate a task report. Please see below task_overview:

_________________________________________________________________________

Total number of tasks:                      {task_total}
Number of completed tasks:                  {complete_num}
Number of incomplete tasks                  {incomplete_num}
Number of incomplete, overdue tasks         {num_incomplete_and_overdue}
Percentage of tasks incomplete              {perc_incomplete:.1f}%
Percentage of tasks incomplete and overdue  {perc_overdue:.1f}%

_________________________________________________________________________
""")
           
            with open("task_overview.txt","w+") as t:
                t.write(task_overview_text)
            #print a confirmation message
            print("""
_______________________________________________________________________________
a user overview report and a task overview report have been saved to:

user_overview.txt 
and 
task_overview.txt 

respectively

The admin can display these by selecting 'display statistics' at the main menu
_______________________________________________________________________________
""")
            
        
#=====display statistics=====
    #this function checks the user is admin and if so checks the files task_overview and user_overview exist. If so, the reports are
    #printed to the terminal, and if not, the reports are generated before the files are accessed.

def display_statistics():
    #Check user is admin and return if not
    if username.lower() != "admin":
        print ("\nSorry, only the admin can display statistics. Please try another option\n")
    
    #If the user is the admin, check the relevant files exist
    else:
        path = "task_overview.txt"
        task_file_exist = os.path.isfile(path)
        path = "user_overview.txt"
        user_file_exist = os.path.isfile(path)

        #If they don't already exist, then generate the reports
        if task_file_exist == False or user_file_exist == False:
            generate_reports()
        
        #print the contents of the files to the terminal
        with open("task_overview.txt","r+") as f:
            task_text = f.read()
        with open("user_overview.txt","r+")as f:
            user_text = f.read()
        print("\n\n")
        print(user_text)
        print(task_text)
    

#============================================== 3) Main stem of code =================================================



#====Login Section====

#This section of code requests username and password from the user and continues to the subsequent 
#sections if these are correct


while True:
    #request input from user (MAKING USERNAME CASE INSENSITIVE AS PER FEEDBACK)
    username = input("Please enter username:\n").lower()
    password = input ("Please enter password:\n")
   

    #open file and check username and password match those in the list
    with open("user.txt","r") as f:
        text = f.read()
        text = text.split("\n")
        match = False
        for element in text:
            #(MAKING USERNAME CASE INSENSITIVE AS PER FEEDBACK)
            if (element.split(", ")[0]).lower() == username and element.split(", ")[1] == password:
                match = True
                break
        #If no match then return to top
        if match == False:
            print("\nUsername or password is incorrect. Please try again.\n")
            continue
        #Otherwise print message and proceed to menu
        else: 
            print("\nUsername and password correct!\n")
            
        

#=====menu section=====

#Once the user is logged in, they are given the option of a number of different options. Each calls the relevant function

    while True:

        menu = input('''Select one of the following options below:
        r - Registering a user (Only admin can do this)
        a - Adding a task
        va - View all tasks
        vm - view my task
        gr - generate reports
        ds - display statistics
        lo - log out
        e - Exit
        : ''').lower()



    #=====Register new user section=====
        #If user enters r, this code allows them to register a new username and password and adds this to file: user.txt

        if menu =='r':
            reg_user()

    #===========Add task section =======
        #if user enters 'a', give them the option to enter a new task and save this as a line in the file tasks.txt

        elif menu == 'a':
            add_task()
            
    #=====View All Tasks Section========
        #If user enters va then open tasks and read each line in turn, splitting each into a list, and printing
        #the contents of that line in an easily readable format

        elif menu == "va":
            view_all()

    #=====View my tasks section=========
        #If user enters vm, open tasks.txt and read line by line converting each line into a list and printing the 
        #contents in an easily readable format, but only for those tasks assigned to the logged-in user

        elif menu == 'vm':

            view_mine()

    #=====Genenerate reports section====
        #If the user enters gr, open tasks.txt and extract task data and present as report
        
        elif menu == 'gr':
            generate_reports()
        
    #=====Display statistics section====
        #if the user enters ds, open task

        elif menu == 'ds':
            display_statistics()

    #=====exit section=====
        #if the user enters e then exit the programme
        elif menu == 'e':

            print('Goodbye!!!')
            exit()

    #=====logout section=====
        #If the user enters lo then display logout message and return to login section
        elif menu == "lo":
            print(f"{username} is now logged out\n")
            break

    #=====error in case user enters incorrect value in the menu section
        else:
            print("You have not entered one of the above options. Please try again")

        