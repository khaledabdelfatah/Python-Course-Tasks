#Write a program to add two lists index-wise. 
#Create a new list that contains the 0th index item from both the list,
# then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"] 

merged_list = []
for i in range(max(len(list1), len(list2))):
    if i < len(list1) and i < len(list2):
        merged_list.append(list1[i] + list2[i])
    elif i < len(list1):
        merged_list.append(list1[i])
    else:
        merged_list.append(list2[i])

print(merged_list)
