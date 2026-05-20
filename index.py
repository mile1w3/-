import random

# 1. 초기 설정
answer = random.randint(1, 100)
max_chances = 7  # 총 기회
count = 0        # 사용한 기회

print("★ 업다운 게임을 시작합니다! ★")
print(f"1부터 100 사이의 숫자를 {max_chances}번 안에 맞춰보세요.")

# 2. 게임 루프 시작
while count < max_chances:
    count += 1
    print(f"\n{count}번째 시도 (남은 기회: {max_chances - count}번)")
    
    # 사용자 입력 받기
    user_input = input("숫자를 입력하세요: ")
    
    # 숫자가 아닌 입력에 대한 예외 처리 (기초 단계에선 생략 가능하지만 넣으면 좋습니다)
    if not user_input.isdigit():
        print("숫자만 입력해 주세요!")
        count -= 1 # 기회를 차감하지 않음
        continue

    guess = int(user_input)

    # 3. 판정 로직
    if guess < 1 or guess > 100:
        print("1에서 100 사이의 숫자만 입력 가능합니다.")
        count -= 1
        continue

    if guess > answer:
        print("DOWN! 더 작은 숫자입니다.")
    elif guess < answer:
        print("UP! 더 큰 숫자입니다.")
    else:
        print(f"축하합니다! {count}번 만에 정답({answer})을 맞추셨습니다!")
        break
else:
    # while문의 조건이 거짓이 되어 종료될 때(즉, 기회를 다 썼을 때) 실행
    print(f"\n아쉽습니다. 모든 기회를 사용하셨습니다. 정답은 {answer}였습니다.")