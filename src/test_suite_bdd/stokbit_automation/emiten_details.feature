@functional
Feature:  emiten details
    Scenario: login with correct account
          Given User successfully navigate to the home page
          When User click the sign in button
              And User fill in the "sample_email@gmail.com" and "1232jvhj&#%^&"
          Then User successfully login with avatar settings pop up
              And redirect to the dashboard

    Scenario: search the emiten
          Given User access the search bar on to the top left
          When User fill in the emiten "POWR"
          Then User will be navigated to the emiten details page

    Scenario: Graph details
          Given User in the emiten details page
          Then The full company name exist
            And The property of the emiten exist
            And Buy Button exist
            And Graph of the emiten exist

    Scenario: Stream details
          Given User in the emiten details page
          When user choose the "Stream" details of the emiten
          Then User can check the order book in the right bottom of the page
            And The latest post with tags "All" exist
            And The latest post with latest post with tags "Ideas" exist
            And The latest post with latest post with tags "Reports" exist
            And The latest post with latest post with tags "Charts" exist
            And The latest post with latest post with tags "Predictions" exist
            And The latest post with latest post with tags "Insiders" exist

    Scenario: News details
          Given User in the emiten details page
          When user choose the "Stream" details of the emiten
          Then User can check the order book in the right bottom of the page
            And The latest post with latest post with tags "News" exist

    Scenario: Key Stat details
          Given User in the emiten details page
          When user choose the "Key Stats" details of the emiten
          Then User can check the order book in the right bottom of the page
            And The key stat of the emiten exist

    Scenario: Analyst details
          Given User in the emiten details page
          When user choose the "Analyst" details of the emiten
          Then the analyst ratings of the emiten exists

    Scenario: Financials details
          Given User in the emiten details page
          When user choose the "Financials" details of the emiten
          Then the financial detail of the emiten exists

    Scenario: Fundachart details
          Given User in the emiten details page
          When user choose the "Fundachart" details of the emiten
          Then the fundamental information of the emiten exists




