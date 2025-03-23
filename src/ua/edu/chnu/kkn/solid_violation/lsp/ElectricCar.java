package ua.edu.chnu.kkn.solid_violation.lsp;

public class ElectricCar extends Vehicle {

    private static final int BATTERY_FULL = 100;
    private int batteryLevel;

    @Override
    public void fillUp() {
        chargeBattery();
    }

    private void chargeBattery() {
        batteryLevel = BATTERY_FULL;
    }

    public int batteryLevel() {
        return batteryLevel;
    }
}
