CRUD API :
1) Django rest Framework is used to create the API.
2) For the single page create/update/delete/get functions, Javascript is used to display and fetch data.

Following are the routes of the api functions:
   full address = url/api/
        'List':'/item-list/',
        'Detail view':'/item-detail/<str:pk/>',
        'Create':'/item-create/',
        'Update':'item-update/<str:pk>',
        'Delete': 'item-delete/<str:pk>',

for the frontend onlhy url is there as its a single page App.