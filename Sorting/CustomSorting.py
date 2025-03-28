'''
Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array. The Player class is provided in the editor below. It has two fields:

: a string.
: an integer.
Given an array of  Player objects, write a comparator that sorts them in order of decreasing score. If  or more players have the same score, sort those players alphabetically ascending by name. To do this, you must create a Checker class that implements the Comparator interface, then write an int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method. In short, when sorting in ascending order, a comparator function returns  if ,  if , and  if .

Declare a Checker class that implements the comparator method as described. It should sort first descending by score, then ascending by name. The code stub reads the input, creates a list of Player objects, uses your method to sort the data, and prints it out properly.

Example
 

Sort the list as . Sort first descending by score, then ascending by name.

Input Format

The first line contains an integer, , the number of players.
Each of the next  lines contains a player's  and , a string and an integer.

Constraints

Two or more players can have the same name.
Player names consist of lowercase English alphabetic letters.
Output Format

You are not responsible for printing any output to stdout. Locked stub code in Solution will instantiate a Checker object, use it to sort the Player array, and print each sorted element.

Sample Input

5
amy 100
david 100
heraldo 50
aakansha 75
aleksa 150
Sample Output

aleksa 150
amy 100
david 100
aakansha 75
heraldo 50
Explanation

The players are first sorted descending by score, then ascending by name.


'''
from functools import cmp_to_key
class User:
    def __init__(self,name:str="",age:int=0,email:str="",scores:int=0):
        self.name=name 
        self.age=age
        self.email=email 
        self.scores=scores
    def comparator(a,b):
      # sorting by their emails for descending order 
        if a.scores > b.scores: 
            return -1 
        elif a.scores < b.scores:
            return 1 
        else:
            if a.name < b.name:
                return -1 
            elif a.name > b.name:
                return 1 
            else: return 0 
def main():
    data=[]
    user_1=User("Shwetha K",23,"shwetha@gmail.com",100)
    user_2=User("Anika N",23,"anikan@gamil.com",60)
    user_3=User("Kavitha S",23,"kavitha@gmail.com",67) 
    user_4=User("Yamuna K",23,"yamuna@gmail.com",75)     
    data.append(user_1)
    data.append(user_2)
    data.append(user_3)
    data.append(user_4)
    data:list[User]=sorted(data,key = cmp_to_key(User.comparator))
    for i in data:
        print(i.name," ",i.email," ",i.age," ",i.scores)     
main()