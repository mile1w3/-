# 할 일을 저장할 빈 리스트 생성
todo_list = []

def show_menu():
    print("\n--- 할 일 목록 매니저 ---")
    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 할 일 삭제")
    print("4. 종료")
    print("------------------------")

def add_task():
    task = input("추가할 할 일을 입력하세요: ")
    todo_list.append(task)
    print(f"'{task}' 항목이 추가되었습니다.")

def view_tasks():
    print("\n[현재 할 일 목록]")
    if not todo_list:
        print("목록이 비어 있습니다.")
    else:
        # enumerate를 사용하면 리스트의 인덱스와 값을 동시에 가져올 수 있습니다.
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    if todo_list:
        try:
            num = int(input("삭제할 번호를 입력하세요: "))
            # 사용자가 입력한 번호(1부터 시작)를 리스트 인덱스(0부터 시작)로 변환
            removed = todo_list.pop(num - 1)
            print(f"'{removed}' 항목이 삭제되었습니다.")
        except (ValueError, IndexError):
            print("잘못된 번호입니다. 다시 확인해 주세요.")

# 프로그램 메인 루프
while True:
    show_menu()
    choice = input("원하는 메뉴 번호를 선택하세요: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 1~4 사이의 숫자를 입력해 주세요.")