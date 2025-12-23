class Singleton:
    '''
    This is a singleton class example.
    '''
    __instance = None

    '''
    Now in python __init__ method acts as a constructor. to override it we can use __new__ method.
    '''

    def __new__(cls):
        '''
        Docstring for __new__
        To ensure only one instance is created.
        :param cls: Description
        '''
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance
    
    def some_business_logic(self):
        '''
        Business logic method.
        '''
        pass
        
'''
To verify that only one instance is created.
'''
s1 = Singleton()
s2 = Singleton()
print(f"Are both instances the same? {s1 is s2}")  # Should print True