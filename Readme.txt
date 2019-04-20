Commit 1: Creating a Serializer class
Set up virtual environment
Installed django, restframework and pygments
Created new project
Added new apps (snippet and rest_framework)

Created Snippet model to store code snippets
Created initial migration for snippet model
Synced database

Defined SnippetSerializer class

Commit 2: Working with Serializers
Made snippet instances and used SnippetSerializer to serialize and deserialize them

Commit 3: Using ModelSerializer
Changed SnippetSerializer to ModelSerializer class

Commit 4: Writing regular Django views using our Serializer
Created view that supports listing all existing snippers or creating a new snippet
Created view that can be used to retrieve, update or delete a snippet