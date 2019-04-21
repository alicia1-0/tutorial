Tutorial 1: Serialization
Set up virtual environment
Installed django, restframework and pygments
Created new project
Added new apps (snippet and rest_framework)
Created Snippet model to store code snippets
Created initial migration for snippet model
Defined SnippetSerializer class
Made snippet instances and used SnippetSerializer to serialize and deserialize them
Changed SnippetSerializer to ModelSerializer class
Created view that supports listing all existing snippers or creating a new snippet
Created view that can be used to retrieve, update or delete a snippet

Tutorial 2: Requests and Responses
Wrote improved views
Added format suffixes to URLs

Tutorial 3: Class-based Views
Rewrote API using class-based views
Made views.py code shorter/cleaner

Tutorial 4: Authentication and Permissions
Associated code snippets to users who created them
Created UserList and UserDetail views
Added 'owner' field to SnippetList and SnippetDetail
Only allowed owners to delete/edit their code snippets

