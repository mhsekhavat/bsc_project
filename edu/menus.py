# Add two items to our main menu
from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

Menu.add_item('main', MenuItem("Professor Panel",
                               reverse("index"),
                               weight=10, ))

student_children = (
    MenuItem("My Courses", reverse('student_enrollments')),
)

Menu.add_item('main', MenuItem("Student Panel",
                               reverse("student"),
                               weight=20, children=student_children))

# Define children for the my account menu
myaccount_children = (
    MenuItem("Edit Profile",
             reverse("index"),
             weight=10,
             icon="user"),
    MenuItem("Admin",
             reverse("admin:index"),
             weight=80,
             separator=True,
             check=lambda request: request.user.is_superuser),
    MenuItem("Logout",
             reverse("index"),
             weight=90,
             separator=True,
             icon="user"),
)

# Add a My Account item to our user menu
Menu.add_item("user", MenuItem("My Account",
                               reverse("index"),
                               weight=10,
                               children=myaccount_children))
