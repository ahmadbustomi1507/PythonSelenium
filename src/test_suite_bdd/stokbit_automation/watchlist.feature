@functional
Feature: e2e test

    Scenario: login with correct account
        Given User successfully navigate to the home page
        When User click the sign in button
            And User fill in the "sample_email@gmail.com" and "1232jvhj&#%^&"
        Then User successfully login with avatar settings pop up
            And redirect to the dashboard


    Scenario: Add watchlist
        Given User click the wishlist menu
        When User fill the wishlist menu as "ADRO"
        Then Wishlist "ADRO" will be shown in the list

