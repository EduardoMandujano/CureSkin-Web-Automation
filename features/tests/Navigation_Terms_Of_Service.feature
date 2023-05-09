# Created by Eduardo Mandujano at 5/8/2023
Feature: Navigation - Terms of Service Page
  Verify that clicking on the Terms of Service link navigates the user back to the Terms of Service Page

  Scenario: On click, the Terms of Service Link navigates the user to the CureSkin Terms of Service Page
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on the Terms Of Service Link
    Then Verify that the user is navigated to the CureSkin Terms Of Service page
