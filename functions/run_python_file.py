import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(target_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        commands = ["python3", target_path]
        if args:
            commands.extend(args)

        result = subprocess.run(
            commands,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output = []
        if result.stdout:
            output.append(f"STDOUT: {result.stdout}")
        if result.stderr:
            output.append(f"STDERR: {result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        if not output:
            return "No output produced."

        return "\n".join(output)
    except Exception as e:
        return f'Error: executing Python file: {e}'
