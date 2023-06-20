# Created by Eduardo Mandujano at 5/29/2023
Feature: Navigation - Privacy Policy
  On click, verify that the user is navigated to the Privacy Policy Page

  Scenario: On click, verify that the user is navigated to the Privacy Policy Page
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on the Privacy Policy Link
    Then Verify that the user is navigated to the CureSkin Privacy Policy Page