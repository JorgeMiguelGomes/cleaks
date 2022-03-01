# -*- coding: utf-8 -*-

# import libraries 

import os
from PIL import Image

import nltk
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.ndimage import gaussian_gradient_magnitude
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS

# import mask image. Search for stencil image for better results

mask = np.array(Image.open("darthvader01.png"))

# define function for grayscale coloring

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

# Load and text and decode 
text = open(('conti_just_body.txt'), "rb").read().decode('UTF-8', errors='replace')

# Load stopwords for EN language from nlkt 
stopwords = nltk.corpus.stopwords.words('english')

# Create Worldcloud

wc = WordCloud(max_words=100000, width=1596, height=584, stopwords=stopwords, mask=mask).generate(text)

# Recolor our Wordcloud

plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
           interpolation="bilinear")

# Save worldcloud file

wc.to_file("CONTI_Darth.png")

