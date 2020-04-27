#ifndef MGP_DATA_HPP
#define MGP_DATA_HPP

#include <string>
#include "mgp_value.hpp"

/**
 * class MGPData
 * =============
 * 
 * This class holds the content of a data point in the most strict sence.
 * Objects of this class are kind of a read-only instances since
 * "getter functions" are available only. MGPData object are used to hold the
 * content of an event in fact it means a labeled measurement, a labeled
 * decision, a labeled action or a labeled something.
 */
class MGPData {

    private:

    std::string label;
    MGPValue value;
    std::string unit;

    public:

    /**
     * Contructor
     * 
     * @param label The label of the data.
     * @param value The actual value of the data.
     * @param unit  The name of the measurement unit.
     */
    MGPData(std::string label, MGPValue value, std::string unit);

    /**
     * Gets the label of the data
     * 
     * @return  The acutal label.
     */
    std::string getLabel();

    /**
     * Gets the measurement unit of the data
     * 
     * @return  The name of the measurement unit.
     */
    MGPValue getValue();

    /**
     * Gets the value, amount of the data
     * 
     * @return  The value of the measurement or action.
     */
    std::string getUnit();

};

#endif