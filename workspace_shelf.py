import shelve

def save_workspace(filename,global_objects):
    my_shelf = shelve.open(filename, 'n')  # 'n' for new
    # remove system objects and libraries from list to store and delete before loading
    obj_list = list(global_objects.keys())

    obj_list = [x for x in obj_list if not '__' in x]
    obj_list = [x for x in obj_list if not 'shelve' in x]
    obj_list = [x for x in obj_list if not 'my_shelf' in x]
    obj_list = [x for x in obj_list if not 'global_objects' in x]

    obj_list = [x for x in obj_list if not 'sys' in x]
    obj_list = [x for x in obj_list if not 'pd' in x]
    obj_list = [x for x in obj_list if not 'np' in x]
    obj_list = [x for x in obj_list if not 'ws' in x]
    obj_list = [x for x in obj_list if not 'save_workspace' in x]
    obj_list = [x for x in obj_list if not 'load_workspace' in x]

    # store objects
    for key in obj_list:
        try:
            my_shelf[key] = global_objects[key]
        except TypeError:
            # __builtins__, my_shelf, and imported modules can not be shelved.
            print('ERROR shelving: {0}'.format(key))
    my_shelf.close()

    return obj_list

def load_workspace(filename):
    global_objects={} # create empty dictionary

    my_shelf = shelve.open(filename) # load objects from shelf
    for key in my_shelf:
        global_objects[key] = my_shelf[key]  # enter objects into dictionary

    my_shelf.close()
    return global_objects
