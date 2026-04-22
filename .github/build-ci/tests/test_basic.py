#!/usr/bin/env spack-python
import pytest

import spack.environment
import subprocess
import spack.util.executable

DEFAULT_ENVIRONMENT_PATH: str = "/opt/runner/environments/default"


@pytest.fixture(autouse=True)
def spack_env():
    # Activate the default environment the packages were installed in, before each test
    e: spack.environment.Environment = spack.environment.Environment(
        DEFAULT_ENVIRONMENT_PATH
    )
    spack.environment.activate(e)

    if not e.active:
        raise RuntimeError(
            f"Couldn't activate the default environment at {DEFAULT_ENVIRONMENT_PATH}"
        )

    # Return control to the test
    yield

    # Once the above completes, deactivate the environment
    spack.environment.deactivate()

@pytest.mark.basic
class TestBasic:
    def test_binaries_exist(self):
        spack.util.executable.which("hello_world.exe", required=True)

    def test_binaries_run(self):
        hello_world = spack.util.executable.which("hello_world.exe", required=True)

        result = subprocess.run(
            ["mpirun", "-n", "6", "--allow-run-as-root", hello_world.path],
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
        hello_world = spack.util.executable.which("hello_world.exe", required=True)

        result = subprocess.run(
            ["mpirun", "-n", "10", "--allow-run-as-root", hello_world.path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )

        print("stdout:\n", result.stdout)
        print("stderr:\n", result.stderr)

        assert result.returncode == 0
