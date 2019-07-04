from importlib import import_module
import glob

def get_challenges(set_name, module):
    for i in range(1, 8):
        challenge = '{}.challenge_{}'.format(set_name, i)
        try:
            m = import_module(challenge, module)
            yield challenge, m
        except ModuleNotFoundError:
            yield challenge, None

def get_sets():
    for i in range(1, 8):
        set_name = 'set_{}'.format(i)
        try:
            m = import_module(set_name)
            yield set_name, m
        except ModuleNotFoundError:
            yield set_name, None

def main():
    for set_name, set_module in get_sets():
        if set_module is None:
            print(set_name, u'\x1b[30;43;1m????????\x1b[0m')
        else:
            status = ''
            for challenge_name, challenge_module in get_challenges(set_name,
                                                                   set_module):
                if challenge_module is None:
                    status += u'\x1b[30;43;1m?\x1b[0m'
                    
                else:
                    try:
                        challenge_module.main()
                        status += u'\x1b[30;42;1m\u2713\x1b[0m'
                    except:
                        status += u'\x1b[30;41;1m\u2717\x1b[0m'
                        pass
            print(set_name, status)

if __name__ == '__main__':
    main()
