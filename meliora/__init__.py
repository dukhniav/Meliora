# pylint: disable=broad-except
"""
Meliora portfolio
"""

__version__ = "develop"
__logger__ = "meliora"

if __version__ == "develop":

    try:
        import subprocess

        __version__ = "develop-" + subprocess.check_output(
            ["git", "log", '--format="%h"', "-n 1"], stderr=subprocess.DEVNULL
        ).decode("utf-8").rstrip().strip('"')

    except Exception:  # pragma: no cover
        # git not available, ignore
        try:
            # Try Fallback to admoneo_commit file (created by CI while building docker image)
            from pathlib import Path

            versionfile = Path("./meliora_commit")
            if versionfile.is_file():
                __version__ = f"docker-{versionfile.read_text()[:8]}"
        except Exception:
            pass
