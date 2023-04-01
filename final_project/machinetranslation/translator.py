"""
IBM Watson Language Translator API testing by Jordon Campbell.
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION = '2023-02-01'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def translation_fr_response(response_json):
    """
    Translate dict response output of Watson Language Translator API
    """
    response_dict = json.loads(response_json)
    translation = response_dict['translations'][0]['translation']
    return translation

def englishToFrench(english_text):
    """
    Translate input text from English to French
    """
    if english_text is None:
        return None
    translation = language_translator.translate(
        text = english_text,
        model_id = 'en-fr'
    ).get_result()
    french_text = translation_fr_response(json.dumps(translation))
    return french_text

def french_ToEnglish(french_text):
    """
    Translate input text from French to English
    """
    if french_text is None:
        return None
    translation = language_translator.translate(
        text = french_text,
        model_id = 'fr-en'
    ).get_result()
    english_text = translation_fr_response(json.dumps(translation))
    return english_text
