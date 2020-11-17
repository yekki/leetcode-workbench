import os


class LeetcodeDAO:
    def __init__(self, d):
        db_dir = os.path.abspath(os.path.join(__file__, "../..", "data"))
        if not os.path.exists(db_dir):
            os.mkdir(db_dir)

        self._db_path = os.path.join(db_dir, 'leetcode.db')
