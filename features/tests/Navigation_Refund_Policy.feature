# Created by Eduardo Mandujano at 5/25/2023
Feature: Navigation - Refund Policy
   On click, verify that the user is navigated to the Refund Policy Page

  Scenario: On click, verify that the user is navigated to the Refund Policy Page
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on the Refund Policy Link
    Then Verify that the user is navigated to the CureSkin Refund Policy Page