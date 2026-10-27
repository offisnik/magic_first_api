
class EveryCheckes:
    status_code = None

    def check_code_answer(self):
        assert self.status_code == 200, f'Ошибка в статус коде, пришло = {self.status_code}'