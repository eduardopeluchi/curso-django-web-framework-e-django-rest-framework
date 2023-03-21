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
        
    # collect static
    
        Django can collect the static files and save them all in one folde to be easy
        to manage them.
        
        First of all please configure in settings.py the STATIC_ROOT
            STATIC_ROOT = BASE_DIR / 'static'
        
        py manage.py collectstatic
        

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
                

# Static Files
    
     - Static files are file who will be delivered exactly as they was saved.
    This files almost don`t have changes so the browser can save this files on cache
    to the page content could be loaded faster.
    Frequently sites can add you static content to the CDNs (Content Delivery Network) who are optimized
    to deliver static files with fast delivery as to keeping this files close to the final user.

# Namespacing

    Help us during the developement to don`t have any issue with names collision for example
    when you have two files or folders with the same name so when django is running and a
    collision happen the django will executu one of the two file and could be the wrong one.
    
    So always as possible give different names to your folder or file.
    
    Example:
         
         base_static/global(*namespacing*)/css/global-style.css
         recipes/static/recipes(*namespacing*)/css/style.css
         
