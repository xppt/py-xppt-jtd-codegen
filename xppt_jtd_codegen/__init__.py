import subprocess
import sys
from pathlib import Path


def main() -> None:
    binary = _binaries.get(sys.platform)
    if binary is None:
        raise NotImplementedError('unsupported os')

    process = subprocess.run(
        [
            str(Path(__file__).absolute().parent / binary),
            *sys.argv[1:],
        ],
    )

    sys.exit(process.returncode)


_binaries = {
    'linux': 'jtd-codegen-linux',
    'win32': 'jtd-codegen-windows.exe',
}


if __name__ == '__main__':
    main()
