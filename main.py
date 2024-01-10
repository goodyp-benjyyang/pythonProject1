class Bird:
    def fly(self):
        print("我在天空自由的飞翔。。。")
class Ostrich(Bird):
    #重写Bird类的fly（）方法
    def fly(self):
        print("我只能子地上奔跑。。")
    def fly_again(self):
        print("吃了神奇小药丸")
        #使用类名调用实例方法（未绑定方法）调用父类被重写的方法
        Bird.fly(self)

os = Ostrich()
os.fly_again()