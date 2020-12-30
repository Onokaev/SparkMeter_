'''
The suggested fixes make the code run, but there are likely logical errors which can only
be debugged with more context on what the code is meant to achieve
'''

import asyncio
import logging
import os

# You need to import datetime
import datetime

logger = logging.getLogger(__name__)
SLEEP_DURATION = os.getenv("SLEEP_DURATION")


class Pipeline:
    ''' The constructor method of a class cannot be made asynchronous. 
    To achieve the intended effect, you can use an external async function to instantiate
    the class or an internal async factory method
    Also, it's a dunderscore method, so a double underscore before and after the word'''

    def __init__(self, *args, **kwargs):
        '''
        you have to prefix an instance variable with self
        Otherwise, this function defines the variable and does nothing with it
        '''
        self.default_sleep_duration = kwargs["default_sleep_duration"]

    @classmethod
    async def create(cls, *args, **kwargs):
        self = Pipeline(*args, **kwargs)
        await self.sleep_for(self.default_sleep_duration)
        return self

    # Please replace coro with self to avoid such errors as the last one below
    async def sleep_for(coro, sleep_duration, *args, **kwargs):

        # You neet to await this function for there to be any effect
        await asyncio.sleep(sleep_duration)
        logger.info("Slept for %s seconds", sleep_duration)

        # datetime.now is not a function
        start = datetime.datetime.now()

        # This line makes no sense: coro is basically self, which is the instance of the class, which is not callable
        # await coro(*args, **kwargs)

        end = datetime.datetime.now()
        time_elapsed = (start - end).total_seconds()
        logger.debug(f"Executed the coroutine for {time_elapsed} seconds")


if __name__ == '__main__':
    asyncio.run(Pipeline.create(default_sleep_duration=2))
