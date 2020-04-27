/**
 * class ExitObject
 * ================
 * 
 * This class holds the content to send from an area to another. Objects of this
 * class are kind of a read-only instances since "getter functions" are
 * available only. ExitObject instances are used inside area controllers to
 * communicate between handlers, filters and the controller.
 */
public class ExitObject {

    private Object flow;
    private Object data;
    private Object ui;

    /**
     * Constructor L0
     * 
     * @param to_flow   Data to send in main flow.
     * @param to_data   Data to send in data flow.
     * @param to_ui     Data to send in ui flow.
     */
    public ExitObject(MGPDataRowL0 to_flow, MGPDataRowL0 to_data, MGPDataRowL0 to_ui) {

        this.flow = to_flow;
        this.data = to_data;
        this.ui = to_ui;

    }

    /**
     * Constructor L1
     * 
     * @param to_flow   Data to send in main flow.
     * @param to_data   Data to send in data flow.
     * @param to_ui     Data to send in ui flow.
     */
    public ExitObject(MGPDataRowL1 to_flow, MGPDataRowL1 to_data, MGPDataRowL1 to_ui) {

        this.flow = to_flow;
        this.data = to_data;
        this.ui = to_ui;

    }

    /**
     * Constructor L2
     * 
     * @param to_flow   Data to send in main flow.
     * @param to_data   Data to send in data flow.
     * @param to_ui     Data to send in ui flow.
     */
    public ExitObject(MGPDataRowL2 to_flow, MGPDataRowL2 to_data, MGPDataRowL2 to_ui) {

        this.flow = to_flow;
        this.data = to_data;
        this.ui = to_ui;

    }

    /**
     * Constructor L3
     * 
     * @param to_flow   Data to send in main flow.
     * @param to_data   Data to send in data flow.
     * @param to_ui     Data to send in ui flow.
     */
    public ExitObject(MGPDataRowL3 to_flow, MGPDataRowL3 to_data, MGPDataRowL3 to_ui) {

        this.flow = to_flow;
        this.data = to_data;
        this.ui = to_ui;

    }

    /**
     * Returns the data which is meant to be sent to the data flow
     * 
     * @return  Data to be sent.
     */
    public Object getData() {
        
        return data;

    }
    
    /**
     * Returns the data which is meant to be sent to the main flow
     * 
     * @return  Data to be sent.
     */
    public Object getFlow() {
        
        return flow;

    }

    /**
     * Returns the data which is meant to be sent to the ui flow
     * 
     * @return  Data to be sent.
     */
    public Object getUi() {
        
        return ui;

    }

}