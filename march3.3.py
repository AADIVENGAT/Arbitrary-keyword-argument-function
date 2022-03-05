#Arbitrary keyword argument
def student_details(name,**k):
    print(name)
    print(k)
student_details("smp",age=7,std=12,school="ahss",city="puducherry")         