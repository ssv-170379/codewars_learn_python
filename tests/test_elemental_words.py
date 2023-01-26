import codewars_test as test  # https://github.com/codewars/python-test-framework

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # add parent directory to system path (to import test objects from ../solution/)

from solution.kyu_4.elemental_words import elemental_forms

test_cases = [
    ('', [
        []
    ]),
    ('Yes', [
        ['Yttrium (Y)', 'Einsteinium (Es)']
    ]),
    ('beach', [
        ['Beryllium (Be)', 'Actinium (Ac)', 'Hydrogen (H)']
    ]),
    ('snack', [
        ['Sulfur (S)', 'Nitrogen (N)', 'Actinium (Ac)', 'Potassium (K)'],
        ['Sulfur (S)', 'Sodium (Na)', 'Carbon (C)', 'Potassium (K)'],
        ['Tin (Sn)', 'Actinium (Ac)', 'Potassium (K)'],
    ]),
]


@test.describe('Sample tests')
def sample_tests():
    @test.it('Testing elemental_forms')
    def tests():
        for word, expected in test_cases:
            actual = elemental_forms(word)
            try:
                actual = sorted(actual)
            except TypeError:
                pass
            test.assert_equals(actual, expected, f'{word=}')
