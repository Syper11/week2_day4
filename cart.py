# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

class Cart():

    def addToCart(x):
        item = input ('What is your item you want to add to your cart?')
        quanity = input (f'How many {item} do you want to add to your cart? ')
        x[item] = quanity

    def showCart(x):
        print(f'These are the items in your cart {x}')

    def removeFromCart(x):
        y = input(f'What item from your cart do you want to remove {x} hit enter to remove! ')
        x.pop(input("item: ")) 

def shopping_cart():
    x = {}
    while True:
        cart=input('What do you want to do? Show/Add/Remove/Quit.')
            
        if cart.lower() == "add":
            Cart.addToCart(x)
           
        elif cart.lower() == "remove":
            Cart.removeFromCart(x)
            
        elif cart.lower() == "show":
            Cart.showCart(x)

        elif cart.lower() == "quit":
            print('Thanks for coming into the store! ')
            print(f'This is your cart! {x}')
            break
    
        else:
            print('Invalid input!')  
        
    return
shopping_cart()



Brett = shopping_cart()
print(Brett)
#Tyler = shopping_cart()
#print(Tyler)