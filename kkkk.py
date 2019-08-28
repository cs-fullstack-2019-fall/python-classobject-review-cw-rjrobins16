# # Python classes review graded

# ### Problem 1:
# Create a Movie class with the following properties/attributes: ```movieName```, ```rating```, and ```yearReleased```.
# * Override the default ```str``` (to-String) method and implement the code that will
# print the value of all the properties/attributes of the Movie class

class Movie:
    def __init__(self,moviename, rating, yearreleased):
        self.moviename = moviename
        self.rating = rating
        self.yearreleased = yearreleased
    def __str__(self):
        my_instance_str = f'{self.moviename} = moviename , {self.rating} = rating , {self.yearreleased} = yearreleased'
        return my_instance_str


# * In your ```main``` function create *two* instances of the Product class
#     * Assign a value of your choosing for each property/attribute
#     * Print all properties to the console.

def main():
    babyboy = Movie("Baby Boy","R",2000)
    cinderella = Movie("Cinderella","G",1980)
    print(babyboy.__str__())
    print(cinderella.__str__())
    lipgloss = Product(2.00,50,"GLOSS")
    dresses = Product(25.00,10,"maxi")
    print (lipgloss.__str__())
    print (dresses.__str__())


# Problem 2:
# Create a class Product that represents a product sold online.
class Product:
    def __init__(self,price,quantity,name):
        self.price = price
        self.quantity = quantity
        self.name = name
    def __str__(self):
        my_instance_str = f'{self.price} = price , {self.quantity} = quantity , {self.name} = name'
        return my_instance_str


# A Product has ```price```, ```quantity``` and ```name``` properties/attributes.
# * Override the default ```str``` (to-String) method and implement the code that
# will print the value of all the properties/attributes of the Product class


# * In your ```main``` function create *two* instances of the Product class
#     * Assign a value of your choosing for each property/attribute
#     * Print all properties to the console.
#


main()