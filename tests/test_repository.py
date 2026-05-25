import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryStructureTests(unittest.TestCase):
    def test_expected_project_files_exist(self):
        expected = [
            "README.md",
            "LICENSE.md",
            "CHANGELOG.md",
            "notebooks/object_detection/Custom_Dataset_Training_with_YOLOv11.ipynb",
            "notebooks/object_detection/Getting_Started_with_Yolov11__Object_Detection.ipynb",
            "tracking/opencv_trackers/kcf.py",
            "tracking/opencv_trackers/csrt.py",
            "assets/banner.png",
            "assets/tracking-demo.gif",
        ]

        missing = [path for path in expected if not (ROOT / path).exists()]
        self.assertEqual(missing, [])

    def test_no_large_accidental_files_committed(self):
        max_size_mb = 25
        ignored_dirs = {".git", "__pycache__", ".ipynb_checkpoints"}
        oversized = []

        for path in ROOT.rglob("*"):
            if not path.is_file():
                continue
            if any(part in ignored_dirs for part in path.parts):
                continue
            if path.stat().st_size > max_size_mb * 1024 * 1024:
                oversized.append(str(path.relative_to(ROOT)))

        self.assertEqual(oversized, [])


if __name__ == "__main__":
    unittest.main()

