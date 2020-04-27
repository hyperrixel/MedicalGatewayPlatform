"""
Medical Gateway Platform - ProcessArea
======================================

This module is part of the MGP library.
"""



from common import MGPError, NullPipe
from time import sleep, time_ns



class ProcessArea(object):
    """
    ProcessArea class
    =================
    This class provides the functionality of the Processing Area. The task of
    the class is to maintain a loop where input data gets processed and sent to
    Area of Gates and other to other flows as well.
    """



    def __init__(self, flow_source, processor_function, loop_interval=100,
                 flow_pipe=None, data_pipe=None, ui_pipe=None):
        """
        Intializes the class
        --------------------
        @Params: flow_source        (PipeConnection)    The pipe where source
                                                        data come from.
                 processor_function (callable)          Callable function to
                                                        process input data.
                                                        Every data gets processed
                                                        with the same function.
                                                    data gating.
                 loop_interval      (int)               [optional] Time in
                                                        milliseconds between
                                                        cycles.
                 flow_pipe          (PipeConnection)    [optional] Pipe to send
                                                        data to the main flow.
                 data_pipe          (PipeConnection)    [optional] Pipe to send
                                                        data to the data flow.
                 ui_pipe            (PipeConnection)    [optional] Pipe to send
                                                        data to the UI flow.
        @Throws: MGPError                               When flow_source is not
                                                        instance of PipeConnection.
                                                        When processor_function
                                                        is not callable.
        """

        if flow_source.__class__.__name__ == 'PipeConnection':
            self.__flow_source = flow_source
        else:
            raise MGPError('ProcessArea: Pipe for main workflow must be instance of PipeConnection but is "{}".'.format(flow_source.__class__.__name__))
        if callable(processor_function):
            self.__processor_function = processor_function
        else:
            raise MGPError('ProcessArea: Parameter for processor function must be at least callable.')
        self.__loop_interval = loop_interval / 1000
        if flow_pipe is not None:
            self.__to_flow = flow_pipe
        else:
            self.__to_flow = NullPipe()
        if data_pipe is not None:
            self.__to_data = data_pipe
        else:
            self.__to_data = NullPipe()
        if ui_pipe is not None:
            self.__to_ui = ui_pipe
        else:
            self.__to_ui = NullPipe()
        self.__do_loop = False



    def loopinterval(self, new_value=None):
        """
        Gets or sets the value of loop interval
        ---------------------------------------
        @Params: new_value  (int)   [optional] The new interval in milliseconds.
        """

        if new_value is not None:
            self.__loop_interval = loop_interval
        else:
            return self.__loop_interval



    def start(self):
        """
        Handles main loop
        -----------------
        """

        self.__do_loop = True
        while self.__do_loop:
            cycle_start = time_ns()
            new_data = []
            while self.__flow_source.poll():
                element = self.__flow_source.recv()
                new_data.append(element)
            if len(new_data) > 0:
                data = self.__processor_function(new_data)
                if data.toflow() is not None:
                    self.__to_flow.send(data.toflow())
                if data.todata() is not None:
                    self.__to_data.send(data.todata())
                if data.toui() is not None:
                    self.__to_ui.send(data.toui())
            sleep_interval = self.__loop_interval - ((time_ns() - cycle_start) / 1000000000)
            if sleep_interval > 0:
                sleep(sleep_interval)
