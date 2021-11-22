list1=[]
n=int(input("enter number of students---"))
for i in range(0,n):
	b=int(input("enter percentage---"))
	list1.append(b)



def bubblesort():
        for i in range(0,len(list1)-1):
            for j in range(len(list1)-1):
                if(list1[j]>list1[j+1]):
                	c= list1[j]
                	list1[j] = list1[j+1]
                	list1[j+1] = c
                print("Bubble Sort---",list1)
bubblesort()
print("Top five highest score---",list1[-5:])



def selectionsort():
	for i in range(len(list1)):
		min=i
		for j in range(i+1,len(list1)):
			if(list1[min]>list1[j]):
				min=j
				c=list1[min]
				list1[j]=list1[min]
				list1[j]=c
			print("selection sort---",list1)
			break
selectionsort()



				
			
	
