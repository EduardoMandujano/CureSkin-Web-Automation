# Created by Eduardo Mandujano at 6/13/2023
Feature: Shop by Face - Mineral Sunscreen SPF50
  Verify the navigation to the Mineral Sunscreen SPF50 from Shop by Face

  Scenario: Shop by Face - Mineral Sunscreen SPF50
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on Shop By Face Link
    And Click on SPF50
    Then Verify SPF50
