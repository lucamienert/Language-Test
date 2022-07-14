import run as run

def main(filename):
    if filename.endswith('.rbl'):
        with open(filename, 'r') as file:
            data = file.read()
    else:
        print('File must end with ".rbl"')
        exit()

    result, error = run.run('<stdin>', data)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
