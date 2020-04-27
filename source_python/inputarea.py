"""
Medical Gateway Platform - InputArea
====================================

This module is part of the MGP library.
"""



from common import MGPError, NullPipe



class InputArea(object):
    """
    InputArea class
    ===============
    This class provides the functionality of the Input Area. The task of the
    class is to translate information received from sensors and state variables
    to data for the Processing Area.
    """



    class InputHandler(object):
        """
        InputHandler.InputArea class
        ============================
        This class wraps handler chain for Input Area processes. The chain
        consists of a handler and a filter function.
        """



        def __init__(self, handler_type, handler_function, filter_function):
            """
            Intializes the class
            --------------------
            @Params: handler_type       (string)            Type of the handler.
                     handler_function   (callable)          The handler function.
                     filter_function    (callable|NoneType) The filter function
                                                            or None if no filter
                                                            should be applied.
            """

            self.__handler_type = handler_type
            self.__handler = handler_function
            if filter_function is not None:
                self.__filter = filter_function
            else:
                self.__filter = lambda exitobject: exitobject



        def filter(self, exitdata):
            """
            Applies filter on the data
            --------------------------
            @Params: exitdata   (ExitObject)    Data to filter.
            @Return: (ExitObject)               The filtered data.
            """

            return self.__filter(exitdata)



        def gettype(self):
            """
            Gets the type of the handler
            ----------------------------
            @Return: (string)   The type of the handler.
            """

            return self.__handler_type



        def handle(self, rawdata):
            """
            Translates the raw data and applies filter
            ------------------------------------------
            @Params: rawdata    (object)    Data to translate and filter.
            @Return: (ExitObject)           The translated and filtered data.
            """

            return self.__filter(self.__handler(rawdata))



        def justhandle(self, rawdata):
            """
            Translates the raw data without filter
            --------------------------------------
            @Params: rawdata    (object)    Data to translate.
            @Return: (ExitObject)           The translated data.
            """

            return self.__handler(rawdata)



    def __init__(self, flow_pipe=None, data_pipe=None, ui_pipe=None):
        """
        Intializes the class
        --------------------
        @Params: flow_pipe  (PipeConnection)    [optional] Pipe to send data to
                                                the main flow.
                 data_pipe  (PipeConnection)    [optional] Pipe to send data to
                                                the data flow.
                 ui_pipe    (PipeConnection)    [optional] Pipe to send data to
                                                the UI flow.
        """

        self.__events = {}
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



    def is_registered(self, name):
        """
        Checks whether a handler is registered or not
        @Params: name   (stirng)    The name of the handler to check.
        @Return: (bool)             True if name is registered, False if not.
        """

        return name in self.__events



    def read(self, handler_name, rawdata):
        """
        Translates raw data to processable data
        ---------------------------------------
        @Params: handler_name   (string)    The identifier of the handler.
                 rawdata        (object)    The data to be sent to the handler.
        @Throws: MGPError                   When non-existing handler is called.
        """

        if handler_name in self.__events:
            data = self.__events[handler_name].handle(rawdata)
            if data.toflow() is not None:
                self.__to_flow.send(data.toflow())
            if data.todata() is not None:
                self.__to_data.send(data.todata())
            if data.toui() is not None:
                self.__to_ui.send(data.toui())
        else:
            raise MGPError('InputArea.read(): Tried to read for non-existing name "{}".'
                           .format(handler_name))



    def register(self, handler_name, handler_type, handler_function, filter_function=None):
        """
        Registers a handler to an identifier
        ------------------------------------
        @Params: handler_name       (string)    Identifier to register.
                 handler_type       (string)    Type of the handler.
                 handler_function   (callable)  The handler function.
                 filter_function    (callable)  [optional]  The filter function.
        @Throws: MGPError                       When tired to register a new
                                                entry to an existing identifier.
        """

        if handler_name not in self.__events:
            self.__events[handler_name] = InputArea.InputHandler(handler_type,
                                                                handler_function,
                                                                filter_function)
        else:
            raise MGPError('InputArea.register(): Tried to register existing name "{}".'
                           .format(handler_name))



    def unregister(self, handler_name):
        """
        Unregisters a handler
        ---------------------
        @Params: handler_name   (string)    The identifier to delete.
        @Throws: MGPError                   If the identifier doesn't exist.
        """

        if handler_name in self.__events:
            del self.__events[handler_name]
        else:
            raise MGPError('InputArea.unregister(): Tried to unregister non-existing name "{}".'
                           .format(handler_name))
