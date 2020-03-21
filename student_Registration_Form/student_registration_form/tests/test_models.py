from django.test import TestCase

from student_registration_form.models import pdf_file,TeachersInfo


class ModelTest(TestCase):

    def test_pdf_file_Upload(self):
        entry = pdf_file(name="course outline")
        self.assertEqual(str(entry), entry.name)

    def test_TeachersInfo(self):
        entry = TeachersInfo(Username="Akhtar")
        self.assertEqual(str(entry), entry.Username)