import os

from google.cloud import translate_v3

"""
Class for using google translate.
The function is taken from Google own instructions found at:
https://cloud.google.com/translate/docs/basic/translating-text

"""

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"googleKey.json"

#USES GOOGLES NMT (NEUROAL MACHINE TRANSLATION)
# # translate_text(target, german)
def translate_text_with_model(target, text, model="nmt"):
    # print("TARNSALTE WITH MODEL:")
    # print()
    """Translates text into the target language.

    Make sure your project is allowlisted.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target, model=model)

    #added myself a return of the translated text as a string, instead of a dic
    return result["translatedText"]

