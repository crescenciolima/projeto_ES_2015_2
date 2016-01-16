"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.test import TestCase
from SPLArch.scoping.models import  *

from django.core.urlresolvers import resolve

class LoginTestCase(TestCase):

    def test_response(self):
        response = self.client.get('/admin/login/')
        self.assertEqual(response.status_code,  200)
        print response.status_code


class ProductTestCase(TestCase):

    def setUp(self):
        self.product1 = Product.objects.create(
            name='product1',
            description='description1',
        )
        self.product1.save()

        self.model = self.product1

    def test_response(self):
        url = reverse("admin:%s_%s_add" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_change" % (self.model._meta.app_label, self.model._meta.module_name), args=[self.model.id])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_delete" % (self.model._meta.app_label, self.model._meta.module_name), args=[self.model.id])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_history" % (self.model._meta.app_label, self.model._meta.module_name), args=[self.model.id])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_changelist" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)


class ProjectTestCase(TestCase):

    def setUp(self):
        self.project1 = Project.objects.create()
        self.project1.save()
        self.model = self.project1

    def test_response(self):
        url = reverse("admin:%s_%s_add" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_change" % (self.model._meta.app_label, self.model._meta.module_name), args=[self.model.id])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_delete" % (self.model._meta.app_label, self.model._meta.module_name), args=[self.model.id])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_history" % (self.model._meta.app_label, self.model._meta.module_name), args=[self.model.id])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_changelist" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

class GlossaryTestCase(TestCase):

     def setUp(self):
        self.glossary1 = Project.objects.create()
        self.glossary1.save()
        self.model = self.glossary1

     def test_response(self):
        url = reverse("admin:%s_%s_add" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_change" % (self.model._meta.app_label, self.model._meta.module_name), args=[self.model.id])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_delete" % (self.model._meta.app_label, self.model._meta.module_name), args=[self.model.id])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_history" % (self.model._meta.app_label, self.model._meta.module_name), args=[self.model.id])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_changelist" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

class FeatureTestCase(TestCase):

    def setUp(self):
        self.feature1 = Feature.objects.create(
            name='',
            description='',
            configuration='',
            variability='mandatory',
            type='abstract',
            binding_time= BindingTime.objects.create(),
        )
        self.feature1.save()
        self.model = self.feature1

    def test_response(self):
        url = reverse("admin:%s_%s_add" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_change" % (self.model._meta.app_label, self.model._meta.module_name), args=[self.model.id])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_delete" % (self.model._meta.app_label, self.model._meta.module_name), args=[self.model.id])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_history" % (self.model._meta.app_label, self.model._meta.module_name), args=[self.model.id])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_changelist" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

class BindingTimeTestCase(TestCase):

     def setUp(self):
        self.binding_time1 = BindingTime.objects.create(name='', description='')
        self.binding_time1.save()
        self.model = self.binding_time1

     def test_response(self):
        url = reverse("admin:%s_%s_add" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_change" % (self.model._meta.app_label, self.model._meta.module_name), args=[self.model.id])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_delete" % (self.model._meta.app_label, self.model._meta.module_name), args=[self.model.id])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_history" % (self.model._meta.app_label, self.model._meta.module_name), args=[self.model.id])
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)

        url = reverse("admin:%s_%s_changelist" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow = True)
        self.assertEqual(response.status_code,  200)


