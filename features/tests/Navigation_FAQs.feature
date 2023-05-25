# Created by Eduardo Mandujano at 5/17/2023
Feature: Navigation - FAQs
  Verify that clicking on the FAQs Link navigates the user to the CureSkin FAQs Page

  Scenario: On click, the Blog Link navigates the user to the FAQs Page
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on the FAQs Link
    Then Verify that the user is navigated to the CureSkin FAQs Page