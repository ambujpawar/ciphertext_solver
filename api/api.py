"""
API for the Ciphertext solver application.
"""
import string

# Third-party imports
from fastapi import FastAPI

# Local imports
from response_models import CipherResponse, CipherText

from ciphertext_solver.caesar_cipher import CaesarCipher

app = FastAPI()
LANGUAGES_SUPPORTED = ["en_US", "fr_FR", "de_DE", "es_ES", "it_IT", "nl_NL"]


@app.get("/api/")
def root():
    return {"message": "Hello World"}


@app.post("/api/solve/echo")
def echo(cipher: CipherText):
    """
    Echo the input ciphertext back to the user.
    """
    alphabets = string.ascii_lowercase
    mapping = {k: v for k, v in zip(alphabets, alphabets)}
    return CipherResponse(
        ciphertext=cipher.ciphertext, plaintext=cipher.ciphertext, mapping=mapping
    )


@app.post("/api/solve")
def solve(cipher: CipherText):
    """
    Solve the ciphertext using the any language.
    """
    best_score = 0
    best_plaintext = None
    best_mapping = None

    for language in LANGUAGES_SUPPORTED:
        caesar_cipher = CaesarCipher(cipher.ciphertext, language)
        plaintext, mapping, score = caesar_cipher.solve()
        if score > best_score:
            best_score = score
            best_plaintext = plaintext
            best_mapping = mapping

    return CipherResponse(
        ciphertext=cipher.ciphertext, plaintext=best_plaintext, mapping=best_mapping
    )


@app.post("/api/solve/en")
def solve_english(cipher: CipherText):
    """
    Solve the ciphertext using the English language.
    """
    caesar_cipher = CaesarCipher(cipher.ciphertext)
    plaintext, mapping, score = caesar_cipher.solve()
    return CipherResponse(
        ciphertext=cipher.ciphertext, plaintext=plaintext, mapping=mapping
    )
