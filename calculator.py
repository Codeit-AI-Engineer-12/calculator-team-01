from ops.add import add
from ops.multiply import multiply
from ops.subtract import subtract
from ops.divide import divide
from ops.power import power

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
}