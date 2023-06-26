# -*- coding: utf-8 -*-

from acore_constants import api


def test():
    _ = api


if __name__ == "__main__":
    from acore_constants.tests import run_cov_test

    run_cov_test(__file__, "acore_constants.api", preview=False)
