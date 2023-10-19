import unittest
from unittest.mock import patch
from io import StringIO
from datetime import datetime
from db_process.db_update import validate_login_pass, update_values_user
from user_work.login import hi_user, login_user, register_user, authorize_user, write_down_active_user_name

class TestLogin(unittest.TestCase):

    @patch('builtins.input', return_value='r')
    def test_hi_user_register(self, mock_input):
        self.assertEqual(hi_user(), 'r')

    @patch('builtins.input', return_value='l')
    def test_hi_user_login(self, mock_input):
        self.assertEqual(hi_user(), 'l')

    @patch('builtins.input', return_value="Please be careful! Only 2 options available: \n  'l' for login or \n  'r' for registration\n")
    def test_hi_user_login(self, mock_input):
        self.assertEqual(hi_user(), 'n')

    @patch('builtins.input', side_effect=['test@email.ru', 'kat123'])
    def test_login_user(self, mock_input):
        self.assertEqual(login_user(), ('test@email.ru', 'kat123'))

    @patch('builtins.input', side_effect=['test@email.ru', 'Kate', 'Smirnova', 'Finam', 'kat123', 'kat123'])
    def test_register_user(self, mock_input):
        expected_output = (
            'test@email.ru',
            'Kate',
            'Smirnova',
            'kat123',
            'Finam',
            datetime.now().strftime("%Y-%m-%d")
        )
        self.assertEqual(register_user(), expected_output)

    def test_authorize_user_correct_login_data(self):
        with patch('builtins.input', side_effect=['test@email.ru', 'kat123']):
            output = StringIO()
            expected_output = "Welcome back, test@email.ru!. You are successfully signed in!\n"
            authorize_user('test@email.ru', 'kat123', ['test@email.ru'], 'kat123')
            self.assertEqual(output.getvalue(), expected_output)

    def test_authorize_user_incorrect_login_data(self):
        with patch('builtins.input', side_effect=['l']):
            output = StringIO()
            expected_output = "Sorry, test@email.ru! Login data is wrong.\nPlease register new account or check login data.\n"
            authorize_user('test@email.ru', 'wrong_password', ['test@email.ru'], 'kat123')
            self.assertEqual(output.getvalue(), expected_output)

    @patch('builtins.open', create=True)
    def test_write_down_active_user_name(self, mock_open):
        write_down_active_user_name('test_user')
        mock_open.assert_called_once_with('active_user_name.txt', 'w')
        handle = mock_open.return_value.__enter__.return_value
        handle.write.assert_called_once_with('test_user')
