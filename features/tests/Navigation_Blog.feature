# Created by Eduardo Mandujano at 5/16/2023
Feature: Navigation - Blog
  Verify that clicking on the Blog Link navigates the user to the CureSkin Blog Page

  Scenario: On click, the Blog link navigates the used to the CureSkin Blog Page
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on the CureSkin Blog Link
    Then Verify that the user is navigated to the CureSkin Blog Page