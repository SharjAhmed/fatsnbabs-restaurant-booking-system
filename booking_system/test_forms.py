from django.test import TestCase
from .forms import ReservationForm


class TestItemForm(TestCase):

    def test_reservation_date_is_requiered(self):
        form = ReservationForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')

    def test_reservation_time_is_requiered(self):
        form = ReservationForm({'time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(form.errors['time'][0], 'This field is required.')

    def test_reservation_table_is_requiered(self):
        form = ReservationForm({'table': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('table', form.errors.keys())
        self.assertEqual(form.errors['table'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ReservationForm()
        self.assertEqual(form.Meta.fields, ['table', 'date', 'time'])
