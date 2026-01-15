def is_editor(user):
    return user.is_superuser or user.groups.filter(name='Editor').exists()

def is_author(user):
    return user.groups.filter(name='Author').exists()
