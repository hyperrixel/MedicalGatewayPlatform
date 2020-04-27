"""
Medical Gateway Platform - DataArea
===================================

This module is part of the MGP library.
"""



from common import MGPError, NullPipe
from time import sleep, time_ns



class DataArea(object):
    """
    DataArea class
    ==============
    This class provides the whole functionality of the Data Area. The task of
    this class is to store and retrieve data with the help of the database
    manager engine selected by the user.

    Member “engine” is class level variable. It provides the singleton-like
    functionality. However in Python DataArea.engine member could be called
    straight. To maintain a clean coding style it’s strongly recommended to use
    DataArea’s loop for data management.
    """



    class __DataAreaEngine(object):
        """
        DataArea.__DataAreaEngine class
        ===============================
        This class provides a wrapper for a DataArea.__EngineCSV,
        DataArea.__EngineDoF or  DataArea.__EngineSQL engine, which serves the
        actual data storage handling. The use of a wrapper has advantages in
        simplification of type check and involves a future possibility to
        improve the data management process workflow. The workflow itself
        consists of basic data storage functionality based on CRUD model.
        """



        def __init__(self, engine):
            """
            Initializes the class
            ---------------------
            @Params: engine (DataArea.__Engine***)  The instance of engine to
                                                    work with.
            """

            self.__engine = engine



        def create(self, level_id, record):
            """
            Wraps the engine's create() function
            ------------------------------------
            @Params: level_id   (int)           The identifier of the storage level.
                     record     (MGPDataRowL*)  The data to store.
            @Return: (int)                      The ID of the record or -1 in case of
                                                failure.
            """

            return self.__engine.create(level_id, record)



        def delete(self, level_id, record_id):
            """
            Wraps the engine's delete() function
            ------------------------------------
            @Params: level_id   (int)   The identifier of the storage level.
                     record_id  (int)   The ID of the record.
            @Return: (bool)             True if succeed, False if failed.
            """

            return self.__engine.delete(level_id, record_id)



        def read(self, level_id, record_id):
            """
            Wraps the engine's read() function
            ----------------------------------
            @Params: level_id   (int)   The identifier of the storage level.
                     record_id  (int)   The ID of the record.
            @Return: (MGPDataRowL*)     Data if succeed, False if failed.
            """

            return self.__engine.read(level_id, record_id)



        def update(self, level_id, record_id, record):
            """
            Wraps the engine's update() function
            ------------------------------------
            @Params: level_id   (int)           The identifier of the storage level.
                     record_id  (int)           The ID of the record.
                     record     (MGPDataRowL*)  The data to update.
            @Return: (bool)                     True if succeed, False if failed.
            """

            return self.__engine.update(level_id, record_id, record)



    class __EngineCSV(object):
        """
        This class provides CSV endpoint to the data management workflow. The
        engine realizes basic data storage functionality based on CRUD model.
        """



        def __init__(self, configdict):
            """
            Initializes the class
            ---------------------
            @Params: configdict (dict)  Settings to instantiate engine.
            """

            pass



        def create(self, level_id, record):
            """
            Creates a new record in the database
            ------------------------------------
            @Params: level_id   (int)           The identifier of the storage level.
                     record     (MGPDataRowL*)  The data to store.
            @Return: (int)                      The ID of the record or -1 in case of
                                                failure.
            """

            return -1



        def delete(self, level_id, record_id):
            """
            Deletes a record from the database
            ----------------------------------
            @Params: level_id   (int)   The identifier of the storage level.
                     record_id  (int)   The ID of the record.
            @Return: (bool)             True if succeed, False if failed.
            """

            return False



        def read(self, level_id, record_id):
            """
            Reads a record from the database
            --------------------------------
            @Params: level_id   (int)   The identifier of the storage level.
                     record_id  (int)   The ID of the record.
            @Return: (MGPDataRowL*)     Data if succeed, False if failed.
            """

            return False



        def update(self, level_id, record_id, record):
            """
            Updates a record in the database
            --------------------------------
            @Params: level_id   (int)           The identifier of the storage level.
                     record_id  (int)           The ID of the record.
                     record     (MGPDataRowL*)  The data to update.
            @Return: (bool)                     True if succeed, False if failed.
            """

            return False



    class __EngineDoF(object):
        """
        This class provides DoF endpoint to the data management workflow. The
        engine realizes basic data storage functionality based on CRUD model.
        """



        def __init__(self, configdict):
            """
            Initializes the class
            ---------------------
            @Params: configdict (dict)  Settings to instantiate engine.
            """

            pass



        def create(self, level_id, record):
            """
            Creates a new record in the database
            ------------------------------------
            @Params: level_id   (int)           The identifier of the storage level.
                     record     (MGPDataRowL*)  The data to store.
            @Return: (int)                      The ID of the record or -1 in case of
                                                failure.
            """

            return -1



        def delete(self, level_id, record_id):
            """
            Deletes a record from the database
            ----------------------------------
            @Params: level_id   (int)   The identifier of the storage level.
                     record_id  (int)   The ID of the record.
            @Return: (bool)             True if succeed, False if failed.
            """

            return False



        def read(self, level_id, record_id):
            """
            Reads a record from the database
            --------------------------------
            @Params: level_id   (int)   The identifier of the storage level.
                     record_id  (int)   The ID of the record.
            @Return: (MGPDataRowL*)     Data if succeed, False if failed.
            """

            return False



        def update(self, level_id, record_id, record):
            """
            Updates a record in the database
            --------------------------------
            @Params: level_id   (int)           The identifier of the storage level.
                     record_id  (int)           The ID of the record.
                     record     (MGPDataRowL*)  The data to update.
            @Return: (bool)                     True if succeed, False if failed.
            """

            return False



    class __EngineSQL(object):
        """
        This class provides SQL endpoint to the data management workflow. The
        engine realizes basic data storage functionality based on CRUD model.
        """



        def __init__(self, configdict):
            """
            Initializes the class
            ---------------------
            @Params: configdict (dict)  Settings to instantiate engine.
            """

            pass



        def create(self, level_id, record):
            """
            Creates a new record in the database
            ------------------------------------
            @Params: level_id   (int)           The identifier of the storage level.
                     record     (MGPDataRowL*)  The data to store.
            @Return: (int)                      The ID of the record or -1 in case of
                                                failure.
            """

            return -1



        def delete(self, level_id, record_id):
            """
            Deletes a record from the database
            ----------------------------------
            @Params: level_id   (int)   The identifier of the storage level.
                     record_id  (int)   The ID of the record.
            @Return: (bool)             True if succeed, False if failed.
            """

            return False



        def read(self, level_id, record_id):
            """
            Reads a record from the database
            --------------------------------
            @Params: level_id   (int)   The identifier of the storage level.
                     record_id  (int)   The ID of the record.
            @Return: (MGPDataRowL*)     Data if succeed, False if failed.
            """

            return False



        def update(self, level_id, record_id, record):
            """
            Updates a record in the database
            --------------------------------
            @Params: level_id   (int)           The identifier of the storage level.
                     record_id  (int)           The ID of the record.
                     record     (MGPDataRowL*)  The data to update.
            @Return: (bool)                     True if succeed, False if failed.
            """

            return False



    __STORAGE_TYPES = ['DoF', 'CSV', 'SQL']



    engine = None # Class level variable for singleton instance



    def __init__(self, storage_type, configdict, data_source,
                 loop_interval=5000, ui_pipe=None):
        """
        Intializes the class
        --------------------
        @Params: storage_type   (string)            Type of the selected storage
                                                    method. Must be one of the
                                                    implemented types.
                 configdict     (dict)              Key value pair based settings
                                                    according to the needs of the
                                                    selected storing engine.
                 data_source    (PipeConnection)    The pipe where source data
                                                    come from.
                 loop_interval  (int)               Time in milliseconds between
                                                    cycles.
                 ui_pipe        (PipeConnection)    Pipe to send data to the UI
                                                    flow.
        @Throws: MGPError                           When storage type is not
                                                    implemented or doesn't exist.
                                                    When data source is not
                                                    instance of PipeConnection.
        """

        if not isinstance(DataArea.engine, DataArea.__DataAreaEngine):
            if storage_type in DataArea.__STORAGE_TYPES:
                if storage_type == 'DoF':
                    DataArea.engine = DataArea.__DataAreaEngine(DataArea.__EngineDof(configdict))
                elif storage_type == 'CSV':
                    DataArea.engine = DataArea.__DataAreaEngine(DataArea.__EngineCSV(configdict))
                elif storage_type == 'SQL':
                    DataArea.engine = DataArea.__DataAreaEngine(DataArea.__EngineSQL(configdict))
            else:
                self.showimplemented()
                raise MGPError('DataArea: Storage "{}" is not valid or not implemented.'
                               .format(storage_type))
            if data_source.__class__.__name__ == 'PipeConnection':
                self.__data_source = data_source
            else:
                raise MGPError('DataArea: Pipe for data source must be instance of PipeConnection but is "{}".'
                               .format(data_source.__class__.__name__))
            self.__loop_interval = loop_interval / 1000
            if ui_pipe is not None:
                self.__to_ui = ui_pipe
            else:
                self.__to_ui = NullPipe()
            self.__do_loop = False


    @classmethod
    def hasengine(cls):
        """
        Gets whether DataArea has an engine or not
        ------------------------------------------
        @Return: (bool) True if engine is instantiated, False else.
        """

        return isinstance(cls.engine, DataArea.__DataAreaEngine)



    def showimplemented(self):
        """
        Prints implemented storage identifiers
        --------------------------------------
        """

        print('Implemented DataArea storages are:')
        for storage in DataArea.__STORAGE_TYPES:
            print('   {}'.format(storage))



    def start(self):
        """
        Handles main loop
        -----------------
        """

        self.__do_loop = True
        while self.__do_loop:
            cycle_start = time_ns()
            while self.__data_source.poll():
                element = self.__data_source.recv()
                if element.__class__.__name__ == 'MGPDataRowL0':
                    DataArea.engine.create(0, element)
                elif element.__class__.__name__ == 'MGPDataRowL1':
                    DataArea.engine.create(1, element)
                elif element.__class__.__name__ == 'MGPDataRowL2':
                    DataArea.engine.create(2, element)
                elif element.__class__.__name__ == 'MGPDataRowL3':
                    DataArea.engine.create(3, element)
            if len(new_data) > 0:
                pass
            sleep_interval = self.__loop_interval - ((time_ns() - cycle_start) / 1000000000)
            if sleep_interval > 0:
                sleep(sleep_interval)
