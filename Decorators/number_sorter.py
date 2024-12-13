def decorator(func):
    def wrap (*args, **kwargs):
        processed_numbers=func(*args, **kwargs)
        formatted_num = f"+91 {processed_numbers}"
        return formatted_num
    return wrap


@decorator
def process_numbers():
    number = input ("enter your number")
    rev = number[::-1][:10]   #list and string slicing read
    print (rev)

    return rev


print(process_numbers())