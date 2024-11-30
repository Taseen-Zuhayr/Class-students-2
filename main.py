class student:
    platform = "Codingal"
    subject = "Python"
    def __init__(self,name,country,favcolor):
        self.name = name
        self.country = country
        self.favcolor = favcolor

student1 = student("Taseen","Bangladesh","White")
student2 = student("Chiamalite","Nigeria","Blue")
student3 = student("Vedanshi","Portugal","Green")

print("The students are {}, {} and {}.".format(student1.name,student2.name,student3.name))



