# Tests CaesarCipher class

import pytest
from ciphertext_solver.caesar_cipher import CaesarCipher

LANGUAGES_SUPPORTED = ["en_US", "fr_FR", "de_DE", "es_ES", "it_IT", "nl_NL"]


@pytest.mark.parametrize(
    "ciphertext, language, expected",
    [
        ("uryyb jbeyq!", "en_US", "hello world!"),
        ("unyyb jreryq!", "nl_NL", "hallo wereld!"),
    ],
)
def test_caesar_cipher(ciphertext, language, expected):
    caesar_cipher = CaesarCipher(ciphertext, language)
    plaintext, mapping, score = caesar_cipher.solve()
    assert plaintext == expected
    assert mapping is not None
    assert score > 0
