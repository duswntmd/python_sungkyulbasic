id = 'abcd'
pw = 'a1234'
input_id = input("아이디 입력: ")
input_pw = input("비밀번호 입력: ")
if id != input_id:
    print("아이디 또는 패스워드가 일치하지 않으면 아이디를 찾을 수 없습니다.")
elif pw != input_pw:
    print("패스워드가 일치하지 않습니다.")
else:
    print("환영합니다." )
