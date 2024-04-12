import time

class TimerException(Exception):
    pass

class Timer:
    def __init__(self):
        self.start_time: float = time.time()
        self._stop_time: float = self.start_time
        self.pauses: list[float, ...] = []
        self.unpauses: list[float, ...] = []
        self._paused = True
        self._running = False

    def __str__(self):
        return (f'Timer('
                f'running={self.running}, '
                f'paused={self.paused}, '
                f'start_time={self.start_time:.2f}, '
                f'stop_time={self.stop_time:.2f}, '
                f'elapsed={self.elapsed:.2f}, '
                f'elapsed_paused={self.elapsed_paused:.2f}, '
                f'elapsed_total={self.elapsed_total:.2f}'
                f')')

    @property
    def stop_time(self) -> float:
        if self._running:
            return time.time()
        else:
            return self._stop_time

    @property
    def elapsed_total(self) -> float:
        return self.stop_time - self.start_time

    @property
    def elapsed_paused(self) -> float:
        """
        Amount of time spent paused.
        :return:
        """
        if len(self.pauses) == len(self.unpauses):
            return sum(unpause - pause for pause, unpause in zip(self.pauses, self.unpauses))
        else:
            return sum(unpause - pause for pause, unpause in zip(self.pauses, self.unpauses)) + (time.time() - self.pauses[-1])

    @property
    def elapsed(self) -> float:
        """
        Amount of time spent unpaused since start.
        :return:
        """
        return self.elapsed_total - self.elapsed_paused

    @property
    def paused(self):
        return self._paused

    @property
    def running(self):
        return self._running

    def start(self):
        """
        Start the timer.
        :return:
        """
        if self._running:
            raise TimerException('Timer already started!')
        self.start_time = time.time()
        self._running = True
        self._paused = False
        return self.start_time

    def stop(self):
        """
        Stop the timer.
        :return:
        """
        if not self._running:
            raise TimerException('Timer already stopped!')
        self._stop_time = time.time()
        self._running = False
        self._paused = True
        return self.elapsed

    def pause(self):
        """
        Pause the timer.
        :return:
        """
        if self._paused:
            raise TimerException('Timer already paused!')
        self.pauses.append(time.time())
        self._paused = True

    def unpause(self):
        """
        Unpause the timer.
        :return:
        """
        if not self._paused:
            raise TimerException('Timer already unpaused!')
        self.unpauses.append(time.time())
        self._paused = False

    def sleep(self, duration: float):
        """
        Sleep while paused for a duration.
        :param duration:
        :return:
        """
        self.pause()
        time.sleep(duration)
        self.unpause()

    def sleep_unpaused(self, duration: float):
        """
        Sleep while unpaused for a duration
        :param duration:
        :return:
        """
        time.sleep(duration)

def main():
    timer = Timer()
    print(timer)
    timer.start()
    print(timer)
    timer.sleep_unpaused(1)
    print(timer)
    timer.sleep(2)
    print(timer)
    timer.sleep_unpaused(3)
    print(timer)
    timer.stop()
    print(timer)

if __name__ == '__main__':
    main()