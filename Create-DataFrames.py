import pandas as pd
import numpy as np
import random
import string


# Empty DataFrame
df = pd.DataFrame()

# DataFrame with random numbers
df_random_numbers = pd.DataFrame(np.random.randn(10, 5), columns=list('RUSHY'))

# DataFrame with Random Integers
df_random_integers = pd.DataFrame(np.random.randint(0,10,size=(25,5)),columns=list('RUSHY'))
df_random_integers

df_random_letters = pd.DataFrame()
for x in list('RUSHY'):
    column_name = x
    for i in range(0,10):
        loop_letters = random.choice(string.ascii_letters)

df_random_letters
