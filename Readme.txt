Tutorial 1: Serialization
Set up virtual environment
Installed django, restframework and pygments
Created new project
Added new apps (snippet and rest_framework)

Created Snippet model to store code snippets
Created initial migration for snippet model
Synced database

Defined SnippetSerializer class

Made snippet instances and used SnippetSerializer to serialize and deserialize them

Changed SnippetSerializer to ModelSerializer class

Created view that supports listing all existing snippers or creating a new snippet
Created view that can be used to retrieve, update or delete a snippet