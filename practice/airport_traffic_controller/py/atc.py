class ATC:
    '''
    Singleton Pattern Basic example using an ATC
    '''
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance= super().__new__(cls)
            cls.__instance = ATC()
        return cls.__instance
    
    def atc_print():
        print("This is the ATC")
    
#Usage
instance1=ATC()
instance2=ATC()

print("If instance1 is instance2 then will print True ",instance1 is instance2)