package ua.edu.chnu.kkn.solid_violation.dip;

import java.time.MonthDay;

public class SystemTimeProvider implements TimeProvider {
    @Override
    public MonthDay getCurrentMonthDay() {
        return MonthDay.now();
    }
}