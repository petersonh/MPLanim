from MPLanim.core.Animation import Animation
from MPLanim.core.Helpers import *
from easing_functions import *
from typing import Callable
import matplotlib
import matplotlib.animation

matplotlib.rcParams['animation.embed_limit'] = 2**128

class LineDraw(Animation):
    
    """Constructs a LineDraw object
    duration -- The duration of the animation in milliseconds
    easing -- The easing function applied to the animation - see https://easings.net/ for examples
    animation_function -- The user defined function that drives the animation
    """
    def __init__(self, 
                 start_time: int,
                 duration: int,
                 easing_function: Callable[[float, float, float], float], 
                 line: matplotlib.lines.Line2D,
                 x_data: list,
                 y_data: list,
                 start_index: int,
                 end_index: int):
        
        super().__init__(start_time, duration, easing_function, self._line_draw)

        self._line = line
        self._x_data = x_data
        self._y_data = y_data
        self._start_index = start_index
        self._end_index = end_index
        
    def _line_draw(self, t):
        index = lerp(self._start_index, self._end_index, t)
        self._line.set_data(self._x_data[:index], self._y_data[:index])
    
class LineDraw2(Animation):
    
    """Constructs a LineDraw object
    duration -- The duration of the animation in milliseconds
    easing -- The easing function applied to the animation - see https://easings.net/ for examples
    animation_function -- The user defined function that drives the animation
    """
    def __init__(self,
                 line: matplotlib.lines.Line2D,
                 x: list,
                 y: list,
                 start: int,
                 duration: int,
                 easing: Callable[[float, float, float], float] = SineEaseInOut):
        
        super().__init__(start, duration, easing, self._line_draw)

        self._line = line
        self._x = x
        self._y = y
        self._data_length = len(x)
        
    def _line_draw(self, t):
        index = lerp(0, self._data_length - 1, t)
        self._line.set_data(self._x[:index], self._y[:index])
        
class MoveMarker(Animation):
    
    """Constructs a MoveMarker object
    duration -- The duration of the animation in milliseconds
    easing -- The easing function applied to the animation - see https://easings.net/ for examples
    animation_function -- The user defined function that drives the animation
    """
    def __init__(self, 
                 start_time: int,
                 duration: int,
                 easing_function: Callable[[float, float, float], float], 
                 marker: matplotlib.lines.Line2D,
                 x_data: list,
                 y_data: list,
                 start_index: int,
                 end_index: int):
        
        super().__init__(start_time, duration, easing_function, self._marker_move)

        self._marker = marker
        self._x_data = x_data
        self._y_data = y_data
        self._start_index = start_index
        self._end_index = end_index
        
    def _marker_move(self, t):
        index = lerp(self._start_index, self._end_index, t)
        index = index - 1 if index > 0 else 0
        self._marker.set_data(self._x_data[index], self._y_data[index])

class MoveMarker2(Animation):
    
    """Constructs a MoveMarker object
    duration -- The duration of the animation in milliseconds
    easing -- The easing function applied to the animation - see https://easings.net/ for examples
    animation_function -- The user defined function that drives the animation
    """
    def __init__(self, 
                 start: int,
                 duration: int,
                 marker: matplotlib.lines.Line2D,
                 x: list,
                 y: list,
                 easing: Callable[[float, float, float], float] = SineEaseInOut):
        
        super().__init__(start, duration, easing, self._marker_move)

        self._marker = marker
        self._x = x
        self._y = y
        self._data_length = len(x)
        
    def _marker_move(self, t):
        index = lerp(0, self._data_length - 1, t)
        index = index - 1 if index > 0 else 0
        self._marker.set_data(self._x[index], self._y[index])
        
class Autoscale(Animation):
    
    """Constructs a Autoscale object
    duration -- The duration of the animation in milliseconds
    ax -- The axes that needs to autoscale
    """
    def __init__(self, 
                 start_time: int,
                 duration: int,
                 ax: matplotlib.axes):
        
        super().__init__(start_time, duration, LinearInOut, self._autoscale)
        
        self._ax = ax
        
    def _autoscale(self, t):
        self._ax.relim()
        self._ax.autoscale_view()

class Autoscale2(Animation):
    
    """Constructs a Autoscale object
    duration -- The duration of the animation in milliseconds
    ax -- The axes that needs to autoscale
    """
    def __init__(self, 
                 start: int,
                 duration: int,
                 ax: matplotlib.axes):
        
        super().__init__(start, duration, LinearInOut, self._autoscale)
        
        self._ax = ax
        
    def _autoscale(self, t):
        self._ax.relim()
        self._ax.autoscale_view()

class Maxscale(Animation):
    
    """Constructs a Maxscale object
    duration -- The duration of the animation in milliseconds
    ax -- The axes that needs to autoscale
    """
    def __init__(self, 
                 start_time: int,
                 duration: int,
                 ax: matplotlib.axes,
                 x_data: list,
                 y_data: list):
        
        super().__init__(start_time, duration, LinearInOut, self._maxscale)
        
        self._ax = ax
        self._x_data = x_data
        self._y_data = y_data
        
    def _maxscale(self, t):
        self._ax.set_xlim(min(self._sin_x), max(self._sin_x))
        self._ax.set_ylim(min(self._sin_y), max(self._sin_y))

