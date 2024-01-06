from attrs import define


@define
class Weights:
    height: float
    lines: float
    holes: float
    bumpiness: float
