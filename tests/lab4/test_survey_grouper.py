"""
Tests survey grouper logic
They check age groups and sorting of persons
"""

import unittest
from src.lab4.survey_grouper import SurveyGrouper


class SurveyGrouperTests(unittest.TestCase):
    """
    This test class checks main logic of SurveyGrouper
    """

    def setUp(self):
        """
        Create SurveyGrouper with default boundaries
        """
        self.grouper = SurveyGrouper()

    def test_example_from_task(self):
        """
        Test example from the task with several persons
        """
        self.grouper.add_person("Кошельков Захар Брониславович", 105)
        self.grouper.add_person("Дьячков Нисон Иринеевич", 88)
        self.grouper.add_person("Иванов Варлам Якунович", 88)
        self.grouper.add_person("Старостин Ростислав Ермолаевич", 50)
        self.grouper.add_person("Ярилова Розалия Трофимовна", 29)
        self.grouper.add_person("Соколов Андрей Сергеевич", 15)
        self.grouper.add_person("Егоров Алан Петрович", 7)

        lines = self.grouper.format_output()

        self.assertEqual(
            "101+: Кошельков Захар Брониславович (105)",
            lines[0]
        )
        self.assertEqual(
            "81-100: Дьячков Нисон Иринеевич (88), Иванов Варлам Якунович (88)",
            lines[1]
        )
        self.assertEqual(
            "46-60: Старостин Ростислав Ермолаевич (50)",
            lines[2]
        )
        self.assertEqual(
            "26-35: Ярилова Розалия Трофимовна (29)",
            lines[3]
        )
        self.assertEqual(
            "0-18: Соколов Андрей Сергеевич (15), Егоров Алан Петрович (7)",
            lines[4]
        )

    def test_empty_groups_not_printed(self):
        """
        Check that empty age groups are not in the output
        """
        # Only one young person
        self.grouper.add_person("Test Person", 10)

        lines = self.grouper.format_output()

        self.assertEqual(1, len(lines))
        self.assertTrue(lines[0].startswith("0-18: "))

    def test_sorting_inside_group(self):
        """
        Check that persons are sorted by age and name
        """
        # All persons are in the same age group 26-35
        self.grouper.add_person("Anna Z", 30)
        self.grouper.add_person("Boris A", 30)
        self.grouper.add_person("Carl B", 32)

        lines = self.grouper.format_output()

        # Should be from older to younger, then by name
        # Group label for 26-35 is "26-35"
        self.assertEqual(
            "26-35: Carl B (32), Anna Z (30), Boris A (30)",
            lines[0]
        )


if __name__ == "__main__":
    unittest.main()
