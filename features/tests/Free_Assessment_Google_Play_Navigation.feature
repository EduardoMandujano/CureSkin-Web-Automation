# Created by Eduardo Mandujano at 8/22/2023
Feature: Free Assessment - Google Play Navigation
  Verify the Navigation to the Google Play App from the Free Assessment Header Button

  Scenario: Free Assessment - Google Play Navigation
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on the Free Assessment Header Button
    Then Verify that the user is navigated to the Google Play Cureskin App Page