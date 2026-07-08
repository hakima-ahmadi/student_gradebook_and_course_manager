class Assessment:

    def __init__(self, title, max_score):
        self._title = title
        self._max_score = max_score

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def max_score(self):
        return self._max_score

    @max_score.setter
    def max_score(self, value):
        if value < 0:
            print("Max score must be positive!")
        self._max_score = value

    def calculate_percentage(self, score):
        print((score/self.max_score) * 100)

    def grade_message(self, score):
        pass

    def display_info(self):
        print(f"{self.title} - Max Score: {self._max_score}")
