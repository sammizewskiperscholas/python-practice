#f= open('my_file.txt')

with open('courses.txt', mode= 'w', encoding= 'utf-8') as course:
    course.write('Course Id, Course Name, Instructor\n')
    course.write('CSIPL01, Intro to A+, Valerie Boss\n')
    course.write('CSILP02, Intro to Python, Sammi G') 

with open('courses.txt', mode ='r+', encoding= 'utf-8') as course1:
    for line in course1.read().split('\n'): #use split function to split at \n
        #print(line) #returns 3 lines
        c_id, c_name, instructor= line.split(',') #split at comma and unpack into variable
        print(c_id, '\t', c_name, '(', instructor, ')')