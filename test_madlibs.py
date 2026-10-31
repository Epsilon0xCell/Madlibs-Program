import subprocess
import sys
import unittest

from madlibs import build_story


class StoryTests(unittest.TestCase):
    def test_story_slots_and_stripping(self):
        story = build_story(" run ", "happy", "dog", "jumped", "sleep")
        self.assertEqual(
            story,
            "Madlib: Joe is Going to run, Joe is really happy, "
            "Unfortunately, Joe got into trouble with dog, "
            "If Joe were to leave now, he would certainly get jumped, "
            "Joe now has sleep.",
        )


class ScriptTests(unittest.TestCase):
    def run_script(self, text):
        return subprocess.run(
            [sys.executable, "madlibs.py"], input=text, capture_output=True, text=True
        )

    def test_full_run_prints_hint(self):
        out = self.run_script("run\nhappy\ndog\njumped\nsleep\n")
        self.assertEqual(out.returncode, 0)
        self.assertIn("Madlib: Joe is Going to run", out.stdout)
        self.assertIn("What happens if you put the only noun as Joe?", out.stdout)

    def test_joe_noun_triggers_easter_egg(self):
        out = self.run_script("run\nhappy\nJoe\njumped\nsleep\n")
        self.assertEqual(out.returncode, 0)
        self.assertIn("You can't do that", out.stdout)

    def test_early_eof_ends_with_status_0(self):
        out = self.run_script("run\n")
        self.assertEqual(out.returncode, 0)
        self.assertIn("Input closed, ending program", out.stdout)


if __name__ == "__main__":
    unittest.main()
