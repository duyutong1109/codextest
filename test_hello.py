import subprocess
import sys
from pathlib import Path


def test_hello_output() -> None:
    script = Path(__file__).with_name("hello.py")
    result = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
        text=True,
        check=True,
    )

    assert result.stdout == "Hello Codex\n"
    assert result.stderr == ""
