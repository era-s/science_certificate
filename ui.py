from database import DataBase
import sys


class UserInterface:
    def __init__(self):
        self.commands = {
            '관리자 모드': self.admin_mode,
            '난이도별 문제': self.select_difficulty,
            '단원별 문제': self.select_unit,
            '복습': self.review,
            '종료': self.quit
        }

        self.admin_commands = {
            '문제 추가': self.admin_add_problems,
            # '문제 수정': self.fix_problems,
            # '문제 삭제': self.delete_problems,
            # '문제 목록',
            # '난이도별 보기',
            # '단원별 보기',
            '관리자 모드 종료': self.admin_quit
        }

    def run(self, admin_notice):
        while True:
            if not admin_notice:
                print("프로그램을 시작합니다.")
            command = input("명령어를 입력해주세요. (난이도별 문제, 단원별 문제, 복습, 종료): ")
            if command in self.commands:
                if command == '관리자 모드':
                    print("관리자 모드로 전환합니다.")
                self.commands[command]()
            else:
                print("잘못된 입력입니다.")

    def admin_mode(self):
        self.admin_display_menu()
        admin_command = input("명령어를 입력해주세요.: ")
        if admin_command in self.admin_commands:
            self.admin_commands[admin_command]()
        else:
            print("잘못된 입력입니다.")

    def admin_display_menu(self):
        print('1. 문제 추가')
        print('2. 문제 수정')
        print('3. 문제 삭제')
        print('4. 문제 목록')
        print('5. 난이도별 보기')
        print('6. 단원별 보기')
        print('7. 관리자 모드 종료')

    def admin_add_problems(self):
        print("문제를 추가합니다.")
        db = DataBase
        add_buffer = []
        add_list_shower = ['단원(숫자)', '난이도(숫자)', '분류(이름)', '문제', '보기', '정답']
        for _ in range(6):
            print(add_list_shower[_], "를 입력해주세요.")
            add_buffer.append(input())
        db.add_database(add_buffer[0], add_buffer[1], add_buffer[2], add_buffer[3], add_buffer[4], add_buffer[5])

    def admin_quit(self):
        print("관리자 모드를 종료합니다.")
        self.run(True)

    def select_difficulty(self):
        difficulty = input("난이도를 입력해주세요. (1, 2, 3): ")
        if difficulty in ('1', '2', '3'):
            # TODO: get problems by difficulty from the database
            print("TODO: get problems by difficulty")
        else:
            print("Invalid difficulty level.")

    def select_unit(self):
        unit = input("단원명을 입력해주세요.: ")
        # TODO: get problems by unit from the database
        print("TODO: get problems by unit")

    def review(self):
        # TODO: get review data from the database
        print("TODO: get review data")

    def quit(self):
        print("오늘도 수고하셨습니다.")
        sys.exit(0)
