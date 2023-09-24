from privileges import Admin

admin = Admin("john", "johnson", ['tennis', 'fishing', 'playing guitar'], 0)

admin.privileges.show_privileges()