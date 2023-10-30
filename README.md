# CSC_500_Module_3
 
Part 1
```pseudo
Function CalculateAndDisplayResults(table_name, total_charges, tip_rate, tax_rate)
    Calculate tip as total_charges multiplied by (tip_rate divided by 100)
    Calculate sales_tax as total_charges multiplied by (tax_rate divided by 100)
    Calculate total_amount as the sum of total_charges, tip, and sales_tax
    
    Display "Receipt for [table_name]:"
    Display "Total Food Charges: $" + total_charges (formatted to 2 decimal places)
    Display "Tip ([tip_rate]%): $" + tip (formatted to 2 decimal places)
    Display "Sales Tax ([tax_rate]%): $" + sales_tax (formatted to 2 decimal places)
    Display "Total Amount: $" + total_amount (formatted to 2 decimal places)
    Display a line to separate this table's output from others
    
    Return tip, sales_tax, total_amount
End Function


Function Main()
    Set default_tip_rate to 18.0
    Set default_tax_rate to 7.0
    
    Ask user "Do you want to use custom tip and tax rates? (yes/no): "
    If user inputs 'yes'
        Ask user "Enter the tip rate (default is 18%): "
        If user presses Enter without typing a number
            Set tip_rate to default_tip_rate
        Else
            Set tip_rate to user input converted to float
        End If
        
        Ask user "Enter the tax rate (default is 7%): "
        If user presses Enter without typing a number
            Set tax_rate to default_tax_rate
        Else
            Set tax_rate to user input converted to float
        End If
    Else
        Set tip_rate to default_tip_rate
        Set tax_rate to default_tax_rate
    End If


    Initialize results dictionary
    Initialize grand_totals dictionary with keys "Food Charges", "Tip", "Sales Tax", and "Total Amount", all set to 0.0
    
    Do
        Ask user for table_name "Enter the table name: "
        Initialize total_charges to 0.0


        Do
            Ask user for food_charge "Enter the charge for the food: $"
            Add food_charge to total_charges


            Ask user "Do you want to add another charge for this table? (yes/no): "
        While user inputs 'yes'


        Call CalculateAndDisplayResults with table_name, total_charges, tip_rate, tax_rate
        Add results to results dictionary with table_name as key and returned values as value


        Update grand_totals with values from this table


        Ask user "Do you want to add charges for another table? (yes/no): "
    While user inputs 'yes'
    
    Display "Summary for all tables:"
    For each entry in results
        Display table name and charges
    End For
    
    Display "Grand Totals:"
    For each entry in grand_totals
        Display total type and grand total
    End For
End Function
```

Part 2
```pseudo
Function CalculateAlarmTime(current_hours, current_minutes, hours_to_wait, minutes_to_wait)
    Set total_minutes to current_minutes + minutes_to_wait
    Calculate extra_hours and final_minutes using division and modulo by 60 on total_minutes
    
    Set total_hours to current_hours + hours_to_wait + extra_hours
    Calculate final_hours using modulo by 24 on total_hours
    
    Return final_hours and final_minutes
End Function

Function Main()
    Prompt user "Enter the current time in 'HH:MM' format (24-hour clock): "
    Get input as time_input
    
    Split time_input into current_hours and current_minutes based on ':' delimiter
    Convert current_hours and current_minutes to integers
    
    Prompt user "Enter the number of hours to wait for the alarm: "
    Get input and convert to integer as hours_to_wait
    
    Prompt user "Enter the number of minutes to wait for the alarm: "
    Get input and convert to integer as minutes_to_wait
    
    Call CalculateAlarmTime with current_hours, current_minutes, hours_to_wait, minutes_to_wait
    Store result in alarm_hours and alarm_minutes
    
    Display "The alarm will go off at [alarm_hours]:[alarm_minutes], formatted to two digits each."
End Function
```