# Created by Eduardo Mandujano at 8/13/2023
Feature: Shop All Main Page CC Cream Text Verification
  Verify the correct navigation of Shop All Page using text

  Scenario: Shop All Main Page CC Cream Text Verification
    Given Open CureSkin Home Page
    # When Click on the X to close the Popup Window
    When Click on the Shop All Header Link
    And Click on CC Cream Link
    Then Verify the text of the CC Cream in the Product Details Page