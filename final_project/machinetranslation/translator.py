"""Module providingFunction for EN-FR and FR-EN translation"""

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
#language_translator.set_disable_ssl_verification(True)


def englishToFrench(english_text):
    """EN-FR Translation method"""
    language_translator.set_service_url(url)
    french_text=language_translator.translate(
    text= english_text,
    model_id='en-fr').get_result()
    return french_text


def frenchToEnglish(french_text):
    """FR-EN Translation method"""
    language_translator.set_service_url(url)
    english_text=language_translator.translate(
    text= french_text,
    model_id='fr-en').get_result()
    return english_text
