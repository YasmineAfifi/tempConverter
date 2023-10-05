
def temp_convert():
    celsius = input("please enter the celsius degree : ")
    result = (float(celsius) * 9/5) + 32
    return celsius +" degrees Celsius are "+str(result)+" degrees Farenheit."



print(temp_convert())