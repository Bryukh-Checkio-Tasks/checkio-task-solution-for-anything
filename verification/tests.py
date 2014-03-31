prepare = """
if not "checkio" in USER_GLOBAL:
    raise NotImplementedError("Where is checkio?")
checkio = USER_GLOBAL['checkio']
"""

run_test = """RET['code_result'] = ({0})
"""

import_re = """import re
"""
import_math = """import math
"""

non_list = "checkio({}) != []"
hello_world = "checkio('Hello') < 'World'"
eighty = "checkio(80) > 81"
re_re = "checkio(re) >= re"
re_math = "checkio(re) <= math"
ord_5 = "checkio(5) == ord"

TESTS = {
    "1. Basics": [
        {
            "test_code": {
                "python-3": prepare + run_test.format(non_list),
                "python-27": prepare + run_test.format(non_list)
            },
            "show": {"python-3": non_list, "python-27": non_list},
            "answer": True
        },
        {
            "test_code": {
                "python-3": prepare + run_test.format(hello_world),
                "python-27": prepare + run_test.format(hello_world)
            },
            "show": {"python-3": hello_world, "python-27": hello_world},
            "answer": True
        },
        {
            "test_code": {
                "python-3": prepare + run_test.format(eighty),
                "python-27": prepare + run_test.format(eighty)
            },
            "show": {"python-3": eighty, "python-27": eighty},
            "answer": True
        },
        {
            "test_code": {
                "python-3": prepare + run_test.format(ord_5),
                "python-27": prepare + run_test.format(ord_5)
            },
            "show": {"python-3": ord_5, "python-27": ord_5},
            "answer": True
        },


    ],
    "2. Module": [
        {
            "test_code": {
                "python-3": prepare + import_re + run_test.format(re_re),
                "python-27": prepare + import_re + run_test.format(re_re)
            },
            "show": {"python-3": re_re, "python-27": re_re},
            "answer": True
        },
        {
            "test_code": {
                "python-3": prepare + import_re + import_math + run_test.format(re_math),
                "python-27": prepare + import_re + import_math + run_test.format(re_math)
            },
            "show": {"python-3": re_math, "python-27": re_math},
            "answer": True
        },
    ]
}
