import subprocess as sp

Output= sp.check_output("C:\Windows\System32\schtasks.exe")
#print(list)
list1= str(Output).split("\\n\\r")
#print(list1[0])
i=0
j=0
task_details={}
#print("---------------TASKS IN QUEUE----------------")
while i<len(list1):
    list2= list1[i].split("\\n\\r")
    #print(list2)
    list3= list2[0].split("\\r\\n")
    #print(list3)
    final= list3[3].split()
    task_details['Task Name']= final[0].strip()
    task_details['Next Run Time']= final[1].strip()
    task_details['status']= final[2].strip() 
    print(task_details)
    i=i+1
#list3= list2[0].split("\\r\\n")
#print(list3[3])

    