class Gparent:
    def property(self):
        print("Grandparent hasn't made any business... But...")
class parent(Gparent):
    def start(self):
        print("Parents started an Empire... then...")
class child(parent):
    def carry(self):
        print("The child is going to build an enormous Empire..!!!")

obj=child()
obj.property()
obj.start()
obj.carry()