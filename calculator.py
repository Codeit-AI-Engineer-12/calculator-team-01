from ops import root
from ops.add import add
from ops.average import average
from ops.derivative import derivative
from ops.divide import divide
from ops.floor_divide import floor_divide
from ops.max import maximum
from ops.minimum import minimum
from ops.multiply import multiply
from ops.power import power
from ops.subtract import subtract

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "//": floor_divide,
    "**": power,
    "diff": derivative,
    "max": maximum,
    "min": minimum,
    "avg": average,
    "root": root,
}
