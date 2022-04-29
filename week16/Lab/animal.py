# Jingbo Wang
# animal.py
# to create and store animal imformation
class Animal:
    # constructer
    def __init__ (self, name, weight, height, habitat):
        self.name = name
        self.weight = weight
        self.height = height
        self.habitat = habitat
        
    # to get animal name
    def get_name(self):
        return self.name
    
    # to get animal weight
    def get_weight(self):
        return self.weight

    # to get animal height
    def get_height(self):
        return self.height

    # to get animal habitat
    def get_habitat(self):
        return self.habitat

    # to set animal weight
    def set_weight(self, weight):
        self.weight = weight

    #to set animal height  
    def set_height(self, height):
        self.height = height

# to print out anmail imformation
def to_string(name, weight, height, habitat):
    string = "Animal's name is " + name + "\nWeight: " + str(weight) + "\nHeight: " + str(height) + "\nHabitat: " + str(habitat)
    return string

def main():
    # to get two two different types of animals
    for i in range(2):
        # to get basic imformation 
        name = input ("Enter the animal's name: ")
        weight = float (input ("Enter the animal's weight (in kg): "))
        height = float (input ("Enter the animal's height (in meters): "))
        habitat = input ("Enter the animal's habitat: ")

        # to create a animal object to hold the basic imformation
        i = str(i)
        i = Animal (name, weight, height, habitat)

        # to print out the basic imformation 
        print(to_string(i.get_name(), i.get_weight(),
                        i.get_height(), i.get_habitat()))
        
        # re-input the new weight and height
        new_weight = float(input("\n\nRe-enter " + i.get_name() + "'s weight: "))
        new_height = float(input("\nRe-enter " + i.get_name() + "'s height: "))

        # to set the new weight and height 
        i.set_weight(new_weight)
        i.set_height(new_height)
        
        print("\n after 3 years!\n")

        # print again the imformation about the animal
        print(to_string(i.get_name(), i.get_weight(),
                        i.get_height(), i.get_habitat()))
        print("\n")
        
main()
