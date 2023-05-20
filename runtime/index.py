import subprocess


def handler(event, context):
    cmd = subprocess.run(
        # "curl --version", # curl 7.88.1
        "curl https://blog.i-tale.jp/",
        shell=True,
        capture_output=True,
        text=True,
    )
    print("====> stdout")
    print(cmd.stdout)
    print("====> stderr")
    print(cmd.stderr)
    return
