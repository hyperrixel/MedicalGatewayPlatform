import java.sql.Timestamp;

/**
 * class MGPDataRowL0
 * ==================
 * This class holds a Zero Level database record. It acts like a read only data
 * container from one side and it is an actual storage handling tool from the
 * other side. As a data container it has "getter functions" only and data must
 * be set at the instantiation. As a data storage helper tool it can be
 * consumed with getting the storage record id or it can be filtered.
 */
public class MGPDataRowL0 {

    private Timestamp timestamp;
    private MGPData data;
    private int equipment_id;
    private String event_type;
    private boolean is_filtered;
    private int id;

    /**
     * Contructor 
     * 
     * @param timestamp     The timestamp when the data was generated.
     * @param data          The actual data to store.
     * @param equipment_id  The ID of the equipment where the data are from.
     * @param event_type    The description of the event connected to the data row.
     */
    public MGPDataRowL0(Timestamp timestamp, MGPData data, int equipment_id, String event_type) {

        this.timestamp = timestamp;
        this.data = data;
        this.equipment_id = equipment_id;
        this.event_type = event_type;
        this.is_filtered = false;
        this.id = -1;

    }

    /**
     * Finalizes the instance
     * 
     * @param result        ID of the saved record.
     * @throws MGPException When the record is already filtered.
     */
    public void consume(int result) throws MGPException {

        if (! is_filtered) {

            this.id = result;

        } else {

            throw new MGPException("MGPDataRowL0.consume() record already filtered.");

        }

    }

    /**
     * Finalizes the instance
     * 
     * @param result        Should be true to consume with filter.
     * @throws MGPException When the record is already saved.
     */
    public void consume(boolean result) throws MGPException {

        if (result == true) {

            if (id == -1) {

                this.is_filtered = true;
    
            } else {
    
                throw new MGPException("MGPDataRowL0.consume() record already saved.");
    
            }
    

        }

    }
    
    /**
     * Gets the equipment’s ID
     * 
     * @return  The ID of the equipment.
     */
    public int getEquipment() {
        
        return equipment_id;

    }

    /**
     * Gets the type of the event
     * 
     * @return  The name of the event type stored in the row.
     */
    public String getEventType() {

        return event_type;

    }

    /**
     * Gets the ID of the row
     * 
     * @return  Positive number if the ID of the row already exists, else -1.
     */
    public int getId() {

        return id;

    }

    /**
     * Gets the label of the stored data
     * 
     * @return  The acutal label.
     */
    public String getLabel() {

        return data.getLabel();

    }

    /**
     * Gets the timestamp of the record
     * 
     * @return  The timestamp.
     */
    public Timestamp getTimestamp() {

        return timestamp;

    }

    /**
     * Gets the measurement unit of the stored data
     * 
     * @return  The name of the measurement unit.
     */
    public String getUnit() {

        return data.getUnit();

    }

    /**
     * Gets the value, amount of the stored data
     * 
     * @return  The value of the measurement or action.
     */
    public Object getValue() {

        return data.getValue();

    }

    /**
     * Gets whether the object is filtered or not
     * 
     * @return  True if the row is filtered, False if not.
     */
    public boolean isFiltered() {

        return is_filtered;

    }

}