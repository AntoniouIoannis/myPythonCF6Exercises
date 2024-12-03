# from 20_student_class_demo.py & pages 73-77
class Student:
    def __init__(self, id: int, firstname: str, lastname: str, univ: str): 
        self.id = id
        self.firstname = firstname 
        self.lastname = lastname
        self.univ = univ


# απο 22_point_class_demo.py & pages 80-83 from chapter02
    # Properties for `id`  
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    # Properties for `firstname`
    @property
    def firstname(self):
        return self.__firstname
    
    @firstname.setter
    def firstname(self, firstname):
        self.__firstname = firstname
    
    # Properties for `lastname`
    @property
    def lastname(self):
        return self.__lastname
    
    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    # Properties for `univ`
    @property
    def univ(self):
        return self.__univ
    
    @univ.setter
    def univ(self, univ):
        self.__univ = univ

def mySign():
    name = "Antoniou Ioannis"
    job = "Full-Stack Software Developer"
    taught = "Taught by A.U.E.B. Coding Factory"
    nickname = "my Nickname: "

    for n in range(len(name)):
        print(name[n], end=" * ")
    print()

    for char in job:
        print(char, end="_")
    print()


    for t in range(len(taught)):
        print(taught[t], end=" ")
    print()

    print(nickname + name[9:10].lower() + "-" + name[:1].lower() + name[1:8])
    

def main():
    student = Student(1, "Ioannis", "Antoniou", "A.U.E.B.")
    
    print("\nStart:\n\tID: ", student.id)
    print("\tFirst Name: ", student.firstname)
    print("\tLast Name: ", student.lastname)
    print("\tUniversity: ", student.univ)
    print("End.")
    print("\nCreated by:")
    mySign()



if __name__ == "__main__":
    main()