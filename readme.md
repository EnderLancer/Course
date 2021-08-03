# Chapter References: #
* Task 1
    1. [Part 1](#part-1)
    2. [Part 2](#part-2)

\

## Part 1 #
1. Log in to the system as root.
    ```
    login as: student
    student@192.168.1.103's password: (1Q2w3E)
    ```
2. Use the passwd command.
    
    ```
    student@CsnKhai:~$ passwd
    Changing password for student.
    (current) UNIX password:
    Enter new UNIX password:
    Retype new UNIX password:
    ```
    
    **basic commands:**
    -a, --all
        This option can be used only with -S and causes show status for all users.

    -d, --delete
        Delete a user's password (make it empty). This is a quick way to
        disable a password for an account. It will set the named account
        passwordless.
        
    -l, --lock
        Users with a locked password are not allowed to change their
        password.
    
    **files:**
    /etc/passwd - contain info about users
    /etc/shadow - contain info about passwords and params
    
3. Determine the users registered in the system.
    Registered users by their directories:
    ```
    student@CsnKhai:~$ w
    21:38:45 up  2:19,  3 users,  load average: 0.00, 0.01, 0.04
    USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
    student  tty1                      19:19    2:18m  0.07s  0.06s -bash
    student  pts/0    192.168.1.102    19:20    3.00s  0.55s  0.00s w
    student  pts/1    192.168.1.102    20:57   38:40   0.11s  0.11s -bash
    ```
    It displayed for each user: login name, the tty name, the remote host, login time, idle time, JCPU, PCPU, and the command line of their current process.

4. Change self info.
    Change home phone number and office room
    ```
    student@CsnKhai:~$ chfn -h 88005553535
    Password:
    student@CsnKhai:~$ chfn -r 144
    Password:
    ```
    
5. Become familiar with the Linux help system.
    Find command by keyword:
    ```
    student@CsnKhai:~$ man -k append
    ssh-import-id (1)    - retrieve one or more public keys from a public keyserv...
    ssh-import-id-gh (1) - retrieve one or more public keys from a public keyserv...
    ssh-import-id-lp (1) - retrieve one or more public keys from a public keyserv...
    ```
    Preview of command:
    ```
    student@CsnKhai:~$ man -f man
    man (1)              - an interface to the on-line reference manuals
    man (7)              - macros to format man pages

    ```

6. Explore the more and less commands.
    The `more` command open file in console with opportunity to slide it down/
    The `less` command open file in text reader and don't scripe something to console

7. Add plan for user
    For plan, you need to create .plan in user directory:
    ```
    student@CsnKhai:~$ finger student
    Login: student                          Name: Student KhAI
    Directory: /home/student                Shell: /bin/bash
    Office: 144                             Home Phone: +8-800-555-3535
    On since Tue Aug  3 19:19 (UTC) on tty1    3 hours 11 minutes idle
         (messages off)
    On since Tue Aug  3 19:20 (UTC) on pts/0 from 192.168.1.102
       5 seconds idle
    On since Tue Aug  3 20:57 (UTC) on pts/1 from 192.168.1.102
       14 minutes 52 seconds idle
    No mail.
    No Plan.
    student@CsnKhai:~$ echo "Work hard on LR1" > .plan
    student@CsnKhai:~$ finger student
    Login: student                          Name: Student KhAI
    Directory: /home/student                Shell: /bin/bash
    Office: 144                             Home Phone: +8-800-555-3535
    On since Tue Aug  3 19:19 (UTC) on tty1    3 hours 13 minutes idle
         (messages off)
    On since Tue Aug  3 19:20 (UTC) on pts/0 from 192.168.1.102
       5 seconds idle
    On since Tue Aug  3 20:57 (UTC) on pts/1 from 192.168.1.102
       17 minutes 43 seconds idle
    No mail.
    Plan:
    Work hard on LR1
    ```
    
8. Show what in home directory:
    With recursive:
    ```
    student@CsnKhai:~$ ls -R
    .:
    test  Work
    
    ./test:
    
    ./Work:
    Course
    
    ./Work/Course:
    Linux Base
    
    ./Work/Course/Linux Base:
    Task1
    
    ./Work/Course/Linux Base/Task1:
    readme.md  tasks.sh
    ```

## Part 2 #