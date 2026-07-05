String=("Rahul","piyush","Manohar","shivam","Harshad","Palak")

String=list(filter(lambda x: len(x)>5,String))
print("string of length > 5:",String)