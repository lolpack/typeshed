from _typeshed import Incomplete
from colorsys import hsv_to_rgb as hsv_to_rgb

class VisualizationMethods:
    plot_ignore: Incomplete

def plot(
    ctx,
    f,
    xlim=[-5, 5],
    ylim: Incomplete | None = None,
    points: int = 200,
    file: Incomplete | None = None,
    dpi: Incomplete | None = None,
    singularities=[],
    axes: Incomplete | None = None,
) -> None: ...
def default_color_function(ctx, z): ...

blue_orange_colors: Incomplete

def phase_color_function(ctx, z): ...
def cplot(
    ctx,
    f,
    re=[-5, 5],
    im=[-5, 5],
    points: int = 2000,
    color: Incomplete | None = None,
    verbose: bool = False,
    file: Incomplete | None = None,
    dpi: Incomplete | None = None,
    axes: Incomplete | None = None,
) -> None: ...
def splot(
    ctx,
    f,
    u=[-5, 5],
    v=[-5, 5],
    points: int = 100,
    keep_aspect: bool = True,
    wireframe: bool = False,
    file: Incomplete | None = None,
    dpi: Incomplete | None = None,
    axes: Incomplete | None = None,
) -> None: ...
