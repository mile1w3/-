import random

# 1. 게임에 사용할 단어 목록 (리스트)
words = ["python", "computer", "programming", "puzzle", "player"]
word = random.choice(words)  # 무작위로 한 단어 선택
word_length = len(word)

# 2. 게임 상태 초기화
hangmen = [  # 행맨 그림 (목숨에 따라 변화)
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """
]

lives = 6  # 목숨
guesses = []  # 사용자가 입력한 글자 저장
display = []  # 화면에 표시될 단어 상태 (예: _ _ _ _)

# 초기 화면 설정 (_ _ _ _) - for문 사용
for _ in range(word_length):
    display.append("_")

print("★ 행맨 게임을 시작합니다! ★")

# 3. 게임 루프 (목숨이 남아있고, 단어를 다 맞추지 못했을 때 반복)
while lives > 0 and "_" in display:
    print(hangmen[6 - lives]) # 현재 행맨 그림 출력
    print(f"남은 목숨: {lives}")
    print("현재 단어: " + " ".join(display))
    print("입력했던 글자들: " + ", ".join(guesses))
    
    # 사용자 입력
    guess = input("글자를 입력하세요: ").lower()
    
    # 중복 입력 확인
    if guess in guesses:
        print(f"이미 '{guess}'를 입력하셨습니다. 다시 입력해주세요.")
        continue
    
    guesses.append(guess)
    
    # 입력한 글자가 단어에 있는지 확인 - for문과 if문 사용
    if guess in word:
        print(f"맞았습니다! '{guess}'가 단어에 있습니다.")
        # 단어의 각 글자를 확인하며 맞춘 글자로 변경
        for index in range(word_length):
            if word[index] == guess:
                display[index] = guess
    else:
        print(f"틀렸습니다. '{guess}'는 단어에 없습니다.")
        lives -= 1

# 4. 게임 결과
if "_" not in display:
    print("\n★ 축하합니다! 단어를 맞추셨습니다! ★")
    print(f"정답: {word}")
else:
    print(hangmen[6]) # 마지막 행맨 그림
    print("\n아쉽습니다. 목숨을 다 잃으셨습니다.")
    print(f"정답: {word}")