import subprocess


def handler(event, context):
    cmd = subprocess.run(
        "curl https://blog.i-tale.jp/",
        shell=True,
        capture_output=True,
        text=True,
    )
    return {
        "stdout": cmd.stdout,
        "stderr": cmd.stderr,
    }
