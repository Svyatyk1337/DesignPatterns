package ua.edu.chnu.kkn.solid_violation.lsp;

public class PetrolCar extends Vehicle {

    private static final int FUEL_TANK_FULL = 100;
    private int fuelTankLevel = 0;

    @Override
    public void fillUp() {
        fillUpWithFuel();
    }

    private void fillUpWithFuel() {
        this.fuelTankLevel = FUEL_TANK_FULL;
    }

    public int fuelTankLevel() {
        return fuelTankLevel;
    }
}
