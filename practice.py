# def profile(name, gender, department):
#     print("이름 : {}\t성별 : {}\t부서 : {} ".format(name, gender, department))
    

# profile("오동규", "남", "MSP")
# profile("서동아", "여", "CC1Group")

# def profile(name, age, main_lang):
#     print("이름 : {}\t나이 : {}\t주 사용 언어: {}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")


### 같은 학교 같은 학년 같은 반 같은 수업.


def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {}\t나이 : {}\t주 사용 언어: {}".format(name, age, main_lang))

profile("유재석")
profile("김태호")
