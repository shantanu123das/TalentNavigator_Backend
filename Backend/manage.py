import os
import subprocess
import sys

# Increase the recursion limit
sys.setrecursionlimit(1500)

PROJECTS = ["libs", "crews", "core"]  # Add more projects as needed


def run(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)


def install():
    run("poetry install --no-root")
    for project in PROJECTS:

        project_path = os.path.join(project)
        if os.path.isdir(project_path):

            print(f"Installing : {project}")
            os.chdir(project_path)
            run("poetry install")
            os.chdir("..")


def format_code():
    for project in PROJECTS:
        project_path = os.path.join(project)
        if os.path.isdir(project_path):
            os.chdir(project_path)
            run("poetry run black .")
            run("poetry run isort .")
            os.chdir("../..")


def lint():
    try:
        for project in PROJECTS:
            project_path = os.path.join(project)
            if os.path.isdir(project_path):
                result = subprocess.run(
                    [
                        "poetry",
                        "run",
                        "flake8",
                        "--exclude=.venv,.git,__pycache__,docs,build,dist,.tox, manage.py,core/alembic,alembic",
                        project_path,
                    ],
                    check=True,
                    capture_output=True,
                    text=True,
                )
                print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stdout)
        print(e.stderr)
        sys.exit(e.returncode)


def run_app():
    os.chdir("core")  # Assuming 'core' is where your main application resides
    run("poetry run app")


def test():
    for project in PROJECTS:
        project_path = os.path.join(project)
        if os.path.isdir(project_path):
            os.chdir(project_path)
            run("poetry run pytest")
            os.chdir("../..")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: manage.py [install|format|lint|test]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "install":
        install()
    elif command == "format":
        format_code()
    elif command == "lint":
        lint()
    elif command == "test":
        test()
    elif command == "run_app":
        run_app()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
