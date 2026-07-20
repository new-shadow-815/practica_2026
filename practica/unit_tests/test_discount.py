import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import pytest
import os
from app.discount import calc_discount, calc_total

config_path = os.path.join(os.path.dirname(__file__), "config.json")

with open(config_path, encoding="utf-8") as f:
    data = json.load(f)


@pytest.mark.parametrize("case", data["discount_tests"])
def test_calc_discount(case):
    assert calc_discount(case["price"], case["percent"]) == case["result"]

#ifk.ifuuviuvkvkuuovhkj
#dtylucvjh.k/ n,
#kvh/jj

@pytest.mark.parametrize("case", data["total_tests"])
def test_calc_total(case):
    assert calc_total(case["price"], case["quantity"]) == case["result"]


@pytest.mark.parametrize("case", data["error_discount"])
def test_discount_errors(case):
    with pytest.raises(ValueError):
        calc_discount(case["price"], case["percent"])


@pytest.mark.parametrize("case", data["error_total"])
def test_total_errors(case):
    with pytest.raises(ValueError):
        calc_total(case["price"], case["quantity"])
