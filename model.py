from database import DataBase
import random


class SolveMode:
    def __init__(self):
        self.solve_commands = {
            '1': self.difficulty_mode,
            '2': self.unit_mode,
            '3': self.review_mode
        }

    def solving_start(self, solve_command):
        if solve_command in self.commands:
            self.commands[solve_command]()
        else:
            print("exitcode(1) .")

    def woojin_math(self, problem_amount, v):
        v_new = []
        v_old = []
        for problem in v:
            if problem[6] == 0:
                v_old.append(problem)
            else:
                v_new.append(problem)
        random.shuffle(v_new)
        random.shuffle(v_old)

        new_amount = problem_amount * 30 // 100
        old_amount = problem_amount - new_amount

        v_fin = []
        for _ in range(new_amount):
            v_fin.append(v_new[_])
        for _ in range(old_amount):
            v_fin.append(v_old[_])
        random.shuffle(v_fin)
        return v_fin

    def difficulty_mode(self, difficulty_command, problem_amount):
        db = DataBase
        v = [db.get_problems_by_difficulty()]
        que = self.woojin_math(problem_amount, v)
        print("난이도 모드 테스트")
        print(que)


    def unit_mode(self, unit_command, problem_amount):
        db = DataBase
        v = [db.get_problems_by_unit()]
        que = self.woojin_math(problem_amount, v)
        print("단원 모드 테스트")
        print(que)

    def review_mode(self):
        print("개발중입니다.")