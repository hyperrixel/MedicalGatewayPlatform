#ifndef EXIT_OBJECT_HPP
#define EXIT_OBJECT_HPP

#include "mgp_data_row.hpp"
/**
 * class ExitObject
 * ================
 * 
 * This class holds the content to send from an area to another. Objects of this
 * class are kind of a read-only instances since "getter functions" are
 * available only. ExitObject instances are used inside area controllers to
 * communicate between handlers, filters and the controller.
 */
class ExitObject {

    private:
    MGPDataRow flow, data, ui;

    public:
    
    /**
     * Constructor
     * 
     * @param to_flow   Data to send in main flow.
     * @param to_data   Data to send in data flow.
     * @param to_ui     Data to send in ui flow.
     */
    ExitObject(MGPDataRow to_flow, MGPDataRow to_data, MGPDataRow to_ui);
    
    /**
     * Returns the data which is meant to be sent to the data flow
     * 
     * @return  Data to be sent.
     */
    MGPDataRow getData();

    /**
     * Returns the data which is meant to be sent to the main flow
     * 
     * @return  Data to be sent.
     */
    MGPDataRow getFlow();

    /**
     * Returns the data which is meant to be sent to the ui flow
     * 
     * @return  Data to be sent.
     */
    MGPDataRow getUi();

};

#endif