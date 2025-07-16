import arxiv

def search_papers(topic, max_results=3):
    search = arxiv.Search(query=topic, max_results=max_results, sort_by=arxiv.SortCriterion.Relevance)
    return [(result.title, result.pdf_url) for result in search.results()]
