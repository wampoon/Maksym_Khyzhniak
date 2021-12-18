Feature: OrangeHRM Demo https://opensource-demo.orangehrmlive.com/
    
    Scenario: login into OrangeHRM
        Given we have username 'Admin' 
            And password 'admin123'
        When we put username into username field
            And we put password into password field
            And we click login button
        Then we must be successfuly logged in

    Scenario: going to Admin section
        Given we are logged in sucessfully
        When we click on 'Admin' section in navbar
        Then Admin page is opened

    Scenario: opening dropdown menu
        Given we are on Admin page
        When we hover on 'Job'
        Then dropdown menu must be shown

    Scenario: going to 'Pay Grades' section
        Given we have 'Job' dropdown menu opened
        When we click 'Pay Grades' button
        Then 'Pay Grades' section is displayed

    Scenario: adding pay grade
        Given we are at Pay Grades page
        When we click 'Add' button in 'Pay Grades' section
            And put 'RandomName' in 'Name' field
            And click 'Save' button
        Then section 'Assigned Currencies' must be displayed

    Scenario: adding assigned currencies
        Given we have 'Assigned Currencies' section displayed
        When we click 'Add' button
            And put 'USD - United States Dollar' in 'Currency' field
            And put '1' in 'Minimum Salary' field
            And put '5' in 'Maximum Salary' field
            And click 'Save' button in editing section
        Then in 'Assigned Currencies' section must be displayed row {'Currency':'United States Dollar, 'Minimum Salary':'1.00', 'Maximum Salary':'5.00'}

    Scenario: removing added Currency
        Given we sucessfully added new Currency
        When we click checkbox in newly added Currency row
            And click "Delete" button
        Then newly added row must become invisible
