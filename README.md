
# Capstone Project: Internal Mail System: slademail.com

## Table of contents

### Section1: Project Description 
### Section 2: Installation Section
### Section 3: Usage Section
### Section 4: Credits


## Section 1: Project Description

<p>This software is a task manager system. There are a number of existing users, and new users can be added by an admin account.<br>
tasks with deadlines can be added for other users and marked as complete or incomplete. This is useful for maintaining an agile system <p>

## Section 2: Installation Section

<p>This programme is made up of a single python file task_manager.py and two text files: user.txt and tasks.txt.<br>
Simply download all these files into a single folder to install.<p>

## Section 3: Usage Section

<p>The file user.txt contains a number of lines of text. These are the usernames of a user followed by ", " and then the password.<br>
task_manager.py accesses this file when the user logs in so it is important it is kept in this format.<br>
The file tasks.txt contain lines of the format: Username, task, task description, assigned date, due date. The dates are stored in the format yyyy-mm-dd.<br>
task_manager.py writes and reads tasks in this exact format.<p> 

<p>email.py when run will give the user a menu of options:<br>
        r - Registering a user (Only admin can do this)<br> 
        a - Adding a task<br> 
        va - View all tasks<br> 
        vm - view my task<br> 
        gr - generate reports<br> 
        ds - display statistics<br> 
        lo - log out<br> 
        e - Exit<p>
        
<p>The user can access these options by typing in the letter next to the option.<p>
<p>vm gives the user the option to edit uncomplete tasks once they have viewed the task:<br>
1 - edit username of person task assigned to <br>
2 - edit the due date of the task<br>
3 - mark the task as complete<br>
4 - exit<p>
<p>gr generates two text files:<p>

<p>1) user_overview.txt which contains the following information for each user:<p>

<p>i) Total number of assigned tasks<br>                     
ii) Percentage of tasks assigned to user<br>               
iii) Percentage of assigned tasks completed<br>             
iv) Percentage of assigned tasks not yet completed<br>     
v) Percentage of assigned tasks not yet completed and overdue<p> 

<p>2) task_overview.txt which contains the following information:<p>

<p>i) Total number of tasks<br>                    
ii) Number of completed tasks<br>                 
iii) Number of incomplete tasks <br>                 
iv) Number of incomplete, overdue tasks<br>       
v) Percentage of tasks incomplete<br> 
vi) Percentage of tasks incomplete and overdue<p>

<p>ds allows the admin to display these statistics to the terminal


## Section 4: Credits

<p>Eirion Slade<p>

