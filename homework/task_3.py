class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 'wage', 'bonus': 'bonus'}

class Position(Worker):
    def get_full_name(self):
        name_surname = f'{self.name} {self.surname}'
        return print(f'И.О. сотрудника: {name_surname}')
    def det_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return print(f'Доход сотрудника {total_income}')

some_worker = Position()

some_worker.name = 'Kirill'
some_worker.surname = 'Kurenev'
some_worker.position = 'Test-Engineer'
some_worker._income['wage'] = 60000
some_worker._income['bonus'] = 50000

some_worker.get_full_name()
some_worker.det_total_income()





