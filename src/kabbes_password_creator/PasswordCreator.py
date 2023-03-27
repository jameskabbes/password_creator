import kabbes_menu
import py_starter as ps
import random


class PasswordCreator( kabbes_menu.Client ):

    _OVERRIDE_OPTIONS = {
        "1": ["Word Passwords", "gen_word_user"],
        "2": ["Fully Random Passwords", "gen_random_user"]
    }

    def __init__( self ):
        kabbes_menu.Client.__init__( self )

    def choose_password( self, passwords ):

        password = ps.get_selection_from_list( passwords, prompt = 'Choose a password', allow_null=True )
        if password != None:
            ps.copy(password)
        return password

    def gen_word_user( self ):
        passwords = self.gen_word_passwords()
        return self.choose_password( passwords )

    def gen_random_user( self ):
        passwords = self.gen_random_passwords()
        return self.choose_password( passwords )

    def gen_word_password( self, **override_kwargs ):

        kwargs = {
            "n_words":2,
            "n_digits":1,
            "n_symbols":1,
            "camelcase":True
        }
        kwargs = ps.merge_dicts( self.cfg_password['gen'].get_dict().copy(), kwargs, override_kwargs )

        words = self.cfg_password['words.Path'].read().split('\n')
        words_to_use = []
        for i in range(kwargs['n_words']):
            words_to_use.append( random.choice(words) )

        password = ''

        for i in words_to_use:
            if kwargs['camelcase']:
                i = i.capitalize()
            password += i

        for i in range(kwargs['n_digits']):
            password += str(random.choice(kwargs['digits']))

        for i in range(kwargs['n_specials']):
            password += str(random.choice(kwargs['specials']))

        return password

    def gen_random_password( self, **override_kwargs ):

        default_kwargs = {}
        kwargs = ps.merge_dicts( self.cfg_password['gen'].get_dict().copy(), default_kwargs, override_kwargs )

        password = ''

        counts = {}
        for option in kwargs['options']:
            counts[option] = {}
            counts[option]['n'] = 0
            counts[option]['available'] = True
            counts[option]['min'] = kwargs[ 'min_' + option ]
            counts[option]['max'] = kwargs[ 'max_' + option ]
                        

        while len(password) < kwargs['length']:

            chars_left = kwargs['length'] - len(password)

            remaining_mins = 0
            for option in counts:
                if counts[option]['n'] == counts[option]['max']:
                    counts[option]['available'] = False

                #see if there is any extra room for random picks
                #max(min()) functionality takes nums and min_num and returns nums unless it is greater than the min_num, then min_num is returned
                remaining_mins += counts[option]['min']
                remaining_mins -= max(min( counts[option]['n'], counts[option]['min']) ,0)

            if remaining_mins == chars_left:
                #emergency mode

                for option in counts:
                    if counts[option]['n'] >= counts[option]['min']:
                        counts[option]['available'] = False

            available = []
            for option in counts:
                if counts[option]['available'] == True:
                    available.append(option)

            option = random.choice( available )
            password += random.choice( kwargs[option] )
            counts[option]['n'] += 1

        return password

    def gen_word_passwords( self, n=20, **kwargs ):

        return [ self.gen_word_password( **kwargs ) for i in range(n) ]

    def gen_random_passwords( self, n=20, **kwargs ):

        return [ self.gen_random_password( **kwargs ) for i in range(n) ]



