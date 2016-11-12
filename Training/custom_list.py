import array

class CustomList():
    
    def __init__(self):
        self.items = array.array('L')
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)
    
    def remove(self, input_index):
        value = self.items.__getitem__(input_index)
        self.items.remove(value)
    
    def print_array(self):
        for item in self.items:
            print item,
        print "\n"


if __name__ == "__main__":
    new_list = CustomList()
    
    new_list.print_array()
    
    new_list.add_item(3)
    
    new_list.print_array()
    new_list.add_item(5)
    new_list.add_item(2)
    new_list.add_item(4)   
    new_list.print_array()
    new_list.remove_item(3)
    new_list.print_array()
    new_list.remove(0)
    new_list.print_array()
    
    
    
    
    


        
        
        
        
        
        