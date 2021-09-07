from typing import Callable, NoReturn

class Animation:
    
    """Constructs a MPLAnimation object
    duration -- The duration of the animation in milliseconds
    easing -- The easing function applied to the animation - see https://easings.net/ for examples
    animation_function -- The user defined function that drives the animation
    """
    def __init__(self,
                 start_time: int,
                 duration: int, 
                 easing_function: Callable[[float, float, float], float], 
                 animation_function: Callable[[float], NoReturn]):
        self._start_time = start_time
        self._duration = duration
        self._easing_function = easing_function()
        self._animation_function = animation_function
    
    @property
    def start_time(self):
        return self._start_time
    
    @start_time.setter
    def duration(self, start_time):
        self._start_time = start_time
    
    @property
    def duration(self):
        return self._duration
    
    @duration.setter
    def duration(self, duration):
        self._duration = duration
    
    @property
    def animation_function(self):
        return self._animation_function
    
    @property
    def easing_function(self):
        return self._easing_function
