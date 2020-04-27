"""
Medical Gateway Platform - OutputArea
=====================================

This module is part of the MGP library.
"""



from common import MGPDataRowL2, MGPError, NullPipe



class OutputArea(object):
    """
    OutputArea class
    ================
    This class provides the functionality of the Output Area. The task of the
    class is to translate information received from the Area of Gate to commands
    that the actuators understand.
    """



    class OutputHandler(object):
        """
        OutputArea.OutputHandler class
        ==============================
        This class wraps handler chain for Output Area processes. The chain
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



        def handle(self, data):
            """
            Translates the data and applies filter
            --------------------------------------
            @Params: data   (ExitObject)    Data to translate and filter.
            @Return: (ExitObject)           The translated and filtered data.
            """

            return self.__filter(self.__handler(rawdata))



        def justhandle(self, rawdata):
            """
            Translates the data without filter
            ----------------------------------
            @Params: data   (ExitObject)    Data to translate.
            @Return: (ExitObject)           The translated data.
            """

            return self.__handler(rawdata)



    def __init__(self, data_pipe=None, ui_pipe=None):
        """
        Intializes the class
        --------------------
        @Params: data_pipe  (PipeConnection)    [optional] Pipe to send data to
                                                the data flow.
                 ui_pipe    (PipeConnection)    [optional] Pipe to send data to
                                                the UI flow.
        """

        self.__actions = {}
        if data_pipe is not None:
            self.__to_data = data_pipe
        else:
            self.__to_data = NullPipe()
        if ui_pipe is not None:
            self.__to_ui = ui_pipe
        else:
            self.__to_ui = NullPipe()



    def act(self, handler_name, data):
        """
        Translates gate action to data for actuator
        -------------------------------------------
        @Params: handler_name   (string)    The identifier of the handler.
                 data           (MGPData)   The data to be sent to the handler.
        @Throws: MGPError                   When non-existing handler is called.
                                            When data is not instance of MGPData.
        """

        if handler_name in self.__events:
            if isinstance(data, MGPDataRowL2):
                finaldata = self.__actions[handler_name].handle(data)
                if finaldata.todata() is not None:
                    self.__to_data.send(finaldata.todata())
                if finaldata.toui() is not None:
                    self.__to_ui.send(finaldata.toui())
            else:
                raise MGPError('OutputArea.act(): Action data must be instance of MGPData but is "{}".'
                               .format(data.__class__.__name__))
        else:
            raise MGPError('OutputArea.act(): Tried to read for non-existing name "{}".'
                           .format(handler_name))



    def is_registered(self, name):
        """
        Checks whether a handler is registered or not
        @Params: name   (stirng)    The name of the handler to check.
        @Return: (bool)             True if name is registered, False if not.
        """

        return name in self.__actions



    def register(self, handler_name, handler_type, handler_function,
                 filter_function=None):
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

        if handler_name not in self.__actions:
            self.__actions[handler_name] = OutputArea.OutputHandler(handler_type,
                                                                    handler_function,
                                                                    filter_function)
        else:
            raise MGPError('OutputArea.register(): Tried to register existing name "{}".'
                           .format(handler_name))



    def unregister(self, handler_name):
        """
        Unregisters a handler
        ---------------------
        @Params: handler_name   (string)    The identifier to delete.
        @Throws: MGPError                   If the identifier doesn't exist.
        """

        if handler_name in self.__actions:
            del self.__actions[handler_name]
        else:
            raise MGPError('OutputArea.unregister(): Tried to unregister non-existing name "{}".'
                           .format(handler_name))
