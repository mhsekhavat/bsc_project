for app in INSTALLED_APPS:
    mod = app.has_attr('stest')
    for sclass in mod:
        register(sclass)
