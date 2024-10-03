"""Recreate submissions from Gradescope zip to move international students to main GS."""

__author__ = "Kaki Ryan <kakiryan@cs.unc.edu>"

import os
import yaml
import zipfile

# set this to be whatever the big gradescope download folder is
GS_ASSIGNMENT_EXPORT: str = 'assignment_716925_export'
# file name for the quiz or whatever assignment
QUIZ = 'quiz_utils.py'
QUIZ_TESTS = 'quiz_utils_test.py'


def main() -> None:
    """Entry point of script. Expects to be run as CLI program."""
    submission_yml = open(GS_ASSIGNMENT_EXPORT + '/submission_metadata.yml', 'r')
    data = yaml.safe_load(submission_yml)
    for submission in os.listdir(GS_ASSIGNMENT_EXPORT):
        file_name = submission
        submission_path = GS_ASSIGNMENT_EXPORT + '/' + submission
        if data.get(submission) is not None:
            if data.get(submission).get(':submitters')[0][':name'] is not None:
                file_name += '_' + data.get(submission).get(':submitters')[0][':name']

        zf = zipfile.ZipFile(file_name + '.zip', "w")

        for (dirpath, dirnames, filenames) in os.walk(submission_path):
            # this is busted, i am sure there is a better way
            # can try to do something like in submission.py later!
            
            for name in filenames:
                # can get rid of QUIZ_TESTS if no tests required
                if name == QUIZ or name == QUIZ_TESTS:
                    zf.write(os.path.join(dirpath, name), 'quiz/qz01/' + name)
        zf.close()
    
    submission_yml.close()


if __name__ == "__main__":
    main()
