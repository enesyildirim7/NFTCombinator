"""
Author: Enes Yıldırım
Github: https://github.com/enesyildirim7
"""

import os
import glob
import random
from tqdm import tqdm
from PIL import Image

BACKGROUND = "./background/"
CHARACTER = "./character/"
CLOTHES = "./clothes/"
EYES = "./eyes/"
HEAD = "./head/"
MOUTH = "./mouth/"
NOSE = "./nose/"

SAVE_NFT = "./NFTArt/"

BACKGROUND_IMAGES = glob.glob(BACKGROUND + "*")
CHARACTER_IMAGES = glob.glob(CHARACTER + "*")
EYE_IMAGES = glob.glob(EYES + "*")
HEAD_ITEM = glob.glob(HEAD + "*")
MOUTH_IMAGES = glob.glob(MOUTH + "*")
NOSE_IMAGES = glob.glob(NOSE + "*")
CLOTHES_ITEM = glob.glob(CLOTHES + "*")

collection_name = str(input("Collection name : "))

def basic_combine(background,character,eyes,noses,mouths):
    number = len(background) * len(character) * len(eyes) * len(noses) * len(mouths)
    print(number)
    collectionNumber = random.sample(range(1, number + 1), number)
    i = 0
    for back in tqdm(background):
        for char in character:
            for eye in eyes:
                for nose in noses:
                    for mouth in mouths:
                        b = Image.open(back).convert("RGBA")
                        c = Image.open(char).convert("RGBA")
                        e = Image.open(eye).convert("RGBA")
                        n = Image.open(nose).convert("RGBA")
                        m = Image.open(mouth).convert("RGBA")
                        bc = Image.alpha_composite(b,c)
                        bce = Image.alpha_composite(bc, e)
                        bcen = Image.alpha_composite(bce,n)
                        ART = Image.alpha_composite(bcen,m)
                        ART.save(f"{SAVE_NFT}{collection_name} #{collectionNumber[i]}.png")
                        i += 1

basic_combine(BACKGROUND_IMAGES, CHARACTER_IMAGES, EYE_IMAGES, NOSE_IMAGES, MOUTH_IMAGES)