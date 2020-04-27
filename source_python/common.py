"""
Medical Gateway Platform - common elements
==========================================

This module is part of the MGP library.
"""



class ExitObject(object):
    """
    ExitObject class
    ================
    This class holds the content to send from an area to another. Objects of
    this class are kind of a read-only instances since "getter functions" are
    available only. ExitObject instances are used inside area controllers to
    communicate between handlers, filters and the controller.
    """



    def __init__(self, to_flow, to_data, to_ui):
        """
        Iniializes the class
        --------------------
        @Params: to_flow    (MGPDataRowL*)  Data to send in main flow.
                 to_data    (MGPDataRowL*)  Data to send in data flow.
                 to_ui      (MGPDataRowL*)  Data to send in ui flow.
        """

        self.__to_flow = to_flow
        self.__to_data = to_data
        self.__to_ui = to_ui



    def todata(self):
        """
        Returns the data which is meant to be sent to the data flow
        -----------------------------------------------------------
        @Return: (MGPDataRowL*) Data to be sent.
        """

        return self.__to_data



    def toflow(self):
        """
        Returns the data which is meant to be sent to the main flow
        -----------------------------------------------------------
        @Return: (MGPDataRowL*) Data to be sent.
        """

        return selft.__to_flow



    def toui(self):
        """
        Returns the data which is meant to be sent to the ui flow
        ---------------------------------------------------------
        @Return: (MGPDataRowL*) Data to be sent.
        """

        return self.__to_ui



class MGPData(object):
    """
    MGPData class
    =============
    This class holds the content of a data point in the most strict sense.
    Objects of this class are kind of a read-only instances since
    "getter functions" are available only.  MGPData object are used to hold the
    content of an event in fact it means a labeled measurement, a labeled
    decision, a labeled action or a labeled something.
    """


    def __init__(self, label, value, unit):
        """
        Iniializes the class
        --------------------
        @Params: label  (string)                The label of the data. It describes
                                                what the data actually is, like
                                                source or action.
                 value  (string|int|float|bool) The actual value of the data.
                 unit   (string)                The name of the measurement unit.
        """

        self.__label = label
        self.__value = value
        self.__unit = unit



    def getlabel(self):
        """
        Gets the label of the data
        --------------------------
        @Return: (string)   The acutal label.
        """

        return self.__label



    def getunit(self):
        """
        Gets the measurement unit of the data
        -------------------------------------
        @Return: (string)   The name of the measurement unit.
        """

        return self.__unit



    def getvalue(self):
        """
        Gets the value, amount of the data
        ----------------------------------
        @Return: (string|int|float|bool)    The value of the measurement or action.
        """

        return self.__value



class MGPDataRowL0(object):
    """
    MGPDataRowL0 class
    ==================
    This class holds a Zero Level database record. It acts like a read only data
    container from one side and it is an actual storage handling tool from the
    other side. As a data container it has "getter functions" only and data must
    be set at the instantiation. As a data storage helper tool it can be
    finalized with getting the storage record id or it can be filtered.

    This class has custom implementation of deconstruction. If tried to
    deconstruct without finalization it throws an error.
    """



    def __init__(self, timestamp, data, equipment_id, event_type):
        """
        Initializes the class
        ---------------------
        @Params: timestamp      (time alike)    The timestamp when the data was
                                                generated. Generate a timestamp
                                                as soon as possible to minimize
                                                the delay.
                 data           (MGPData)       The actual data to store.
                 equipment_id   (string)        The ID of the equipment where
                                                the data are from.
                 event_type     (string)        The description of the event
                                                connected to the data row.
        @Throws: MGPError                       When data not instance of MGPData.
        """

        self.__timestamp = timestamp
        if isinstance(data, MGPData):
            self.__data = data
        else:
            raise MGPError('MGPDataRowL0: Parameter data must be instance of MGPData.')
        self.__equipment_id = equipment_id
        self.__evemt_type = event_type
        self.__is_filtered = False
        self.__id = None



    def __del__(self):
        """
        Handles instance's deconstruction
        ---------------------------------
        @Throws MGPError    When instance is not finalized yet.
        """

        if not (self.__is_filtered or slef.__id is not None):
            raise MGPError('MGPDataRowL0: tried to delete a record without use.')



    def finalize(self, result):
        """
        Finalizes the instance
        ----------------------
        @Params: result (int|NoneType)  The result of consumption of the data.
                                        If it is stored, the result is an ID.
                                        If it is filtered, the result should be
                                        NoneType.
        """

        if result is not None:
            self.__id = result
        else:
            slef.__is_filtered = True



    def getequipment(self):
        """
        Gets the equipment’s ID
        -----------------------
        @Return: (string)   The ID of the equipment.
        """

        return self.__equipment_id



    def geteventtype(self):
        """
        Gets the type of the event
        --------------------------
        @Return: (string)   The name of the event type stored in the row.
        """

        return self.__evemt_type



    def getid(self):
        """
        Gets the ID of the row
        ----------------------
        @Return: (int|NoneType) If the ID of the row already exists, it returns
                                it, else it returns None.
        """

        return self.__id



    def getlabel(self):
        """
        Gets the label of the stored data
        ---------------------------------
        @Return: (string)   The acutal label.
        """

        return self.__data.getlabel()



    def getunit(self):
        """
        Gets the measurement unit of the stored data
        --------------------------------------------
        @Return: (string)   The name of the measurement unit.
        """

        return self.__data.getunit()



    def getvalue(self):
        """
        Gets the value, amount of the stored data
        -----------------------------------------
        @Return: (string|int|float|bool)    The value of the measurement or action.
        """

        return self.__data.getvalue()



    def is_filtered(self):
        """
        Gets whether the object is filtered or not
        ------------------------------------------
        @Return: (bool) True if the row is filtered, False if not.
        """

        return self.__is_filtered



