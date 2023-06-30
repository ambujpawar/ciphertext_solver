"""
Solve a ciphertext using the Caesar cipher.
"""

import string
from typing import Iterable

# Third-party imports
import enchant


class CaesarCipher:
    """
    Class to solve a ciphertext using the Caesar cipher.
    """

    def __init__(self, ciphertext: str, language: str = "en_US"):
        """
        Initialise the class with the ciphertext to be solved.
        """
        self.ciphertext = ciphertext
        self.language = language
        self.spell = enchant.Dict(self.language)

    def solve(self) -> Iterable:
        """
        Solve the ciphertext.
        """
        all_solutions = self._brute_force()
        shift, score, plaintext = self._find_solution(all_solutions)
        mapping = self._generate_mapping(shift)
        return plaintext, mapping, score

    def _brute_force(self):
        """
        Brute force the solution.
        """
        alphabets = string.ascii_lowercase
        all_solutions = []
        for shift in range(1, 26):
            mapping = {k: alphabets[(i - shift) % 26] for i, k in enumerate(alphabets)}
            solution = "".join([mapping.get(c, c) for c in self.ciphertext])
            all_solutions.append((shift, solution))

        return all_solutions

    def _find_solution(self, all_solutions: list) -> Iterable:
        """
        Find the solution.
        """
        best_score = 0
        best_sentence = None
        best_shift = None
        for shift, sentence in all_solutions:
            score = sum(1 for word in sentence.split() if self.spell.check(word))
            if score > best_score:
                best_score = score
                best_sentence = sentence
                best_shift = shift
        return best_shift, best_score, best_sentence

    def _generate_mapping(self, shift: int):
        """
        Generate the mapping.
        """
        if not shift:
            return None
        alphabets = string.ascii_lowercase
        mapping = {k: alphabets[(i - shift) % 26] for i, k in enumerate(alphabets)}
        return mapping
