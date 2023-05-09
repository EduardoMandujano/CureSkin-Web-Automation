# Created by Eduardo Mandujano at 5/9/2023
Feature: Navigation - About Us Page
  Verify that clicking on the About Us link navigates the user to the CureSkin About Us Page

  Scenario: On click, the About Us Link navigates the user to the CureSkin About Us Page
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on the About Us Link
    Then Verify that the user is navigated to the CureSkin About Us page