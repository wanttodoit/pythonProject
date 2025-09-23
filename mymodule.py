def my_add(a, b):
    return a+b

def my_sub(a, b):
    return a - b

class Character:
    def __init__(self, name):
        self.name = name
    def speak(self)
        print(f"저는 {self.name}입니다.")

print(f"mymodule안에서의 __name__: {__name__}")






if __name__ == "__main__":
    print(my_add(1, 2))
    print(my_sub(3, 4))
    wizard = character("법사")
    wizard.speak()
