import pytest

import subprocess
import shutil


@pytest.mark.basic
class TestBasic:
    def test_binaries_exist(self):
        executable = shutil.which("hello_world.exe")

        assert executable is not None, "hello_world.exe should be in PATH"

    def test_binaries_run(self):
        executable = shutil.which("hello_world.exe")

        assert executable is not None, "hello_world.exe should be in PATH"

        result = subprocess.run(
            ["mpirun", "-n", "6", "--allow-run-as-root", executable],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )

        print("stdout:\n", result.stdout)
        print("stderr:\n", result.stderr)

        assert result.returncode == 0

@pytest.mark.slow
class TestSlow:
    def test_many_process_binaries(self):
        executable = shutil.which("hello_world.exe")

        assert executable is not None, "hello_world.exe should be in PATH"

        result = subprocess.run(
            ["mpirun", "-n", "10", "--allow-run-as-root", executable],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )

        print("stdout:\n", result.stdout)
        print("stderr:\n", result.stderr)

        assert result.returncode == 0
