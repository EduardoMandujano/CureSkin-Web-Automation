# Created by Eduardo Mandujano at 6/14/2023
Feature: Shop by Face - Under Eye Gel
   Verify the navigation to Under Eye Gel from Shop by Face

  Scenario: Shop by Face - Under Eye Gel
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on Shop By Face Link
    And Click on Under Eye Gel
    Then Verify that the user is navigated to the Under Eye Gel Page