from assessment import Assessment


class Exam(Assessment):

    def __init__(self, title, max_score):
        super().__init__(title, max_score)

    def display_info(self):
        print(f"{self.title} - Max score: {self.max_score}")

    def grade_message(self, score):
        if score < 0 or score > self.max_score:
            print("Invalid score!")
        elif score >= 50:
            print("Passed exam!")
        else:
            print("Filed exam!")
