echo "1) you already login, isn't you?"
echo "2) change password by `passwd` command"
passwd
echo "3) check all users registered now"
w
echo "4) change home phone number and office room"
chfn -h 88005553535
chfn -r 144
echo "5) use couple of commands for help system"
echo "(search by keyword `append`)"
man -k append
echo "(short description of command `man`)"
man -f man
echo "6) Explore the more and less commands using the help system. (I don't want to pollute your console, so nothing to execute)"
echo "7) add plan for user"
finger student
echo "Work hard on LR1" > .plan
finger student
echo "8) show all user files"
ls -R