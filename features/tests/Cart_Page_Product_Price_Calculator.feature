# Created by Eduardo Mandujano at 4/23/2023
Feature: Task 3
  Cart Page - Product Price Calculator

  Scenario: Cart calculates price for the same product
    Given Open Product Details page of CureSkin Cleansing Gel
    When Click on Add to cart button
    And Open cart page
    And Store the current price
    And Click plus icon to increase product quantity
    Then Verify total price has doubled
    And Verify that product quantity is set to 2


