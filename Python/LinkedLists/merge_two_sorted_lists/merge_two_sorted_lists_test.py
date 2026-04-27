import unittest

from merge_two_sorted_lists import ListNode, Solution


def build_linked_list(values):
    dummy = ListNode()
    cur = dummy
    for val in values:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def linked_list_to_list(head):
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


class TestMergeTwoSortedLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_both_empty(self):
        result = self.solution.mergeTwoLists(None, None)
        self.assertIsNone(result)

    def test_list1_empty(self):
        list2 = build_linked_list([0, 2, 4])
        result = self.solution.mergeTwoLists(None, list2)
        self.assertEqual(linked_list_to_list(result), [0, 2, 4])

    def test_list2_empty(self):
        list1 = build_linked_list([1, 3, 5])
        result = self.solution.mergeTwoLists(list1, None)
        self.assertEqual(linked_list_to_list(result), [1, 3, 5])

    def test_leetcode_example(self):
        list1 = build_linked_list([1, 2, 4])
        list2 = build_linked_list([1, 3, 4])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 1, 2, 3, 4, 4])

    def test_interleaving_values(self):
        list1 = build_linked_list([1, 3, 5, 7])
        list2 = build_linked_list([2, 4, 6, 8])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_all_values_from_list1_smaller(self):
        list1 = build_linked_list([1, 2, 3])
        list2 = build_linked_list([10, 11, 12])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 10, 11, 12])

    def test_all_values_from_list2_smaller(self):
        list1 = build_linked_list([10, 11, 12])
        list2 = build_linked_list([1, 2, 3])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 10, 11, 12])

    def test_duplicates_and_equal_values(self):
        list1 = build_linked_list([1, 1, 2, 3])
        list2 = build_linked_list([1, 2, 2, 4])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 1, 1, 2, 2, 2, 3, 4])

    def test_negative_and_positive_values(self):
        list1 = build_linked_list([-10, -3, 0, 5])
        list2 = build_linked_list([-6, -4, 2, 8])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [-10, -6, -4, -3, 0, 2, 5, 8])

    def test_single_element_each(self):
        list1 = build_linked_list([1])
        list2 = build_linked_list([2])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [1, 2])

    def test_single_element_equal(self):
        list1 = build_linked_list([5])
        list2 = build_linked_list([5])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(result), [5, 5])

    def test_longer_lists(self):
        list1 = build_linked_list([1, 4, 7, 10, 13, 16])
        list2 = build_linked_list([2, 3, 5, 6, 8, 9, 11, 12, 14, 15])
        result = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual(
            linked_list_to_list(result),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
        )


if __name__ == "__main__":
    unittest.main()
