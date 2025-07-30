from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            priority='high',
            status='pending',
            assigned_to=self.user
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertEqual(self.task.priority, 'high')
        self.assertEqual(self.task.status, 'pending')
        self.assertEqual(self.task.assigned_to, self.user)

    def test_task_str_method(self):
        self.assertEqual(str(self.task), 'Test Task')

    def test_task_ordering(self):
        task2 = Task.objects.create(
            title='Second Task',
            assigned_to=self.user
        )
        tasks = Task.objects.all()
        self.assertEqual(tasks[0], task2)  # Most recent first


class TaskViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            assigned_to=self.user
        )

    def test_task_list_requires_login(self):
        response = self.client.get(reverse('task_list'))
        self.assertRedirects(response, '/login/?next=/')

    def test_task_list_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')

    def test_task_detail(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('task_detail', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
        self.assertContains(response, 'Test Description')

    def test_task_create(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'New Description',
            'priority': 'medium',
            'status': 'pending'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_task_update(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('task_update', args=[self.task.pk]), {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'priority': 'low',
            'status': 'in_progress'
        })
        self.assertEqual(response.status_code, 302)
        updated_task = Task.objects.get(pk=self.task.pk)
        self.assertEqual(updated_task.title, 'Updated Task')
        self.assertEqual(updated_task.status, 'in_progress')

    def test_task_delete(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_user_can_only_see_own_tasks(self):
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        other_task = Task.objects.create(
            title='Other Task',
            assigned_to=other_user
        )
        
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('task_list'))
        self.assertContains(response, 'Test Task')
        self.assertNotContains(response, 'Other Task')
        
        # Try to access other user's task
        response = self.client.get(reverse('task_detail', args=[other_task.pk]))
        self.assertEqual(response.status_code, 404)