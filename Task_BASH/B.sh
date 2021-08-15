#!/bin/bash

file_out=out_script
echo "1. From which ip were the most requests:"
grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" $1 | sort | uniq -c | sort -gr > $file_out
{
read line1
} < $file_out
echo $line1
echo "2. What is the most requested page:"
awk '{print $7}' $1 | sort | uniq -c | sort -gr > $file_out
{
read line1
}<$file_out
echo $line1
echo "3. How many requests were there from each ip:"
site=$(printf '%s' "$line1" | sed 's/^[0-9] //')
grep -E "$site" $1 | awk '{print $1}' | sort | uniq -c | sort -gr > $file_out
{
read line1
echo "$line1"
while [ "$line1" ]
do 
  read line1
  echo "$line1"
done
} < $file_out

echo "4. What non-existent pages were clients referred to:"
grep -E -o "/error404" $1 | wc -l > $file_out
{
read line1
} < $file_out
echo $line1

echo "5. What time did site get the most requests:"
grep -E -o "[0-9]{1,2}/.../[0-9]{4}:[0-9]{2}:[0-9]{2}" $1 | sort | uniq -c | sort -gr > $file_out
{
read line1
} < $file_out
file_out2=output
sed 's/ / requests at /6' "$file_out" > $file_out2
{
read line1
} < $file_out2
echo $line1

echo "6. What search bots have accessed the site (UA + IP):"
grep -E  "bot" $1 | awk '{print $12, $1}' | uniq | sed 's/"//' > $file_out
{
read line1
echo "$line1"
while [ "$line1" ]
do
  read line1
  echo "$line1"
done
} < $file_out

echo < $file_out

