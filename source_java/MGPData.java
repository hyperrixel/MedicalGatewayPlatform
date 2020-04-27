/**
 * class MGPData
 * =============
 * 
 * This class holds the content of a data point in the most strict sense.
 * Objects of this class are kind of a read-only instances since
 * "getter functions" are available only. MGPData object are used to hold the
 * content of an event in fact it means a labeled measurement, a labeled
 * decision, a labeled action or a labeled something.
 */
public class MGPData {
    
    private String  label;
    private Object  value;
    private String  unit;
    
    /**
     * Contructor for floating point values
     * 
     * @param label The label of the data.
     * @param value The actual value of the data.
     * @param unit  The name of the measurement unit.
     */
    public MGPData(String label, double value, String unit) {
        
        this.label = label;
        this.value = value;
        this.unit = unit;
        
    }

    /**
     * Contructor for integer values
     * 
     * @param label The label of the data.
     * @param value The actual value of the data.
     * @param unit  The name of the measurement unit.
     */
    public MGPData(String label, int value, String unit) {
        
        this.label = label;
        this.value = value;
        this.unit = unit;
        
    }
    
    /**
     * Contructor for textual values
     * 
     * @param label The label of the data.
     * @param value The actual value of the data.
     * @param unit  The name of the measurement unit.
     */
    public MGPData(String label, String value, String unit) {
        
        this.label = label;
        this.value = value;
        this.unit = unit;
        
    }
    
    /**
     * Gets the label of the data
     * 
     * @return  The acutal label.
     */
    public String getLabel() {
        
        return label;
        
    }

    /**
     * Gets the measurement unit of the data
     * 
     * @return  The name of the measurement unit.
     */
    public String getUnit() {
        
        return unit;
        
    }

    /**
     * Gets the value, amount of the data
     * 
     * @return  The value of the measurement or action.
     */
    public Object getValue() {

        return value;

    }
    
}