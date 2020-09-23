#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:41:50 2020

@author: stevesytsai
"""

import wikipedia as wiki
import matplotlib.pyplot as plt # To display our wordcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image # To load our image
import numpy as np # To get the color of our image 

# Content-related
text = open('ObamaSpeech1.txt').read()
stopwords = set(STOPWORDS)

# Appearance-related
custom_mask = np.array(Image.open('batman.png')) # To get the color of pics
wc = WordCloud(background_color = (255, 255, 255), mask = custom_mask,
               stopwords = stopwords) 
wc.generate(text)

# To change the color 
#image_colors = ImageColorGenerator(custom_mask)
#wc.recolor(color_func = image_colors) 

# Plotting
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.show()

#print(len(STOPWORDS)) # how many stopwords 
#print(custom_mask[0]) # To get the RGB of pics and change it 
#wc.to_file('Batman_Obama_wordcloud.png') # To save the file as png