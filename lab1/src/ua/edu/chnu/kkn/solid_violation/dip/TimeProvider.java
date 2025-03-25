package ua.edu.chnu.kkn.solid_violation.dip;

import java.time.MonthDay;

public interface TimeProvider {
    MonthDay getCurrentMonthDay();
}