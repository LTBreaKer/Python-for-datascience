def all_thing_is_obj(object: any) -> int:

    object_type = type(object)

    type_labels = {
        tuple: 'tuple',
        list: 'list',
        set: 'set',
        dict: 'dict',
        str: 'is in the kitchen'
    }

    label = type_labels.get(object_type, "Type not found")

    if label == "Type not found":
        print(label)
    elif label == 'is in the kitchen':
        print(f"{object} {label} : {object_type}")
    else:
        print(f"{label} : {object_type}")
    return 42
