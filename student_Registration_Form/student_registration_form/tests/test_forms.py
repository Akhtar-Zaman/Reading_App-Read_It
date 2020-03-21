from django.test import SimpleTestCase
from student_registration_form.forms import StudentRegistrationForm, Teachers_Signing_Form, uploadpdf


class TestForms(SimpleTestCase):

    def test_Teachers_Signing_Form_valid(self):
            form = Teachers_Signing_Form(data={
                    'Username': 'akhtar',
                    'First_Name': 'Akhtar',
                    'Last_Name': 'Zaman',
                    'Email': 'akhtar@gmail.com',
                    'Password': 'akhtar1611319042',
                    'Confirm_Password': 'akhtar1611319042'
            })

            self.assertTrue(form.is_valid())


    def test_Teachers_Signing_Form_notvalid(self):

        form = Teachers_Signing_Form(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)


    def test_pdffile_upload_valid(self):
            form = uploadpdf(data={
                    'name': 'course outline',
                    'pdffile': 'Spring2019-CSE327-Course_Outline.pdf'
            })


    def test_pdffile_upload_notvalid(self):

        form = uploadpdf(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)