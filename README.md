# password_creator
Easily generate random passwords

[Documentation](https://jameskabbes.github.io/password_creator)<br>
[PyPI](https://pypi.org/project/kabbes-password-creator)

<br> 

# Installation
`pip install kabbes_password_creator`

<br>

# Usage
For more in-depth documentation, read the information provided on the Pages. Or better yet, read the source code.

## Main

```
python -m kabbes_password_creator
```

## Supplemental

```python
import kabbes_password_creator as kpc
```

### Fully Random Password
```python 
kpc.generator_support.rand_password()
```
```
>>> Choose the number of characters in the password:  (1-1000): 10
>>> Press any key to choose specific options:
>>> ['B!!897$*69', 'VokFRrP33H', '7j&ApDJ#@2', 'nWio0Qy2aj', 'f#RWtdcV^a', 'NW6a8UwF7!', 'P(9S%7pH)G', '7*BW(gTv70', '63%B0DBpDH', 'OuBd5wF00b', 'J^38I&7)f6', '!b#Kp!V(c^', ')XN!lD(PO*', 'I9a8URbL81', 'cq2F1O5Gk9', '!gYBw*(jq5', '6Cj4p5rRV7', 'Hw^dXc37Xk', 'So&)**E6xQ', '1Tvj5on^iH']
```

### Word Passwords
Before using this, you must have a text file called words.txt saved

```python 
kpc.generator_support.word_password()
```
```
>>> 'PlattersCoach3)'

<br>


# Author
James Kabbes

