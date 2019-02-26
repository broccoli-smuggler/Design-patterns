public class CoffeeTouchscreenAdapter implements CoffeeMachineInterface {
    private OldCoffeeMachine oldMachine;

    CoffeeTouchscreenAdapter(OldCoffeeMachine oldMachine) {
        this.oldMachine = oldMachine;
    }

    @Override
    public void chooseFirstSelection() {
        this.oldMachine.selectA();
    }

    @Override
    public void chooseSecondSelection() {
        this.oldMachine.selectB();
    }
}