import py_starter as ps
import kabbes_password_creator
import random

numbers = ['0','1','2','3','4','5','6','7','8','9']
lowercases = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
specials = ['!','@','#','$','%','^','&','*','(',')']
uppercases = []
for i in lowercases:
    uppercases.append(i.upper())


def count(string, index):

    if index == 0:
        #numbers
        list = numbers
    if index == 1:
        #lower
        list = lowercases
    if index == 2:
        #spec
        list = specials
    if index == 3:
        #high
        list = uppercases

    count = 0
    for i in string:
        if i in list:
            count += 1
    return count

def gen_passwords(min_num, max_num, min_low, max_low, min_spec, max_spec, min_up, max_up, number_to_make, char_num):

    passwords = []
    for x in range(number_to_make):
        new = ''

        nums = 0
        lows = 0
        specs = 0
        ups = 0
        remaining_mins = min_num + min_low + min_spec + min_up
        available = [0,1,2,3]

        while len(new) < char_num:
            #print (new)
            #print (available)
            chars_left = char_num - len(new)

            if nums == max_num:
                if 0 in available:
                    del available[available.index(0)]
            if lows == max_low:
                if 1 in available:
                    del available[available.index(1)]
            if specs == max_spec:
                if 2 in available:
                    del available[available.index(2)]
            if ups == max_up:
                if 3 in available:
                    del available[available.index(3)]

            remaining_mins = min_num + min_low + min_spec + min_up - max(min(nums, min_num) ,0) - max(min(lows, min_low) ,0) - max(min(specs, min_spec) ,0) - max(min(ups, min_up) ,0)
            #see if there is any extra room for random picks
            #max(min()) functionality takes nums and min_num and returns nums unless it is greater than the min_num, then min_num is returned

            #print (remaining_mins)
            if remaining_mins == chars_left:
                #emergency mode

                if nums >= min_num:
                    if 0 in available:
                        del available[available.index(0)]
                if lows >= min_low:
                    if 1 in available:
                        del available[available.index(1)]
                if specs >= min_spec:
                    if 2 in available:
                        del available[available.index(2)]
                if ups >= min_up:
                    if 3 in available:
                        del available[available.index(3)]


            number = random.choice(available)

            if number == 0:
                new += random.choice(numbers)
                nums += 1
            elif number == 1:
                new += random.choice(lowercases)
                lows += 1
            elif number == 2:
                new += random.choice(specials)
                specs += 1
            elif number == 3:
                new += random.choice(uppercases)
                ups += 1

        a = count(new, 0)
        assert a >= min_num
        assert a <= max_num
        b = count(new, 1)
        assert b >= min_low
        assert b <= max_low
        c = count(new, 2)
        assert c >= min_spec
        assert c <= max_spec
        d = count(new, 3)
        assert d >= min_up
        assert d <= max_up


        passwords.append(new)
    return passwords

def rand_password():

    max_length = 1000

    char_num = ps.get_int_input(1, max_length, prompt = 'Choose the number of characters in the password: ')
    options = (input('Press any key to choose specific options: ' ) != '')

    min_num = 0
    max_num = max_length
    min_low = 0
    max_low = max_length
    min_spec = 0
    max_spec = max_length
    min_up = 0
    max_up = max_length

    if options:
        running_total = 0
        min_num = ps.get_int_input(0, char_num - running_total, prompt = 'Choose the minimum number of numbers to be found in the password: ')
        running_total += min_num
        max_num = ps.get_int_input(min_num, min_num + char_num - running_total, prompt = 'Choose the maximum number of numbers to be found in the password: ')

        min_low = ps.get_int_input(0, char_num - running_total, prompt = 'Choose the minimum number of lowercase letters to be found in the password: ')
        running_total += min_low
        max_low = ps.get_int_input(min_low, min_low + char_num - running_total, prompt = 'Choose the maximum number of lowercase letters to be found in the password: ')

        min_spec = ps.get_int_input(0, char_num - running_total, prompt = 'Choose the minimum number of special characters to be found in the password: ')
        running_total += min_spec
        max_spec = ps.get_int_input(min_spec, min_spec + char_num- running_total, prompt = 'Choose the maximum number of special characters to be found in the password: ')

        min_up = ps.get_int_input(0, char_num - running_total, prompt = 'Choose the minimum number of uppercase characters to be found in the password: ')
        running_total += min_up
        max_up = ps.get_int_input( max( (char_num - running_total), min_up  )        , min_up + char_num - running_total, prompt = 'Choose the maximum number of uppercase characters to be found in the password: ')

    to_generate = 20
    passwords = gen_passwords(min_num, max_num, min_low, max_low, min_spec, max_spec, min_up, max_up, to_generate, char_num)
    return passwords


def word_passwords(number, num_words, num_digits, num_symbols, camelcase):

    passwords = []
    for i in range(number):
        passwords.append( word_password(num_words = num_words, num_digits = num_digits, num_symbols = num_symbols, camelcase = camelcase) )

    return passwords

def word_password(num_words = 2, num_digits = 1, num_symbols = 1, camelcase = True):

    import random

    words = kabbes_password_creator.settings.words.Path.read().split('\n')
    words_to_use = []
    for i in range(num_words):
        words_to_use.append( random.choice(words) )

    password = ''

    for i in words_to_use:
        if camelcase:
            i = i.capitalize()
        password += i

    for i in range(num_digits):
        password += str(random.choice(numbers))

    for i in range(num_symbols):
        password += str(random.choice(specials))

    return password


def make_password():

    #passwords = gen_passwords(1, 10, 1, 10, 1, 10, 1, 10, 1, 8)
    #return passwords[0]

    return word_password()
