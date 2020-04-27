/**
 * class MGPException
 * ==================
 * 
 * This class provides unique error interface for Medical Gateway Platform. It
 * is a subclass of Exception. It doesn’t have any additional behavior than its
 * parent.
 */
public class MGPException extends Exception {

    static final long serialVersionUID = 0;

    /**
     * Constructor with message only
     * 
     * @param message   Message to display.
     */
    public MGPException(String message) {

        super(message);

    }

    /**
     * Constructor with message and throwable
     * 
     * @param message   Message to display.
     * @param throwable Throwable to follow.
     */
    public MGPException(String message, Throwable throwable) {

        super(message, throwable);

    }

}
