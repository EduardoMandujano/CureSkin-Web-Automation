# Created by Eduardo Mandujano at 9/5/2023
Feature: Shopping Cart - View Cart/Remove Item
  Verify that removing an item navigates the user to the Empty Cart Page

  Scenario: Shopping Cart - View Cart/Remove Item
    Given Open CureSkin Home Page
    When Click on the X to close the Popup Window
    And Click on What's New Item Add to Cart Button
    And Click on the Sidebar View Cart Button
    Then Verify that the user was navigated to the Your Cart Page
    Then Verify that the cart contains the Item Added
    When Click on the Minus Icon
    Then Verify that the cart is empty