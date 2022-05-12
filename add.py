class students:
    def __init__(self,roll,name,marks_list):
        self.roll=roll
        self.name=name
        self.marks_list=marks_list
    def calculate_percentage(self):
        percentage=sum(self.marks_list)//len(self.marks_list)
        return percentage
    def grade(self):
        percentage=self.calculate_percentage()
        if percentage>=90:
            return 'A'
        elif percentage>=60:
            return 'B'
        elif percentage>=50:
            return  'C'
        else:
            return 'U'
roll=int(input("ENTER THE ROLL NUMBER:"))
name=input("ENTER THE ROLL NAME:")
count=int(input("no of sub:"))
marks=[]
for i in range(count):
    marks.append(int(input()))
s=students(roll,name,marks)
print(s.calculate_percentage())
print(s.grade())
