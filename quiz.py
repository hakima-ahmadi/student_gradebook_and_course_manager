from assessment import Assessment


class Quiz(Assessment):

    def __init__(self, title, max_score):
        super().__init__(title, max_score)

    def display_info(self):
        print(f"{self.title} - Max score: {self.max_score}")

    def grade_message(self, score):
        if score < 0 or score > self.max_score:
            print("Invalid score!")
        elif score >= 5:
            print("Great quiz result!")
        else:
            print("Needs more practice!")
