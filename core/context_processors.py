import subprocess


def git_version(request):
    git_version = (
        subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
        .decode("utf-8")
        .strip()
    )

    return {"version": git_version}
