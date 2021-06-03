#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 11:01:44 2021

@author: e.mcgill

"""

def clinical():
    '''
    Method from: Mulyar et al. (2019) Experiments with Pre-Trained Deep Neural Language Models
    for Clinical NLP: ConceptNormalization and Semantic Similarity
    Source: https://github.com/AndriyMulyar/semantic-text-similarity
    Based on BERT
    '''
    from semantic_text_similarity.models import WebBertSimilarity

    web_model = WebBertSimilarity(device='cpu', batch_size=10) #defaults to GPU prediction

    # print(web_model.predict([("She won an olympic gold medal","The women is an olympic champion")]))
    # print(web_model.predict([("She won an olympic gold medal. Then, the quick brown fox jumped over the lazy dog.","She won an olympic gold medal. Then, the quick brown fox jumped over the lazy dog.")]))

    line_no = 0
    with open('wikipedia/parallel/aligned-labelled/aligned-simp.txt','r') as sim, open('wikipedia/parallel/aligned-labelled/aligned-english.txt','r') as en:
        for line in zip(sim,en):
            line_no += 1
            # fancy print
            # print("line no.:",line_no,web_model.predict([line]))
            # normal print
            print(web_model.predict([line]))

def other():
    pass

clinical()