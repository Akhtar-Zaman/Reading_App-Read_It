from django.test import TestCase, Client
from django.urls import reverse
from student_registration_form.models import pdf_file, TeachersInfo



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.student_form_url = reverse('student_form')
        self.TeacherForm_url = reverse('TeacherForm')
        self.student_login_url = reverse('login')
        self.pdf_view_url = reverse('mainpage')
        self.pdf_up_url = reverse('pdf_upload_page')
        self.teacher_login_url = reverse('teacher_login')
        self.image_capture_url = reverse('image')

    def test_studentform(self):

        response = self.client.get(self.student_form_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'studentform.html')

    def test_TeacherForm(self):

        response = self.client.get(self.TeacherForm_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_signing_form.html')

    def test_studentLogin(self):

        response = self.client.get(self.student_login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_PdfView(self):

        response = self.client.get(self.pdf_view_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainpage.html')

    def test_PdfUp(self):

        response = self.client.get(self.pdf_up_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'fileupload.html')

    def test_TeacherLogin(self):

        response = self.client.get(self.teacher_login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

