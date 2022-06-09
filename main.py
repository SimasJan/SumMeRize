from distutils.log import warn
from logging import warning
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import spacy
from spacy.matcher import Matcher
import json
import os
import re
import argparse
import warnings

warnings.filterwarnings("ignore")

# define header
header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/533+ (KHTML, like Gecko)'}

def parse_args():
    parser = argparse.ArgumentParser('Find enTITIES')
    parser.add_argument('-s', '--source', help='Original source')
    parser.add_argument('-e', '--entities', nargs='+', help='Entity type to look for')
    return parser.parse_args()

def make_request(url):
    r = requests.get(url, headers=header)
    r.raise_for_status()
    return r

def make_soup(response):
    return BeautifulSoup(response.content, features='html.parser')

def parse_html(soup, target):
    results = soup.find_all(re.compile(target))

    # create a single string from the article, and create found source metadata
    article_str = ""
    urls_found_metadata = []

    for i,p in enumerate(results):
        if p.a:
            d = {'line': i, 'text': p.text.strip(), 'url': p.a.get('href')}
            # TODO: include metadata (original article url, date accessed, etc.)
            urls_found_metadata.append(d)
        article_str += p.text.strip()
    return {'string': article_str, 'sources_meta': urls_found_metadata}

def find_entities(document, entities:list, unique=True):
    results = {}
    for ent in document.ents:
        if ent.label_ in entities:
            if ent.label_ not in results:
                results[ent.label_] = [ent.text]
            else:
                results[ent.label_].append(ent.text)
    # check arg condition
    if unique == True:
        for k in results:
            results[k] = list(set(results[k]))
    return results

def find_entities(document, entity, unique=True):
    res = [ent.text.strip() for ent in document.ents if ent.label_ == entity]
    if unique: return list(set(res))
    else: return res

def print_template(entity:str, values:list):
    t = f"""
    ---------- RESULTS ----------
    Entity: "{entity}"
    Found:  {len(values)}
    Results: {', '.join(values)}
    """
    print(t)

if __name__ == "__main__":

    args = parse_args()
    # print(args)
    source = args.source
    entities = args.entities
    print(entities)

    # make first request
    response = make_request(source)
    soup = make_soup(response)

    # find all tags whose name starts (^) and ends ($) with letter "p".
    target = "^p$"
    parsed_data = parse_html(soup, target)
    text_str = parsed_data.get('string')
    
    # make spacy nlp doc
    nlp = spacy.load("en_core_web_sm") # nlp language model
    doc = nlp(text_str)
    
    # find entities
    results = []
    for ent in entities:
        res = find_entities(doc, ent)
        print_template(ent, res)