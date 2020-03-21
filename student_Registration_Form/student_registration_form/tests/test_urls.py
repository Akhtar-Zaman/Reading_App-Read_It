from django.test import SimpleTestCase
from django.urls import reverse, resolve
from student_registration_form.views import success, studentform, teacher_form, student_login, pdf_view, pdf_up, teacher_login_form, image_capture


class TestUrls(SimpleTestCase):

    def test_homepage_url(self):
        url = reverse('homepage')
        self.assertEquals(resolve(url).func, success)

    def test_student_form_url(self):
        url = reverse('student_form')
        self.assertEquals(resolve(url).func, studentform)

    def test_TeacherForm_url(self):
        url = reverse('TeacherForm')
        self.assertEquals(resolve(url).func, teacher_form)

    def test_student_login_url(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, student_login)

    def test_pdf_view_url(self):
        url = reverse('mainpage')
        self.assertEquals(resolve(url).func, pdf_view)

    def test_pdf_up_url(self):
        url = reverse('pdf_upload_page')
        self.assertEquals(resolve(url).func, pdf_up)

    def test_teacher_login_form_url(self):
        url = reverse('teacher_login')
        self.assertEquals(resolve(url).func, teacher_login_form)

    def test_image_capture_url(self):
        url = reverse('image')
        self.assertEquals(resolve(url).func, image_capture)