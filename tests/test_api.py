# -*- coding: utf-8 -*-

import os
import pytest


def test():
    from acore_constants import api

    _ = api.TagKey
    _ = api.TagKey.SERVER_ID
    _ = api.TagKey.WOW_STATUS
    _ = api.TagKey.WOW_STATUS_MEASURE_TIME


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
