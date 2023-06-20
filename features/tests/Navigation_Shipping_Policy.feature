# Created by Eduardo Mandujano at 6/7/2023
Feature: Navigation - Shipping Policy
  On click, verify that the user is navigated to the CureSkin Shipping Policy Page

  Scenario: Navigation - Shipping Policy
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on the Shipping Policy Link
    Then Verify that the user is navigated to the CureSkin Shipping Policy Page