class MGPDataRowL1(object):
    """
    MGPDataRowL1 class
    ==================
    This class holds a First Level database record. It acts like a read only data
    container from one side and it is an actual storage handling tool from the
    other side. As a data container it has "getter functions" only and data must
    be set at the instantiation. As a data storage helper tool it can be
    finalized with getting the storage record id or it can be filtered.

    This class has custom implementation of deconstruction. If tried to
    deconstruct without finalization it throws an error.
    """



    def __init__(self, timestamp, data, l0_id=None, patient_id=None, patient_pwd=None):
        """
        Initializes the class
        ---------------------
        @Params: timestamp      (time alike)    The timestamp when the data was
                                                generated. Generate a timestamp
                                                as soon as possible to minimize
                                                the delay.
                 data           (MGPData)       The actual data to store.
                 l0_id          (int)           [optional] The ID of an L0 row
                                                from which the flow is inherited.
                 patient_id     (int)           [optional] The ID of the patient.
                 patient_pwd    (string)        [optional] The password to get
                                                the ID of the patient.
        @Throws: MGPError                       When data not instance of MGPData.
        """

        self.__timestamp = timestamp
        if isinstance(data, MGPData):
            self.__data = data
        else:
            raise MGPError('MGPDataRowL1: Parameter data must be instance of MGPData.')
        self.__l0_id = l0_id
        self.__patient_id = patient_id
        self.__patient_pwd = patient_pwd
        self.__is_filtered = False
        self.__id = None



    def __del__(self):
        """
        Handles instance's deconstruction
        ---------------------------------
        @Throws MGPError    When instance is not finalized yet.
        """

        if not (self.__is_filtered or slef.__id is not None):
            raise MGPError('MGPDataRowL1: tried to delete a record without use.')



    def finalize(self, result):
        """
        Finalizes the instance
        ----------------------
        @Params: result (int|NoneType)  The result of consumption of the data.
                                        If it is stored, the result is an ID.
                                        If it is filtered, the result should be
                                        NoneType.
        """

        if result is not None:
            self.__id = result
        else:
            slef.__is_filtered = True



    def getid(self):
        """
        Gets the ID of the row
        ----------------------
        @Return: (int|NoneType) If the ID of the row already exists, it returns
                                it, else it returns None.
        """

        return self.__id



    def getl0id(self):
        """
        Gets L0 record ID
        -----------------
        @Return: (int|NoneType) If there is an ID of an L0 row from which the
                                flow is inherited, it returns it, else it
                                returns None.
        """

        return self.__l0_id



    def getlabel(self):
        """
        Gets the label of the stored data
        ---------------------------------
        @Return: (string)   The acutal label.
        """

        return self.__data.getlabel()



    def getpatientid(self, patient_pwd=None):
        """
        Gets the patient’s ID
        ---------------------
        @Params: patient_pwd    (string)    The password the get the patient’s ID.
        @Return: (int)                      It returns the ID of the patient if
                                            there is an ID stored and the password
                                            or the lack of password matches the
                                            original setup, else it returns None
        """

        return self.__patient_id if patient_pwd == self.__patient_pwd else None



    def getunit(self):
        """
        Gets the measurement unit of the stored data
        --------------------------------------------
        @Return: (string)   The name of the measurement unit.
        """

        return self.__data.getunit()



    def getvalue(self):
        """
        Gets the value, amount of the stored data
        -----------------------------------------
        @Return: (string|int|float|bool)    The value of the measurement or action.
        """

        return self.__data.getvalue()



    def is_filtered(self):
        """
        Gets whether the object is filtered or not
        ------------------------------------------
        @Return: (bool) True if the row is filtered, False if not.
        """

        return self.__is_filtered



