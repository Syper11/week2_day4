# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

class Cart():

    def __init__(self,cart,name):
        self.cart = cart
        self.name = name

    def addToCart(self):
        item = input (f'What is your item you want to add to your cart {self.name}?')
        quanity = input (f'How many {item} do you want to add to your cart? ')
        self.cart[item] = quanity

    def showCart(self):
        print(f'These are the items in your cart {self.cart}')

    def removeFromCart(self):
        y = input(f'What item from your cart do you want to remove {self.cart} hit enter to remove! ')
        self.cart.pop(input("item: ")) 

    def shopping_cart(self):
        
        while True:
            y =input(f'What do you want to do {self.name}? Show/Add/Remove/Quit.')
            
            if y.lower() == "add":
                Cart.addToCart(self)
           
            elif y.lower() == "remove":
                Cart.removeFromCart(self)
            
            elif y.lower() == "show":
                Cart.showCart(self)

            elif y.lower() == "quit":
                print('Thanks for coming into the store! ')
                print(f'This is your cart {self.name}! {self.cart}')
                break
    
            else:
                print('Invalid input!')  
        
        return