#ifndef MGP_DATA_ROW_L0_HPP
#define MGP_DATA_ROW_L0_HPP

#include <ctime>
#include <string>
#include "mgp_data.hpp"

class MGPDataRowL0 {

    private:
    
    std::time_t timestamp;
    MGPData data;
    unsigned int equipment_id;
    std::string event_type;
    unsigned char is_filtered;
    unsigned int id;

    public:

    /**
     * Contructor 
     * 
     * @param timestamp     The timestamp when the data was generated.
     * @param data          The actual data to store.
     * @param equipment_id  The ID of the equipment where the data are from.
     * @param event_type    The description of the event connected to the data row.
     */
    MGPDataRowL0(std::time_t timestamp, MGPData data, int equipment_id, std::string event_type);

    /**
     * Finalizes the instance
     * 
     * @param result        ID of the saved record, or -1 if filtered.
     */
    void consume(int result);

    /**
     * Gets the equipment’s ID
     * 
     * @return  The ID of the equipment.
     */
    int getEquipment();

    /**
     * Gets the type of the event
     * 
     * @return  The name of the event type stored in the row.
     */
    std::string getEventType();

    /**
     * Gets the ID of the row
     * 
     * @return  Positive number if the ID of the row already exists, else -1.
     */
    int getId();

    /**
     * Gets the label of the stored data
     * 
     * @return  The acutal label.
     */
    std::string getLabel();

    /**
     * Gets the timestamp of the record
     * 
     * @return  The timestamp.
     */
    std::time_t getTimestamp();

    /**
     * Gets the measurement unit of the stored data
     * 
     * @return  The name of the measurement unit.
     */
    std::string getUnit();

    /**
     * Gets the value, amount of the stored data
     * 
     * @return  The value of the measurement or action.
     */
    MGPData getValue();

    /**
     * Gets whether the object is filtered or not
     * 
     * @return  1 (True) if the row is filtered, 0 (False) if not.
     */
    unsigned char isFiltered();

};

#endif