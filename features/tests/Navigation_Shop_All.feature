# Created by Eduardo Mandujano at 6/8/2023
Feature: Navigation - Shop All
  On click, verify that the user is navigated to the Shop All Page

  Scenario: Navigation - Shop All
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on the Shop All Link
    Then Verify that the user is navigated to the CureSkin Shop All Page