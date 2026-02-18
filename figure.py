class Figure:
    def __init__(self):
        self.__figure = ["-------", "|   |", "|", "|", "|", "|"]
        self.__is_head_added = False
        self.__is_body_added = False
        self.__is_left_arm_added = False
        self.__is_right_arm_added = False
        self.__is_left_leg_added = False
        self.__is_right_leg_added = False
        
    def add_head(self) -> None:
        self.__figure[2] = "|   O"
        self.__is_head_added = True
        
    def get_head_status(self) -> bool:
        return self.__is_head_added
    
    def add_body(self) -> None:
        self.__figure[3] = "|   |"
        self.__is_body_added = True
        
    def get_body_status(self) -> bool:
        return self.__is_body_added
    
    def add_left_arm(self) -> None:
        if self.__figure[3] == "|":
            self.__figure[3] = "|  -|"
        else:
            self.__figure[3] = "|  -|"
        self.__is_left_arm_added = True
        
    def get_left_arm_status(self) -> bool:
        return self.__is_left_arm_added
    
    def add_right_arm(self) -> None:
        self.__figure[3] = "|  -|-"
        self.__is_right_arm_added = True
        
    def get_right_arm_status(self) -> bool:
        return self.__is_right_arm_added
    
    def add_left_leg(self) -> None:
        self.__figure[4] = "|  /  "
        self.__is_left_leg_added = True
        
    def get_left_leg_status(self) -> bool:
        return self.__is_left_leg_added
    
    def add_right_leg(self) -> None:
        if self.__figure[4] == "|":
            self.__figure[4] = "|    \\"
        elif self.__figure[4] == "|  /  ":
            self.__figure[4] = "|  / \\"
        else:
            self.__figure[4] = "|    \\"
        self.__is_right_leg_added = True
        
    def get_right_leg_status(self) -> bool:
        return self.__is_right_leg_added
    
    def display(self) -> None:
        """Helper method to display the figure"""
        for line in self.__figure:
            print(line)
        print("^^^^^^^^^^")