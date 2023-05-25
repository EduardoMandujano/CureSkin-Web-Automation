# Created by Eduardo Mandujano at 5/11/2023
Feature: Navigation - Grievance Policy
  Verify that clicking on the Grievance Policy Link navigates the user to the Grievance Policy Page

  Scenario: On click, the Grievance Policy Link navigates the user to the Grievance Policy Page
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on the Grievance Policy Link
    Then Verify that the user is navigated to the CureSkin Grievance Policy Page
