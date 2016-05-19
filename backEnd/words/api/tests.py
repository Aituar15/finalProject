from rest_framework.test import APIRequestFactory
from ..models import Word
from django.test import TestCase


class WordTestCase(TestCase):
    def setUp(self):
        Word.objects.create(title="tea", definition="drink", language="en")

    def testWord(self):
        tea = Word.objects.get(title="tea")
        self.assertTrue(tea.title == "tea")
        self.assertTrue(tea.definition == "drink")
        self.assertTrue(tea.language == "en")
