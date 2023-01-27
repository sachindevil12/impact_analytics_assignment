class AttendanceCombinations:
    def __init__(self, days, absent_limit=4):
        self.absent = '0'
        self.present = '1'
        self.days = days
        self.max_absences_pattern = absent_limit * self.absent
        self.combinations_list = self._generate_combinations()

    def _generate_combinations(self):
        combinations_list = []
        self._generate_combinations_recursively(self.days, '', combinations_list)
        return combinations_list

    def _generate_combinations_recursively(self, days, combination, combinations_list):
        if days == 0:
            combinations_list.append(combination)
        else:
            self._generate_combinations_recursively(days - 1, combination + self.absent,
                                                   combinations_list)
            self._generate_combinations_recursively(days - 1, combination + self.present,
                                                   combinations_list)

    def get_allowed_combinations(self):
        allowed_combinations = list(
            filter(lambda way: self.max_absences_pattern not in way, self.combinations_list))
        return allowed_combinations

    def calculate_miss_graduation_probability(self):
        missed_last_class = 0
        allowed_combinations = self.get_allowed_combinations()
        for combination in allowed_combinations:
            if combination[-1] == '0':
                missed_last_class += 1
        return f'{missed_last_class}/{len(allowed_combinations)}'


if __name__ == '__main__':
    attendance_combinations = AttendanceCombinations(5)
    print(attendance_combinations.calculate_miss_graduation_probability())
