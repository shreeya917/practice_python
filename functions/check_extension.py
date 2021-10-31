def check_extension(filename):
    f_extn = filename.split(".")
    return f_extn


filename = input("Input your  Filename: ")
extension = check_extension(filename)
print(extension[-1])
