# 변수 
# 애완동물을 소개해 주세요~ 
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print(animal)
print(name)
print(age)

print("-----------------------")

print("우리집 " + animal +"의 이름은 " + name + "예요")
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# + 대신 , 사용 가능하지만 ,를 사용하는 경우에는 띄어쓰기가 한칸씩 들어가게 된다.
# 그리고 문자열이 아닌 타입을 str로 형변환 해주지 않아도 사용 가능하다.
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))