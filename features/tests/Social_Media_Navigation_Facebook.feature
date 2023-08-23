# Created by Eduardo Mandujano at 8/13/2023
Feature: Social Media Navigation Verification - Facebook
  Verify CureSkin's Social Media Links Navigation

  Scenario: Social Media Navigation Verification - Facebook
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    When Click on the Footer Facebook Icon
    Then Verify the user is Navigated to the CureSkin Facebook Page
