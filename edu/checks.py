from edu.models import Offering
from insanity.sanity_check import SanityCheck


def unbind_and_compare(bound_method, class_method):
    # TDOO: this is a very bad toff! find the correct implementation!
    import inspect
    return inspect.getsource(bound_method) == inspect.getsource(class_method)


class CapacityCheck(SanityCheck):
    def given(self, offering, student, **kwargs):
        self.old_capacity = offering.capacity
        return True

    def when(self, *args, func, **kwargs):
        return unbind_and_compare(func, Offering.enroll)

    def then(self, offering, student, return_value, **kwargs):
        if return_value:  # TODO: this condition should be moved to either `when` or `given`
            assert self.old_capacity > 0
            assert offering.capacity == self.old_capacity - 1
            # assert student in offering.get_students() TODO: implement
            # assert student.get_current_semester_units() <= student.get_max_units() TODO: implement
        else:
            pass
            # TODO: assert
