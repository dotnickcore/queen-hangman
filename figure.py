class Figure:
    def __init__(self):
        self.__figure = ["-------", "|   |"]
        self.__is_head_added = False
        self.__is_body_added = False
        self.__is_left_arm_added = False
        self.__is_right_arm_added = False
        self.__is_left_leg_added = False
        self.__is_right_leg_added = False
        
    def add_head(self):
        self.__figure.append("|   O")
        self.__is_head_added = True
        
    def get_head_status(self):
        return self.__is_head_added
    
    def add_body(self):
        self.__figure.append("|   |")
        self.__is_body_added = True
        
    def get_body_status(self):
        return self.__is_body_added
    
    def add_left_arm(self):
        self.__figure[-1] = "|  -|"
        self.__is_left_arm_added = True
        
    def get_left_arm_status(self):
        return self.__is_left_arm_added
    
    def add_right_arm(self):
        self.__figure[-1] = "|  -|-"
        self.__is_right_arm_added = True
        
    def get_right_arm_status(self):
        return self.__is_right_arm_added
    
    def add_left_leg(self):
        self.__figure.append("|  /  ")
        self.__is_left_leg_added = True
        
    def get_left_leg_status(self):
        return self.__is_left_leg_added
    
    def add_right_leg(self):
        self.__figure[-1] = "|  / \\"
        self.__is_right_leg_added = True
        
    def get_right_leg_status(self):
        return self.__is_right_leg_added
    
    def display(self):
        """Helper method to display the figure"""
        for line in self.__figure:
            print(line)
        print("^^^^^^^^^^")