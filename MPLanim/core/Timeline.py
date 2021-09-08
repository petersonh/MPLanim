from typing import List
from MPLanim.core.Animation import Animation
import matplotlib
import math
import matplotlib.animation
from IPython.display import HTML, display


class Timeline:
    
    def __init__(self, animations: List[Animation], fig: matplotlib.figure.Figure, frames_per_second: int):
        self._animations = animations
        self._frames_per_second = frames_per_second
        self._duration = max(list(map(lambda x: x.start_time + x.duration, animations)))
        self._duration = self.__milliseconds_to_frames(self._duration, frames_per_second) + 1        
        self._animation = matplotlib.animation.FuncAnimation(fig, self.__animate, self._duration, init_func=lambda: None, interval=1000/frames_per_second)

    @staticmethod
    def __milliseconds_to_frames(milliseconds, frames_per_second) -> int:
        return math.ceil(milliseconds / (1000 / frames_per_second))
    
    @property
    def duration(self):
        return self._duration
    
    def __animate(self, i):
        for animation in self._animations:
            self.print_progress((i+1) / self._duration)
            # print(i)
            # print(self._duration)
            animation_start_frame = self.__milliseconds_to_frames(animation.start_time, self._frames_per_second)
            animation_end_frame = self.__milliseconds_to_frames(animation.duration, self._frames_per_second) + animation_start_frame
            if i >= animation_start_frame and i <= animation_end_frame:
                t = (i - animation_start_frame) / (animation_end_frame - animation_start_frame)
                t = animation.easing_function(t)
                animation.animation_function(t)
    
    def show_in_notebook(self):
        display(HTML(self._animation.to_jshtml()))
        
    def print_progress(self, progress: float):
        percent_complete = int(progress/1.0 * 100.0)
        message = "Rendering "
        total_bars = 20
        progress_int = int(progress * total_bars)
        remainder_int = int(total_bars - (progress * total_bars))
        progress_bars = ''.join(['▰' for x in range(progress_int)])
        remainder_bars = ''.join(['▱' for x in range(remainder_int)])
        progress_bar = progress_bars + remainder_bars
        message += progress_bar
        print(message + " " + str(percent_complete) + "%  ", end='\r')
        # if percent_complete == 100:
        #     print(message + " 100%  ", end='\r')

    def save(self, filename: str):
        FFMpegWriter = matplotlib.animation.writers['ffmpeg']
        metadata = dict(title='', artist='', comment='')
        writer = FFMpegWriter(fps=self._frames_per_second, bitrate=5000, metadata=metadata)
        self._animation.save(filename + ".mp4", writer=writer, dpi=120)