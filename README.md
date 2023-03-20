# curso-django-web-framework-e-django-rest-framework

 # Commands:
 
    # creating a python virtual machine 
    
        py -m venv venv 
        
      Thats works like a bubble for your project, you can use a specific python version in a virtual machine
      and other version in another for example.
    
    # activating the virtual machine
    
        venv\Scripts\activate 
    
    # creating a Django Apps
    
        py manage.py startapp recipes 
        
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Render

    Can receive a request, a template, context and many other things

    render(request, 'template path -> file)
    
    example: 
            def home(request):
                return render(request, 'recipes/home.html', context={
                    'name': 'Eduardo',
                })
    
# Emmet Abbreviation ( ! )

    When using the caractere ~!~ generates a generic html.
    
# Django HTML notations
  
    When we want to show something in the pages we need to use the notation {{ }}, 
         for example: <span>Recipes {{ name }}</span>
         
    When we want to execute something in the pages we need to use the notation {% %} 
         for example: {%if ... %} or {%for ... %} 
             // {% include 'recipes/partials/head.html' %} //
             
    - Pages and Partials
    
           We can divide the HTML in two files, one for the <body> -> recipes/pages
           and one for the <head> -> recipes/partials who may be used to others pages
           
           The motive for that is that we can use the same <head> for many others pages using the notation 
           {% include 'recipes/partials/head.html' %} to do that
           
    - How to create variables for CSS
    
         example:
                :root {
            --color-primary: #269fe6;
            --color-primary-hover: #2086c2;
            --color-primary-dark: #13141f;
            --color-primary-dark-hover: #212336;
            --color-primary-light: #d4ecfa;
            --color-primary-light-hover: #bdd8e7;
            }
            
            Using:
            
                .main-header-container {
            background: var(--color-primary-dark);
            }
                
