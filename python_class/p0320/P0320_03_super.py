class Car:
    value = "부모의 값 1"
    def car_func(self):
        print("부모의 값을 출력합니다.")

# 상속 - 자식클래스        
class Am(Car):
    value = "자식의 값 2"
    def car_func(self):
        print("[ 자식클래스에서 부모값 출력 ]")
        # 부모의 값을 출력하고 싶을때 super()사용
        super().car_func()
        print("부모의 값 : ",super().value) # 부모값 출력
        print("자식의 값 : ",self.value)    # 자식값 출력
        
a1 = Am()
a1.car_func()               