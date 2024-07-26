from _typeshed import Incomplete

def polyval(ctx, coeffs, x, derivative: bool = False): ...
def polyroots(
    ctx,
    coeffs,
    maxsteps: int = 50,
    cleanup: bool = True,
    extraprec: int = 10,
    error: bool = False,
    roots_init: Incomplete | None = None,
): ...
