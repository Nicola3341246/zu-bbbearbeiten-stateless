import unittest
import helper


class UnitTestForHelper(unittest.TestCase):
    def test_add(self):
        helper.add("TodoName")
        items = helper.get_all()
        self.assertEqual(items[0].todo, "TodoName")

    def test_add2(self):
        helper.add("Verbisierung")
        items = helper.get_all()
        self.assertEqual(items[0].todo, "Verbbbisierung")

    def test_get(self):
        helper.add("TodoName")
        item = helper.get(0)
        self.assertEqual(item.todo, "TodoName")

    def test_update(self):
        helper.add("TodoName")
        helper.update(0)
        item = helper.get(0)
        self.assertEqual(item.isCompleted, True)

    def test_delete_all(self):
        helper.add("TodoName")
        helper.delete_all()
        items = helper.get_all()
        self.assertEqual(len(items), 0)
