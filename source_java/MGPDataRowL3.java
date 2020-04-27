import java.sql.Timestamp;

/**
 * class MGPDataRowL3
 * ==================
 * This class holds a Third Level database record. It acts like a read only data
 * container from one side and it is an actual storage handling tool from the
 * other side. As a data container it has "getter functions" only and data must
 * be set at the instantiation. As a data storage helper tool it can be
 * consumed with getting the storage record id or it can be filtered.
 */
public class MGPDataRowL3 {

    private Timestamp timestamp;
    private int l2id;
    private String response;
    private boolean is_filtered;
    private int id;

    /**
     * Constructor
     * 
     * @param timestamp The timestamp when the data was generated.
     * @param l2id      The ID of an L2 row from which the flow is inherited.
     * @param response  The response resulted from L2 record.
     */
    public MGPDataRowL3(Timestamp timestamp, int l2id, String response) {

        this.timestamp = timestamp;
        this.l2id = l2id;
        this.response = response;
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
    public int getL2Id() {

        return l2id;

    }

    /**
     * Gets the stored response
     * 
     * @return  The content of the stored response.
     */
    public String getResponse() {

        return response;

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
     * Gets whether the object is filtered or not
     * 
     * @return  True if the row is filtered, False if not.
     */
    public boolean isFiltered() {

        return is_filtered;

    }

}