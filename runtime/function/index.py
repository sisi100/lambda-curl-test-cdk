import subprocess


def handler(event, context):
    cmd = subprocess.run(
        "curl https://www.google.com/",
        shell=True,
        capture_output=True,
        text=True,
    )
    return {
        "stdout": cmd.stdout,
        "stderr": cmd.stderr,
    }
