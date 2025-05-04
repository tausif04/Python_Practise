class Institution:
    pass

class School(Institution):
    pass

school_instance = School()
print(isinstance(school_instance, Institution))  
