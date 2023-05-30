import random

import numpy
from PIL import Image
from matplotlib import font_manager
from wordcloud import WordCloud


__WORDS = {'abstraction': 1,
           'Alonzo Church': 2,
           'application': 1,
           'binding': 1,
           'calculus': 3,
           'category': 1,
           'complexity': 1,
           'computability': 1,
           'computation': 1,
           'curry': 2,
           'definition': 1,
           'expression': 1,
           'form': 1,
           'formal': 1,
           'foundations': 1,
           'function': 5,
           'Haskell': 3,
           'Haskell Curry': 2,
           'lambda': 5,
           'lambda calculus': 5,
           'logic': 2,
           'mathematics': 4,
           '(MN)': 3,
           'model': 1,
           'parameter': 1,
           'programming': 1,
           'proof': 1,
           'reduction': 1,
           'Rosser': 1,
           'semantics': 1,
           'substitution': 1,
           'system': 1,
           'term': 1,
           'theorem': 1,
           'typed': 4,
           'universal': 2,
           'untyped': 4,
           'value': 3,
           'variable': 3,
           'x': 4,
           'α-conversion': 3,
           'β-normal': 2,
           'β-reduction': 3,
           'λ': 5,
           'λ-calculus': 5,
           '(λx.M)': 3,
           '((λx.M)E)→(M[x:=E])': 2,
           '(λx.M[x])→(λy.M[y])': 2}


def color(*args, **kwargs):
    colors = [(56, 174, 204), (40, 113, 137), (24, 52, 70)]
    return random.choice(colors)


def font():
    fonts = font_manager.findSystemFonts()
    hoped = [font for font in fonts if 'Carlito' in font and 'Regular' in font]
    sans = [font for font in fonts if 'Sans' in font and 'Regular' in font]
    if len(hoped) > 0:
        font = hoped[0]
    elif len(sans) > 0:
        font = random.choice(sans)
    else:
        font = random.choice(fonts)

    return font


def generate():
    with Image.open('lambda.png') as img:
        mask = numpy.array(img)
    cloud = WordCloud(font_path=font(),
                      mask=mask,
                      max_font_size=100,
                      repeat=True,
                      max_words=1000,
                      background_color='white',
                      color_func=color)
    cloud.generate_from_frequencies(__WORDS)
    img = cloud.to_image()
    img = img.resize((500, 500))
    img.save('avatar.png')


if __name__ == '__main__':
    generate()
