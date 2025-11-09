import os
from random import randint


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# before function File storage
def get_filename_ext_rand(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    random1 = randint(100, 999)
    random2 = randint(100, 999)
    output = f'{random1}{random2}'
    return ext.lower(), output


# ######### for users imgs ######### #
def user_image_path(instance, filename):
    ext, output = get_filename_ext_rand(filename)
    final_name = f"{output}{ext}"
    return f"users/{final_name}"
    
# ######### for degrees imgs ######### #
def degree_image_path(instance, filename):
    ext, output = get_filename_ext_rand(filename)
    final_name = f"{output}{ext}"
    return f"degrees/{final_name}"

# ######### for portfolio imgs ######### #
def portfolio_image_path(instance, filename):
    ext, output = get_filename_ext_rand(filename)
    final_name = f"{output}{ext}"
    return f"portfolio/{final_name}"