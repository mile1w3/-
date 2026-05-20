import itertools as it
import time as t

def brute_force_simulation(target_password, chars):
    
    length = len(target_password)
    attempts = 0
    start_time = t.time()

    print(f"[*] 공격 시작: 목표 비밀번호 '{target_password}'")
    print(f"[*] '{chars}' 문자의 {length}자리 순열을 생성하여 대입합니다...\n")

    for guess in it.product(chars, repeat=length):
        attempts += 1
        guess_str = "".join(guess)
        
        print(f"[시도 {attempts}] {guess_str}")

        if guess_str == target_password:
            end_time = t.time()
            duration = end_time - start_time
            print("-" * 30)
            print(f"[성공] 비밀번호를 찾았습니다: {guess_str}")
            print(f"[정보] 총 시도 횟수: {attempts}번")
            print(f"[정보] 소요 시간: {duration:.4f}초")
            return

    print("[실패] 순열 범위 내에 비밀번호가 없습니다.")

characters = input("비밀번호를 찾는데 사용할 문자들을 적어주세요.(알파벳+숫자를 원하면 AbC123을 입력)")

if(characters == "AbC123"):
    characters = "ABCDEFGHIJKLNMOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz1234567890"    

target = input("비밀번호를 입력해주세요.")

brute_force_simulation(target, characters)