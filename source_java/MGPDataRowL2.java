import java.sql.Timestamp;

/**
 * class MGPDataRowL2
 * ==================
 * This class holds a Second Level database record. It acts like a read only data
 * container from one side and it is an actual storage handling tool from the
 * other side. As a data container it has "getter functions" only and data must
 * be set at the instantiation. As a data storage helper tool it can be
 * consumed with getting the storage record id or it can be filtered.
 */
public class MGPDataRowL2 {

    private Timestamp timestamp;
    private MGPData ch1_data;
    private MGPData ch2_data;
    private int l1id;
    private boolean is_filtered;
    private int id;

    /**
     * Constructor
     * 
     * @param timestamp The timestamp when the data was generated.
     * @param ch1_data  Data from channel 1 (processed source)
     * @param ch2_data  Data from channel 2 (automated source)
     */
    public MGPDataRowL2(Timestamp timestamp, MGPData ch1_data, MGPData ch2_data) {

        this.timestamp = timestamp;
        this.ch1_data = ch1_data;
        this.ch2_data = ch2_data;
        this.l1id = -1;
        this.is_filtered = false;
        this.id = -1;

    }

    /**
     * Constructor
     * 
     * @param timestamp The timestamp when the data was generated.
     * @param ch1_data  Data from channel 1 (processed source)
     * @param ch2_data  Data from channel 2 (automated source)
     * @param l1id      The ID of an L1 row from which the flow is inherited.
     */
    public MGPDataRowL2(Timestamp timestamp, MGPData ch1_data, MGPData ch2_data, int l1id) {

        this.timestamp = timestamp;
        this.ch1_data = ch1_data;
        this.ch2_data = ch2_data;
        this.l1id = l1id;
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

            throw new MGPException("MGPDataRowL2.consume() record already filtered.");

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
    
                throw new MGPException("MGPDataRowL2.consume() record already saved.");
    
            }
    

        }

    }
    
    /**
     * Gets the ID of the row
     * 
     * @return  Non negative number if the ID of the row already exists, else -1.
     */
    public int getId() {

        return id;

    }

    /**
     * Gets L1 record ID
     * 
     * @return   None negative number if the L1 ID exists, else -1.
     */
    public int getL1Id() {

        return l1id;

    }

    /**
     * Gets the label of the stored data
     * 
     * @return  The acutal label.
     */

    /**
     * Gets the label of the stored data
     * 
     * @param channel       The ID of the channel to get label from.
     * @return              The actual label.
     * @throws MGPException When non existing channel ID is given.
     */
    public String getLabel(int channel) throws MGPException {

        switch (channel) {

            case 1:
                return ch1_data.getLabel();

            case 2:
                return ch2_data.getLabel();

            default:
                throw new MGPException("MGPDataRowL2.getlabel() requested unsupported channel.");

        }

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
     * @param channel       The ID of the channel to get unit from.
     * @return              The name of the measurement unit.
     * @throws MGPException When non existing channel ID is given.
     */
    public String getUnit(int channel) throws MGPException {

        switch (channel) {

            case 1:
                return ch1_data.getUnit();

            case 2:
                return ch2_data.getUnit();

            default:
                throw new MGPException("MGPDataRowL2.getUnit() requested unsupported channel.");

        }

    }


    /**
     * Gets the value, amount of the stored data
     * 
     * @param channel       The ID of the channel to get value from.
     * @return              The value of the measurement or action.
     * @throws MGPException When non existing channel ID is given.
     */
    public Object getValue(int channel) throws MGPException {

        switch (channel) {

            case 1:
                return ch1_data.getValue();

            case 2:
                return ch2_data.getValue();

            default:
                throw new MGPException("MGPDataRowL2.getValue() requested unsupported channel.");

        }

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