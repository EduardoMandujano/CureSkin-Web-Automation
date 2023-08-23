# Created by Eduardo Mandujano at 8/18/2023
Feature: Social Media Navigation Verification - Linkedin
  Verify CureSkin's Social Media Links Navigation

  Scenario: Social Media Navigation Verification - Linkedin
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on the Footer Linkedin Icon
    Then Verify the user is Navigated to the CureSkin Linkedin Page