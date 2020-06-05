from flask import render_template,request,redirect,url_for
from . import main
from app.requests import get_articles,get_source,search_source


#Views
@main.route('/')
def index():
    top_news = get_source('sources')

    title = 'best news stories'
    search_source = request.args.get('sources_query')

    if search_source:
        return redirect(url_for('search',source_name=search_source))
    else:
        return render_template('index.html', title = title, sources = top_news) 
    # description =describe_sources

@main.route('/articles')
def display_articles():
    # general = get_articles('general')

    # return render_template('articles.html', general=general) 
        
    top_articles = get_articles()
    print(top_articles)
    
    
    return render_template('articles.html',  get_articles = top_articles )

@main.route('/search/<source_name>')
def search(source_name):
    '''
    function to display search results
    '''
    source_name_list = source_name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_source = search_source(source_name_format)
    title = f'search results for {source_name}'
    
    return render_template('search.html',sources=searched_source)