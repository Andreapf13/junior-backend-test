from unittest.mock import MagicMock 
import unittest

class TestMessage(unittest.TestCase):
  def test_message(self):
    my_bot = WhatsappBot(language="en")  # Bot should re instantiated for each conversation
    my_bot.message("Yes, I would like to receive notifications", "newsletter")
    self.assertEqual(my_bot.conversation_status, "start")

if __name__ == '__main__':
    unittest.main()
