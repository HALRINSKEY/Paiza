vowel = ["a","i","u","e","o","A","I","U","E","O"]

def name_make(name):
    handle_name = str()

    for n in name:
        if n not in vowel:
            handle_name += n

    print(handle_name)

name_make(input())