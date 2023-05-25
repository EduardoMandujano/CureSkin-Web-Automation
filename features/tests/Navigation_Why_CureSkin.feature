# Created by Eduardo Mandujano at 5/16/2023
Feature: Navigation - Why CureSkin Policy
  Verify that clicking on the Why CureSkin Link navigates the user to the Why CureSkin Page

  Scenario: On click, clicking on the Why CureSkin Link navigates the user to the Why CureSkin Page
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on the Why CureSkin Link
    Then Verify that the user is navigated to the Why CureSkin Page