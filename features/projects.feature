Feature: Projects
  As a developer
  I want to see my projects
  So I can know when the build breaks

  @wip
  Scenario: Show Projects
    Given I have a CI server with projects:
      | name              |
      | My Project        |
      | My Other Project  |
    And the app is running
    Then I see projects "My Project, My Other Project"
