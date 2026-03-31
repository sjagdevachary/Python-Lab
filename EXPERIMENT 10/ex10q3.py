class Father:
    def skill1(self):
        print("Son possess...\n")
        print("Preaching Skills..")
class Mother:
    def skill2(self):
        print("Singing Skills")
class son(Father,Mother):
    def skill3(self):
        print("Drumming Skills")
        
o=son()
o.skill1()
o.skill2()
o.skill3()