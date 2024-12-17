def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if isinstance(result, list):
            print(func.__name__)
            for item in result:
                print(item)

        elif isinstance(result, dict):
            print(func.__name__)
            for key, value in result.items():
                print(f'{key} = {value}')

        else:
            print(func.__name__)
            print(result)

        return result
    return wrapper

@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]


test_1()
test_2()
test_3()
test_4()