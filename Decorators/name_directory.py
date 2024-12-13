from operator import itemgetter

def decorator (func):
    def wrap (*args, **kwargs):
        gender_sort = func (*args, **kwargs)

        for person in gender_sort:
            first_name = person[0]
            last_name = person[1]
            age = person [2]
            sex = person[3]

            if sex == 'f':
                print (f" Ms. {first_name} {last_name}  age: {age}")
            else :
                print (f" Mr. {first_name} {last_name} age: {age}")


        
        return gender_sort

        
    return wrap





@decorator
def name_input():
    n= int (input ("Enter the number of data you want to store: "))

    people = []

    for i in range(n):
        first_name = input ("name: ")
        last_name = input("lastname: ")
        age = input("age: ")
        sex = input("sex: ")
        age = int (age)

        people.append ((first_name,last_name,age,sex))
    

    people.sort (key=itemgetter(2))
    sorted_by_age = people
    return sorted_by_age
    




name_input()