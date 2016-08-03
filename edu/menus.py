# Add two items to our main menu
from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

Menu.add_item('main', MenuItem("Professor Panel",
                               reverse('index'),
                               weight=10,
                               check=lambda request: hasattr(request.user, 'professor'),
                               ))

student_children = (
    MenuItem("My Courses", reverse('student_enrollments')),
)

Menu.add_item('main', MenuItem("Student Panel",
                               reverse('student'),
                               weight=20,
                               children=student_children,
                               check=lambda request: hasattr(request.user, 'student'),
                               ))

staff_children = (
    MenuItem("Students", reverse('staff_students')),
)

Menu.add_item('main', MenuItem("Staff Panel",
                               reverse('staff'),
                               weight=20,
                               children=staff_children,
                               check=lambda request: request.user.is_staff,
                               ))

Menu.add_item('main', MenuItem("Django Admin",
                               '/admin/',
                               check=lambda request: request.user.is_superuser,
                               ))
