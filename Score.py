from Utils import SCORES_FILE_NAME


class Score:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.points_of_winning = (self.difficulty * 3) + 5
        self.current_score = self.points_of_winning

    def write_to_file(self):
        with open(SCORES_FILE_NAME, 'w', encoding='utf-8') as scores_file:
            scores_file.write(str(self.current_score))

    def add_score(self):
        try:
            with open(SCORES_FILE_NAME, 'r', encoding='utf-8') as scores_file:
                self.current_score = int(scores_file.read())
            self.current_score += self.points_of_winning
            self.write_to_file()
        except FileNotFoundError:
            self.write_to_file()
        finally:
            return self.current_score

