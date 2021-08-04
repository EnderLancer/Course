# Chapter References: #
* Task 1
    1. [Part 1](#part-1)
    2. [Part 2](#part-2)


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
1. Log in to the system as root.
    Show all files that starts with 'c' or contain 'sk' in name.
    ```
    student@CsnKhai:~$ tree -P 'c*|*sk*'
    .
    ├── test
    └── Work
        └── Course
            └── Linux Base
                └── Task1
                    ├── task1part1.sh
                    └── task1part2.sh
    
    5 directories, 2 files
    ```
    List subdirectories of the root directory up to and including the second nesting level.
    ```
    student@CsnKhai:~$ tree -P 'c*|*sk*' -L 2
    .
    ├── test
    └── Work
        └── Course
    
    3 directories, 0 files
    ```
    
2. Determine the type of file.
    ```
    student@CsnKhai:~/Work/Course/Linux Base$ file readme.md
    readme.md: UTF-8 Unicode text, with CRLF line terminators
    ```
    
3. Navigation.
    `cd` - command for navigation. 
    `cd /` - navigate to root (absolute).
    `cd ~` - navigate to home.
    `cd ..` - navigate to previous derictory.
    
    ```
    student@CsnKhai:~/Work/Course/Linux Base/Task1$ cd ~
    student@CsnKhai:~$ cd ../../etc/
    student@CsnKhai:/etc$ 
    ```
4. The ls command.
    Let's print all files and directories without ignore files starting with "." (-a),
    full info, but without group column (-o) (like -l, but without groups),
    with slash at the end of derictory (-p).
    ```
    student@CsnKhai:~$ ls -oap
    total 60
    drwxr-xr-x 6 student 4096 Aug  4 01:22 ./
    drwxr-xr-x 3 root    4096 Sep 15  2015 ../
    -rw------- 1 student  391 Aug  3 09:12 .bash_history
    -rw-r--r-- 1 student  220 Sep 15  2015 .bash_logout
    -rw-r--r-- 1 student 3637 Sep 15  2015 .bashrc
    drwx------ 2 student 4096 Sep 15  2015 .cache/
    -rw-rw-r-- 1 student   49 Aug  3 23:03 .gitconfig
    -rw-rw-r-- 1 student   17 Aug  3 22:33 .plan
    -rw-r--r-- 1 student  675 Sep 15  2015 .profile
    drwx------ 2 student 4096 Aug  2 14:41 .ssh/
    drwxrwxr-x 2 student 4096 Aug  2 12:55 test/
    -rw------- 1 student 5805 Aug  3 21:22 .viminfo
    drwxrwxr-x 3 student 4096 Aug  3 07:45 Work/
    -rw------- 1 student  212 Aug  4 01:22 .Xauthority
    ```
5. Sequence of operations.
    
    ```
    student@CsnKhai:~$ mkdir for_fifth_task
    student@CsnKhai:~$ ls -od /*/ > for_fifth_task/root_d_info.txt
    student@CsnKhai:~$ less for_fifth_task/root_d_info.txt
    student@CsnKhai:~$ cp for_fifth_task/root_d_info.txt relative_copy.txt
    student@CsnKhai:~$ cp ~/for_fifth_task/root_d_info.txt absolute_copy.txt
    student@CsnKhai:~$ ls -d *copy*
    absolute_copy.txt  relative_copy.txt
    student@CsnKhai:~$ rm -rf for_fifth_task
    student@CsnKhai:~$ ls
    absolute_copy.txt  relative_copy.txt  test  Work
    student@CsnKhai:~$ rm absolute_copy.txt relative_copy.txt
    student@CsnKhai:~$ ls
    test  Work
    ```
    
6. Sequence of operations. Links.
    
    - `student@CsnKhai:~$ mkdir test`
    - `student@CsnKhai:~$ cp .bash_history test/labwork2`
    - ```
      student@CsnKhai:~$ ln test/labwork2 test/hard_ln  
      student@CsnKhai:~$ ln -s test/labwork2 test/soft_ln
      ```
    - The differance: hard link - like second name, symbolic link - reference to file/directory  
      ```
      student@CsnKhai:~$ ls -od test/*ln
      -rw------- 2 student 399 Aug  4 02:56 test/hard_ln
      lrwxrwxrwx 1 student   8 Aug  4 02:55 test/soft_ln -> labwork2
      ```
    - Append file with word "changes" in new line by symbolic link to data file  
    `student@CsnKhai:~$ echo "changes" >> test/soft_ln`  
    - `student@CsnKhai:~$ mv test/hard_ln test/hard_lnk_labwork2`  
    - `student@CsnKhai:~$ mv test/soft_ln test/soft_lnk_labwork2`  
    - `student@CsnKhai:~$ rm -rf test`  
    After all (if links wasn't in test directory wich was deleted), hard link would works normally, but symbolic link reference to non-existing file.  
    
7. Using the locate utility.
    

8. Determine the type of file.

9. Determine the type of file.


10. Determine the type of file.

11. Determine the type of file.

12. Determine the type of file.

13. Determine the type of file.

14. Determine the type of file.

15. Determine the type of file.