class Maxscale2(Animation):
    
    """Constructs a Maxscale object
    duration -- The duration of the animation in milliseconds
    ax -- The axes that needs to autoscale
    """
    def __init__(self, 
                 start: int,
                 duration: int,
                 ax: matplotlib.axes,
                 x: list,
                 y: list):
        
        super().__init__(start, duration, LinearInOut, self._maxscale)
        
        self._ax = ax
        self._x = x
        self._y = y
        
    def _maxscale(self, t):
        self._ax.set_xlim(min(self._x), max(self._x))
        self._ax.set_ylim(min(self._y), max(self._y))

class ScaleX(Animation):
    
    """Constructs a ScaleX object
    duration -- The duration of the animation in milliseconds
    ax -- The axes that needs to autoscale
    """
    def __init__(self, 
                 start_time: int,
                 duration: int,
                 ax: matplotlib.axes,
                 left: float,
                 right: float):
        
        super().__init__(start_time, duration, LinearInOut, self._scalex)
        
        self._ax = ax
        self._left = left
        self._right = right
        self._start_xlim = None
        
    def _scalex(self, t):
        self._start_xlim = self._ax.get_xlim() if self._start_xlim == None else self._start_xlim
        left = lerp_float(self._start_xlim[0], self._left, t)
        right = lerp_float(self._start_xlim[1], self._right, t)
        self._ax.set_xlim(left=left, right=right)

class ScaleX2(Animation):
    
    """Constructs a ScaleX object
    duration -- The duration of the animation in milliseconds
    ax -- The axes that needs to autoscale
    """
    def __init__(self, 
                 start: int,
                 duration: int,
                 ax: matplotlib.axes,
                 left: float,
                 right: float):
        
        super().__init__(start, duration, LinearInOut, self._scalex)
        
        self._ax = ax
        self._left = left
        self._right = right
        self._start_xlim = None
        
    def _scalex(self, t):
        self._start_xlim = self._ax.get_xlim() if self._start_xlim == None else self._start_xlim
        left = lerp_float(self._start_xlim[0], self._left, t)
        right = lerp_float(self._start_xlim[1], self._right, t)
        self._ax.set_xlim(left=left, right=right)    

class ScaleY(Animation):
    
    """Constructs a ScaleY object
    duration -- The duration of the animation in milliseconds
    ax -- The axes that needs to autoscale
    """
    def __init__(self, 
                 start_time: int,
                 duration: int,
                 ax: matplotlib.axes,
                 bottom: float,
                 top: float):
        
        super().__init__(start_time, duration, LinearInOut, self._scaley)
        
        self._ax = ax
        self._bottom = bottom
        self._top = top
        self._start_ylim = None
        
    def _scaley(self, t):
        self._start_ylim = self._ax.get_ylim() if self._start_ylim == None else self._start_ylim
        bottom = lerp_float(self._start_ylim[0], self._bottom, t)
        top = lerp_float(self._start_ylim[1], self._top, t)
        self._ax.set_ylim(bottom=bottom, top=top)
    
class AnnotateMovingMarker(Animation):

    """Constructs a AnnotateMovingMarker object
    duration -- The duration of the animation in milliseconds
    ax -- The axes that needs to autoscale
    """
    def __init__(self, 
                 start_time: int,
                 duration: int,
                 easing_function: Callable[[float, float, float], float],
                 ax: matplotlib.axes,
                 annotation: matplotlib.text.Annotation,
                 x_data: list,
                 y_data: list,
                 start_index: int,
                 end_index: int,
                 y_text_position_pixels: int):
        
        super().__init__(start_time, duration, easing_function, self.__annotate_moving_marker)
        
        self._ax = ax
        self._annotation = annotation
        self._x_data = x_data
        self._y_data = y_data
        self._start_index = start_index
        self._end_index = end_index
        self._y_text_position_pixels = y_text_position_pixels
        
    def __annotate_moving_marker(self, t):
        index = lerp(self._start_index, self._end_index, t)
        index = index - 1 if index > 0 else 0
        xy_pos = (self._x_data[index], self._y_data[index])        
        xdisplay, ydisplay = self._ax.transData.inverted().transform((0,self._y_text_position_pixels))
        self._annotation.xy = xy_pos
        self._annotation.set_position((xy_pos[0], ydisplay))

class LineDrawWindow(Animation):
    
    """Constructs a MPLAnimationLineDraw object
    duration -- The duration of the animation in milliseconds
    easing -- The easing function applied to the animation - see https://easings.net/ for examples
    animation_function -- The user defined function that drives the animation
    """
    def __init__(self, 
                 start_time: int,
                 duration: int,
                 easing_function: Callable[[float, float, float], float], 
                 line: matplotlib.lines.Line2D,
                 x_data: list,
                 y_data: list,
                 start_index: int,
                 end_index: int,
                 window_size: int):
        
        super().__init__(start_time, duration, easing_function, self._line_draw_window)

        self._line = line
        self._x_data = x_data
        self._y_data = y_data
        self._start_index = start_index
        self._end_index = end_index
        self._window_size = window_size
        
    def _line_draw_window(self, t):
        index = lerp(self._start_index, self._end_index, t)
        start_index = (index - self._window_size) if (index - self._window_size) >= 0 else 0
        self._line.set_data(self._x_data[start_index:index], self._y_data[start_index:index])
