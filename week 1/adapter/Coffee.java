
class Coffee {
    public static void main(String[] args) {
        OldCoffeeMachine oldMachine = new OldCoffeeMachine();
        CoffeeTouchscreenAdapter adapter = new CoffeeTouchscreenAdapter(oldMachine);
        adapter.chooseFirstSelection();
        adapter.chooseSecondSelection();
    }
}