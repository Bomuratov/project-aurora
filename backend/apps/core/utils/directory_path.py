def upload_path_menu(instance, filename):
    file = filename.rfind(".")
    formatt = filename[file:]
    name = instance.name + formatt
    return "{0}/category/{1}/{2}".format(
        instance.restaurant.name, instance.category.name, name
    )


def upload_path_vendor_backgroud(instance, file):
    return f"vendors/{instance.name}/backgroud/{file}"

def upload_path_vendor_logo(instance, file):
    return f"vendors/{instance.name}/logo/{file}"