import kabbes_password_creator 
import py_starter as ps

def run_main():

    ans = input('Fully Random or Word Password (r/w): ')
    if ans == 'w':
        passwords = kabbes_password_creator.generator_support.word_passwords(20, 2, 1, 1, True)
    else:
        passwords = kabbes_password_creator.generator_support.rand_password()

    password = ps.get_selection_from_list( passwords, prompt = 'Choose a password' )
    ps.copy(password)

    return password

if __name__ == '__main__':
    password = run_main()
