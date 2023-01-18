with open("demo.txt", mode='w', encoding='utf-8') as file:
    file.write("This is the first line\n")
    file.write("This is the second line\n")
    file.write("This is the last line\n")

with open("demo.txt", mode='r', encoding='utf-8') as file2:
    print(file2.read(3))
    print(file2.readline())
    print(file2.read())
    file2.seek(0)
    print(file2.tell())
    print(file2.readlines())
    file2.seek(0)
    print(list(file2))

with open("courses.txt", mode='r', encoding='utf-8') as course:
    file.write("Course Id,Course Name,Instructor\n")
    file.write("C1,Intro to A+,Valerie Boss\n")
    file.write("C2,Intro to Python,Sammi G\n")
