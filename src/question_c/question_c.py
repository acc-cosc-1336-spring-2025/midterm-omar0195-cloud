#write functions here, don't add input('') statements here!
global_num = 25

def use_global():
    globals()['global_num'] = 10

def get_global_num():
    return globals()['global_num']
