"""
Medical Gateway Platform - AreaOfGates
===================================

This module is part of the MGP library.
"""



from common import MGPDataRowL2
from time import sleep, time, time_ns



class AreaOfGates(object):
    """
    AreaOfGates class
    =================
    This class provides the functionality of the Area Of Gates. The task of the
    class is to maintain a loop where processed and automation data is handled
    together to decide whether to output something to an actuator or not.

    Handler functions of gating must always send output to each label that is
    handled by the Area of Gate. The class, as a parent of those handler objects
    copies all the registered labels to .gates member of the handlers. The
    channel 1 handler must have an .eval() function and the channel 2 handler
    must have a .tick() function. The output of both functions should be a tuple.
    The first element of the tuple should be a dictionary of
    AreaOfGates.GateObject alike objects with all the keys from the gates list.
    """



    class GateObject(object):
        """
        AreaOfGates.GateObject class
        ============================
        This class stores the result of a single gate label process from channel
        1 or channel 2. The use of this simple class is not necessary but it
        shows the minimal required setup of a class to be used for this purpose.
        No additional check is included since object of this class has minimum
        life-cycle, they  get instantiated and deleted almost countless.
        """



        def __init__(self, open, data):
            """
            Intializes the class
            --------------------
            @Params: open   (bool)      Whether to open the gate or not.
                     data   (MGPData)   Data to be transferred through the gate.
            """

            self.open = open
            self.data = data



    __GATE_TYPES = ['P OR A (P)', 'P OR A (A)', 'P AND A (P)', 'P AND A (A)',
                    'P XOR A', 'P > A', 'P < A', 'P ONLY', 'ONLY A']



    def __logic_and_a(ch1, ch2, ch1data, ch2data):
        """
        Performs logic P AND A (A)
        --------------------------
        @Params ch1     (bool)      Whether channel 1 asks for opening or not.
                ch2     (bool)      Whether channel 2 asks for opening or not.
                ch1data (MGPData)   Data from channel 1.
                ch2data (MGPData)   Data from channel 2.
        """

        if ch1 and ch2:
            return (True, ch2data)
        else:
            return (False, None)



    def __logic_and_p(ch1, ch2, ch1data, ch2data):
        """
        Performs logic P AND A (P)
        --------------------------
        @Params ch1     (bool)      Whether channel 1 asks for opening or not.
                ch2     (bool)      Whether channel 2 asks for opening or not.
                ch1data (MGPData)   Data from channel 1.
                ch2data (MGPData)   Data from channel 2.
        """

        if ch1 and ch2:
            return (True, ch1data)
        else:
            return (False, None)



    def __logic_or_a(ch1, ch2, ch1data, ch2data):
        """
        Performs logic P OR A (A)
        -------------------------
        @Params ch1     (bool)      Whether channel 1 asks for opening or not.
                ch2     (bool)      Whether channel 2 asks for opening or not.
                ch1data (MGPData)   Data from channel 1.
                ch2data (MGPData)   Data from channel 2.
        """

        if ch1 and ch2:
            return (True, ch2data)
        elif ch1:
            return (True, ch1data)
        elif ch2:
            return (True, ch2data)
        else:
            return (False, None)



    def __logic_or_p(ch1, ch2, ch1data, ch2data):
        """
        Performs logic P OR A (P)
        -------------------------
        @Params ch1     (bool)      Whether channel 1 asks for opening or not.
                ch2     (bool)      Whether channel 2 asks for opening or not.
                ch1data (MGPData)   Data from channel 1.
                ch2data (MGPData)   Data from channel 2.
        """

        if ch1 and ch2:
            return (True, ch1data)
        elif ch1:
            return (True, ch1data)
        elif ch2:
            return (True, ch2data)
        else:
            return (False, None)



    def __logic_only_a(ch1, ch2, ch1data, ch2data):
        """
        Performs logic ONLY A
        ---------------------
        @Params ch1     (bool)      Whether channel 1 asks for opening or not.
                ch2     (bool)      Whether channel 2 asks for opening or not.
                ch1data (MGPData)   Data from channel 1.
                ch2data (MGPData)   Data from channel 2.
        """

        if ch2:
            return (True, ch2data)
        else:
            return (False, None)



    def __logic_only_p(ch1, ch2, ch1data, ch2data):
        """
        Performs logic P ONLY
        ---------------------
        @Params ch1     (bool)      Whether channel 1 asks for opening or not.
                ch2     (bool)      Whether channel 2 asks for opening or not.
                ch1data (MGPData)   Data from channel 1.
                ch2data (MGPData)   Data from channel 2.
        """

        if ch1:
            return (True, ch1data)
        else:
            return (False, None)



    def __logic_p_g_a(ch1, ch2, ch1data, ch2data):
        """
        Performs logic P > A
        --------------------
        @Params ch1     (bool)      Whether channel 1 asks for opening or not.
                ch2     (bool)      Whether channel 2 asks for opening or not.
                ch1data (MGPData)   Data from channel 1.
                ch2data (MGPData)   Data from channel 2.
        """

        if ch1:
            return (True, ch1data)
        elif ch1 is False:
            return (False, None)
        elif ch2:
            return (True, ch2data)
        else:
            return (False, None)



    def __logic_p_l_a(ch1, ch2, ch1data, ch2data):
        """
        Performs logic P < A
        --------------------
        @Params ch1     (bool)      Whether channel 1 asks for opening or not.
                ch2     (bool)      Whether channel 2 asks for opening or not.
                ch1data (MGPData)   Data from channel 1.
                ch2data (MGPData)   Data from channel 2.
        """

        if ch2:
            return (True, ch2data)
        elif ch2 is False:
            return (False, None)
        elif ch1:
            return (True, ch1data)
        else:
            return (False, None)



    def __logic_xor(ch1, ch2, ch1data, ch2data):
        """
        Performs logic P XOR A
        ----------------------
        @Params ch1     (bool)      Whether channel 1 asks for opening or not.
                ch2     (bool)      Whether channel 2 asks for opening or not.
                ch1data (MGPData)   Data from channel 1.
                ch2data (MGPData)   Data from channel 2.
        """

        if ch1 and ch2:
            return (False, None)
        elif ch1:
            return (True, ch1data)
        elif ch2:
            return (True, ch2data)
        else:
            return (False, None)



    def __init__(self, flow_source, outputarea, ch1, ch2, gatelogics,
                 loop_interval=100, data_pipe=None, ui_pipe=None):
        """
        Intializes the class
        --------------------
        @Params: flow_source    (PipeConnection)    The pipe where source data
                                                    come from.
                 outputarea     (OutputArea)        The instance of Output Area
                                                    where actuator functionality
                                                    is implemented.
                 ch1            (object)            Handler object for processed
                                                    data gating.
                 ch2            (object)            Handler object for automated
                                                    gating.
                 gatelogics     (dict)              Dictionary of gate logics.
                                                    Key must be the gates to
                                                    register and values must be
                                                    the logic identifier of the
                                                    gate.
                 loop_interval  (int)               [optional] Time in milliseconds
                                                    between cycles.
                 data_pipe      (PipeConnection)    [optional] Pipe to send
                                                    data to the data flow.
                 ui_pipe        (PipeConnection)    [optional] Pipe to send
                                                    data to the UI flow.
        @Throws: MGPError                           When flow_source is not
                                                    instance of PipeConnection.
                                                    When outputarea is not
                                                    instance of OutputArea.
                                                    When ch1 doesn't have a
                                                    callable member .eval().
                                                    When ch2 doesn't have a
                                                    callable member .tick().
                                                    When gatelogics contains non
                                                    existing gate logic string.
        """

        if flow_source.__class__.__name__ == 'PipeConnection':
            self.__flow_source = flow_source
        else:
            raise MGPError('AreaOfGates: Pipe for main workflow must be instance of PipeConnection but is "{}".'
                           .format(flow_source.__class__.__name__))
        if outputarea.__class__.__name__ == 'OutputArea':
            self.__output_area = flow_source
        else:
            raise MGPError('AreaOfGates: Object of Output Area must be instance of OutputArea but is "{}".'
                           .format(outputarea.__class__.__name__))
        if callable(getattr(ch1, 'eval')):
            self.__ch1 = ch1
        else:
            raise MGPError('AreaOfGates: Channel 1 object must have a callable member "eval".')
        if callable(getattr(ch2, 'tick')):
            self.__ch2 = ch2
        else:
            raise MGPError('AreaOfGates: Channel 2 object must have a callable member "tick".')
        self.__gates = {}
        self.__empty_results = {}
        for key, value in gatelogics.items():
            if value not in AreaOfGates.__GATE_TYPES:
                self.showimplemented()
                raise MGPError('AreaOfGates: Logic "{}" at label "{}" is not valid or not implemented.'
                               .format(key, value))
            else:
                if value == 'P OR A (P)':
                    self.__gates[key] = AreaOfGates.__logic_or_p
                elif value == 'P OR A (A)':
                    self.__gates[key] = AreaOfGates.__logic_or_a
                elif value == 'P AND A (P)':
                    self.__gates[key] = AreaOfGates.__logic_and_p
                elif value == 'P AND A (A)':
                    self.__gates[key] = AreaOfGates.__logic_and_a
                elif value == 'P XOR A':
                    self.__gates[key] = AreaOfGates.__logic_xor
                elif value == 'P > A':
                    self.__gates[key] = AreaOfGates.__logic_p_g_a
                elif value == 'P < A':
                    self.__gates[key] = AreaOfGates.__logic_p_l_a
                elif value == 'P ONLY':
                    self.__gates[key] = AreaOfGates.__logic_only_p
                elif value == 'ONLY A':
                    self.__gates[key] = AreaOfGates.__logic_only_a
                self.__empty_results[key] = (False, None)
        keylist = list(self.__gates.keys())
        self.__ch1.gates = keylist.copy()
        self.__ch2.gates = keylist.copy()
        self.__loop_interval = loop_interval / 1000
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



    def showimplemented(self):
        """
        Prints implemented get logic identifiers
        ----------------------------------------
        """

        print('Implemented AreaOfGates logics are:')
        for logic in AreaOfGates.__GATE_TYPES:
            print('   {}'.format(logic))



    def start(self):
        """
        Handles main loop
        -----------------
        """

        self.__do_loop = True
        self.__start_ns = time_ns()
        self.__ch2_ns = time_ns()
        self.__journal = []
        while self.__do_loop:
            cycle_start = time_ns()
            new_data = []
            while self.__flow_source.poll():
                element = self.__flow_source.recv()
                new_data.append(element)
                self.__journal.append(element)
            if len(new_data) > 0:
                ch1_data, clear = self.__ch1(new_data, self.__journal)
                if clear:
                    del self.__journal[:]
            else:
                ch1_data = self.__empty_results.copy()
            ch2_data, clear = self.__ch2.tick(self.__start_ns, self.__ch2_ns)
            if clear:
                self.__ch2_ns = time_ns()
            for key, keyfunction in self.__gates.items():
                open, data = keyfunction(ch1_data[key].open, ch2_data[key].open, ch1_data[key].data, ch2_data[key].data)
                if open:
                    outputarea.act(key, data)
                    row = MGPDataRowL2(time(), ch1_data, ch2_data)
                    self.__to_data.send(row)
                    self.__to_ui.send(row)
            sleep_interval = self.__loop_interval - ((time_ns() - cycle_start) / 1000000000)
            if sleep_interval > 0:
                sleep(sleep_interval)
