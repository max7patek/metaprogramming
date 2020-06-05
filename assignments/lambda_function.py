import json
import subprocess
import os
import tempfile

BASE_DIR = "assignments"
TMP_DIR = tempfile.gettempdir()
RUNNER_FILENAME = "runner.py"
SUBMISSION_FILENAME = "submission.py"


def lambda_handler(event, context):
    
    # find puzzle
    puzzle_id = event["puzzleID"]
    dir = os.listdir(BASE_DIR)
    for puz in dir:
        if puz.startswith(puzzle_id):
            puzzle_name = puz
            break
    else:
        return {'statusCode': 404}
    
    # make paths
    puzzle_dir = os.path.join(BASE_DIR, puzzle_name)
    puzzle_workspace = os.path.join(TMP_DIR, puzzle_name)
    submission_path = os.path.join(puzzle_workspace, SUBMISSION_FILENAME)
    runner_path = os.path.join(puzzle_workspace, RUNNER_FILENAME)
            
    # copy puzzle to workspace
    subprocess.run(["cp", "-r", puzzle_dir, TMP_DIR])
    with open(submission_path, 'w') as submission_file:
        print(event["code"], file=submission_file)
    
    # execute
    sp = subprocess.run(["python3", runner_path], capture_output=True)
    if sp.returncode == 0:
        return {
            'statusCode': 200,
            'body': "OK",
            'stdout': sp.stdout.decode('utf8'),
            'stderr': sp.stderr.decode('utf8'),
        }
    return {
        'statusCode': 200,
        'body': "BAD",
        'exitCode': sp.returncode,
        'stdout': sp.stdout.decode('utf8'),
        'stderr': sp.stderr.decode('utf8'),
    }
