package ua.edu.chnu.kkn.solid_violation.dip;

import java.time.MonthDay;

public class Clock {
    public MonthDay monthDay(){
        return MonthDay.now();
    }
}
