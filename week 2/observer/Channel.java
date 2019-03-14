import java.util.ArrayList;

public class Channel implements Subject {
    private ArrayList<Observer> observers = new ArrayList<Observer>();
    private String channelName, status;

    public Channel(String channelName, String status) {
        this.channelName = channelName;
        this.status = status;
    }

    /**
     * @return the status
     */
    public String getStatus() {
        return status;
    }

    /**
     * @param status the status to set
     */
    public void setStatus(String status) {
        this.status = status;
        this.notifyObservers();
    }

    @Override
    public void notifyObservers() {
        for (Observer observer : this.observers) {
            observer.notify();
        }
    }

    @Override
    public void registerObserver(Observer obsever) {
        observers.add(observer);
    }

    @Override
    public void unregisterObserver(Observer obsever) {
        observers.remove(observer);
    }
}