from edu.models import Offering
from insanity.sanity_check import SanityCheck


class CapacityCheck(SanityCheck):
    def given(self, student, offering, **kwargs):
        self.old_capacity = offering.capacity
        return True

    def when(self, func, **kwargs):
        return func == Offering.enroll

    def then(self, student, offering, return_value):
        if return_value:  # TODO: this condition should be moved to either `when` or `given`
            assert self.old_capacity > 0
            assert offering.capacity == self.old_capacity - 1
            assert student in offering.students
            assert student.get_current_semester_units() <= student.get_max_units()
        else:
            pass
            # TODO: assert
