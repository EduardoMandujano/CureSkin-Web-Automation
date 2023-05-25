# Created by Eduardo Mandujano at 5/10/2023
Feature: Navigation - our Doctors Page
  Verify that clicking on the Our Doctors link navigates the user to the CureSkin Our Doctors Page

  Scenario: On click, the Our Doctors Link navigates the user to the CureSkin About Us Page
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on the Our Doctors Link
    Then Verify that the user is navigated to the CureSkin Our Doctors page