class MGPDataRowL2(object):
    """
    MGPDataRowL2 class
    ==================
    This class holds a Second Level database record. It acts like a read only data
    container from one side and it is an actual storage handling tool from the
    other side. As a data container it has "getter functions" only and data must
    be set at the instantiation. As a data storage helper tool it can be
    finalized with getting the storage record id or it can be filtered.

    This class has custom implementation of deconstruction. If tried to
    deconstruct without finalization it throws an error.
    """



    def __init__(self, timestamp, data_ch1, data_ch2, l1_id=None):
        """
        Initializes the class
        ---------------------
        @Params: timestamp      (time alike)    The timestamp when the data was
                                                generated. Generate a timestamp
                                                as soon as possible to minimize
                                                the delay.
                 data_ch1       (MGPData)       Data from channel 1 (processed
                                                source).
                 data_ch2       (MGPData)       Data from channel 2 (automated
                                                source).
                 l1_id          (int)           [optional] The ID of an L1 row
                                                from which the flow is inherited.
        @Throws: MGPError                       When data not instance of MGPData.
        """

        self.__timestamp = timestamp
        if isinstance(data_ch1, MGPData) or data_ch1 is None:
            self.__data_ch1 = data_ch1
        else:
            raise MGPError('MGPDataRowL2: Parameter data channel #1 must be instance of MGPData or NoneType.')
        if isinstance(data_ch2, MGPData) or data_ch2 is None:
            self.__data_ch1 = data_ch2
        else:
            raise MGPError('MGPDataRowL2: Parameter data channel #2 must be instance of MGPData or NoneType.')
        self.__l1_id = l1_id
        self.__is_filtered = False
        self.__id = None



    def __del__(self):
        """
        Handles instance's deconstruction
        ---------------------------------
        @Throws MGPError    When instance is not finalized yet.
        """

        if not (self.__is_filtered or slef.__id is not None):
            raise MGPError('MGPDataRowL0: tried to delete a record without use.')



    def finalize(self, result):
        """
        Finalizes the instance
        ----------------------
        @Params: result (int|NoneType)  The result of consumption of the data.
                                        If it is stored, the result is an ID.
                                        If it is filtered, the result should be
                                        NoneType.
        """

        if result is not None:
            self.__id = result
        else:
            slef.__is_filtered = True



    def getid(self):
        """
        Gets the ID of the row
        ----------------------
        @Return: (int|NoneType) If the ID of the row already exists, it returns
                                it, else it returns None.
        """

        return self.__id



    def getl1id(self):
        """
        Gets L1 record ID
        -----------------
        @Return: (int|NoneType) If there is an ID of an L1 row from which the
                                flow is inherited, it returns it, else it
                                returns None.
        """

        return self.__l1_id



    def getlabel(self, channel):
        """
        Gets the label of the stored data
        ---------------------------------
        @Params: channel    (int)   The ID of the channel to get label from.
        @Return: (string)           The actual label.
        @Throws: MGPError           When non existing channel ID is given.
        """

        if channel == 1:
            return self.__data_ch1.getlabel()
        elif channel == 2:
            return self.__data_ch2.getlabel()
        else:
            raise MGPError('MGPDataRowL2.getlabel(): channel "{}" is not supported.'
                           .format(channel))



    def getunit(self, channel):
        """
        Gets the measurement unit of the stored data
        --------------------------------------------
        @Params: channel    (int)   The ID of the channel to get unit from.
        @Return: (string)           The name of the measurement unit.
        @Throws: MGPError           When non existing channel ID is given.
        """

        if channel == 1:
            return self.__data_ch1.getunit()
        elif channel == 2:
            return self.__data_ch2.getunit()
        else:
            raise MGPError('MGPDataRowL2.getunit(): channel "{}" is not supported.'
                           .format(channel))



    def getvalue(self, channel):
        """
        Gets the value, amount of the stored data
        -----------------------------------------
        @Params: channel    (int)   The ID of the channel to get value from.
        @Return: (string|int|float) The value of the measurement or action.
        @Throws: MGPError           When non existing channel ID is given.
        """

        if channel == 1:
            return self.__data_ch1.getvalue()
        elif channel == 2:
            return self.__data_ch2.getvalue()
        else:
            raise MGPError('MGPDataRowL2.getvalue(): channel "{}" is not supported.'
                           .format(channel))



    def is_filtered(self):
        """
        Gets whether the object is filtered or not
        ------------------------------------------
        @Return: (bool) True if the row is filtered, False if not.
        """

        return self.__is_filtered



