import os
import filecmp
import csv

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	fopen=open(file)
	list3=[]
	for b in fopen:
		data=b.split(',')
		dictionary_students={}
		dictionary_students['First']=data[0]
		dictionary_students['Last']=data[1]
		dictionary_students['Email']=data[2]
		dictionary_students['Class']=data[3]
		dictionary_students['DOB']=data[4]
		list3.append(dictionary_students)
	return (list3[1:])


#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	#data=getData(file)

	q=sorted(data,key=lambda k: k[col])
	qb=(q[0]["First"]),str(q[0]["Last"])
	qbstr=str(qb)
	qbstrr=qbstr.replace("(","")
	qbstrrr=qbstrr.replace(")","")
	qbstrrrr=qbstrrr.replace(",","")
	qbstrrrrr=qbstrrrr.replace("'","")
	return (qbstrrrrr)

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	year_dict={}
	for a in data:
		if a["Class"] not in year_dict:
			year_dict[a["Class"]]=0
		year_dict[a["Class"]]+=1
	tuples_year=list(year_dict.items())
	sortedty=sorted(tuples_year, key=lambda x: x[1],reverse=True)
	return (sortedty)



# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	days_dict={}
	for b in a:
		q=b["DOB"].split("/")
		if q[1] not in days_dict:
			days_dict[q[1]]=0
		days_dict[q[1]]+=1
	tuples_days=list(days_dict.items())
	days_sorted=sorted(tuples_days, key=lambda x:x[1])
	daysstr=str(days_sorted[-1][0])	
	qbr=daysstr.strip()
	qbrint=int(qbr)
	return (qbrint)


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	ages_number=0
	amount_of_ages=0
	for b in a:
		q=b["DOB"].split("/")
		ages_number+=(2017-int(q[2]))
		amount_of_ages+=1
	return(int(ages_number/amount_of_ages))



#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here
	q=sorted(a,key=lambda k: k[col])
	filename=open(fileName, "w")
	keys=q[0].keys()
	csv_w=csv.DictWriter(filename,keys)

	for a in q:
		b=a.keys()
		a.pop('DOB', None)
		a.pop("Class", None)
		csv_w.writerow(a)
		#a[-1]="\n"
	filename.close()
	return




################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

