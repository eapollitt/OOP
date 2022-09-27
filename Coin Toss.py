import CoinClass as c #note this import statement; it's the name of the file (case matters based on how you name your file)
#first have to access the blueprints to create the object 

# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'

       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter

       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10): #10 times
           my_coin.toss()# calling the toss method of the instance; important to do my.coin not Coin
           my_coin.sideup = "Heads" # if you did this it owuld be heads everytime because if sideup is not hidden
           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())
           #everytime the toss method is called, the get_sideup method is called

           


       

# Call the main function.

main()


# class | attribute method 
# program | instances  -->^ method




#object
#name = 'john' #name is an instance of the sting object
#print(name.capitalize() #method called capitalize that performs an action on the string object
# --> John



#name : string as my.coin : Coin

#my.coin.get_sideup()
# get_sideup is a method that belongs to the Coin class