class MGPDataRowL3(object):
    """
    MGPDataRowL3 class
    ==================
    This class holds a Third Level database record. It acts like a read only data
    container from one side and it is an actual storage handling tool from the
    other side. As a data container it has "getter functions" only and data must
    be set at the instantiation. As a data storage helper tool it can be
    finalized with getting the storage record id or it can be filtered.

    This class has custom implementation of deconstruction. If tried to
    deconstruct without finalization it throws an error.
    """



    def __init__(self, timestamp, l2_id, response):
        """
        Initializes the class
        ---------------------
        @Params: timestamp  (time alike)    The timestamp when the data was
                                            generated. Generate a timestamp as
                                            soon as possible to minimize the
                                            delay.
                 l2_id      (int)           The ID of an L2 row from which the
                                            flow is inherited.
                 response   (string)        The response resulted from L2 record.
        """

        self.__timestamp = timestamp
        self.__l2_id = l2_id
        self.__response = response
        self.__is_filtered = False
        self.__id = None



    def __del__(self):
        """
        Handles instance's deconstruction
        ---------------------------------
        @Throws MGPError    When instance is not finalized yet.
        """

        if not (self.__is_filtered or slef.__id is not None):
            raise MGPError('MGPDataRowL0: tried to delete a record without use.')



    def finalize(self, result):
        """
        Finalizes the instance
        ----------------------
        @Params: result (int|NoneType)  The result of consumption of the data.
                                        If it is stored, the result is an ID.
                                        If it is filtered, the result should be
                                        NoneType.
        """

        if result is not None:
            self.__id = result
        else:
            slef.__is_filtered = True



    def getid(self):
        """
        Gets the ID of the row
        ----------------------
        @Return: (int|NoneType) If the ID of the row already exists, it returns
                                it, else it returns None.
        """

        return self.__id



    def getl2id(self):
        """
        Gets L2 record ID
        -----------------
        @Return: (int)  The ID of the L2 row from which the flow is inherited.
        """

        return self.__l2_id



    def getresponse(self):
        """
        Gets the stored response
        ------------------------
        @Return: (string)   The content of the stored response.
        """

        return self.__response



    def is_filtered(self):
        """
        Gets whether the object is filtered or not
        ------------------------------------------
        @Return: (bool) True if the row is filtered, False if not.
        """

        return self.__is_filtered



class MGPError(Exception):
    """
    MGPError class
    ==============
    This class provides unique error interface for Medical Gateway Platform. It
    is a subclass of Exception. It doesn’t have any additional behavior than its
    parent.
    """



    pass




class MGPFilter(object):
    """
    MGPFilter class
    ===============
    This class is a wrapper class for custom filter functions. It is kind of a
    read-only wrapper since attributes cannot be set run-time.
    """



    def __init__(self, rule_function, filter_type):
        """
        Initializes the class
        ---------------------
        @Params: rule_function  (callable)  A function that is called to be used
                                            as a filter. However this class
                                            supports the freedom to accept
                                            positional and keyword arguments,
                                            it’s highly recommended to accept
                                            ExitObject as first argument in the
                                            function.
                 filter_type    (string)    The identifier of the filter.
        """

        self.__rule = rule_function
        self.__filter_type = filter_type



    def apply(self, *args, **kwargs):
        """
        Calls rule function and returns its result
        ------------------------------------------
        @Params: (object[s])    Parameters to be transferred to rule function.
        @Return: (ExitObject)   The result of filtering process.
        """

        return self.__rule(*args, **kwargs)



    def gettype(self):
        """
        Gets the given type identifier of the filter
        --------------------------------------------
        @Return: (string)   The type identifier of the filter.
        """

        return self.__filter_type



class NullPipe(object):
    """
    NullPipe class
    ==============
    This class provides endpoint-less alternative to multiprocessing.PipeConnection
    class sending functionality. The goal of the class is to speed up the workflow
    of the areas since no if junctions are needed to filter non-running data flows.
    """



    def send(self, arg):
        """
        Does nothing
        ------------
        @Params: arg    (object)    Data to ignore.
        """

        pass
