#To write a script that creates groups from a list
#We import random
import random, math

def random_grouping(filename,members_per_group):
    #We initialize a list
    everyone = []
    #For the last part, we initialize the range of the range
    start,end = 0,members_per_group

    #we open the file and iterate through it.
    with open(filename,"r") as f:
        for i in f:
            #we use append to add each line which is a name in the txt file
            everyone.append(i) 

        #we shuffle the items in the list using 'random'
        random.shuffle(everyone)

        #we find the total number of people in the list and number of possible groups
        number_of_people = len(everyone)
        possible_groups = math.ceil(number_of_people/members_per_group)
        #ceil is used to make the decimal points round to the next number
        #since we cannot have decimals in groups

        #We print the total number of people and the possible number of groups
        print(f"We have {number_of_people} people. Therefore, {possible_groups} can be created")

        
        #creating groups
        group_number = 1 #we initialize the group number to 1

        #we iterate through the list and change the corresponding number to the group
        while group_number < possible_groups +1:
            print(f"\nGroup {group_number}")
            for i in range(start,end):
                if i < number_of_people:
                    print(everyone[i].strip("\n"))
                    
            #change the group name, by altering the group number
            group_number +=1
            start+= members_per_group #we add the number each group is supposed to have
            end += members_per_group  #to the range
      
            
#The user gives the number of people they want per group
members_per_group = int(input("How many members do you want in a group? "))

#The name of the file. where necessary, add the file path
filename = input("What is the name of the file? \n")
#random_grouping('names.txt', 2)
#random_grouping('legends.txt',8)
random_grouping(filename,members_per_group)        
