import sys
import time
from typing import get_args

from curl_cffi import BrowserTypeLiteral

import lbc


def main() -> None:
    working_impersonates: list[str] = []

    for impersonate in get_args(BrowserTypeLiteral):
        try:
            client = lbc.Client(impersonate=impersonate)
            benchmark = 0
            for _ in range(3):
                try:
                    time.sleep(10)
                    client.search(text="Voiture")
                    benchmark += 1
                except:  # noqa
                    break
            print(f"{impersonate} ({benchmark}/3)", file=sys.stderr)
            if benchmark == 3:
                working_impersonates.append(impersonate)
        except Exception as e:  # noqa
            print(f"{impersonate} error: {e}", file=sys.stderr)

    print("\n".join(working_impersonates))


if __name__ == "__main__":
    main()
