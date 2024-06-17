class Result:
    def __init__(self, test_result: float, mid_result: float, final_result: float) -> None:
        self.test_result: float = test_result
        self.mid_result: float = mid_result
        self.final_result: float = final_result
    
    def get_result(self) -> float:
        return (self.test_result + self.mid_result + self.final_result)
    
    def get_grade(self) -> str:
        result=self.get_result()
        if result>= 80:
            return "A"
        elif result < 80 and result >= 60:
            return "B"
        elif result < 60 and result >= 50:
            return "C"
        elif result < 50 and result >= 40:
            return "D"
        else:
            return "F"
        
class Course(Result):
    def __init__(self, course_name: str, course_id: str, test_result: float, mid_result: float, final_result: float) -> None:
        super().__init__(test_result, mid_result, final_result)
        self.course_name = course_name
        self.course_id = course_id
        self.grade = self.get_grade()

    def __str__(self) -> str:
        return  self.course_name
    
    def getCourseNameAndGrade(self)->str:
        return  f'{self.course_name} : {self.grade} '

class Student(Course):
    def __init__(self,fullName:str,stud_id:str) -> None:
        self.fullName=fullName
        self.stud_id=stud_id
        self.courses=[]

    def add_course(self,course:Course):
        if len(self.courses) <5:
           self.courses.append(course)
           print("Corse Added Successfully ")
        else:
            print("You can not add more than 5 courses !!!")

    
    def __str__(self) -> str:
        t=','.join([course.getCourseNameAndGrade() for course in self.courses])
        return f'Name: {self.fullName} student ID: {self.stud_id} Course Name: {t}'


def main()->None:
    count:int=0
    students=[]

    while True:
        print("------------------------------------------------")
        print("------------------------------------------------")
        print("----     Student Grade Management System    ----")
        print("------------------------------------------------")
        print("------------------------------------------------\n")
        print("----  1. Register  Student                  ----")
        print("----  2. Display  Student Name              ----")
        print("----  3. Register  Course  and  Result  For Student----")
        print("----  4. Show Student Grade                 ----")
        print("----  5. Quit                               ----")
        print("------------------------------------------------\n")
        
        chose:int=int(input("Enter Chose: "))

        if chose == 1:
            name:str=input("Enter Name of Student: ")
            stud_id:str=input("Enter Student ID: ")
            
            student:Student=Student(name,stud_id)
            students.append(student)

        if chose == 2:
            for stud in students:
                print(stud.fullName)

        if chose == 3:
            i=1
            for stud in students:
                print(f"{i}:{stud.fullName}")
                i+=1
                
            ch=int(input("Chose Student You want to add course and result:"))
            stud=students[ch-1]
            count=1
            while True:
                course_name=input("Enter Course Name: ")
                course_id=input("Enter Course Code: ")
                test:float=float(input("Enter Test Result: "))
                mid:float=float(input("Enter Mid Test Result: "))
                final:float=float(input("Enter Final Test Result: "))
                course=Course(course_name,course_id,test,mid,final)
                stud.add_course(course)
                count+=1
                print("------------------------------------------------\n")
                print("Sorry You can not add more than 5 courses !!!") if count > 5 else print("----  1. Add Other Corses                ----")
                print("----  2. Quit             ----")
                print("------------------------------------------------\n")
                ch:int=int(input("Enter Chose: "))

                if ch == 1:
                    pass
                elif ch==2:
                    break
                else:
                    print ("unknown character sry!!")
                    break
            
        if chose == 4:
            i=1
            j=1
            for stud in students:
                    print(f"{i}:{stud.fullName}")
                    i+=1

            stud_chose=int(input("Chose Student You Want To See Grade:"))
            stud=students[stud_chose-1]
            
            for corse in stud.courses:
                print(f"{j}:{corse.course_name}")
                j+=1

            course_chose=int(input("Chose Student You Want To See Grade:"))
                

            print(stud.courses[course_chose-1].getCourseNameAndGrade())

        if chose == 5:
            break

    
if __name__ == '__main__':
    main()

