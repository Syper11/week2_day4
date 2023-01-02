class String():
    def __init__(self):
        self.string1 = ""

    def get_string(self):
        self.string1 = input()
    
    def print_string(self):
        print(self.string1.upper())

string1 = String()
string1.get_string()
string1.print_string()