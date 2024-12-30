def NULL_not_found(object: any) -> int:
    type_labels = {
        float: 'cheese',
        int: 'Zero',
        str: 'Empty',
        bool: 'Fake',
    }

    if not object or object != object:
        object_type = type(object)
        label = type_labels.get(object_type, 'Nothing')
        print(f"{label}: {object} {object_type}")
        return 0
    print("Type not found")
    return 1
