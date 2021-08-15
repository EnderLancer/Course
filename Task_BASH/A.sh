#!/bin/bash
if [ "$#" == "0" ]; then
  echo "You need to pass the argument. The --all key displays the IP addresses and symbolic names of all hosts in the current subnet. The --target key displays a list of open system TCP ports." 
  exit
fi
#TEMP=`getopt -o atm: --long all,target,memory:,debugfile:,minheap:,maxheap: \
#             -n 'javawrap' -- "$@"`
#
#if [ $? != 0 ] ; then echo "Terminating..." >&2 ; exit 1 ; fi
#
# Note the quotes around `$TEMP': they are essential!
#eval set -- "$TEMP"
function all(){
  for var in $(ip -4 addr | grep -oP '(?<=inet\s)\d+(\.\d+){3}' | grep -v "127.0.0.1")
  do
    echo "$var"
    local res="$(nmap -sP "$var/24")"
    echo "$res"
  done
}
function target(){
  echo "$(sudo ss -tulpn)"
}

while true; do
  case "$1" in
    -a | --all ) echo "IP of all hosts in the current subnet"; all; shift ;;
    -t | --target ) echo "List of open system TCP ports."; target; shift ;;
    -- ) shift; break ;;
    * ) break ;;
  esac
done
