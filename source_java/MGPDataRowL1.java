import java.sql.Timestamp;

/**
 * class MGPDataRowL1
 * ==================
 * This class holds a First Level database record. It acts like a read only data
 * container from one side and it is an actual storage handling tool from the
 * other side. As a data container it has "getter functions" only and data must
 * be set at the instantiation. As a data storage helper tool it can be
 * consumed with getting the storage record id or it can be filtered.
 */
public class MGPDataRowL1 {

    private Timestamp timestamp;
    private MGPData data;
    private int l0id;
    private int patient_id;
    private String patient_pwd;
    private boolean is_filtered;
    private int id;

    /**
     * Constructor
     * 
     * @param timestamp The timestamp when the data was generated.
     * @param data      The actual data to store.
     */
    public MGPDataRowL1(Timestamp timestamp, MGPData data) {

        this.timestamp = timestamp;
        this.data = data;
        this.l0id = -1;
        this.patient_id = -1;
        this.patient_pwd = "";
        this.is_filtered = false;
        this.id = -1;

    }

    /**
     * Constructor
     * 
     * @param timestamp The timestamp when the data was generated.
     * @param data      The actual data to store.
     * @param l0id      The ID of an L0 row from which the flow is inherited.
     */
    public MGPDataRowL1(Timestamp timestamp, MGPData data, int l0id) {

        this.timestamp = timestamp;
        this.data = data;
        this.l0id = l0id;
        this.patient_id = -1;
        this.patient_pwd = "";
        this.is_filtered = false;
        this.id = -1;

    }

    /**
     * Constructor
     * 
     * @param timestamp     The timestamp when the data was generated.
     * @param data          The actual data to store.
     * @param l0id          The ID of an L0 row from which the flow is inherited.
     * @param patient_id    The ID of the patient.
     * @param patient_pwd   The password to get the ID of the patient.
     */
    public MGPDataRowL1(Timestamp timestamp, MGPData data, int l0id, int patient_id, String patient_pwd) {

        this.timestamp = timestamp;
        this.data = data;
        this.l0id = l0id;
        this.patient_id = patient_id;
        this.patient_pwd = patient_pwd;
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

            throw new MGPException("MGPDataRowL1.consume() record already filtered.");

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
    
                throw new MGPException("MGPDataRowL1.consume() record already saved.");
    
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
     * Gets L0 record ID
     * 
     * @return   None negative number if the L0 ID exists, else -1.
     */
    public int getL0Id() {

        return l0id;

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
     * Gets the patient’s ID
     * 
     * @param password  The password the get the patient’s ID.
     * @return          It returns the ID of the patient if there is an ID stored
     *                  and the password or the lack of password matches the
     *                  original setup, else it returns -1.
     */
    public int getPatientId(String password) {

        if (patient_pwd.equals(password)) {

            return patient_id;

        } else {

            return -1;

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