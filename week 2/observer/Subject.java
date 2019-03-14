public interface Subject {
   public void registerObserver(Observer obsever);

   public void unregisterObserver(Observer obsever);

   public void notifyObservers();
}