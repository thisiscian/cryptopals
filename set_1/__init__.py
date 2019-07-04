from importlib import import_module

set_name = 'set_1'

def main():
    g = globals()
    for i in range(1, 8):
        challenge = 'challenge_{}'.format(i)
        try:
            m = import_module(challenge)
            try:
                m.main()
                print('{}.{}: passed'.format(set_name, challenge))
            except:
                print('{}.{}: failed'.format(set_name, challenge))
                
        except ModuleNotFoundError:
            print('{}.{}: not attempted'.format(set_name, challenge))

if __name__ == '__main__':
    main()
