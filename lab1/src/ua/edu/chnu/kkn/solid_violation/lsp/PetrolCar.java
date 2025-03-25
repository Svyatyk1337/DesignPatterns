package ua.edu.chnu.kkn.solid_violation.lsp;

public class PetrolCar extends Vehicle implements Refuelable {
    private static final int FUEL_TANK_FULL = 100;
    private int fuelTankLevel = 0;

    @Override
    public void fillUpWithFuel() {
        this.fuelTankLevel = FUEL_TANK_FULL;
    }

    @Override
    public int fuelTankLevel() {
        return fuelTankLevel;
    }
}