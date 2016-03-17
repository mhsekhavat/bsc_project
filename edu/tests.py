# tests
# TEST 1

# given s, o
# when enroll(s, o)
# then o1.capacity == o2.capacity + 1 && o1.capacity > 0


# code
@action()
def enroll(student, offering):
    pass


def action(func):
    def wrapper(**kwargs):
        tests = filter(lambda test: test.given(kwargs), all_tests)
        ret = func(**kwargs)
        for test in tests:
            test.then(return_value=ret, **kwargs)

    return wrapper


class test_1():
    def given(self, student, offering, **kwargs):
        self.old_capacity = offering.capacity

    def when(self, func):
        return func == enroll

    def then(self, student, offering):
        assert self.old_capacity > 0
        assert offering.capacity == self.old_capacity - 1
        assert student in offering.students
        assert student.current_semester_units() <= student.get_max_units()
