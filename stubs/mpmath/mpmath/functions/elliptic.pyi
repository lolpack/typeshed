from _typeshed import Incomplete

def eta(ctx, tau): ...
def nome(ctx, m): ...
def qfrom(
    ctx,
    q: Incomplete | None = None,
    m: Incomplete | None = None,
    k: Incomplete | None = None,
    tau: Incomplete | None = None,
    qbar: Incomplete | None = None,
): ...
def qbarfrom(
    ctx,
    q: Incomplete | None = None,
    m: Incomplete | None = None,
    k: Incomplete | None = None,
    tau: Incomplete | None = None,
    qbar: Incomplete | None = None,
): ...
def taufrom(
    ctx,
    q: Incomplete | None = None,
    m: Incomplete | None = None,
    k: Incomplete | None = None,
    tau: Incomplete | None = None,
    qbar: Incomplete | None = None,
): ...
def kfrom(
    ctx,
    q: Incomplete | None = None,
    m: Incomplete | None = None,
    k: Incomplete | None = None,
    tau: Incomplete | None = None,
    qbar: Incomplete | None = None,
): ...
def mfrom(
    ctx,
    q: Incomplete | None = None,
    m: Incomplete | None = None,
    k: Incomplete | None = None,
    tau: Incomplete | None = None,
    qbar: Incomplete | None = None,
): ...

jacobi_spec: Incomplete

def ellipfun(
    ctx,
    kind,
    u: Incomplete | None = None,
    m: Incomplete | None = None,
    q: Incomplete | None = None,
    k: Incomplete | None = None,
    tau: Incomplete | None = None,
): ...
def kleinj(ctx, tau: Incomplete | None = None, **kwargs): ...
def RF_calc(ctx, x, y, z, r): ...
def RC_calc(ctx, x, y, r, pv: bool = True): ...
def RJ_calc(ctx, x, y, z, p, r, integration): ...
def elliprf(ctx, x, y, z): ...
def elliprc(ctx, x, y, pv: bool = True): ...
def elliprj(ctx, x, y, z, p, integration: int = 1): ...
def elliprd(ctx, x, y, z): ...
def elliprg(ctx, x, y, z): ...
def ellipf(ctx, phi, m): ...
def ellipe(ctx, *args): ...
def ellippi(ctx, *args): ...
