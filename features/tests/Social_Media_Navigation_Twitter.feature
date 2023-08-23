# Created by Eduardo Mandujano at 8/15/2023
Feature: Social Media Navigation Verification - Twitter
  Verify CureSkin's Social Media Links Navigation

  Scenario: Social Media Navigation Verification - Twitter
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on the Footer Twitter Icon
    Then Verify the user is Navigated to the CureSkin Twitter Page